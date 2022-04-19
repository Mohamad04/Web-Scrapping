



from BST import *
import re                           # regular expression
import requests                     
from bs4 import BeautifulSoup       # html parser
from collections import deque



# to het th eheight of a node in the binary tree
def getHeight(tree_node):
  if tree_node:
    return 1  + max( getHeight(tree_node.left), getHeight(tree_node.right) )
  return 0


# to check if the balance of the  binary tree 
def checkBalance(tree_node):
    if tree_node:
        h_left = getHeight(tree_node.left)
        h_right = getHeight(tree_node.right)

        return abs(h_left - h_right) <= 1 and checkBalance(tree_node.left) is True and checkBalance(tree_node.right) is True
           
    return True 


# traverse the binary tree
def inorderTraversal(tree_node):
    if tree_node:              
        inorderTraversal(tree_node.left)
        print(tree_node.data)
        inorderTraversal(tree_node.right)






# to check if the binary tree is complete
def isComplete(tree_node):
 
    # return if the tree is empty
    if tree_node is None:
        return True
 
    # create an empty queue and enqueue the tree_node node
    queue = deque()
    queue.append(tree_node)
 
    # flag to mark the end of full nodes
    flag = False
 
    # loop till queue is empty
    while queue:
        # dequeue front node
        front = queue.popleft()
 
        # if we have encountered a non-full node before and the current node
        # is not a leaf, a tree cannot be complete
        if flag and (front.left or front.right):
            return False
 
        # if the left child is empty and the right child exists,
        # a tree cannot be complete
        if front.left is None and front.right:
            return False
 
        # if the left child exists, enqueue it
        if front.left:
            queue.append(front.left)
 
        # if the current node is a non-full node, set the flag to true
        else:
            flag = True
 
        # if the right child exists, enqueue it
        if front.right:
            queue.append(front.right)
 
        # if the current node is a non-full node, set the flag to true
        else:
            flag = True
 
    return True






# using the documentation of the Beautifulsoap. The se-Factory souce html file contains tags and class responsible for displayng the FSW Content
def getFullStackInfo(results):
    FSW_elements = results.find_all("div", class_="row sqs-row")
    
    FSW_weeks = FSW_elements[-1].find_all("p")


    #  search for the last week written and print it
    match_results = FSW_weeks[-1].find_all(string=re.compile("Week"))
    print("It will take between ", re.sub(r"[Week]+","", match_results[0]), " weeks  \n" )
   
    # print(len(FSW_weeks)) #12
    # loop through weeks and display what is inside the <strong> tag
    for week_tech in FSW_weeks:

        if FSW_weeks.index(week_tech) == 1:
            print( week_tech.text.strip()   , " \n") 
        else:

            print(week_tech.find_all(string=re.compile("Week"))[0] )
            title_element = week_tech.find("strong")
            print( title_element.text.strip() , " \n")



    
 



def main():
    # using url for scraping online websites
    url = "https://sefactory.io/fsw"

    result = requests.get(url)                    # get the raw HTML content of the webpage
    doc = BeautifulSoup(result.text , "lxml")     # use lxml for speed
    
    #file -- when working offline on local html file
    # result =  open("C:/Users/moham/Downloads/Learning languages/Python/Computer Science Foundation/Final/seFactory.html", "r")
    # doc = BeautifulSoup(result, "html.parser")


    filter_words = list(set( re.findall(r"[a-zA-z0-9]{5,}",  doc.text) ))       # find all alphanumeric character, numbers strings whose length greater than 4

    tree_node = Node( filter_words[0] )
                       
   

    for i in  filter_words:    
        insertIntoBST(tree_node, i )              
        # print(i)
    



    # inorderTraversal(tree_node)

    # if checkBalance(tree_node):
    #     print("Great job, this is a balanced Tree ")
    # else:
    #     print("this tree is not  balanced !!!")


    # if isComplete(tree_node):
    #     print("Great job, this is a Complete Tree ")
    # else:
    #     print("this is not a Complete tree !!!")


    # In the SE Factory html file. the id of the relevant div that contains the FSW information
    # results = doc.find(id="page-section-5ec4e9adb1bf9c4a8cc396ea")
    # getFullStackInfo(results)








main()








#Resources
# 1 - https://realpython.com/python-web-scraping-practical-introduction/
# 2- https://www.crummy.com/software/BeautifulSoup/bs4/doc/#searching-the-tree
#
#
#
#
#