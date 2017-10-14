import os
from suffix_tree import SuffixTree


fpath_t=os.path.join("data", "titles.txt")
ft=open(fpath_t,'r')

tree=SuffixTree()
first=1

for title in ft:
	title=title.split("|")
	title=os.path.join("data/tales",title[1].rstrip())
	f=open(title,'r')
	
	for row in f:
		row=row.split('|')
		doc_num=row[0]
		line_num=row[1]
		sent=row[2].rstrip()
		if(int(doc_num)==1):
			#print(doc_num,line_num,sent)
			if(first):
				print("Creating tree",doc_num,line_num,sent)
				tree.CreateTree(int(doc_num),int(line_num),sent)
				first=0
			else:
				print("adding to tree",doc_num,line_num,sent)
				tree.AddToTree(int(doc_num),int(line_num),sent)
			#print(tree.Display())
tree.Query("tasted")
	



