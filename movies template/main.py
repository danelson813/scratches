# movies/main.py

import pandas as pd
from utils.selenium_template import get_soup, form_dataframe, to_sqlite


url = "https://www.rottentomatoes.com/browse/movies_in_theaters/"
base = "https://www.rottentomatoes.com"

if __name__ == '__main__':
    results = []
    soup = get_soup(url)
    # button = soup.find('div.discovery__actions > button').click()
    movies = soup.select('.flex-container ')
    for movie in movies:
        result = {
            'title' : movie.select_one('.p--small').text.strip(),
            'open_date' : movie.select_one('.smaller').text.strip(),
            'link' : base+movie.select_one('a')['href'],
            'image_link' : movie.select_one(".posterImage")['src'],
        }
        results.append(result)
    data = form_dataframe(results)
    data.to_csv('data/movies.csv', index=False)
    to_sqlite(data)
