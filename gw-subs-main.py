#!/usr/bin/env python
import praw
import time
import sys
from datetime import timedelta

fileName = "title3_1-13.txt"
#fileName will now be "titles_{id number}_{Hours Running}_{Data Started}.txt"
#so 'titles_1_12_1-12.txt' is an example be sure to change the title every time. 
logfilename = "log-py-gw.txt"

subreddit = "gonewild"
#subreddit = "sweden"

#lim = 2
lim = 25

length = 64800.0	#12 hours so 60*60*12
sleepyLength = 600.0 # 10 mins so 600 

def niceTime(t):
	return str(timedelta(seconds=int(t)))
	#return time.strftime("%H:%m:%S",time.gmtime(t))
	#return time.strftime("%d Days\n%H Hours\n%m Mins\n%S Seconds",time.gmtime(t))

def write_twice(s):
	with open(logfilename,"a+") as f:
		f.write(s)
	sys.stdout.write(s)
	sys.stdout.flush()

def get_submissions():
	r = praw.Reddit(user_agent="test_application")
	subs = r.get_subreddit(subreddit).get_new(limit=lim)
	with open(fileName,"a+") as f:
		f.write("Begin:\n")
		for t in subs:
		    #t.title might be returning a unicode string 
		    line = t.title.encode('ascii','ignore')
		    f.write(line+'\n')
		    write_twice('.')
		f.write("END\n\n")
	write_twice("]\n")

		
def loop_an_hour():
	with open(fileName,"w+")as f:
		f.write("Created [{}]:\n".format(time.asctime()))
	with open(logfilename,"w+")as f:
		f.write("[{}] - Created {} Log\n".format(time.asctime(),subreddit))
	start_time = time.time()
	count = 0
	write_twice("Subreddit: {}\n Run  Length: {}\nSleep Length: {}\n".format(subreddit,niceTime(length),niceTime(sleepyLength) ))
	while (time.time() - start_time < length):	#an hour is 3600. 
		write_twice("[{}] - {}:[".format(time.asctime(),niceTime(sleepyLength*count) ))
		get_submissions()
		count +=1
		try:
			time.sleep(sleepyLength)
		except KeyboardInterrupt:
			write_twice("\n[{}] - Script Interrupted During Sleep\nExiting...\n".format(time.asctime()))
			sys.exit()

	write_twice("[{}] - Script Completed\nTime Elapsed: {}\n".format( time.asctime() , niceTime(time.time() - start_time)))

loop_an_hour()


"""
TODO: Get the top 25 posts for each day in 2014
Should be able, in praw, to get_hot or get_top with some date element so like:
.get_top(limit=25,date="Some date format") probably similar to time.time() or something
will default to like noon or something then add number of seconds in a day
Maybe I can't do that.
There is the idea of a place holder that could be used to get even older data or something
"""