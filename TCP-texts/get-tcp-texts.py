#retrieve-from-flickr.py

#import os
import csv
import requests

#DATE,TCP_Number,ESTC_Number,AUTHOR,PUBLISHER,WORD COUNT,TITLE,,,,,,,,

with open('ecco-tcp-ids2.csv', 'rb') as infile :
	csvin = csv.DictReader(infile, delimiter=',', quotechar='"')
	
	for row in csvin :
		tcpID = str(row['TCP_Number'])
		estcNum = str(row['ESTC_Number'])
		#id = row['flickr_link'].rpartition('/')[2]
		#urllib2.urlopen(row['flickr_link'],id)
		#print "wget(" + row['flickr_link'] + ", " + id + ")"
		url = "https://raw.githubusercontent.com/textcreationpartnership/" + tcpID + "/master/" + tcpID + ".xml"
		r = requests.get(url)
		with open(tcpID + ".xml", "wb") as code:
			code.write(r.content)