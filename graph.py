class Graph(object):

    def __init__(self, dictionary_G=None):
        if dictionary_G == None:
            dictionary_G = {}
        self.dictionary_G = dictionary_G
        paths={}
        self.paths=paths

    def GraphVertices(self):
        return list(self.dictionary_G.keys())

    def EdgesForVertex(self,v):
        return self.dictionary_G[v]

    def GraphEdges(self):
        edges=[]
        for v in self.dictionary_G:
            for v2 in self.dictionary_G[v]:
                if([v,v2] not in edges and [v2,v] not in edges):
                    edges.append([v,v2])
        return edges

    def ChangeVertex(self,v,newv):
        for node, edges in self.dictionary_G.items():  
            for i in range(0,len(edges)):
                if(edges[i]==v):
                    self.dictionary_G[node][i]=newv
        self.dictionary_G[newv]=self.dictionary_G[v]
        del self.dictionary_G[v]


    def AddVertex(self, v): #v has start and end index
        (start,end,doc_num,line_num)=v
        #print("start",start,"end",end)
        if v not in self.dictionary_G:
            self.dictionary_G[v] = []


    def AddSingleEdge(self,edge): #edge=list of 2 vertices, each vertex is a tuple
        v1=edge[0]
        v2=edge[1]
        self.AddVertex(v1)
        self.AddVertex(v2)
        if v1 in self.dictionary_G:
            if v2 not in self.dictionary_G[v1]:
                self.dictionary_G[v1].append(v2)
        else:
            if v2 not in self.dictionary_G[v1]:
                self.dictionary_G[v1].append(v2)



    def DisplayGraph(self):
        return(self.dictionary_G)

       # A function used by DFS
    def DFSUtil(self,v,visited,Map,nodes):
 
        # Mark the current node as visited and print it
        index=Map[v]
        visited[index]= True
        print("vertex",v)
        nodes.append(v)
        # Recur for all the vertices adjacent to this vertex
        for i in self.dictionary_G[v]:
            j=Map[i]
            if visited[j] == False:
                self.DFSUtil(i, visited,Map,nodes)
        return(nodes)
 
    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self,v):
        
        print("v",v)
        # Mark all the vertices as not visited
        visited=[False]*(len(self.dictionary_G))
        Map={}
        i=0
        for x in self.GraphVertices():

            Map[x]=i
            i=i+1

        return self.DFSUtil(v,visited,Map,[])


    


        

 