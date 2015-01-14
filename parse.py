import operator

filename = "finalTitles.txt"

all_word_dict = {}
both_word_dict = {}
male_word_dict = {}
female_word_dict = {}


def add_word(word,i):
	if i == 0:
		#female
		if word in female_word_dict:
			female_word_dict[word] += 1
		else:
			female_word_dict[word] = 1
	elif i == 1:
		#male
		if word in male_word_dict:
			male_word_dict[word] += 1
		else:
			male_word_dict[word] = 1
	elif i == 2:
		#both
		if word in both_word_dict:
			both_word_dict[word] += 1
		else:
			both_word_dict[word] = 1
	if word in all_word_dict:
		all_word_dict[word] += 1
	else:
		all_word_dict[word] = 1

def print_dict():
	print "All Words: Word | Count"
	for x in all_word_dict:
		print "\t{}: {}".format(x,all_word_dict[x])

	print "Female Words: Word | Count"
	for x in female_word_dict:
		print "\t{}: {}".format(x,female_word_dict[x])

	print "Male Words: Word | Count"
	for x in male_word_dict:
		print "\t{}: {}".format(x,male_word_dict[x])

	print "Both Words: Word | Count"
	for x in both_word_dict:
		print "\t{}: {}".format(x,both_word_dict[x])


def get_male_word(word):
	word = word.strip()
	if len(word) < 4:
		#ignore
		return ""
	if "{m}" in word:
		word = word.replace('{m}','m')
		return word
	elif "[m]" in word:
		word = word.replace('[m]','m')
		return word
	elif "(m)" in word:
		word = word.replace('(m)','m')
		return word
	elif "<m>" in word:
		word = word.replace('<m>','m')
		return word
	else:
		return ""


def get_female_word(word):
	#Need to find way to remove the brackets and stuff
	word = word.strip()
	if len(word) < 4:
		#ignore
		#print word
		return ""
	if "{f}" in word:
		word = word.replace('{f}','f')
		return word
	elif "[f]" in word:
		word = word.replace('[f]','f')
		return word
	elif "(f)" in word:
		word = word.replace('(f)','f')
		return word
	elif "<f>" in word:
		word = word.replace('<f>','f')
		return word
	else:
		return ""

def parse(title):
	words = title.split(' ')
	found_words = []
	line = ""
	for word in words:
		has_female = False
		#print word
		w = get_female_word(word)
		if w != "":
			has_female =True
			#print "Female Word: {}".format(w)
		else:
			w = word
			#add word to dict
		ww = get_male_word(w)
		if ww != "":
			if has_female:
				#print "Male and Female Word: {}".format(ww)
				found_words.append(ww)
				line += 'B'
				#print "MF[{}]:{}".format(ww,title) 
				add_word(ww,2)
			else:		
				#print "Male Word: {}".format(ww)
				found_words.append(ww)
				line += 'M'
				#print "M[{}]:{}".format(ww,title)
				add_word(ww,1)
			#add word to dict
		elif has_female:
			#print "Female Word: {}".format(w)
			found_words.append(w)
			line += 'F'
			#print "F[{}]:{}".format(w,title)
			add_word(w,0)
	#print "{}:{}:{}".format( line , found_words , title )

def remove_redundent():
	pass

def open_titties_file():
	with open(filename,'r') as f:
		count = 1
		for line in f:
			parse(line.lower())
			
def get_details(word):
	f,m,b = 0,0,0
	if word in female_word_dict:
		f = female_word_dict[word]
	if word in male_word_dict:
		m = male_word_dict[word]
	if word in both_word_dict:
		b = both_word_dict[word]
	return f,m,b


def print_top_ten(x_dic):
	top_ten = [] #0 pos being most common word 10 being less common
	sorted_x = sorted(x_dic.items(), key=operator.itemgetter(0)) #Sorts by alphabetical order
	sorted_x = sorted(sorted_x, key=operator.itemgetter(1),reverse=True)[:10] #Sorts by word_count
	len_x_list = []
	for i in sorted_x:
		len_x_list.append(len(i[0]))
	maxlen = max(len_x_list)
	print "Top Ten:"
	max 
	count = 0
	numb = 1
	for_ties = 0
	for_header = " {} | {:^"+str(maxlen)+"s} | {"+":^3"+"} | {"+":^5"+"} | {"+":^5"+"} | {"+":^5"+"} |"	#Word Centered
	for_data   = "{:2} | {:"+str(maxlen)+"s} | {"+":^3"+"} | {"+":^5"+"} | {"+":^5"+"} | {"+":^5"+"} |"	#Word Left Aligned
	header = for_header.format("#","Word","Cnt","F Cnt","M Cnt","B Cnt")
	print header
	#print "_"*len(header)
	for x in sorted_x:
		numb += 1
		if x[1] != for_ties:
			count += 1
		f,m,b = get_details(x[0])
		line = for_data.format(count,x[0],x[1],f,m,b)	# need to get the numbers for 
		#line = "{:>2}. {}".format(count,x[0])
		for_ties = x[1]
		print line


open_titties_file()
#print_dict()
print_top_ten(all_word_dict)





"""
So got it working and it seems to be working well enough.
Only problem is I am only limited to 25 titles at a time.
So im going to have to a either run it continously for a
few days or put the new submisions into a txt file then 
just parse that file and get the stats. I prefer the last one
as it would get the better part of the data only problem is
repeated data. I will try it out with some sleep timers like every
10 mins. 
Should include no word where the person did not not try to create
a word with the gender tag
"""
