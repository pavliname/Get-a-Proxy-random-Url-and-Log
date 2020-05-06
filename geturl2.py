import os
from dotenv import load_dotenv
import random
import time
import io
import datetime
import requests
from lxml.html import fromstring

load_dotenv()

def get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:20]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            #Grabbing IP and corresponding PORT
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies

proxylist = get_proxies()
counter = 0
ran = random.random()
if ran <= 0.1:
	try:
		s =requests.Session()
		s.proxies = proxylist
		a = s.get(os.getenv("URL1"))
		time.sleep(3)
		r = s.get(os.getenv("URL2"))
		time.sleep(5)
		b = s.get(os.getenv("URL3"))
		time.sleep(15)
		c = s.get(os.getenv("URL4"))
		time.sleep(15)
		d = s.get(os.getenv("URL5"))
		time.sleep(15)
		e = s.get(os.getenv("URL6"))
		col1=ran
		col2 = datetime.date.today().strftime('%Y-%m-%d %H:%M:%S')
		col3 = proxylist
		counter +=1
		row = [col1, col2, col3]
		import csv
		with io.open (r"C:\Users\Pavlina\Desktop\Scripts\testwritecsv.csv", "a", newline = '\n', encoding="utf-8") as f:
			writer = csv.writer(f)
			writer.writerow([col1]+ [col2] + [col3])

	except Exception as err:
		col1=err
		col2 = datetime.date.today().strftime('%Y-%m-%d %H:%M:%S')
		row = [col1, col2]
		import csv
		with open (r"C:\Users\Pavlina\Desktop\Scripts\testwritecsv.csv", "a", newline = '\n') as f:
			writer = csv.writer(f)
			writer.writerow([col1]+ [col2])

	print(ran)
	print(proxylist)
elif ran <= 0.2:

	try:
		s =requests.Session()

		s.proxies = proxylist
		r = s.get(os.getenv("URL7"))
		time.sleep(15)
		a = s.get(os.getenv("URL8"))
		time.sleep(15)
		b = s.get(os.getenv("URL9"))

		col1=ran
		col2 = datetime.date.today().strftime('%Y-%m-%d %H:%M:%S')
		col3 = proxylist
		counter +=1
		row = [col1, col2, col3]
		import csv
		with io.open (r"C:\Users\Pavlina\Desktop\Scripts\testwritecsv.csv", "a", newline = '\n', encoding="utf-8") as f:
			writer = csv.writer(f)
			writer.writerow([col1]+ [col2] + [col3])

	except Exception as err:
		col1=err
		col2 = datetime.date.today().strftime('%Y-%m-%d %H:%M:%S')
		row = [col1, col2]
		import csv
		with open (r"C:\Users\Pavlina\Desktop\Scripts\testwritecsv.csv", "a", newline = '\n') as f:
			writer = csv.writer(f)
			writer.writerow([col1]+ [col2])

	print(ran)
	print(proxylist)
elif ran <= 0.3:

	try:
		s =requests.Session()

		s.proxies = proxylist
		r = s.get(os.getenv("URL10"))
		time.sleep(15)
		a = s.get(os.getenv("URL11"))
		time.sleep(15)
		b = s.get(os.getenv("URL12"))

		col1=ran
		col2 = datetime.date.today().strftime('%Y-%m-%d %H:%M:%S')
		col3 = proxylist
		counter +=1
		row = [col1, col2, col3]
		import csv
		with io.open (r"C:\Users\Pavlina\Desktop\Scripts\testwritecsv.csv", "a", newline = '\n', encoding="utf-8") as f:
			writer = csv.writer(f)
			writer.writerow([col1]+ [col2] + [col3])

	except Exception as err:
		col1=err
		col2 = datetime.date.today().strftime('%Y-%m-%d %H:%M:%S')
		row = [col1, col2]
		import csv
		with open (r"C:\Users\Pavlina\Desktop\Scripts\testwritecsv.csv", "a", newline = '\n') as f:
			writer = csv.writer(f)
			writer.writerow([col1]+ [col2])

	print(ran)
	print(proxylist)
elif ran <= 0.4:

	try:
		s =requests.Session()

		s.proxies = proxylist
		r = s.get(os.getenv("URL13"))
		time.sleep(15)
		a = s.get(os.getenv("URL14"))

		col1=ran
		col2 = datetime.date.today().strftime('%Y-%m-%d %H:%M:%S')
		col3 = proxylist
		counter +=1
		row = [col1, col2, col3]
		import csv
		with io.open (r"C:\Users\Pavlina\Desktop\Scripts\testwritecsv.csv", "a", newline = '\n', encoding="utf-8") as f:
			writer = csv.writer(f)
			writer.writerow([col1]+ [col2] + [col3])

	except Exception as err:
		col1=err
		col2 = datetime.date.today().strftime('%Y-%m-%d %H:%M:%S')
		row = [col1, col2]
		import csv
		with open (r"C:\Users\Pavlina\Desktop\Scripts\testwritecsv.csv", "a", newline = '\n') as f:
			writer = csv.writer(f)
			writer.writerow([col1]+ [col2])

	print(ran)
	print(proxylist)
elif ran <= 0.5:

	try:
		s =requests.Session()

		s.proxies = proxylist
		r = s.get(os.getenv("URL15"))
		time.sleep(15)
		a = s.get(os.getenv("URL16"))

		col1=ran
		col2 = datetime.date.today().strftime('%Y-%m-%d %H:%M:%S')
		col3 = proxylist
		counter +=1
		row = [col1, col2, col3]
		import csv
		with io.open (r"C:\Users\Pavlina\Desktop\Scripts\testwritecsv.csv", "a", newline = '\n', encoding="utf-8") as f:
			writer = csv.writer(f)
			writer.writerow([col1]+ [col2] + [col3])

	except Exception as err:
		col1=err
		col2 = datetime.date.today().strftime('%Y-%m-%d %H:%M:%S')
		row = [col1, col2]
		import csv
		with open (r"C:\Users\Pavlina\Desktop\Scripts\testwritecsv.csv", "a", newline = '\n') as f:
			writer = csv.writer(f)
			writer.writerow([col1]+ [col2])

	print(ran)
	print(proxylist)
elif ran <= 0.6:

	try:
		s =requests.Session()

		s.proxies = proxylist
		r = s.get(os.getenv("URL17"))
		time.sleep(15)
		a = s.get(os.getenv("URL18"))

		col1=ran
		col2 = datetime.date.today().strftime('%Y-%m-%d %H:%M:%S')
		col3 = proxylist
		counter +=1
		row = [col1, col2, col3]
		import csv
		with io.open (r"C:\Users\Pavlina\Desktop\Scripts\testwritecsv.csv", "a", newline = '\n', encoding="utf-8") as f:
			writer = csv.writer(f)
			writer.writerow([col1]+ [col2] + [col3])

	except Exception as err:
		col1=err
		col2 = datetime.date.today().strftime('%Y-%m-%d %H:%M:%S')
		row = [col1, col2]
		import csv
		with open (r"C:\Users\Pavlina\Desktop\Scripts\testwritecsv.csv", "a", newline = '\n') as f:
			writer = csv.writer(f)
			writer.writerow([col1]+ [col2])

	print(ran)
	print(proxylist)
elif ran <= 0.7:

	try:
		s =requests.Session()

		s.proxies = proxylist
		r = s.get(os.getenv("URL19"))
		time.sleep(15)
		a = s.get(os.getenv("URL20"))

		col1=ran
		col2 = datetime.date.today().strftime('%Y-%m-%d %H:%M:%S')
		col3 = proxylist
		counter +=1
		row = [col1, col2, col3]
		import csv
		with io.open (r"C:\Users\Pavlina\Desktop\Scripts\testwritecsv.csv", "a", newline = '\n', encoding="utf-8") as f:
			writer = csv.writer(f)
			writer.writerow([col1]+ [col2] + [col3])

	except Exception as err:
		col1=err
		col2 = datetime.date.today().strftime('%Y-%m-%d %H:%M:%S')
		row = [col1, col2]
		import csv
		with open (r"C:\Users\Pavlina\Desktop\Scripts\testwritecsv.csv", "a", newline = '\n') as f:
			writer = csv.writer(f)
			writer.writerow([col1]+ [col2])

	print(ran)
	print(proxylist)

else:

	try:

		s.proxies = proxylist
		b = s.get(os.getenv("URL21"))
		time.sleep(15)
		c = s.get(os.getenv("URL22"))
		time.sleep(15)
		d = s.get(os.getenv("URL23"))
		time.sleep(15)
		e = s.get(os.getenv("URL24"))

		col1=ran
		col2 = datetime.date.today().strftime('%Y-%m-%d %H:%M:%S')
		col3 = proxylist
		counter +=1
		row = [col1, col2, col3]
		import csv
		with io.open (r"C:\Users\Pavlina\Desktop\Scripts\testwritecsv.csv", "a", newline = '\n', encoding="utf-8") as f:
			writer = csv.writer(f)
			writer.writerow([col1]+ [col2] + [col3])

	except Exception as err:
		col1=err
		col2 = datetime.date.today().strftime('%Y-%m-%d %H:%M:%S')
		row = [col1, col2]
		import csv
		with open (r"C:\Users\Pavlina\Desktop\Scripts\testwritecsv.csv", "a", newline = '\n') as f:
			writer = csv.writer(f)
			writer.writerow([col1]+ [col2])

	print(ran)
	print(proxylist)
