import twitter
from twitter import *

import config
import sys
import csv



def main():

	latitude = 40.730610	# geographical centre of search
	longitude = -73.935242	# geographical centre of search
	max_range = 20 			# search range in kilometres
	num_results = 50		# minimum results to obtain
	outfile = "output.csv"

	#-----------------------------------------------------------------------
	# load our API credentials 
	#-----------------------------------------------------------------------
	

	#-----------------------------------------------------------------------
	# create twitter API object
	#-----------------------------------------------------------------------
	

	api = twitter.Api(consumer_key=config.consumer_key, consumer_secret=config.consumer_secret,
                      access_token_key=config.access_key, access_token_secret=config.access_secret,
                      )

	#-----------------------------------------------------------------------
	# open a file to write (mode "w"), and create a CSV writer object
	#-----------------------------------------------------------------------
	csvfile = open(outfile, "w")
	csvwriter = csv.writer(csvfile)

	#-----------------------------------------------------------------------
	# add headings to our CSV file
	#-----------------------------------------------------------------------
	row = [ "user", "text", "latitude", "longitude" ]
	csvwriter.writerow(row)

	#-----------------------------------------------------------------------
	# the twitter API only allows us to query up to 100 tweets at a time.
	# to search for more, we will break our search up into 10 "pages", each
	# of which will include 100 matching tweets.
	#-----------------------------------------------------------------------
	result_count = 0
	last_id = 0.
	while result_count <  num_results:
		#-----------------------------------------------------------------------
		# perform a search based on latitude and longitude
		# twitter API docs: https://dev.twitter.com/docs/api/1/get/search
		#-----------------------------------------------------------------------
		query = api.GetSearch(geocode = "%f,%f,%dkm" % (latitude, longitude, max_range), count = 100, since_id=last_id + 1, since='2016-08-08')
		print(query, "\n _____ \n")
		for result in query:
			#-----------------------------------------------------------------------
			# only process a result if it has a geolocation
			#-----------------------------------------------------------------------
			# print(result.geo)
			# print(type(result.geo))
			if result.geo:
				user = result.user.screen_name
				text = result.text
				text = text.encode('ascii', 'replace')
				latitude = result.geo['coordinates'][0]
				longitude = result.geo['coordinates'][1]

				# now write this row to our CSV file
				row = [ user, text, latitude, longitude ]
				csvwriter.writerow(row)
				result_count += 1
			last_id = result.id

		#-----------------------------------------------------------------------
		# let the user know where we're up to
		#-----------------------------------------------------------------------
		print ("got %d results" % result_count)

	#-----------------------------------------------------------------------
	# we're all finished, clean up and go home.
	#-----------------------------------------------------------------------
	csvfile.close()

	print ("written to %s" % outfile)


if __name__ == '__main__':
	main()
