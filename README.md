# Reddit_scraper
A simple scraper for reddit using BeautifulSoup and selenium.\
It extracts the titles and other information (upvotes, comments, awards) of Reddit posts for a given search result and saves it to a xlsx file.

# Usage example:
```
python reddit_scraper.py bitcoin bitcoin_doc --number-of-pages 10 --scroll-pause-time 0.5
```
## First two fields are required:
first (bitcoin): keyword to search for in reddit\
second (bitcoin_doc): file name the xlsx to be saved\
third (Optional)[default=0]: number of pages to scroll\
fourth: (Optional)[default=1.0]: time to wait between scrolling (can be adjusted in case of slower internet speed)\
