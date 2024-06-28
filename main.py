import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service()
driver = webdriver.Chrome(service=service)
driver.get('https://www.nbcnews.com/')

results = []
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')

for element in soup.findAll(attrs={'class': 'styles_headline__ZoJUw'}):
    name = element.find('a')
    if name:
        results.append(name.text)
    else:
        results.append('')

df = pd.DataFrame({'Titles': results})
df.to_csv('names.csv', index=False, encoding='utf-8')

driver.quit()