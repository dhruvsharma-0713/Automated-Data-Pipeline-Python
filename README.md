# Automated-Data-Pipeline-Python
An Automated Python Script that scrapes, clean, and visualizes data from 'Wikipedia's List of Largest Cities' Page.

# Automated Wikipedia Data Scraper & Visualizer

### Overview
This repository contains a complete, automated data pipeline built in Python. The system scrapes tabular data from Wikipedia's "List of largest cities" page, cleans the data, generates a data visualization, and is scheduled to run automatically.

### Features
**Automated Data Scraping:** Connects to Wikipedia and extracts the main data table using the `requests` and `pandas` libraries.
**Data Cleaning & Processing:** Prepares the raw scraped data for analysis by cleaning and converting data types.
**Data Visualization:** Creates a professional bar chart of the "Top 10 Most Populous Cities" using `Matplotlib` and saves it as a PNG image.
**Full Automation & Scheduling:** Includes a main script (`main.py`) that uses the `schedule` library to run the entire data pipeline automatically at a set time.

### Technologies Used
**Language:** `Python`
**Libraries:** `pandas`, `requests`, `matplotlib`, `schedule`

### How to Run
1.  Ensure you have Python and the required libraries installed (`pip install pandas requests matplotlib schedule`).
2.  To run the full automated system, execute the main controller script from your terminal: `python main.py`
3.  To run just a single instance of the scraper and visualizer, run: `python scraper.py`

### Project Output
The script generates two files:
1.  `largest_cities.csv`: A clean CSV file containing the scraped data.
2.  `top_10_cities_population.png`: An image of the generated bar chart.
