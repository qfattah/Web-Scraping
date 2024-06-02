# Web Scraping and Analytics for PlayStation and Xbox Released Games

This project aims to scrape data from the [VGChartz](https://www.vgchartz.com/) website to analyze and visualize the sales and release dates of PlayStation and Xbox games. The project involves web scraping, data pre-processing, and various visualizations to provide insights into the gaming industry.

You can review the code here: [VGCharts_Web_Scraping](https://github.com/qfattah/Web-Scraping/blob/master/VGcharts_PS_Xbox_Scrape.ipynb)

## Table of Contents
- [Introduction](#introduction)
- [Setup](#setup)
- [Web Scraping](#web-scraping)
- [Data Pre-Processing](#data-pre-processing)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Conclusion](#conclusion)

## Introduction

The project involves the following steps:
1. **Importing Libraries**: Importing necessary libraries for web scraping, data processing, and visualization.
2. **Web Scraping**: Scraping the VGChartz website to collect data on PlayStation and Xbox games.
3. **Data Pre-Processing**: Cleaning and transforming the scraped data for analysis.
4. **Exploratory Data Analysis (EDA)**: Analyzing the data and creating visualizations to understand trends and patterns.

## Setup

### Prerequisites
- Python 3.x
- Jupyter Notebook

### Libraries
Install the required libraries using pip:
```bash
pip install requests beautifulsoup4 pandas tqdm numpy matplotlib seaborn
```
## Web Scraping Code Sections

Defining the URL: The URL of the website to scrape.
Requesting a Response: Requesting a response from the URL to get the HTML data.
Parsing HTML Content: Using BeautifulSoup to parse the HTML content.
Selecting Consoles: Selecting PlayStation and Xbox consoles and extracting the relevant data.
Data Pre-Processing

## Data Pre-Processing

### Fixing N/A Values
N/A values in the dataset are replaced with NaN to correctly represent missing data.

### Transforming Numeric Columns
Numeric columns that include "m" (indicating millions) are transformed to numeric values for accurate analysis.

### Fixing the Release Date Column
Release date formats are standardized and converted to datetime objects.

### Mapping Console Keys to Names
Console keys are mapped to their respective names for easier analytics.

## Exploratory Data Analysis

### Number of Games Published Per System
A bar plot showing the number of games published for each system.

### Compare Number of Games Published for Xbox vs. PlayStation
A comparison of the number of games published for all Xbox and PlayStation systems.

### Top Selling Games Per Console
A visualization of the top 3 selling games for each console.

### Console Sales Over Time
A time series analysis of the total shipped units over time for PlayStation and Xbox systems.

## Conclusion

The analysis provides insights into the gaming industry, specifically focusing on PlayStation and Xbox consoles. The data shows trends in game releases, sales performance, and comparisons between different gaming systems.
