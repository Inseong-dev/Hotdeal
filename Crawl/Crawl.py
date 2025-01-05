# import requests
# from bs4 import BeautifulSoup

# def crawl_website(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, 'html.parser')
#         data = []
#         for item in soup.find_all('a', href=True):
#             title - item.text.strip()
#             link = item['href']
#             data.append({"title": title, "link": link})
#             return data
#     else:
#         print("Failed to fetch the webpage")
#         return None