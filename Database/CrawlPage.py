# import requests
import sys
# from bs4 import BeautifulSoup
# def crawl_website(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, 'html.parser')
#         data = []
#         for item in soup.find_all('a', href=True):
#             title = item.text.strip()
#             link = item['href']
#             Database.Main.Page.append({"title": title, "link": link, ""})
#             return data
#     else:
#         print("Failed to fetch the webpage")
#         return None
def returnList():
    Page = []
    Page.extend(
        [{
            'site': 'site1',
            'link': 'link1',
            'photo': 'photo1',
            'title': 'title1'

        },
        {

            'site': 'site2',
            'link': 'link2',
            'photo': 'photo2',
            'title': 'title2'
        },
        {

            'site': 'site3',
            'link': 'link3',
            'photo': 'photo3',
            'title': 'title3'
        }]
    )

    return Page

