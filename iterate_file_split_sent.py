import os
import re
import sys
sys.path.append('/usr/lib/python2.7/site-packages')
sys.path.insert(0,'/usr/lib/python2.7/site-packages')
import nltk
import nltk.data

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

def Split_Sentences(filename):

	text = ''.join(open(filename).readlines())
	f=open(filename,'w')
	f.write("\n".join(tokenizer.tokenize(text.strip())))




directory=os.path.join("data/tales")


for filename in os.listdir(directory):
	if filename.endswith(".txt"): 
		fn=os.path.join(directory, filename)
		Split_Sentences(fn)
	else:
		continue