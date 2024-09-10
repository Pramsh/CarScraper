import json
import os
import queue
from datetime import datetime
from queue import Queue
from threading import Semaphore
import threading
from modules.build_link import build_link
from modules.common_fun import parse_html_by_link, thread_all, c_msg, filter_link_from_items, delete_file_if_exist, \
    thread_all_and_resolve
from modules.constants import basic_report_path, storage_file_name, base_storage_path, advanced_report_path, \
    not_valid_urls, car_schema
from modules.define_item_spec import car_details_attr, get_model, get_price, get_seller_info_name, get_features, \
    get_link, get_grouped_attributes
from modules.get_inputs import date_input, get_inputs, y_or_n
from modules.handle_link_storage import handle_link_storage


def generate_basic_analysis(data):
    with open(basic_report_path,"w", encoding="utf-8") as f:
        json.dump(data,f, indent=4)
        print(f"Basic report generated at {basic_report_path}")

def retrieve_basic_analysis():
    with open(basic_report_path, "r", encoding='utf-8') as f:
        data = json.load(f)
    return data


def retrieve_link_storage() -> list[dict[str,any] or []]:
    try:
        custom_path = base_storage_path + os.getlogin() + "/" +storage_file_name
        with open(custom_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError as e:
        return []



def get_stored_links() -> list[dict[str,any] or []]:
    data = retrieve_link_storage()
    return filter_link_from_items(data)


def string_to_date(date_string:str):
    day, month, year = date_string.split("-")
    date_obj = datetime(int(year), int(month), int(day))
    return date_obj

def create_schema_if_not_exist():
    user_data = None
    try:
        with open(car_schema, "r", encoding='utf-8') as f:
            user_data = json.load(f)
        use_old_schema = y_or_n(
            "Some filters are already persisted, do you want to proceed using this schema? {} \n (take note generating a new schema will delete the old one)\n Y or N: ".format(
                user_data))
        if not use_old_schema:
            raise FileNotFoundError()
    except FileNotFoundError:
        user_data = get_inputs()
        with open(car_schema, "w", encoding='utf-8') as f:
            json.dump(user_data, f, ensure_ascii=False, indent=4)
    finally:
        return user_data


def thread_on_basic_report(user_schema, page, semaphore:Semaphore, output_queue: Queue):
    with semaphore:
        link = build_link(user_schema["fuel"] or "", user_schema["brand"], user_schema["price"], page)
        soup = parse_html_by_link(link)
        cars_details_box_container = soup.find('main', class_='ListPage_main___0g2X')
        cars_details_box = cars_details_box_container.find_all('article')
        for el in cars_details_box:
            single_item = {
                "model": get_model(el),
                "price": get_price(el),
                "km": "",
                "fuel": "",
                "year": "",
                "CV": "",
                "gears": "",
                "seller": get_seller_info_name(el),
                "features": get_features(el).split(","),
                "link": get_link(el)
            }
            single_item = {**single_item, **get_grouped_attributes(el)}
            output_queue.put(single_item)


def process_pages_in_threads(total_pages:int, user_schema:dict[str:str], max_page_to_process_concurrently = 5):
    q = queue.Queue()
    output_data = []
    threads = []
    semaphore = threading.Semaphore(max_page_to_process_concurrently)
    for page in range(2, int(total_pages)+1):
        t = threading.Thread(target=thread_on_basic_report, args=(user_schema, page, semaphore, q))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    while not q.empty():
        output_data.append(q.get())

    return output_data



def get_basic_report_data(user_schema) -> list[dict[str,any]]:
    link = build_link(user_schema["fuel"], user_schema["brand"], user_schema["price"])
    parsed_html = parse_html_by_link(link)
    pagination_box = parsed_html.find("nav", class_='scr-pagination')
    pages = pagination_box.find_all("li", class_="pagination-item")
    total_pages = pages[-1].text
    output_data = process_pages_in_threads(total_pages, user_schema)
    return output_data


def store_link_and_build_basic_report(user_schema) -> None:
    output_data = get_basic_report_data(user_schema)
    link_cars = [data["link"] for data in output_data]
    thread_all_and_resolve([
        threading.Thread(target=handle_link_storage, args=(link_cars, user_schema)),
        threading.Thread(target=generate_basic_analysis, args=(output_data,))
    ])



def get_storage_in_time_range(data=None):
    c_msg("Select the time range.")
    inp_start_date = date_input("Start date", False)
    inp_end_date = date_input("End date")
    inp_end_date = inp_end_date if inp_end_date != "" else datetime.now().strftime('%d-%m-%Y')
    if data is None:
        data = retrieve_link_storage()
    datetime_format = "%d-%m-%Y"
    start_date = string_to_date(inp_start_date)
    end_date = string_to_date(inp_end_date)
    res = []
    for item in data:
        stored_date_obj = datetime.strptime(item["timestamp"], "%Y-%m-%d %H:%M:%S")
        if start_date <= datetime.strptime(stored_date_obj.strftime('%d-%m-%Y'), datetime_format) <= end_date:
            res.append(item)
    return res

def get_storage_last_items(data=None) -> dict[str:any]:
    if data is None:
        data = retrieve_link_storage()
    for i in range(1,len(data)+1):
            if len(data[-i]["items"]) > 0:
                return data[-i]


def handle_reports_storage(file_path, data, discard_old_data_bool):
    if discard_old_data_bool:
        delete_file_if_exist(file_path)
    try:
        with open(file_path, "r+", encoding='utf-8') as f:
            persisted_data = json.load(f)
            persisted_data.extend(data)
            f.seek(0)
            json.dump(persisted_data, f, indent=4)
            print(f"Sys... data stored in {file_path}")
    except FileNotFoundError as e:
        with open(file_path, "w", encoding="utf8") as f:
            json.dump([], f)
        return handle_reports_storage(file_path, data, False)



def store_valid_items(data, discard_old_data_bool):
    return handle_reports_storage(advanced_report_path, data, discard_old_data_bool)


def store_invalid_items(data, discard_old_data_bool):
    return handle_reports_storage(not_valid_urls,data, discard_old_data_bool)

def handle_chunk(info, chunk_size=10):
    if len(info["data"]) >= chunk_size and len(info["data"]) % chunk_size == 0:
        store_valid_items(info["data"], info["discard_old_data"])
        info["data"] = []
        info["discard_old_data"] = False

def handle_chunk_in_diff_threads(valid_links, invalid_links):
    thread_all(([
        threading.Thread(target=handle_chunk, args=(valid_links, )),
        threading.Thread(target=handle_chunk, args=(invalid_links,))
    ]))
"""
def handle_html_parsing_and_chunks_storage(link, res, invalid_links, chunks=10):
    try:
        if len(res["data"]) >= chunks or len(invalid_links["data"]) >= chunks:
            handle_chunk_in_diff_threads(res, invalid_links)
        main_block = parse_html_by_link(link).find("main")
        item = car_details_attr(main_block)
        res["data"].append(item)
    except Exception as e:
        print(link, " SUSPECT LINK")
        print(e)
        invalid_links["data"].append(link)
"""

def generate_advanced_analysis(links:list[str]):
    res =  {
        "data": [],
        "discard_old_data": True
    }
    invalid_links = {
        "data": [],
        "discard_old_data": True
    }
    counter = 0
    chunks = 10
    for link in links:
        try:
            if len(res["data"]) >= chunks or len(invalid_links["data"]) >= chunks:
                handle_chunk_in_diff_threads(res, invalid_links)
                print("chunk! ",counter,"/",len(links))
            main_block  = parse_html_by_link(link).find("main")
            item = car_details_attr(main_block)
            res["data"].append(item)
            counter += 1

        except Exception as e:
            print(link, " SUSPECT LINK")
            print(e)
            invalid_links["data"].append(link)
    thread_all([
        threading.Thread(target=store_valid_items, args=(res["data"], res["discard_old_data"])),
        threading.Thread(target=store_invalid_items, args=(invalid_links["data"], invalid_links["discard_old_data"]))
    ])
