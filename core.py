#service
import time
import requests
import thread

urls = []

def check_up(url):
  while True:
		print 'Making request'

		request = requests.get(url)

		timevalue = time.ctime(time.time())

		if request.status_code == 200 :
			print "Server is up ",url,timevalue
		else :
			print "Server down ",request.status_code,timevalue
		time.sleep(10)

for url in urls:
	 thread.start_new_thread(check_up,(url,))

while True:
	pass
