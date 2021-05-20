"""
    This class implements WebPageIndex with representation of a webpage into
    an AVL tree map
    Date: March 4th, 2021
    Written by: Ngoc Bao Han, Nguyen
    Student ID: 20188794
"""
import AVLTreeMap as avl
import re

class WebPageIndex:
    """
    This class represent a text file in an AVL tree map with key-value pair
    of word and its reference
    (1) createTree(self): adding key value pair into the tree AVL
    (2) stringToPair(self, string): create a dictionary key value pair for
    all words in the list
    (3) getCount(self, word): get how many time a word occurs in a text
    """
    def __init__(self, file):
        self.text = open(file, "r").read().lower()
        self.dict = self.stringToPair(self.text)
        self.tree = self.createTree()

    def createTree(self):
        tree = avl.AVLTreeMap()
        for key, val in self.dict.items():
            tree.put(key, val)
        return tree

    def stringToPair(self, string):
        text = re.sub(r'[^\w]', ' ',string)
        wordList = list(text.split(" "))
        strList = list(filter(None, wordList))
        uniqueWord = []
        for word in wordList:
            if word not in uniqueWord:
                uniqueWord.append(word)
        uniqueWord = list(filter(None, uniqueWord))

        wordDict = {}
        for i in range(len(uniqueWord)):
            placement = []
            for j in range(len(strList)):
                if uniqueWord[i] == strList[j]:
                    placement.append(j)
            wordDict[uniqueWord[i]] = placement
        return wordDict

    def getCount(self, word):
        for key in self.dict.keys():
            if key == word:
                return len(self.dict.get(key))

if __name__ == "__main__":
    wpi1 = WebPageIndex("data/doc1-arraylist.txt")
    print(wpi1.getCount("the"))


