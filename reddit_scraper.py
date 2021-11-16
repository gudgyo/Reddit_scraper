from bs4 import  BeautifulSoup
from selenium import webdriver
import pandas as pd
import typer
from typing import Optional
import time

def main(search: str, file_name: str, number_of_pages: Optional[int]=0,  scroll_pause_time: Optional[float]=1.0):

    url = f'https://www.reddit.com/search/?q={search}'
    driver = webdriver.Chrome()
    driver.get(url)

    SCROLL_PAUSE_TIME = scroll_pause_time
    last_height = None

    for x in range(number_of_pages):
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    result = soup.find_all("a",{"class":"SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE"})
    info = soup.find_all("span", {"class":"_vaFo96phV6L5Hltvwcox"})

    # for item in result:
    #     print(item.text)
    # for item in info:
    #     print(item.text)

    to_save = pd.DataFrame([[title.text, upvote.text, comment.text, award.text] \
                            for title, upvote, comment, award in \
                            zip(result, info[::3], info[1::3], info[2::3])])
    to_save.to_excel(f'{file_name}.xlsx')

if __name__ == "__main__":
    typer.run(main)