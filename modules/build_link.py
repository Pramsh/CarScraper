from modules.constants import fuel
def build_link(fuel_key: str or "", brand: str or "", price:str or "", page=1):
    """"
    This function is used to dinamically build the target link to scrape
    """
    return f"https://www.autoscout24.it/lst/{brand}?atype=C&cy=I&damaged_listing=exclude&desc=0&fuel={fuel.get(fuel_key, '')}&mmvco=1&page={page}&powertype=hp&priceto={price}"



# path = idBrand + %7C%7C%7C%2C + idBrand + %7C%7C%7C
# audi_bmw_vw = "https://www.autoscout24.it/lst?fuel=D&mmmv=9%7C%7C%7C%2C13%7C%7C%7C%2C74%7C%7C%7C&mmvco=1&powertype=hp&sort=standard&ustate=N%2CU"
# audi_bmw = "https://www.autoscout24.it/lst?fuel=D&mmmv=13%7C%7C%7C%2C9%7C%7C%7C&mmvco=1&powertype=hp&search_id=24afzwm1ag9&sort=standard&ustate=N%2CU"
# audi = "https://www.autoscout24.it/lst/audi?fuel=D&mmvco=1&powertype=hp&search_id=6uwzpstty2&sort=standard&ustate=N%2CU"
#9 AUDI
#13 BMW
#74 VW
