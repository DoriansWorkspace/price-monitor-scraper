import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_motor_price(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        
        price_tag = soup.find("span", class_="product-price product-page-price")
        
        if price_tag:
            raw_price = price_tag.get_text().strip()
            clean_price = "".join(filter(str.isdigit, raw_price))
            return int(clean_price)
            
    except Exception as e:
        return f"Error: {e}"
    
    return "Price not found"

def save_price(price):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    with open("prices.txt", "a", encoding="utf-8") as file:
        file.write(f"{timestamp} - Price: {price} HUF\n")
    print("Data saved to prices.txt")

if __name__ == "__main__":
    product_url = "https://www.tornadohelmets.hu/cassida-integral-30-mf-zart-bukosisak-napszemuveggel-sotetitett-plexivel-2382"
    
    current_price = get_motor_price(product_url)
    
    if isinstance(current_price, int):
        print(f"Current price: {current_price} HUF")
        save_price(current_price)
    else:
        print(current_price)