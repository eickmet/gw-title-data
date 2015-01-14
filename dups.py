
"""
Script is to remove duplicate titles
"""
from tempfile import mkstemp
from shutil import move
from os import remove, close, stat
import sys

fn = "cptitle3.txt"
fnwrite = "finalTitles2.txt"


#Taken from Stackoverflow was an answer to a question.
#Should probably give credit
def replace(file_path, pattern, subst):
	fh, abs_path = mkstemp()
	new_file = open(abs_path,'w')
	old_file = open(file_path)
	for line in old_file:
		new_file.write(line.replace(pattern,subst))
	new_file.close()
	close(fh)
	old_file.close()
	remove(file_path)
	move(abs_path,file_path)

def make_write():
	with open(fnwrite,'w+') as write:
		write.write("Created:\n")

def remove_all_instances_of_line(line):
	replace(fn,line,'')


def write_line(line):
	with open(fnwrite,'a+') as w:
		w.write(line)

def get_line():
	with open(fn,'r') as r:
		return r.readline()
		#return r[0]

def main(): 
	make_write()
	# Need to loop below until fn file is empty
	#for now just one line
	count = 0
	while (stat(fn).st_size != 0):
		line = get_line()
		write_line(line)
		remove_all_instances_of_line(line)
		count += 1

	print count

main()