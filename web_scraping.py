from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time

base_url = "https://books.toscrape.com/catalogue/page-{}.html"

data = []

try:
    for page in range(1, 51):
        url = base_url.format(page)
        print(f"Scraping page {page}")
        
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        
        books = soup.find_all("article", class_="product_pod")
        
        for book in books:
            title = book.h3.a["title"]
            
            price = book.find("p", class_="price_color").text
            price = price.replace("Â£", "£")
            
            rating = book.p["class"][1]

            detail_url = urljoin(url, book.h3.a["href"])
            detail_resp = requests.get(detail_url)
            detail_soup = BeautifulSoup(detail_resp.text, "html.parser")

            genre = detail_soup.select_one("ul.breadcrumb li:nth-of-type(3) a").get_text(strip=True)
            genre = genre.replace("Add a comment", "Default").strip()
            
            data.append({
                "title": title,
                "genre": genre,
                "price": price,
                "rating": rating,
                "page": page
            })
        
        time.sleep(1)

except Exception as e:
    print(f"An error occurred at page {page}: {e}")

df = (
    pd.DataFrame(data)
      .sort_values("title")
      .drop_duplicates(subset=["title"])
)

df["title"] = df["title"].str.strip().str.title()

df.to_csv("Books.csv", index=False, encoding="utf-8-sig")

print(df.head(10))




