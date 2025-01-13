from selenium import webdriver
from bs4 import BeautifulSoup
# Chrome Webdriver 초기화
driver = webdriver.Chrome('')

url = ''
driver.get(url)

# 페이지를 끝까지 내려서 로드하는 코드 작성하기

driver.implicitly_wait(5)

#끝까지 로딩된 페이지를 HTML로 추출
result_html = driver.page_source
driver.quit()
"""
필요한 데이터를 추출하고, data라는 리스트 변수에 저장해 리턴하는 함수 제작
데이터는 dictionary형태로 만들고,
{'title': title, 'price': price, 'link': link} 형태로.
title은 상품 이름, price는 상품의 가격, link는 커뮤니티의 상세 페이지로 가는 링크를 입력
"""


