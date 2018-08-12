# This simple file will get all media data
# and download it
import re, wget
f = open("username_mined_data.csv",'r')
for item in f:
	z = re.findall('(https://pbs.twimg.com/\S*)',item)
	try:
		wget.download(z[0])
	except:
		pass