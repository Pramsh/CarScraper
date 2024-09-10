from modules.basic_and_advance_report import get_stored_links
from modules.get_inputs import y_or_n
from modules.handle_interraction import cached_flow, delete_all_cache, basic_flow



def main():
    cached_items = get_stored_links()
    if len(cached_items) > 0:
        delete_data = y_or_n("There is already some data in your storage, do you want to delete it?")
        if delete_data:
            delete_all_cache()
            return basic_flow()
        else:
            return cached_flow()
    else:
        return basic_flow()





if __name__ == "__main__":
    main()
