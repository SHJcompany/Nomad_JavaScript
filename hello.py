import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="


# filename = "시가총액-200.csv"
# f = open(filename, "w", encoding="utf-8-sig", newline="")

# writer = csv.writer(f)

for page in range(1, 5):
    
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html.parser")
    
    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")

    for row in data_rows : 
        cols = row.find_all("td")

        data = [col.get_text() for col in cols]

        print(data)