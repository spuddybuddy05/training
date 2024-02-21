import requests
from bs4 import BeautifulSoup

url = "https://www.scrapethissite.com/pages/simple/"
response = requests.get(url)

if response.status_code == 200:

    soup = BeautifulSoup(response.content, "html.parser")
    
    country_divs = soup.find_all("div", class_="country")
    
    for country_div in country_divs:
       
        country = country_div.find("h3", class_="country-name").get_text().strip()
        population = country_div.find("span", class_="country-population").get_text().strip()
        
        print(country, ":", population)
