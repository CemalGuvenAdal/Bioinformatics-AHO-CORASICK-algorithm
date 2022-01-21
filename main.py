import argparse

#parser
parser = argparse.ArgumentParser()
parser.add_argument("-i")
args = parser.parse_args()
file1Name = args.i
class Node:
    def __init__(self):

        self.char='-'
        self.children=[None]*128
        self.end=False
        self.parent=None
        self.ID=0
        self.n=None
        self.height=0
        self.text=""

class Tree:

    def __init__(self):
        self.root = self.getNode()
        self.root.height=-1

    def getNode(self):
        return Node()
    def insert(self,word,ID):
        IDinsert=ID
        passing = self.root
        length = len(word)
        for level in range(length):
            i = ord(word[level])-ord('\0')


            if not passing.children[i]:
                passing.children[i] = self.getNode()
                passing.children[i].char=word[level]
                passing.children[i].parent=passing
                passing.children[i].ID=IDinsert
                passing.children[i].height=passing.height+1
                IDinsert=IDinsert+1
            if passing==self.root:
                passing.children[i].n=self.root

            passing = passing.children[i]

        passing.end = True
        passing.text = word
        return IDinsert
#printing---------------



#BreadFirstSearch--------------------------------------------
def bfs( node):

  queue = []
  queue.append(node)

  list1=[]
  while queue:
      s = queue.pop(0)
      for i in range(0,128):

          if s.children[i]:
              queue.append(s.children[i])
              list1.append(s.children[i])
  return list1

file1 = open(file1Name, 'r')
Lines = file1.readlines()
T=""
T2=""
countline=0
for line in Lines[0:1]:
    countline += 1
    T=T+line.strip()

for line in Lines[1:]:
    countline += 1
    T2=T2+line.strip()

keys = T
output = T2

#FailuareLink--------------------
def FailuareLink(listofnodes,root):
    for i in range(0,len(listofnodes)):

        nodeV=listofnodes[i]
        vP=nodeV.parent
        char=nodeV.char
        x=ord(char)-ord('\0')
        w=vP.n
        while(w!=root and w!=None and w.children[x]==None):
            w=w.n
        if(w!=None and w.children[x]!=None):
            nodeV.n=w.children[x]
        else:
            nodeV.n=root



#--ahocorasic algorithm-------------
def AhocorasicAlg(keys,text):
    t= Tree()
    ID=1
    for j in keys:
        ID=t.insert(j,ID)

    list2=bfs(t.root)
    FailuareLink(list2,t.root)

    root=t.root
    x=root
    high=1
    printList(list2)
    print("Search:----------------------------")
    counter=0
    outputlist=[]

    while counter<len(text):

        i=ord(text[counter])-ord('\0')
        while x.children[i]!=None:
            x=x.children[i]
            counter=counter+1
            if(counter >= len(text)):
                break
            i=ord(text[counter])-ord('\0')
            if(x.end):
                print("keyword: ",x.text, " index: ", high)

        if(x != root):
            x=x.n

        high=counter-x.height
        counter=counter+1




def printList(list2):
    for i in range(0,len(list2)):
        for j in range(0,len(list2)):
            if(list2[j].ID==i+1):
                str1=[]
                for k in range(0,128):
                    if list2[j].children[k]:
                        str1.append(list2[j].children[k].ID)
                        str1.sort()
                print("char: ",list2[j].char, "Next States: ",str1, "  Fail State: " ,list2[j].n.ID,"  Output: ['",list2[j].text,"']")
#----------------------------------------------------------
#Taking the words
words1 = keys.split()

#print(words1)


#--------------------------------
AhocorasicAlg(words1,output)

#Printing results----------------------------
