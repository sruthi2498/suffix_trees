import os
import re
import sys

def WordEnd(sent,start,end):
	sent_len=len(sent)
	sent=sent.replace(" ","$")


def Format(val,filename):
	lines=open(filename).readlines()
	f=open(filename,'w')
	
	for i in range(0,len(lines)):
		lines[i]=lines[i].rstrip()
		lines[i]=lines[i].lower()
		lines[i]=lines[i].replace("\n"," ")
		lines[i]=lines[i].replace(" ","$")
		#print(len(temp))
		#print("\n" in lines[i])
		lines[i]=str(val)+"|"+str(i)+"|"+lines[i]
		#print(lines[i])
	#print(lines)
	lines="\n".join(lines)
	#print(lines)
	f.write(lines)
#1-doc number, 2- line number


titlesf=os.path.join("data", "titles.txt")
ft=open(titlesf,'r')

for row in ft:
	row=row.split('|')
	#print(row)
	title=os.path.join("data/tales",row[1].rstrip())
	val=row[0]

	Format(val,title)
