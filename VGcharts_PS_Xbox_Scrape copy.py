{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Web Scraping and Analytics for Playstation and Xbox  Released Games"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Importing the Libraries"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests # Importing requests to perform a request and response and get the html data from the website\n",
    "from bs4 import BeautifulSoup # Importing BeautifulSoup to perform html scraping\n",
    "import pandas as pd # Importing pandas to store the data in a dataframe for further processing \n",
    "from tqdm import tqdm  # Import the tqdm to show progress in for for loops\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "import matplotlib.dates as mdates"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Web Scraping"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Selecting Playstation and Xbox consoles"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The general steps to performing web scraping are:\n",
    "\n",
    " 1. Define the URL\n",
    " 2. Request a response from the URL and verify the code\n",
    " 3. Define the content of the response in a variable (usually 'html')\n",
    " 4. Define a BeautifulSoup instance\n",
    " 5. Utilize manual inspection and find_all function to scrap through the data\n",
    " 6. Create a URL for the scrape process\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# URL of the website to scrape\n",
    "url = \"https://www.vgchartz.com/gamedb/games.php\"\n",
    "\n",
    "# Define the response and print it to confirm webage retreival\n",
    "\n",
    "response = requests.get(url)\n",
    "print(response.status_code)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Parse the HTML website in preparation to scrape the data\n",
    "\n",
    "html = response.content\n",
    "soup = BeautifulSoup(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# This code is searching for a < select > element in the HTML document with the attribute name set to 'console', meaning it's looking for values in the console drop-down menu\n",
    "# The \"console\" attribute was found by inspecting the website, below a screenshot:\n",
    "\n",
    "console_select = soup.find('select', {'name': 'console'})"
   ]
  },
  {
   "attachments": {
    "image.png": {
     "image/png": "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"
    }
   },
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "![image.png](attachment:image.png)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Here we can see that we have all the values of the consoles in the \"console_select\" element. \n",
    "\n",
    "if console_select:\n",
    "    # Loop through the option elements\n",
    "    for option in console_select.find_all('option'):\n",
    "        # Print the value attribute of each option\n",
    "        print(option.get_text())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# We need to extract the text and the value pairs for each xbox and playstation options\n",
    "# I will create a dictionary comrehension to extract the options\n",
    "\n",
    "if console_select:\n",
    "    # Create a dictionary comprehension to extract the options starting with 'xbox' or 'playstation'\n",
    "    desired_consoles = {option.get_text(): [option.get('value'), 1] \n",
    "                       for option in console_select.find_all('option') \n",
    "                       if option.get('value') and (option.get_text().lower().startswith('xbox') or option.get_text().lower().startswith('playstation'))}\n",
    "\n",
    "    print(desired_consoles)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## Here I am creating a output text that will look like a dictionary\n",
    "## This way I can just copy the code in the box below to get the console selection I want\n",
    "\n",
    "print(\"Desired_Consoles = {\")\n",
    "for key, value in desired_consoles.items():\n",
    "    print(f'\"{key}\"'.ljust(40), ':', value,\",\")\n",
    "\n",
    "print(\"}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Defining Scrape Parameters and Scrape URL"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "When a search is performed on the website, the parameters of the search are defined in the URL, we will need to pre-specify those parameters to successfully pull the correct view"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Find all the parameters that will define the view of the website:\n",
    "# I created this list to ensure correctly spelling in defining parameters\n",
    "\n",
    "list_of_element_types = ['input', 'select']\n",
    "\n",
    "for element_type in list_of_element_types:\n",
    "    # Find elements of the current type\n",
    "    if element_type == 'input':\n",
    "        # For input elements, filter by type\n",
    "        element_elements = soup.find_all(element_type, {'type': ['text', 'checkbox']})\n",
    "    else:\n",
    "        # For select elements, just find all select elements\n",
    "        element_elements = soup.find_all(element_type)\n",
    "    \n",
    "    # Extract and print the name of each element\n",
    "    for element in element_elements:\n",
    "        element_name = element.get('name')\n",
    "        if element_name:\n",
    "            print(f\"{element_type.capitalize()} Element Name:\", element_name)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def open_url(system_desired):\n",
    "    '''\n",
    "    Here we will create the URL for the scrape process. You may want to change some parameters if wanted\n",
    "    \n",
    "    '''\n",
    "    base_url = \"https://www.vgchartz.com/games/games.php?\"\n",
    "    params = {\n",
    "        'name': '',\n",
    "        'keyword': '',\n",
    "        'console': '',  # Placeholder for the console name\n",
    "        'region': 'All',\n",
    "        'developer': '',\n",
    "        'publisher': '',\n",
    "        'goty_year': '',\n",
    "        'genre': '',\n",
    "        'boxart': 'Both',\n",
    "        'banner': 'Both',\n",
    "        'ownership': 'Both',\n",
    "        'showmultiplat': 'Yes',\n",
    "        'results': '100000',         ## put a huge value here to get all the results in one page\n",
    "        'order': 'TotalShipped',\n",
    "        'showtotalsales': '1',\n",
    "        'showpublisher': '0',\n",
    "        'showvgchartzscore': '0',\n",
    "        'shownasales': '1',\n",
    "        'showdeveloper': '0',\n",
    "        'showcriticscore': '0',\n",
    "        'showpalsales': '1',\n",
    "        'showreleasedate': '1',\n",
    "        'showuserscore': '0',\n",
    "        'showjapansales': '1',\n",
    "        'showlastupdate': '0',\n",
    "        'showothersales': '1',\n",
    "        'showshipped': '1'\n",
    "    }\n",
    "\n",
    "    params['console'] = system_desired  # Set the console parameter\n",
    "    console_url = base_url + '&'.join([f\"{k}={v}\" for k, v in params.items()])\n",
    "    response = requests.get(console_url)\n",
    "    html = response.content\n",
    "    soup = BeautifulSoup(html, 'html.parser')\n",
    "    games_table_in = soup.find('div', id='generalBody')\n",
    "    rows_in = games_table_in.find_all('tr', style=True)  # Retrieve all the rows first to count them\n",
    "\n",
    "    return rows_in\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Scraping The Data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "games_data = []\n",
    "# Use tqdm to wrap the iteration and provide a progress bar\n",
    "\n",
    "#For each console in our desired_console list\n",
    "for console in tqdm(desired_consoles.keys(), desc=\"looking in systems\", unit = \"system\"):\n",
    "    # we check if the user selected \"1\" (as in \"I want to scrape data from this console\")\n",
    "    if desired_consoles[console][-1] == 1:\n",
    "        #we open the url for the console\n",
    "        rows = open_url(desired_consoles[console][0])\n",
    "        #and download every row data\n",
    "        for game_row in tqdm(rows, desc=\"Scraping games for \"+ console , unit=\"row\"):\n",
    "            cells = game_row.find_all('td')\n",
    "            system_image = cells[3].find('img')  # Find the <img> tag within the System cell\n",
    "            system = system_image['alt'] if system_image and 'alt' in system_image.attrs else 'No system info'  # Get the alt text or a default\n",
    "            game_image_url = cells[1].find('img')['src'] if cells[1].find('img') else 'N/A'\n",
    "\n",
    "            if len(cells) > 1:  # This checks if the row is not a header or empty\n",
    "                game_info = {\n",
    "                    'Game Name': cells[2].get_text(strip=True),\n",
    "                    'Image_URL': \"https://www.vgchartz.com\"+game_image_url,\n",
    "                    'System': system,\n",
    "                    'Total Shipped': cells[4].get_text(strip=True),\n",
    "                    'Total Sales': cells[5].get_text(strip=True),\n",
    "                    'NA Sales': cells[6].get_text(strip=True),\n",
    "                    'PAL Sales': cells[7].get_text(strip=True),  \n",
    "                    'Japan Sales': cells[8].get_text(strip=True),\n",
    "                    'Other Sales': cells[9].get_text(strip=True),\n",
    "                    'Release Date': cells[10].get_text(strip=True)\n",
    "                }\n",
    "                games_data.append(game_info)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Data Pre-Processing"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Create a DataFrame from the games data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.DataFrame(games_data)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Fixing N/As"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can see that N/A represents missing data so it needs to be correctly represented in the DataFrame as NaN"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# We replace \"N/A\" with NaN\n",
    "\n",
    "df.replace('N/A', np.nan, inplace=True)\n",
    "\n",
    "# Check again\n",
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Pandas recognizes Nulls correctly now"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Fix the Numeric Columns"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The Numeric columns (Total Shipped, Total sales, etc.) include \"m\" in the end indicating the unit in millions, this needs to be removed to make them numeric fields"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# List of columns to transform\n",
    "columns_to_transform = ['Total Shipped', 'Total Sales', 'NA Sales', 'PAL Sales', 'Japan Sales', 'Other Sales']\n",
    "\n",
    "for col in columns_to_transform:\n",
    "    # Remove 'm' and convert to numeric for each column in the list\n",
    "    df[col] = df[col].str.replace('m', '').astype(float)\n",
    "\n",
    "df"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Fix the Release Date Column"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Remove 'th', 'st', 'nd', 'rd' suffixes from the 'Release Date' column\n",
    "df['Release Date'] = df['Release Date'].str.replace(r'(\\d+)(st|nd|rd|th)', r'\\1', regex=True)\n",
    "\n",
    "# Convert the 'Release Date' column to datetime\n",
    "df['Release Date'] = pd.to_datetime(df['Release Date'], format='%d %b %y')\n",
    "\n",
    "df"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Map the Console Keys to their Names for Easier Analytics"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Mapping dictionary based on the provided image\n",
    "console_mapping = {\n",
    "    'PS': 'PlayStation',\n",
    "    'PS2': 'PlayStation 2',\n",
    "    'PS3': 'PlayStation 3',\n",
    "    'PS4': 'PlayStation 4',\n",
    "    'PS5': 'PlayStation 5',\n",
    "    'PSN': 'PlayStation Network',\n",
    "    'PSP': 'PlayStation Portable',\n",
    "    'PSV': 'PlayStation Vita',\n",
    "    'XB': 'Xbox',\n",
    "    'X360': 'Xbox 360',\n",
    "    'XBL': 'Xbox Live',\n",
    "    'XOne': 'Xbox One',\n",
    "    'XS': 'Xbox Series'\n",
    "}\n",
    "\n",
    "# Replace the keys in the 'System' column with the corresponding names\n",
    "df['System'] = df['System'].replace(console_mapping)\n",
    "\n",
    "# Remove PSN and Xbox Live as they're not consoles\n",
    "df = df[df['System'] != 'PlayStation Network'] \n",
    "df = df[df['System'] != 'Xbox Live'] \n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Exploratory Data Analysis - EDA"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Explore the Number of Games Published Per System"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Explore the Number of Games Published by System\n",
    "\n",
    "# Count the number of games published by each system\n",
    "game_counts = df['System'].value_counts()\n",
    "\n",
    "# Plot the data using matplotlib\n",
    "plt.figure(figsize=(10, 6))\n",
    "sns.barplot(x=game_counts.index, y=game_counts.values, palette='viridis')\n",
    "plt.title('Number of Games Published by System')\n",
    "plt.xlabel('System')\n",
    "plt.ylabel('Number of Games')\n",
    "plt.xticks(rotation=45)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Compare Number of Games Published for Xbox vs. Playstation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Define Xbox and PlayStation systems\n",
    "xbox_systems = ['Xbox', 'Xbox 360', 'Xbox Live', 'Xbox One', 'Xbox Series']\n",
    "playstation_systems = [\n",
    "    'PlayStation', 'PlayStation 2', 'PlayStation 3', 'PlayStation 4',\n",
    "    'PlayStation 5', 'PlayStation Network', 'PlayStation Portable', 'PlayStation Vita'\n",
    "]\n",
    "\n",
    "# Filter and count the number of games for each system\n",
    "xbox_count = df[df['System'].isin(xbox_systems)].shape[0]\n",
    "playstation_count = df[df['System'].isin(playstation_systems)].shape[0]\n",
    "\n",
    "# Prepare data for visualization\n",
    "comparison_data = pd.DataFrame({\n",
    "    'System': ['Xbox', 'PlayStation'],\n",
    "    'Count': [xbox_count, playstation_count]\n",
    "})\n",
    "\n",
    "# Plot the data\n",
    "plt.figure(figsize=(10, 6))\n",
    "sns.barplot(x='System', y='Count', data=comparison_data, palette='viridis')\n",
    "plt.title('Number of Games Published by System')\n",
    "plt.xlabel('System')\n",
    "plt.ylabel('Number of Games')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Explore Top Selling Games Per Console"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Replace 'm' with an empty string and fill NaN values with 0\n",
    "df['Total Shipped With Zeros'] = df['Total Shipped'].fillna(0)\n",
    "\n",
    "# Define function to get top N games for each system\n",
    "def get_top_n_games(df, n=3):\n",
    "    return df.groupby('System').apply(lambda x: x.nlargest(n, 'Total Shipped With Zeros')).reset_index(drop=True)\n",
    "\n",
    "# Get top 3 games for each system\n",
    "top_games = get_top_n_games(df, n=3)\n",
    "\n",
    "# Rank the games within each console\n",
    "top_games['Rank'] = top_games.groupby('System')['Total Shipped With Zeros'].rank(method='first', ascending=False)\n",
    "\n",
    "# Create a mapping for game names based on the system name and game name\n",
    "top_games['GameRank'] = top_games.apply(lambda x: f\"{x['System']} {x['Game Name']}\", axis=1)\n",
    "# Define a color palette for ranks\n",
    "rank_palette = {1.0: '#FFD700', 2.0: '#C0C0C0', 3.0: '#CD7F32'}  # Gold, Silver, Bronze\n",
    "\n",
    "# Create a new column for colors based on rank\n",
    "top_games['Color'] = top_games['Rank'].map(rank_palette)\n",
    "\n",
    "# Plot the data\n",
    "plt.figure(figsize=(14, 8))\n",
    "\n",
    "# Use the color column for the palette\n",
    "sns.barplot(x='System', y='Total Shipped With Zeros', hue='GameRank', data=top_games, dodge=False, palette=top_games['Color'].tolist())\n",
    "\n",
    "plt.title('Top 3 Selling Games on Each Console')\n",
    "plt.xlabel('System')\n",
    "plt.ylabel('Total Shipped (in millions)')\n",
    "plt.xticks(rotation=45)\n",
    "plt.legend(title='Game', bbox_to_anchor=(1.05, 1), loc='upper left')\n",
    "plt.tight_layout()  # Adjust layout to fit everything\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### PS5 vs Xbox Sales Over Time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Temporarily filter out rows with invalid dates and remove Xbox Live for plotting\n",
    "temp_df = df.dropna(subset=['Release Date'])\n",
    "\n",
    "# Map systems to 'PlayStation' or 'Xbox'\n",
    "temp_df['System Group'] = temp_df['System'].apply(lambda x: 'PlayStation' if 'PlayStation' in x else 'Xbox' if 'Xbox' in x else None)\n",
    "temp_df = temp_df.dropna(subset=['System Group'])\n",
    "\n",
    "\n",
    "# Aggregate the data by system group and year\n",
    "temp_df['Year'] = temp_df['Release Date'].dt.year\n",
    "df_agg = temp_df.groupby(['System Group', 'Year'])['Total Shipped With Zeros'].sum().reset_index()\n",
    "\n",
    "# Filter the DataFrame to include only years 1995 and later and remove entries with zero sales\n",
    "df_agg = df_agg[(df_agg['Year'] >= 1995) & (df_agg['Total Shipped With Zeros'] > 0)]\n",
    "\n",
    "\n",
    "# Plot the time series chart comparing PlayStation and Xbox\n",
    "plt.figure(figsize=(16, 10))\n",
    "sns.lineplot(data=df_agg, x='Year', y='Total Shipped With Zeros', hue='System Group', marker='o', palette='tab10')\n",
    "plt.title('Total Shipped Over Time: PlayStation vs. Xbox')\n",
    "plt.xlabel('Year')\n",
    "plt.ylabel('Total Shipped (in millions)')\n",
    "plt.grid(True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Console Sales Over Time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Temporarily filter out rows with invalid dates and remove Xbox Live for plotting\n",
    "temp_df = df.dropna(subset=['Release Date'])\n",
    "\n",
    "# Aggregate the data by system and year\n",
    "temp_df['Year'] = temp_df['Release Date'].dt.year\n",
    "df_agg = temp_df.groupby(['System', 'Year'])['Total Shipped With Zeros'].sum().reset_index()\n",
    "\n",
    "# Filter the DataFrame to include only years 1995 and later and remove entries with zero sales\n",
    "df_agg = df_agg[(df_agg['Year'] >= 1995) & (df_agg['Total Shipped With Zeros'] > 0)]\n",
    "\n",
    "\n",
    "# Plot the time series chart\n",
    "plt.figure(figsize=(16, 10))\n",
    "sns.lineplot(data=df_agg, x='Year', y='Total Shipped With Zeros', hue='System', marker='o', palette='tab10')\n",
    "plt.title('Total Shipped Over Time by System')\n",
    "plt.xlabel('Year')\n",
    "plt.ylabel('Total Shipped (in millions)')\n",
    "plt.grid(True)\n",
    "plt.legend(title='System', bbox_to_anchor=(1.05, 1), loc='upper left')\n",
    "plt.xticks(rotation=45)\n",
    "plt.tight_layout()  # Adjust layout to fit everything\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can see that the data for Xbox Series is not very reliable mainly due to the cross platform enabled gameplay with the PS5 and PC. The analytical conclusions for Playstation 5 and Xbox Series can't be trusted. "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}