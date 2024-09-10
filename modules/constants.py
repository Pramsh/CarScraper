PREFIX = "https://www.autoscout24.it"
car_schema = "./schema/car_schema.json"

basic_report_path = "./report/basic_report.json"
advanced_report_path = "./report/advanced_report.json"
not_valid_urls = "./report/not_valid_urls.json"

base_storage_path = "C:/Users/"
storage_file_name = "car_storage.json"

fuel: dict[str, str] = {
    "diesel": "D",
    "gasoline": "B",
    "gpl":  "L",
    "methane": "C"
}

params: dict[str, str] = {
    "brand": "Insert a brand",
    "fuel": "Insert a fuel type",
    "price": "Insert a price below you want to stay"
}

brand_list: list[str] = ["volkswagen", "mercedes-benz", "volvo", "toyota", "honda","bmw","audi"]



sample_links = ['/annunci/volvo-v70-2-5-ft-summum-gpl-scadenza-2034-gpl-beige-6e964f5c-d9b7-4934-9a51-97a6b50d1c19', '/annunci/volvo-v50-gpl-valido-auto-come-nuova-gpl-bianco-9fa953b4-0fee-45a4-8a7f-934c8fd30efb', '/annunci/volvo-v50-2-0f-polar-trifuel-gpl-gpl-grigio-921c22cd-a0e6-4d4d-a00a-7a06af6a02d7', '/annunci/volvo-v50-drive-momentum-1-8-f-gpl-benzina-trifuel-gpl-argento-687f3e91-bb8b-4adc-8ded-938a202806f0', '/annunci/volvo-s70-v70-2-0-r-awd-226cv-gpl-gpl-blu-azzurro-f5c8e346-e82b-4149-98c0-6bca5c06255b', '/annunci/volvo-940-volvo-940-945-polar-gpl-verde-a154afc0-7ec4-4925-b5ca-5336d6881890', '/annunci/volvo-s60-2-4t-optima-gpl-argento-e63844eb-79cc-4c74-b955-0c1ee868500c', '/annunci/volvo-850-850-sw-2-0i-s-a-t5-20v-gpl-grigio-b0940d7e-6c0c-4b54-9e41-74d1fd1e1d7e', '/annunci/volvo-240-polar-gpl-bianco-9df06136-4d2d-4070-96c7-e16f8f00ed53', '/annunci/volvo-480-1-7t-c-abs-clima-cat-gpl-verde-dae66e8e-e141-41ed-877e-47e176a456d6', '/annunci/volvo-c70-c70-i-1997-cabrio-2-0-163cv-gpl-grigio-b5891011-f390-43ad-9f94-efda9e75cd62', '/annunci/volvo-v50-2-0f-polar-trifuel-gpl-gpl-argento-5a659f55-75c3-45b9-af50-90fb2cebe4fa', '/annunci/volvo-v50-v50-1-6d-momentum-gpl-argento-c1a6e2ee-96d9-47c7-90cd-d841154713d5', 'https://www.autoscout24.it/lst/volvo/c30', 'https://www.autoscout24.it/lst/volvo/c40', 'https://www.autoscout24.it/lst/volvo/ex30', 'https://www.autoscout24.it/lst/volvo/s60', 'https://www.autoscout24.it/lst/volvo/v40', 'https://www.autoscout24.it/lst/volvo/v40-cross-country', 'https://www.autoscout24.it/lst/volvo/v50', 'https://www.autoscout24.it/lst/volvo/v60', 'https://www.autoscout24.it/lst/volvo/v60-cross-country', 'https://www.autoscout24.it/lst/volvo/v70', 'https://www.autoscout24.it/lst/volvo/v90', 'https://www.autoscout24.it/lst/volvo/v90-cross-country', 'https://www.autoscout24.it/lst/volvo/xc40', 'https://www.autoscout24.it/lst/volvo/xc60', 'https://www.autoscout24.it/lst/volvo/xc90']
