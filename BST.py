






class Node():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right



def insertIntoBST(parent_node, value):                #   Complexity  =  O (height)                     
        if parent_node.data is None:                  # if parent node is empty
            parent_node.data = value                  # make value the root of the tree
            return

        if value < parent_node.data:              #  if it less then the data => must be on the left 
            if parent_node.left is None:        
                parent_node.left = Node(value)    # parent is parent_node.left
            
            else:
                insertIntoBST(parent_node.left, value)   


        else:                         
            if parent_node.right is None:          
                parent_node.right = Node(value)    
            
            else:
                insertIntoBST(parent_node.right, value)   
   






# A binary tree is considered full if every node has exactly 0 or 2 children.
# A binary tree is considered complete if every level is full except the last, and all nodes are pushed as far left as possible.






# b = Node( 'm' )
# # print(b.data)

# words = ['reserved', 'international', 'august', 'admission', 'weekly', 'connect']

# for i in words:
#     insertIntoBST(b, i )


# inorderTraversal(b)