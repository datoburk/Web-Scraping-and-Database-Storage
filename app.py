import requests
from bs4 import BeautifulSoup
import sqlite3


def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    titles = [heading.text for heading in soup.find_all('h1')]

    return titles


def store_in_database(data):
    conn = sqlite3.connect('scraped_data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS titles
                 (id INTEGER PRIMARY KEY, title TEXT)''')
    for title in data:
        c.execute('INSERT INTO titles (title) VALUES (?)', (title,))
    conn.commit()
    conn.close()


def main():
    base_url = 'https://en.wikipedia.org/wiki/'
    pages = ['Python_(programming_language)', 'Artificial_intelligence', 'Machine_learning',
             'Natural_language_processing', 'Data_science']

    all_titles = []
    for page in pages:
        url = base_url + page
        titles = scrape_website(url)
        all_titles.extend(titles)

    store_in_database(all_titles)


if __name__ == '__main__':
    main()
