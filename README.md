# WebScraper

A simple web scraper for retrieving and saving articles from the Nature website. This project was created to practice my skills in HTML parsing and HTTP requests processing. While it's simple, it serves as a practical tool for scraping and storing content from web pages.

## How does it work?

The scraper works by retrieving articles from the Nature website based on the number of pages and the type of article you specify. For each page you request, the program creates a separate directory, and within each directory, it saves the articles of the specified type.

### Features:
- Scrapes multiple pages from the Nature website.
- Filters articles by type (e.g., "News", "Nature Briefing").
- Creates a directory for each page and saves articles as '.txt' files.
- Automatically cleans and formats filenames to remove spaces and punctuation.

## How to Use It?

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/WebScraper.git
   
2. Navigate to the project directory:
   ```bash
   cd WebScraper

3. Run the scraper.py file:
   ```bash
   python scraper.py

4. When prompted, input the number of pages you want to scrape, the year and the type of article you're interested in:
   ```bash
   Enter the number of pages to scrape:
    > 4
   Enter the article type to scrape:
    > News
   Enter the year of publication to scrape (e.g., 2020):
    > 2024

5. The program will create directories for each page and save the articles in those directories as .txt files.

## Note:

The URL used for scraping is hardcoded to scrape articles from the Nature website. If you want to scrape articles from a different site, you can modify the base_url variable in the code. Adjustments may be needed to work correctly on other pages.

## Requirements

This project requires Python 3 and the following Python libraries:

- requests
- beautifulsoup4

You can install the dependencies using pip:

  ```bash
  pip install requests beautifulsoup4
