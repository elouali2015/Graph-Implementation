class Node(object): 
	#name of a node
	def __init__(self,name): 
		self.name=name
	def getName(self):
		return self.name 

	def __str__(self):
		return self.name


class Edge(object):
	def __init__(self,source,destination): #source and destination are the names of nodes 

		self.source=source
		self.destination=destination

	def getSource(self):

		return self.source

	def getDestination(self):

		return self.destination

	def __str__(self):

		return "the edge:"+self.source+"->"+self.destination


class Diagraph(object):
	# Diagraph is a drected graph
	# we define edeges as dictionary
	def __init__(self):
		self.edeges={}
	def addNode(self,node):
		if node in self.edeges:
			raise "Duplicate Node"
		else:
			self.edeges[node]={} 
	def addEdge(self,edge):    #edges are represented by values as destination and sources as key of dictionary 
		source=edge.getSource()
		destination=edge.getDestination()

		if not(source in self.edeges and destination in self.edeges):

			raise ValueError("nodes dosen't exist") 
		else:
			self.edeges[source].append(destination)  
    
#every Graph is a Diagraph but not the inverse
 class Graph(Diagraph):
 	def addEdge(self,edge):
 		Diagraph.addEdge(self,edge)
 		rev=Edge(edge.getDestination(),edge.getSource())
 		Diagraph.addEdge(self,rev)








