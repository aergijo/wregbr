import requests
import csv
from bs4 import BeautifulSoup


url = 'https://znanierussia.ru/articles/index.php?search=bmw&title=%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F%3A%D0%9F%D0%BE%D0%B8%D1%81%D0%BA&profile=default&fulltext=1'  # Замените на нужный вам URL
titles = []
description = []

response = requests.get(url)

if response.status_code == 200:
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    
    paragraphs = soup.find_all('div',class_="mw-search-result-heading")  
    

    for p in paragraphs:
        titles.append(p.get_text())
        print(p.get_text()) 

    paragraphs1 = soup.find_all('div',class_="searchresult")  
    
    for p in paragraphs1:
        description.append(p.get_text())
        print(p.get_text()) 
else:
    print(f'Ошибка при запросе: {response.status_code}')

    
with open('output.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # Записываем заголовки столбцов (опционально)
    writer.writerow(['Название', 'Описание'])

    # Записываем данные
    for title, description in zip(titles, description):
        writer.writerow([title, description])