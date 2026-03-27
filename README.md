# Python Price Tracker

A lightweight web scraping tool designed to monitor product prices and log historical data.

## Key Features
Automated Data Fetching: Uses BeautifulSoup and Requests to extract real-time price data from e-commerce websites.
Data Cleaning: Implements string filtering to convert raw HTML text into clean, numerical data for analysis.
Historical Logging: Automatically saves price updates with timestamps into a local text file (prices.txt).

## Technologies Used
Python 3,x
BeautifulSoup4 (Web Scraping)
Requests (HTTP Library)

## How It Works
The script sends a request to the target URL, parses the HTML to find the specific price tag, cleans the currency formatting, and appends the result to a tracking file. This allows for long-term price trend monitoring without manual effort.
