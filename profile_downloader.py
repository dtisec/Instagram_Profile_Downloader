import requests
from bs4 import BeautifulSoup as bs
import json
import random
import os.path
import instaloader

ig = instaloader.Instaloader()
dp = input("Kullanıcı adı giriniz : ")

ig.download_profile(dp , profile_pic_only=True)



insta_url='https://www.instagram.com'
inta_username= input('kullanıcı adı giriniz : ')


response = requests.get(f"{insta_url}/{inta_username}/")

if response.ok:
	html = response.text

	bs_html = bs(html, features="lxml")
	bs_html = bs_html.text
	index = bs_html.find('profile_pic_url_hd') + 21

	remaining_text = bs_html[index:]
	remaining_text_index = remaining_text.find('requested_by_viewer')-3
	string_url = remaining_text[:remaining_text_index].replace("\\u0026","&")

	print(string_url, "\n \n yükleniyor..........")
while True:
	filename = 'pic' + str(random.randint(1, 100000)) + '.jpg'
	file_exists = os.path.isfile(filename)

	if not file_exists:
		with open(filename, 'wb+') as handle:
			response = requests.get(string_url, stream = True)
			if not response.ok:
				print(response)
			for block in response.iter_content(1024):
				if not block:
					break
				handle.write(block)
	else:
		continue
	break
print("\n			 yükleme işlemi tamamlandı ..............")
