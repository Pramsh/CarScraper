# Introduction
This is CarScraper and it's built for those who want a Car with a special deal

## Config and Storage

### Where to store the app
The script goes in the ```C:\Users\<user>``` directory or in a subfolder of that directory

### Schema
Within the usage of the application you'll be asked to insert filters for the car scraping. Once you've given you're preferences the system will generate a JSON schema describing you're input in  ```./schema/car_schema.json```. This schema will be suggested to be retrieve every time you'll perform a new scraping. **Note: if you create a new schema, it will replace the old one**

### Link storage
Every car analysed goes in the file ```C:\Users\<user>\car_storage.json```. This file is used for caching purpose and allows to skip the basic report and build directly an advance one, on the top of the scrapings you made last times.

### Reports
The reports will be created under the report directory. Reports are of two kinds:
* **basic report**: scraping of the PLPs of the cars according to the filters stored in ```./schema/car_schema.json```
* **advanced report**: scraping of the PDPs according to the links scraped within the PLPs in the **basic report**. Advanced report can be performed even on a time range.







The logic behind the storage is easy. Every time a new basic report is generated, a new item is added to the JSON present in the ```C:\Users\<user>\car_storage.json``` file mentioned above.
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

The storage of these items is useful to retrieve items based on a *time range* and soon also *id*, or *filter_schema*.

I recommend allow the system to delete the cache more frequently if it's not used behind an automation.


### Future improvements
#### User:
* Add filters to schema
* Give the possibility to filter the links by schema
  
#### Sys:
* Manage the advanced report in multi thread and queues like the basic report

