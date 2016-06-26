#!/usr/bin/python
class Node(object):
	def __init__(self, data = -1, lchild = None, rchild = None):
        	self.data = data
	        self.lchild = lchild
        	self.rchild = rchild

class BinaryTree(object):
	def __init__(self):
        	self.root = Node()
	def add(self, data):
        	node = Node(data)
	        if self.isEmpty():
			self.root = node
       		else:
			tree_node = self.root
			queue = []
                        queue.append(self.root)
        	        while queue:
                		tree_node = queue.pop(0)
	                	if tree_node.lchild == None:
	        	           tree_node.lchild = node
        	        	   return
		                elif tree_node.rchild == None:
		                   tree_node.rchild = node
		                   return
                		else:
                    			queue.append(tree_node.lchild)
			                queue.append(tree_node.rchild)
	def get(self, partent):
		node=partent
		if node==None:
			return
		if node.lchild==None and node.rchild==None:
			return
		elif node.lchild==None and node.rchild!=None:
			print node.rchild
		elif node.lchild!=None and node.rchild==None:
			print node.lchild
		else:
			print (node.lchild, " ", node.rchild, " ")
		self.get(node.lchild)
		self.get(node.rchild)


