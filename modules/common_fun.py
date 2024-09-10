import os.path
from threading import Thread
from time import sleep
from datetime import datetime
import requests
import bs4

def parse_html_by_link(link:str, retry = 3):
    try:
        response = requests.get(link)
        response.raise_for_status()
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        return soup
    except Exception as e:
        print(e)
        if retry > 0:
            sleep(2)
            return parse_html_by_link(link, retry -1)

def c_msg(msg:str):
    print(msg)
    sleep(1)


def is_in_list(array_list,element):
    return any(x == element for x in array_list)

def delete_file_if_exist(path:str):
    if os.path.exists(path):
        os.remove(path)


def validate_date(date_text, nullable=True):
    try:
        if nullable and date_text == "":
            return True
        if date_text != datetime.strptime(date_text, "%d-%m-%Y").strftime('%d-%m-%Y'):
            raise False
        return True
    except ValueError:
        return False


def thread_all(thread_list: list[any]) -> list[any]:
    for t in thread_list:
        t.start()
    return thread_list

def thread_all_and_resolve(threads: list[Thread]):
    for promise in thread_all(threads):
        promise.join()

def filter_link_from_items(data):
    items = []
    if len(data) != 0:
        for item in data:
            items.extend(item["items"])
    return items

def ab_input(msg):
    answer = input(
        f"\n{msg}\nAnswer with 'a' or 'b'\n")
    if answer != "a" and answer != "b":
        return ab_input(msg)
    return answer
