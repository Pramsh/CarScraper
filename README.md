# CarScraper

Welcome to CarScraper! This project is a humble exercise in Python scripting, focused on scraping a specific car sales site to help you find cars according to your input. This tool is not intended to be a comprehensive car scraping solution for all sites but serves as a practice ground for scripting, queue management, and multi-threading.

## Usage Disclaimer

**Important:** CarScraper is intended solely for personal use and educational purposes. It is designed to scrape data from a specific car sales site to help users find cars with special deals. The script is not intended for any malicious activities or other unethical practices. The creator of CarScraper is not responsible for any misuse or legal consequences that may arise from improper use of this script.

If you intend to use this script or any modifications of it for purposes other than personal use or learning, please ensure you have the necessary permissions and adhere to ethical guidelines.

Thank you for using CarScraper responsibly.

## Introduction

CarScraper is designed to scrape car listings from a particular site, allowing users to filter results based on their preferences. The application is currently functional on Windows, with plans to support Linux in the near future.

## Configuration and Storage

### Where to Store the App

Place the folder in the `C:\Users\<user>` directory or any subfolder within that directory.

### Schema

During usage, you'll be prompted to enter filters for car scraping. The application will generate a JSON schema that describes your input and save it to `./schema/car_schema.json`. This schema will be proposed for subsequent scraping sessions. **Note: A new schema will overwrite the existing one.**

### Link Storage

Scraped car data is saved to `C:\Users\<user>\car_storage.json`. This file serves as a cache to bypass basic report generation and directly build advanced reports from previous scrapes. 

### Reports

Reports are created in the `report` directory and come in two types:

* **Basic Report**: Scrapes PLPs (Product Listing Pages) based on the filters specified in `./schema/car_schema.json`.
* **Advanced Report**: Scrapes PDPs (Product Detail Pages) from the links collected in the basic report. Advanced reports can be generated for a specified time range.

The storage logic is straightforward: Each new basic report adds an item to `C:\Users\<user>\car_storage.json`. The structure of these items is as follows:

```json
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
When generating a new report, URLs are checked against those already stored to prevent duplication and excessive data usage. This feature also supports daily automation to return only recent updates.

Frequent cache clearing is recommended if the system is not automated.

## Future Improvements

**User:**
- Add more filters to the schema.
- Enable filtering of links based on the schema.

**System:**
- Implement multi-threaded and queued management for advanced reports, similar to basic reports.
