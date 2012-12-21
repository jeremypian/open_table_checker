import time
import urllib2
from batch import MDBatch

class OpenTableChecker(MDBatch.MDBatch):
	notify_emails = ['xpian@yelp.com']
	date = '31'
	def run(self):
		while True:
			url =\
			'http://www.opentable.com/opentables.aspx?t=rest&r=40507&m=74&p=2&d=12/%s/2012%%207:00:00%%20PM&scpref=114'
			try:
				page = urllib2.urlopen(url % self.date)
				dom = page.read()
			except:
				continue
			num_avail_times = dom.count('<span class="t">')
			print 'number of available times is %s' % num_avail_times
			if 'No tables are available' in dom:
				print 'Not Found'
				self.notify_email('NOT!')
			elif num_avail_times > 1 or not '<span class="t">4:30</span>' in dom:
				print 'Found!'
				self.notify_email('Found! Hurry!')
				print 'Email sent!'
			else:
				print 'Only 4:30 is available.'
			time.sleep(60)


if __name__ == '__main__':
	OpenTableChecker().run()
