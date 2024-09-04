import os
import requests
from bs4 import BeautifulSoup
from http import HTTPStatus
import string

base_url = "https://www.nature.com/nature/articles?searchType=journalSearch&sort=PubDate"

def clean_filename(title):
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    return ''.join(c for c in title if c in valid_chars).replace(' ', '_')

def scrape_articles(pages, article_type, year):
    for page in range(1, pages + 1):
        url = f"{base_url}&year={year}&type={article_type}&page={page}"
        print(f"Scraping URL: {url}")

        try:
            response = requests.get(url)

            if response.status_code == HTTPStatus.OK:
                soup = BeautifulSoup(response.content, 'html.parser')
                articles = soup.find_all('article')

                if not articles:
                    print(f"No articles found on page {page}.")
                    continue

                page_dir = f"Page_{page}_{year}"
                os.makedirs(page_dir, exist_ok=True)

                for article in articles:
                    article_span = article.find('span', {'data-test': 'article.type'})
                    if article_span and article_span.text.strip().lower() == article_type.lower():
                        link = article.find('a', {'data-track-action': 'view article'})
                        if link:
                            article_url = "https://www.nature.com" + link.get('href')
                            title = link.text.strip()

                            file_name = clean_filename(title) + ".txt"
                            file_path = os.path.join(page_dir, file_name)

                            article_response = requests.get(article_url)
                            if article_response.status_code == HTTPStatus.OK:
                                article_soup = BeautifulSoup(article_response.content, 'html.parser')

                                article_body = article_soup.find('div', {'class': 'c-article-body'})

                                if article_body:
                                    content = "\n".join(p.text.strip() for p in article_body.find_all('p'))

                                    with open(file_path, 'w', encoding='utf-8') as file:
                                        file.write(content)
                                    print(f"Saved article: {file_name}")
                                else:
                                    print(f"Body not found for article: {title}")
                            else:
                                print(f"Failed to retrieve article page: {article_url}")
            else:
                print(f"The URL returned {response.status_code}!")

        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")

pages = int(input("Enter the number of pages to scrape:\n> "))
article_type = input("Enter the article type to scrape (e.g., news, research, briefing):\n> ")
year = int(input("Enter the year of publication to scrape (e.g., 2020):\n> "))

scrape_articles(pages, article_type, year)

print("Finished scraping.")
