import os
import re
import sys
sys.path.append('/usr/lib/python2.7/site-packages')
sys.path.insert(0,'/usr/lib/python2.7/site-packages')
import nltk
import nltk.data

fpath=os.path.join("data", "AesopTales.txt")
f=open(fpath,'r')
lines=f.readlines()

fpath_t=os.path.join("data", "titles.txt")
ft=open(fpath_t,'a+')

titles=[]
file_titles=[]
titles.append(lines[0])
lastlines=[]
i=1
j=0
current_title=titles[j]

while(i<len(lines)):
	t=current_title.replace(' ','_')
	t=t.rstrip()
	t=t.replace("\n","")
	current_file=t+".txt"
	if(current_file not in file_titles):
		file_titles.append(current_file)
	fpath2=os.path.join("data/tales", current_file)
	f2=open(fpath2,'a+')



	if(i<len(lines)-2):
		if(len(lines[i])<=3 and len(lines[i+1])<=3) :
			titles.append(lines[i+2])
			current_title=lines[i+2]

	#print(current_title)
	
	if(lines[i]!=current_title and len(lines[i])>3):
		lines[i]=lines[i].replace("\n"," ")
		lines[i]=lines[i].rstrip()	
		lines[i]=lines[i]+" "	
		f2.write(lines[i])
			

	i=i+1


for i in range(0,len(file_titles)):
	ft.write(str(i+1)+"|"+file_titles[i]+"\n")