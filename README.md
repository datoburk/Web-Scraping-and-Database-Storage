Web Scraping and Database Storage
This Python script demonstrates how to scrape data from a website using requests and beautifulsoup4, and store the scraped data in an SQLite database using sqlite3.

Features:
Scrapes titles from multiple pages of a website (Wikipedia in this example).
Stores the scraped titles in an SQLite database (scraped_data.db).
Example includes scraping titles from pages related to Python programming language, Artificial Intelligence, Machine Learning, Natural Language Processing, and Data Science.
Requirements:
Python 3.x
requests library (pip install requests)
beautifulsoup4 library (pip install beautifulsoup4)


The script will create an SQLite database file named scraped_data.db in the same directory.
The database will contain a table named titles with the scraped titles.
