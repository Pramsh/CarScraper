from modules.constants import PREFIX


def get_attribute(html_el, tag, class_attr=None):
    if class_attr:
        attr_tag = html_el.find(tag, class_=class_attr)
        return attr_tag.get_text() if attr_tag else ""
    else:
        attr_tag = html_el.find(tag)
        return attr_tag.get_text() if attr_tag else ""

def get_model(html_el, advanced=False):
    return get_attribute(html_el, "h2") if not advanced else get_attribute(html_el, "div", "StageTitle_modelVersion__Yof2Z")

def get_brand(html_el, advanced=False):
    return "" if not advanced else get_attribute(html_el, "span","StageTitle_boldClassifiedInfo__sQb0l")

def get_location(html_el):
    return get_attribute(html_el, "a", "LocationWithPin_locationItem__tK1m5")

def get_price(html_el, advanced=False):
    return get_attribute(html_el, "p", "PriceAndSeals_current_price__ykUpx") if not advanced else get_attribute(html_el, "span", "PriceInfo_price__XU0aF")

def is_valid(value):
    if value != "" and value != " " and value is not None:
        return True
    else:
        return False

def validate_grouped_attr(att):
    return att.get_text() if is_valid(att) else ""


def get_grouped_attributes(html_el):
    all_attr = html_el.find_all("span", class_="VehicleDetailTable_item__4n35N")
    return {
        "km": validate_grouped_attr(all_attr[0]),
        "gears": validate_grouped_attr(all_attr[1]),
        "year": validate_grouped_attr(all_attr[2]),
        "fuel": validate_grouped_attr(all_attr[3]),
        "CV": validate_grouped_attr(all_attr[4]),
    }

def get_seller_info_name(html_el):
    return get_attribute(html_el, "span","SellerInfo_name__nR9JH")

def get_features(html_el):
    return get_attribute(html_el, "span","ListItem_subtitle__VEw08")

def get_link(html_el):
    attr = html_el.find("a", class_="ListItem_title__ndA4s")
    return PREFIX + attr.get("href") if attr else ""


def get_table_key_and_values(table, dt_class, dd_class):
    try:
        all_keys = table.find_all("dt", class_=dt_class)
        all_values = table.find_all("dd", class_=dd_class)
        res = {}
        for index, key in enumerate(all_keys):
            item = {
                f"{key.get_text()}":f"{all_values[index].get_text()}"
            }
            res.update(item)
        return res
    except Exception as e:
        print(e)
        raise e

def get_grouped_fixed_info(html_el):
    box = html_el.find("div", class_="VehicleOverview_containerMoreThanFourItems__691k2")
    if box:
        all_spec_html_el = box.find_all("div","VehicleOverview_itemText__AI4dA")
        km, transmission, year, fuel, power, seller = [ s.get_text() for s in all_spec_html_el ]
        return {
            "km":km,
            "transmission":transmission,
            "year":year,
            "fuel":fuel,
            "power":power,
            "seller":seller
        }
    return {}

def get_fixed_info(html_el):
    return {
        "brand":get_brand(html_el, True),
        "model":get_model(html_el,True),
        "price": get_price(html_el, True),
        "location": get_location(html_el),
        **get_grouped_fixed_info(html_el)
    }

def get_all_grouped_attributes(html_el, dl_class, h2_class, dt_class, dd_class):
    all_section_container = html_el.find_all("section", class_="DetailsSection_container__68Nlc")
    res = []
    for container in all_section_container:
        title = container.find("h2", class_=h2_class) or None
        table = container.find("dl", class_=dl_class)
        if title is not None and table:
            res.append({
                f"{ title.get_text()}": get_table_key_and_values(table, dt_class, dd_class)
            })
    return {
        **get_fixed_info(html_el),
        "specifications": res
    }

def car_details_attr(html_el):
    return get_all_grouped_attributes(html_el, "DataGrid_defaultDlStyle__xlLi_", "DetailsSectionTitle_text__KAuxN","DataGrid_defaultDtStyle__soJ6R", "DataGrid_defaultDdStyle__3IYpG")
