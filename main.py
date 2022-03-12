from bs4 import BeautifulSoup
import requests
import re

rep = 100000 #repetitions

ans = [0 for i in range(10)]

i = 1

while(i<=rep):
	try:
		html_text = requests.get('https://en.wikipedia.org/wiki/Special:Random').text
		soup = BeautifulSoup(html_text, 'lxml')

		print(f'{i}. checking website {soup.title.text}')

		content = soup.find('div', class_ = "mw-parser-output")

		numbers = re.findall('[1-9][0-9]+', content.text)

		for number in numbers:
			x = int(number[0])
			ans[x] = ans[x] + 1
		i+=1
	except:
		print("Error!")

print(ans)
