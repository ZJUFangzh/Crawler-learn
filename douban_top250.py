# reference    https://zhuanlan.zhihu.com/p/20423182
# https://movie.douban.com/top250/

import requests
from bs4 import BeautifulSoup
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36', }


def getHTMLText(url):
    html = requests.get(url, headers=headers)
    return html.text


URL = 'https://movie.douban.com/top250/'
movie_dict = {}


def parser_url(html):
    global movie_dict
    soup = BeautifulSoup(html, 'html.parser')
    ol = soup.find('ol', attrs={'class': 'grid_view'})

    for movie_li in ol.find_all('li'):
        num = movie_li.find('em').text
        movie_list = []
        name = movie_li.find('span', attrs={'class': 'title'}).text
        rating_num = movie_li.find(
            'span', attrs={'class': 'rating_num'}).text
        try:
            quote = movie_li.find('span', attrs={'class': 'inq'}).text
        except:
            quote = '--'
        movie_list = [name, rating_num, quote]
        movie_dict.update({num: movie_list})

    #    return movie_dict
    next_page = soup.find('span', attrs={'class': 'next'}).find('a')
    if next_page:
        return URL + next_page['href']
    else:
        return None


def main():
    url = URL
    path = r'D:\Python-trying\Crawler-learn\doubantop250.txt'
    a = '{0:10}\t{1:{4}^25}\t{2:10}\t{3:10}'
    while url:
        html = getHTMLText(url)
        url = parser_url(html)
    with open(path, 'w', encoding='utf-8') as f:
        print(a.format('rank', '片名', 'star', 'quote', chr(12288)), file=f)
        for key in movie_dict:
            print(a.format(
                key, movie_dict[key][0], movie_dict[key][1], movie_dict[key][2], chr(12288)), file=f)


main()
