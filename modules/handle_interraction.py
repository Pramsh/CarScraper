import sys
import threading
from modules.basic_and_advance_report import create_schema_if_not_exist, store_link_and_build_basic_report, \
    get_storage_in_time_range, retrieve_link_storage, generate_advanced_analysis, get_storage_last_items
from modules.common_fun import filter_link_from_items, c_msg, thread_all, thread_all_and_resolve, delete_file_if_exist, \
    ab_input
from modules.constants import advanced_report_path, basic_report_path, not_valid_urls
from modules.get_inputs import y_or_n
from modules.handle_link_storage import get_storage_directory


def handle_time_range_question(data=None):
    input("Please search by timerange")
    cached_items = get_storage_in_time_range(data)
    if len(cached_items) < 1:
        c_msg("No items found in timerange.")
        all_records_or_time_range = y_or_n("Insert y to analyse all the items stored, insert n if you want to retry with the timerange")
        if all_records_or_time_range:
            return retrieve_link_storage()
        return handle_time_range_question()
    return cached_items

def split_storage_info_and_items(data:dict[str,any]):
    params = data
    link = params.pop('items')
    params.pop('id')
    return params, link


def delete_all_cache():
    links_path = get_storage_directory()
    thread_all_and_resolve([
        threading.Thread(target=delete_file_if_exist, args=(links_path,)),
        threading.Thread(target=delete_file_if_exist, args=(basic_report_path,)),
        threading.Thread(target=delete_file_if_exist, args=(advanced_report_path,)),
        threading.Thread(target=delete_file_if_exist, args=(not_valid_urls,))
    ])

def basic_flow():
    user_data = create_schema_if_not_exist()
    store_link_and_build_basic_report(user_data)
    build_advanced_report = y_or_n("Do you want me to build an advanced report?")
    if build_advanced_report:
        return choose_advanced_criteria()
    else:
        return cached_flow()


def choose_advanced_criteria():
    last_report_or_time_range = ab_input("Would you rather build an advanced report based on the last basic report generation (a) or based on time range (b)?")
    if last_report_or_time_range.lower() == "a":
        params, links = split_storage_info_and_items(get_storage_last_items())
        c_msg(f"""

                          These are the parameters for the advanced report:

                              PARAMS:

                                  {params}

                          """)
        confirm = y_or_n("Do you want to proceed?")
        if confirm:
            generate_advanced_analysis(links)
            sys.exit(0)
        else:
            a = "A"
            return cached_flow()
    elif last_report_or_time_range.lower() == "b":
        full_items = get_storage_in_time_range()
        all_links = []
        for index, item in enumerate(full_items):
            params, links = split_storage_info_and_items(item)
            c_msg(f"""
    
                       Filter {index+1}
    
                           PARAMS:
    
                               {params}
    
                       """)
            all_links.extend(links)
        proceed = y_or_n("Do you want to proceed?")
        if proceed:
            generate_advanced_analysis(all_links)
            sys.exit(0)
        else:
            return cached_flow()


def cached_flow():
    answer = ab_input("Would you rather create a basic report (a) or leverage the information of a previous basic report to produce an advanced report (b)?")
    if answer != "a" and answer != "b":
        return cached_flow()
    elif answer == "a":
        sure = y_or_n("Take note this will override the old basic report. Do you want to proceed?")
        if sure:
            return basic_flow()
        else:
            return cached_flow()
    elif answer == "b":
        sure = y_or_n("Take note this will override the old advanced report. Do you want to proceed?")
        if sure:
            return choose_advanced_criteria() ##filter by the last research or by time range

