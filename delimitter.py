import os
import re
import sys
sys.path.append('/usr/lib/python2.7/site-packages')
sys.path.insert(0,'/usr/lib/python2.7/site-packages')
import nltk
import nltk.data

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
fpath=os.path.join("data", "AesopTales.txt")
f=open(fpath,'r')
fpath2=os.path.join("data", "AesopTales_modified.txt")
f2=open(fpath2,'a+')
i=0

fpath3=os.path.join("data", "test.txt")

text = ''.join(open(fpath3).readlines())
print("\n-----\n".join(tokenizer.tokenize(text.strip())))

# lines=f.readlines()

# titles=[]
# titles.append(lines[0])
# lastlines=[]
# i=1

# while(i<len(lines)):
# 	if(i<len(lines)-2):
# 		if(len(lines[i])<=3 and len(lines[i+1])<=3) :
# 			titles.append(lines[i+2])
# 		#if(len(lines[i+1])==2 and len(lines[i+2])==2):
# 		#	lastlines.append(lines[i])
# 		if(len(lines[i+1])<=3 and len(lines[i+2])<=3):
# 			lastlines.append(lines[i])
# 			#print lines[i+3]
# 	i=i+1




# lastlines.append(lines[len(lines)-1])
# #print titles
# #print lastlines

# i=0
# fpath=os.path.join("data", "AesopTales.txt")
# f=open(fpath,'r')
# count=1
# for row in f:
# 	if row in lastlines:
# 		lastlines.remove(row)
# 		#print row
# 		row=row.replace("\r\n",'#D'+str(count))
# 		print row
# 		count=count+1
# print count
# print len(lastlines)