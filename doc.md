# Introduction
This is 2HAutoScraper and it's built for those who want a Car with a special deal
https://www.autoscout24.it/lst/mercedes-benz?atype=C&cy=I&damaged_listing=exclude&desc=0&mmvco=1&powertype=kw&search_id=2z2hou64ls&sort=standard&ustate=N%2CU
mi salvo i dati della filter in un oggetto nella solita cartella, e vado a riprendermi le informazioni all'apertura
marca
fuel = {
    "diesel":"D",
    "ga[get_inputs.py](modules%2Fget_inputs.py)soline":"B",
    "gpl":"L",
    "methane":"C",
}

&fuel=C%2CD

## Config and Storage

### Where to store the app
The script goes in the ```C:\Users\<user>``` directory or in a subfolder of that directory

### Link storage
Every car analysed goes in the file ```C:\Users\<user>\car_storage.json```

The logic behind the storage is easy. Every time a new basic report is generated, a new item is added to the array obj present in the file mentioned above.
The structure of the items looks like this:
```
    {
        "id": "7a2a5cf6-19f6-45ed-857f-e4ebc837b54f",
        "timestamp": "2024-09-08 03:45:11",
        "filter_schema": {
            "fuel": "diesel",
            "brand": "bmw",
            "price": "20000"
        },
        "items": [
            "url",
            "url",
            ...
        ]
    }    
```
When you generate a new report there is a check on the URLs already stored, to avoid duplications and too much data usage. This also allows to bind this app to a daily automation which returns just the recent updated cars.

The storage of these items is useful to retrieve them based on a *time range*, *id*, or *filter_schema*.

I recommend allow the system to delete the cache more frequently if it's not used behind an automation.
