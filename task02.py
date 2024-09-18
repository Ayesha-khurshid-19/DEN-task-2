import pandas as pd
import requests
from bs4 import BeautifulSoup

# Base URL of the website
web_url = 'https://www.shopmodest.pk/collections/sale?page=2'

data = []

for i in range(1, 10):  
    url = f'{web_url}?page={i}'
    page = requests.get(url)
    
    if page.status_code == 200:
        print('Data fetched successfully', i)
        soup = BeautifulSoup(page.content, 'html.parser')
        
        # Find all watch names
        clothes = soup.find_all(attrs={'class': 't4s-product-info'})
        
        # Find all watch prices
        prices = soup.find_all(attrs={'class': 'money'})
        
        for cloth, price in zip(clothes, prices):
            # cloth_name = cloth.text().strip().replace('\n', "").replace('\r', "")
            cloth_name = cloth.get_text().strip().replace('\n', "").replace('\r', "")
            price_value = price.get_text().strip().replace('\n', "").replace('\r', "")
            data.append([url, cloth_name, price_value])
        # for cloth, price in zip(clothes, prices):
        #     cloth_name =cloth.text().strip().replace('\n', "").replace('\r', "")
        #     price_value = price.text().strip().replace('\n', "").replace('\r', "")
        #     data.append([url, cloth_name, price_value])
    else:
        print('URL not found', i)

# Convert the data into a DataFrame
df = pd.DataFrame(data, columns=['url', 'watch', 'price'])
print(df)

# Save the DataFrame to a CSV file
df.to_csv('pagedata.csv', index=False)

print(len(clothes))
print(len(prices))