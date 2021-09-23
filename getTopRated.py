from bs4 import BeautifulSoup
import requests
import pandas

source = requests.get('https://codeforces.com/').text

soup = BeautifulSoup(source, 'lxml')

handle_list = []
profile_lists = []


for name in soup.find('div', class_='roundbox sidebox top-contributed', style="").find('table', class_='rtable').find('tbody').find_all('a'):
	handle_list.append(name.text)
	profile_lists.append(f"https://codeforces.com/profile/{name.text}")
	

df = pandas.DataFrame({'Handle':handle_list, 'Profile':profile_lists})
df.to_csv('getTopRated.csv', index = False, encoding = 'utf-8')


