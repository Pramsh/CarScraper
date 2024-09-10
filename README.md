
# CarScraper

**CarScraper** is a Python-based web scraping application designed to help users find cars with special deals from various websites. By leveraging BeautifulSoup and Requests, the app scrapes car listings based on user-defined filters, stores the data in an organized structure, and generates both basic and advanced reports.

## Features
- **Filter-based scraping**: Specify custom filters (e.g., fuel type, brand, price) to target specific cars.
- **Report generation**: Create basic and advanced reports based on the cars scraped, offering detailed insights.
- **Data caching**: Prevents redundant scraping and optimizes data retrieval through JSON-based caching.
- **Time range filtering**: Allows retrieving cars scraped within a specific time period.

---

## Installation and Setup

### Prerequisites
To run this application, you need:
- Python 3.x installed on your system
- Install required Python libraries:
  ```bash
  pip install requests beautifulsoup4
  ```

### Directory Setup
Store the application script in the following location on your system:
```C:\Users\<user>``` or a subdirectory of it. The app relies on this folder structure for storage and configuration.

---

## Usage

### Configuration and Input Schema
On the first run, you'll be prompted to provide filters for the scraping, such as car brand, fuel type, and price range. These preferences are stored in a JSON file at:
```
./schema/car_schema.json
```
Each time you start a new scraping session, this schema will be suggested for reuse. If you create a new schema, it will replace the previous one.

### Link Storage (Caching)
Every car link scraped is saved in:
```
C:\Users\<user>\car_storage.json
```
This file caches the car listings to avoid scraping the same links repeatedly. The stored links allow for efficient retrieval and advanced reporting based on past scraping sessions.

---

## Reports

### Basic Report
The basic report scrapes car listings (PLPs) according to the filters defined in `car_schema.json`. It provides a high-level overview of the cars matching your filters.

### Advanced Report
The advanced report scrapes detailed car pages (PDPs) for the links stored in the basic report. You can also perform an advanced report on a specific time range to capture only the most recent listings.

### Report Storage
Reports are stored in the `./report` directory:
- **Basic report**: Generated after scraping the listing pages (PLPs).
- **Advanced report**: Generated based on the links from basic reports, offering detailed insights.

---

## Data Structure

The storage structure for cached data is as follows, located in `C:\Users\<user>\car_storage.json`:
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
        "url1",
        "url2",
        "..."
    ]
}
```
This data structure ensures that duplicates are avoided and the app can retrieve items based on time ranges. It's recommended to allow frequent cache cleanups if the app is not automated.

---

## Future Improvements

### User Features
- **Additional filters**: Add more customizable filters to the schema for more precise scraping.
- **Link filtering**: Enable filtering of stored car links based on the filter schema.

### System Features
- **Multithreading**: Implement multithreaded and queued processing for advanced reports to enhance performance, similar to the basic report.

---

## License
This project is licensed under the MIT License.

---

This README provides a quick start and overview of the CarScraper application. Follow the instructions to set up, use, and explore the scraping capabilities efficiently!
