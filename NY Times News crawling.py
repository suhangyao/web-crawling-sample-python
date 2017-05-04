##########How to craw NY times News#####

import urllib.request
import re
nydata=urllib.request.urlopen("https://www.nytimes.com/").read()
nydata=nydata.decode("utf-8","ignore")
pat='href="(https://www.nytimes.com/.*?)"'
allurl=re.compile(pat).findall(nydata)

for i in range(0,len(allurl)):
	try:
		print(str(i)+"try")
		thisurl=allurl[i]
		file="/Users/yaosuhang/Library/Mobile Documents/com~apple~CloudDocs/python/NYnews/"+str(i)+".html"
		urllib.request.urlretrieve(thisurl,file)
		print("---SUCCEED---")
	     
	except urllib.error.URLError as e:
		if hasattr(e,"code"):
			print(e.code)
		if hasattr(e,"reason"):
			print(e.reason)