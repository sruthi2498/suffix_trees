from graph import Graph
from difflib import SequenceMatcher
from file_output import *
import string

class SuffixTree(object):

	def __init__(self):
		Tree={}
		Tree=Graph(Tree)
		self.STree=Tree
		self.Root=(0,0,0,0)
		self.STree.AddVertex(self.Root)
		self.String=''


	def Add_To_Tree(self,string,doc_num,line_num):

		n1=len(self.String)
		self.String=self.String+string
		n2=len(self.String)

		for i in range(n1,n2):
			current_suffix=self.String[i:n2]
			new_node=(i,n2,doc_num,line_num)

			print "############### curr",current_suffix
			(nodes,size,pathh,flag)=self.Search(current_suffix,self.Root,[],[],0)
			print(nodes,size,flag)
			ln=self.Root
			if(len(nodes)>0):
				ln=nodes[len(nodes)-1]
			if(flag==-1 or flag==0):
				#print("flag -1")
				self.STree.AddSingleEdge((ln,new_node))
				#print("added edge",ln,new_node)
			else:

				(start,end,dn,lin)=ln
				#print "ln",start,end,dn,lin
				change_val=end-start-size
				#print "change val",change_val
				all_edges_of_ln=self.STree.EdgesForVertex(ln)
				for j in range(0,len(self.STree.dictionary_G[ln])):
					#print "child of ",ln,self.STree.dictionary_G[ln][j]
					(sv,ev,dv,lv)=self.STree.dictionary_G[ln][j]
					sv=sv-change_val
					#print "changing it to",sv,ev,dv,lv
					self.STree.dictionary_G[ln][j]=(sv,ev,dv,lv)
					#print "changed",self.STree.dictionary_G[ln][j]

				old_node=(start,start+size,dn,lin)
				new_node=(i+size,n2,doc_num,line_num)
				#print "new node",i+size,n2
				old_node_2=(start+size,end,dn,lin)

				#print "splitting",ln,"into",old_node,"and",old_node_2,"   adding",new_node

				self.STree.ChangeVertex(ln,old_node)
				#print "changed ",ln,"to",old_node
				self.STree.AddSingleEdge( [ old_node , old_node_2] )
				#print "added edge ",old_node,old_node_2
				self.STree.AddSingleEdge( [ old_node , new_node] )
				#print "added edge ",old_node,new_node
			#print self.STree.DisplayGraph()




	def Search(self,string,r,path,nodes,size):
		print "Search 1 :searching for",string, "at root",r
		#print "children",self.DisplayChildren(r)
		(start,end,doc_num,line_num)=r
		root_string=self.String[start:end]
		edges=self.STree.EdgesForVertex(r)
		if(len(edges)==0):
			#print "no more levels"
			if(r not in nodes):
				nodes.append(r)
			return (nodes,size,path,-1)

		else:
			for v in edges:
				(start,end,doc_num,line_num)=v
				node_string=self.String[start:end]

				i=1
				s=0

				while(i<len(string) and node_string[0:i]==string[0:i]):
					#print("matched",node_string[0:i],string[0:i])
					i=i+1
					s=s+1

				if(s>0): #matched with string partially 
					path.append(node_string[0:size])
					nodes.append(v)
					#print("nodes",nodes)
					if(s==len(string)): #matched perfectly

						string=string[size+1:]
						#print("new string",string)
						return self.Search(string,v,path,nodes,size+s)

					else: #some matched, so return whatever matched
						return (nodes,size+s,path,1)

			return (nodes,size+s,path,0)

	def Search2(self,string,r,path,nodes,size):
		print "Search2 :searching for",string, "at root",r
		#print "children",self.DisplayChildren(r)
		(start,end,doc_num,line_num)=r
		root_string=self.String[start:end]
		edges=self.STree.EdgesForVertex(r)
		if(len(edges)==0):
			print "no more levels"
			if(r not in nodes):
				nodes.append(r)
			return (nodes,size,path,-1)

		else:
			for v in edges:
				(start,end,doc_num,line_num)=v
				node_string=self.String[start:end]
				print(v,node_string,string)
				i=1
				s=0
				while(i<len(string) and node_string[0:i]==string[0:i]):
					print("matched",node_string[0:i],string[0:i])
					i=i+1
					s=s+1
					print("size",s)

				if(s>0): #matched with string partially 
					path.append(node_string[0:s])
					print("path",path)
					nodes.append(v)
					print("nodes",nodes)
					string=string[s:]
					print("new string",string)
					if(len(string)>0 and string!='$'):
						return self.Search2(string,v,path,nodes,size+s)
					else:
						return (nodes,size+s,path,1)


			return (nodes,size+s,path,0)

	def Query(self,new_string):
		s=new_string.split(' ')

		for i in s:
			print("###################################################\n")
			i=i+'$'
			#print(i,' ' in i)
			self.AllMatches(i,[],[],0,[])

	def AllMatches(self,new_string,nodes,path,size,allM):
		print("All matches : searching for ",new_string)
		if(len(new_string)==0):
			print("no match found")
			return 0
		i=0
		new_string=new_string.replace(" ","$")
		#print("All matches")
		(nod,s,p,f)=self.Search2(new_string,self.Root,[],[],0)
		
		allM.append((nod,s,p))
		print "ALl till now",allM
		#(path,nodes)=self.Search_2(new_string,(0,0,-1,-1),[],[])
		print("path",p,"nodes",nod,"size",s,"flag",f)
		if( len(nod)==0 or f==0):
			if (new_string[i+1:len(new_string)] !='$'):
				self.AllMatches(new_string[i+1:len(new_string)],nodes,path,size,allM)
		else:
			allM=sorted(allM,key=lambda x: x[1],reverse=True)
			print allM
			for (nod,s,p) in allM:
				print "ranked s",s,"nodes",nod
				if(len(nod)>0):
					last_node=nod[len(nod)-1]
					x=self.PrintAllPaths(last_node)


	def PrintAllPaths(self,s):
		#print("here")
		visited=[False]*(len(self.STree.GraphVertices()))
		l=self.STree.GraphVertices()
		#print(l)
		Map={}
		for i in range(0,len(l)):
			#print(l[i])
			Map[l[i]]=i
		#print(Map)
        # Create an array to store paths
		path = []
		paths=[]
        # Call the recursive helper function to print all paths
		self.PrintAllPathsUtil(s,visited,Map, path,1,s)
		
	def PrintAllPathsUtil(self, u, visited,Map, path,flag,r):
		
		index=Map[u]
		visited[index]= True
		path.append(u)

		u_edges=self.STree.EdgesForVertex(u)
		if(len(u_edges)==0):
			self.CurrentPath(path)
		for i in u_edges:
			j=Map[i]
			if visited[j]==False:
				self.PrintAllPathsUtil(i, visited,Map, path,0,r)

                     
        # Remove current vertex from path[] and mark it as unvisited
		path.pop()
		index=Map[u]
		visited[index]= False
		return 1

	def CurrentPath(self,path):
		p=''
		last_node=path[len(path)-1]
		for node in path:
			(start,end,doc_num,line_num)=node
			s=self.String[start:end]
			p=p+"|"+s
		print("path:",p)
		(start,end,doc_num,line_num)=last_node
		#matched_with=p.replace('|','..')
		matched_with=p
		matched_with=matched_with.replace('$',' ')
		OpenDocLine(doc_num,line_num,matched_with)
		return 1

	def DisplayChildren(self,r):
		for v in self.STree.EdgesForVertex(r):
			print "\t\t",self.String[v[0]:v[1]]

	def Display(self):
		for v in self.STree.GraphVertices():
			print "parent:",v,self.String[v[0]:v[1]]
			print "\tchildren:"
			print "\t",self.DisplayChildren(v)

