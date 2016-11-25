from TwitterSearch import *

import config


latitude, longitude, radius = 40.730610, -73.935242, 100

def main():

	try:
		tso = TwitterSearchOrder() # create a TwitterSearchOrder object
		print('kkok')
		tso.set_keywords(['hi'])
		tso.set_positive_attitude_filter() # and don't give us all those entity information
		# tso.set_negative_attitude_filter() # and don't give us all those entity information
		print('kuku')
		tso.set_geocode(latitude=latitude, longitude=longitude, radius=radius)
		print('kuku1')
		# it's about time to create a TwitterSearch object with our secret tokens
		ts = TwitterSearch(
		    consumer_key = config.consumer_key,
		    consumer_secret = config.consumer_secret,
		    access_token = config.access_key,
		    access_token_secret = config.access_secret
		 )
		 # this is where the fun actually starts :)
		counter = 0
		t_counter = 0
		for tweet in ts.search_tweets_iterable(tso):
			# print (tweet)
			t_counter += 1
			if tweet['place'] != None:
				for key in tweet:
					print (key, '===', tweet[key])
				break
				counter+= 1
				print(counter, t_counter)
		   	# print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
		print(counter, t_counter)
	except TwitterSearchException as e: # take care of all those ugly errors if there are some
	    print(e)


if __name__ == '__main__':
	main()