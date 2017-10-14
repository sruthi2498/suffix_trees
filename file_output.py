import os


titlesf=os.path.join("data", "titles.txt")
ft=open(titlesf,'r')

all_titles=ft.readlines()

def OpenDocLine(doc_num,line_num,matched_with):
	title_row=all_titles[doc_num-1]
	title=title_row.split('|')
	title=title[1].replace("\n","")
	t=title
	title=os.path.join("data/tales",title)
	f=open(title,'r')
	x=f.readlines()
	line=x[line_num]
	line=line.replace("$"," ")
	t=t.replace('_'," ")
	t=t[0:len(t)-4]
	print "-----------------------------"
	print "Title : ",t
	line=line.split('|')
	line=line[2]
	print "Matched with : ",matched_with
	print("Sentence Found :")
	print(line)
	print "-----------------------------"