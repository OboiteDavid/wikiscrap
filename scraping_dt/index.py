from bs4 import BeautifulSoup # type: ignore
import requests # type: ignore

# Fetch the web page
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page = requests.get(url)

# Initialize BeautifulSoup object
soup = BeautifulSoup(page.content, "html.parser")

# Print the page title to verify the BeautifulSoup object
# print(soup.title.text)

# Print the page title to verify the BeautifulSoup object
# print(soup)


# table = soup.find('table')
# print(table)

# table = soup.find_all('table')[1]
# print(table)


# print(table)

# table=soup.find('table', class_='wikitable sortable')[1]
# print(table)

table = soup.find_all('table', class_='wikitable sortable')[1]
# print(table)

world_titles = table.find_all('th')
# print(world_titles)

world_table_titles = [title.text.strip() for title in world_titles]
print(world_table_titles)

import pandas as pd # type: ignore
df = pd.DataFrame(columns=world_table_titles)
df  

column_data = table.find_all('tr')
for row in column_row:
(row.find_all('td'))