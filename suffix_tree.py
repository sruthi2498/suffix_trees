from graph import Graph
from difflib import SequenceMatcher
from file_output import *
import string
str_punct=string.punctuation

class SuffixTree(object):

	def __init__(self):
		Tree={}
		Tree=Graph(Tree)
		self.STree=Tree
		#self.String=string
		#self.doc_num=doc_num
		#self.line_num=line_num
		#self.CreateTree()


	def CreateTree(self,doc_num,line_num,string):
		self.String=''
		# self.doc_num=doc_num
		# self.line_num=line_num
		self.STree.AddSingleEdge( [ (0,0,-1,-1) , (0,len(self.String),doc_num,line_num) ] )
		self.Root=(0,0,-1,-1)
		self.AddToTree(doc_num,line_num,string)


	def AddToTree(self,doc_num,line_num,string):
		string=reduce(lambda s,c: s.replace(c, '$'), str_punct, string)
		string=string+'$'
		string=string.replace(' ','')
		n1=len(self.String)
		self.String=self.String+string
		n2=len(self.String)
		#print("initial tree",self.Display())
		for i in range(n1,n2):
			curr_suffix=self.String[i:n2]
			#print("adding suffix",curr_suffix)
			(path,nodes,size)=self.SearchCreateTree(curr_suffix,(0,0,-1,-1),[],[])
			#print(path,nodes)
			if(len(nodes)==0):
				flag=-1
				node=(0,0,-1,-1)
			else:
				flag=1
				node=nodes[len(nodes)-1]
			#(node,flag,size)=self.SearchCreateTree(curr_suffix,self.Root)
			print("searched for suffix",curr_suffix,"returned node",node,"flag",flag)
			
			if(flag==-1 and len(self.String[i:i+len(curr_suffix)])>0): #not found
				#print ("adding node")
				self.STree.AddSingleEdge( [ node , (i,i+len(curr_suffix),doc_num,line_num) ] )
			# if(flag==0):  #entire string found
			# 	#print ("adding leaf")
			# 	self.STree.AddSingleEdge( [ node , (i,i+len(curr_suffix),doc_num,line_num) ] )
			if(flag==1): #partial match
				
				#print("original node",node)
				v1=node[0]
				v2=node[1]

				new_node=(v1,v1+size,doc_num,line_num)
				node1=(v1+size,v2,doc_num,line_num)
				node2=(i+size,i+len(curr_suffix)-1,doc_num,line_num)
				self.STree.ChangeVertex(node,new_node)
				self.STree.AddSingleEdge( [ new_node , node1] )
				self.STree.AddSingleEdge( [ new_node , node2] )

				#print(self.Display())
	def ShowEdges(self,r):
		print(r,"edges")
		edges=self.STree.EdgesForVertex(r)
		for v in edges:
			(start,end,doc_num,line_num)=v
			print(self.String[start:end])
	def Search_2(self,new_string,r,path,nodes):
		print("root",r,"search for",new_string)
		(start,end,doc_num,line_num)=r
		root_str=self.String[start:end]

		edges=self.STree.EdgesForVertex(r)
		self.ShowEdges(r)

		if(len(edges)==0):
			print("no more levels")
			return (path,nodes)

		for v in edges:
			(start,end,doc_num,line_num)=v
			node_str=self.String[start:end]
			print ("root",root_str,"node",node_str)
			s=0
			i=1
			while(i<=len(new_string) and node_str[0:i]==new_string[0:i]):
				print("matched node ",node_str[0:i],"with",new_string[0:i])
				i=i+1
				s=s+1
			if(s>0):
				nodes.append(v)
				path=path.append(node_str[0:s])
				new_string=new_string[s:]
				if(len(new_string)==0):
					return (path,nodes)
				else:
					return self.Search_2(new_string,v,path,nodes)
		return (path,nodes)



	def Search(self,new_string,r,path,nodes):
		print("root",r,"path",path,"nodes",nodes)
		(start,end,doc_num,line_num)=r
		root_str=self.String[start:end]
		#print "search for ",new_string ,"root",root_str,"curr path",path,"curr nodes",nodes
		match=self.MatchStrings(root_str,new_string)
		if(match.size>0 and match.a==0 and match.b==0):
		#  	print("match node",root_str,"match",match)
		#  	path.append(root_str[0:match.size])
		# 	nodes.append(r)
		 	return (path,nodes,len(root_str),1)

		
		edges=self.STree.EdgesForVertex(r)
		size=0
		for v in edges:
			#print(v)
			(start,end,doc_num,line_num)=v
			node_str=self.String[start:end]
			print ("root",root_str,"node",node_str)
			size=0
			i=1
			while(i<=len(node_str) and node_str[0:i]==new_string[0:i]):
				print "matched",node_str[0:i],new_string[0:i]
				i=i+1
				size=size+1
			if(size>=1):
			
				#print("node",node_str,"match",match)
				path.append(node_str[0:match.size])
				nodes.append(v)
				#print("path",path,"nodes",nodes)
				new_string=new_string[size:]
				print("searching for newstring",new_string)
				if(len(new_string)==0):
					return (path,nodes,size,0)
				else:
					(path,nodes,size,found)=self.Search(new_string,v,path,nodes)
				#print("recursive search returned",path,nodes,size,found)
				# if(found):
				# 	return (path,nodes,size,1)

		return (path,nodes,size,1)



	def SearchCreateTree(self,new_string,r,path,nodes):
		#print("root",r,"path",path,"nodes",nodes)
		new_string=new_string.strip()
		#print "search for ",new_string
		(start,end,doc_num,line_num)=r
		root_str=self.String[start:end]
		match=self.MatchStrings(root_str,new_string)
		if(match.size>0 and match.a==0 and match.b==0):
		 	#print("match node",root_str,"match",match)
		 	path.append(root_str[0:match.size])
			nodes.append(r)
			return (path,nodes,len(root_str))

		
		edges=self.STree.EdgesForVertex(r)
		size=0
		for v in edges:
			(start,end,doc_num,line_num)=v
			node_str=self.String[start:end]
			node_str=node_str.replace(' ','')
			size=0
			i=1
			#print("eq",node_str[0:i],new_string[0:i],(node_str[0:i]==new_string[0:i]))
			while(i<=len(node_str) and node_str[0:i]==new_string[0:i]):
				
				i=i+1
				size=size+1
			if(size>=1):
			
				#print("node",node_str,"match",match)
				path.append(node_str[0:match.size])

				nodes.append(v)
				#print("path",path,"nodes",nodes)
				new_string=new_string[size:]
				return (path,nodes,size)
		
		return (path,nodes,size)

	def Query(self,new_string):
		s=new_string.split(' ')

		for i in s:
			print("###################################################\n")
			i=i+'$'
			#print(i,' ' in i)
			self.AllMatches(i)

	def AllMatches(self,new_string):
		print("searching for ",new_string)
		if(len(new_string)==0):
			print("no match found")
			return 0
		i=0
		new_string=new_string.replace(" ","$")
		#print("All matches")
		(path,nodes,size,found)=self.Search(new_string,(0,0,-1,-1),[],[])
		#(path,nodes)=self.Search_2(new_string,(0,0,-1,-1),[],[])
		#print("path",path,"nodes",nodes)
		if(len(nodes)==0):
			self.AllMatches(new_string[i+1:len(new_string)])
		if(len(nodes)>0):
			first_node=nodes[0]
			last_node=nodes[len(nodes)-1]
			#print("last",last_node)
			start=first_node[0]
			end=last_node[1]

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
			#print(path)
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

	def MatchStrings(self,string1,string2):
		match = SequenceMatcher(None, string1, string2).find_longest_match(0, len(string1), 0, len(string2))
		return match

	def Display(self,r):
		print "r",self.String[r[0]:r[1]]

		edges=self.STree.EdgesForVertex(r)
		for v in edges:
			x="\t"+self.String[v[0]:v[1]]+"\t"
			print(x)
		for v in edges:
			self.Display(v)
