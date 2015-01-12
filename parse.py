
test_title1 = " i'(M) do you like white" 
#No Proper word

test_title2 = "I've missed you. Have some [f]ace" 
#Word is "face"

test_title3 = "I have quite the spank(f)ul"
#Word is "spankful"

test_title4 = "didn't (f)eel like I got any recognition last ti(m)e anymore love for"
#word is "feel" and "time"

test_title5 = "This is a test {m}or stuff"
#word is "for"

test_titleHard = "Here {f}ro(m) dusk till dawn"
#Interesting issue with a word with both m and f it duplicates it 


test_titles = []
test_titles.append(test_title1)
test_titles.append(test_title2)
test_titles.append(test_title3)
test_titles.append(test_title4)
test_titles.append(test_title5)
test_titles.append(test_titleHard)

def get_male_word(word):
	if len(word) < 4:
		#ignore
		return ""
	if "{m}" in word:
		word = word.replace('{m]','m')
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
	for word in words:
		has_female = False
		#print word
		w = get_female_word(word)
		if w != "":
			has_female =True
			#print "Female Word: {}".format(w)

			#add word to dict
		ww = get_male_word(w)
		if ww != "":
			if has_female:
				print "Male and Female Word: {}".format(ww)
			else:		
				print "Male Word: {}".format(ww)
			#add word to dict
		elif has_female:
			print "Female Word: {}".format(w)


	"""words = []
	lookfor = ''
	length = 0
	for i in range[0:len(title)]:
		letter = title[i]
		print letter
		w = ''
		if letter == '{':
			lookfor = '}'
			while (title[i] =! lookfor) or (length > 1):

		elif letter == '[':
			lookfor = '}'
			while (title[i] =! lookfor) or (length > 1):

		elif letter == '(':
			lookfor = '}'
			while (title[i] =! lookfor) or (length > 1):

		elif letter == '<':
			lookfor = '}'
			while (title[i] =! lookfor) or (length > 1):

		else:"""

for tt in test_titles:
	parse(tt.lower())
	break