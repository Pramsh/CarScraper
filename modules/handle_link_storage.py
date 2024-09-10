import json
import os
import sys
from datetime import datetime

from modules.common_fun import c_msg
from modules.constants import base_storage_path, storage_file_name
import uuid

def get_storage_directory():
    try:
        psw = os.getcwd()
        normalized_path = psw.replace("\\", "/")
        if base_storage_path in normalized_path:
            storage_directory =  base_storage_path + normalized_path.replace(base_storage_path,"").split("/")[0] + "/" + storage_file_name
            return storage_directory
    except Exception as e:
        c_msg("This script is currently available just for Windows")
        sys.exit(1)

def is_valid_url(link: str):
    return True if "/annunci/" in link else False


def link_filter(links:list[str],storage_directory:str):
    links = [ l for l in links if is_valid_url(l)]
    links = set(links)
    if os.path.exists(storage_directory):
        with open(storage_directory, "r", encoding="utf-8") as f:
            data = json.load(f)
            car_links = [ l for d in data for l in d["items"]]
        car_links = set(car_links)
        links = links - car_links
    else:
        with open(storage_directory, "w", encoding="utf8") as f:
            json.dump([], f)
    return list(links)



def handle_link_storage(links:list[str], user_data):
    storage_directory = get_storage_directory()
    link_to_store = link_filter(links,storage_directory)
    _id = uuid.uuid4()
    storage_payload = {
        "id": str(_id),
        "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "filter_schema":user_data,
        "items": link_to_store
    }
    with open(storage_directory, "r+", encoding='utf-8') as f:
        file_content = json.load(f)
        file_content.append(storage_payload)
        f.seek(0)
        json.dump(file_content, f, indent=4)
        print(f"Sys... data stored in {storage_directory}")


