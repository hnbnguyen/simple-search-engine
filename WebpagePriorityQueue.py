"""
    This program creates heap-based implementation of a priority queue named
    WebpagePriorityQueue. Use an array based approach to hold the data items.
    Max Heap implementation with teh mose relevant web-page given a specific query
    will have the highest priority
    Date: March 4th, 2021
    Written By: Ngoc Bao Han, Nguyen
    Student ID: 2018874
"""
import WebPageIndex as wpi
import re

class WebpagePriorityQueue:
    """
    This class implements max heap priority queue in a key-pair format
    (1) reheap(self, query): redesigning the heap with a new query info
    (2) peek(self, count): see the most relevant item
    (3) poll(self, count): remove the most relevant item
    (4) addPriority(self, webList): add a priority value to each file
    (5) inOrder(self, l): rearranging the heap using priority value as guidance
    (6) heapify(self, l, n, i): shuffling item to their places based on priority value
    """
    def __init__(self, webSet, query = None):
        self.heap = []
        self.query = query
        self.webSet = webSet
        if query: # if instance initialized without query just yet
            temp = self.addPriority(webSet)
            self.inOrder(temp)
            self.heap = temp


    def reheap(self, newQuery):
        self.heap = [] #clear out the current heap
        self.query = newQuery
        temp = self.addPriority(self.webSet)
        self.inOrder(temp)
        self.heap = temp

    def peek(self, count=False):
        # the priority is returned with file if user want to get the
        # count of query
        if count is True:
            return self.heap[0]
        else:
            return self.heap[0][1]

    def poll(self, count=False):
        top = self.heap[0]

        if len(self.heap) == 0: #empty case
            return
        if len(self.heap) == 1:#only one element
            self.heap.pop()
            return top

        endIndex = len(self.heap) - 1

        self.heap[0] = self.heap[-1]
        del self.heap[-1]

        for id in range(len(self.heap) // 2 - 1):
            #get child index
            left = 2 * id + 1
            right = 2 * id + 2

            # reaching the end of the heap
            if right > endIndex and left > endIndex:
                break
            elif right > endIndex and left < endIndex:
                if self.heap[id][0] > self.heap[left][0]:
                    self.heap[id], self.heap[left] = self.heap[left], self.heap[item]
                break
            else:
                if(self.heap[id][0] < self.heap[left][0]) or (self.heap[id][0] < self.heap[right][0]):
                    self.heap[id], self.heap[left] = self.heap[left], self.heap[id]
                else:
                    self.heap[id], self.heap[right] = self.heap[right],self.heap[id]

        if count is True:
            return top
        else:
            return top[1]


    def addPriority(self, webList):
        # create a set of list with the second element as the priority node
        querySplit = re.sub(r'[^\w]', ' ',self.query).lower().split()
        newList = []
        for webPage in webList:
            priority = 0
            for query in querySplit:
                if query in webPage.dict.keys(): # only count if word exist in file
                    # get sum from all occurence of words
                    priority += webPage.getCount(query)
            newList.append([priority, webPage])
        return newList

    def inOrder(self, l):
        n = len(l)

        # start organizing from the last element back towards the front
        for i in range(n//2 -1, -1, -1):
            self.heapify(l, n, i)

        for i in range(n-1, 0, -1):
            l[i], l[0] = l[0], l[i]
            self.heapify(l, i, 0)

    def heapify(self, l, n, i):
        top = i
        # get child index
        left = 2 * i + 1
        right = 2 * i + 2

        # swap with left child
        if left < n and l[i][0] > l[left][0]:
            top = left

        # swap with right child
        if right < n and l[top][0] > l[right][0]:
            top = right

        #swap
        if top != i:
            l[i], l[top] = l[top], l[i]
            self.heapify(l, n, top)


if __name__ == "__main__":
    files = ["data/doc1-arraylist.txt", "data/doc2-graph.txt", "data/doc3-binarysearchtree.txt", "data/doc4-stack.txt",
             "data/doc5-queue.txt", "data/doc6-AVLtree.txt", "data/doc7-redblacktree.txt", "data/doc8-heap.txt", "data/doc9-hashtable.txt"]
    webList = []
    for file in files:
        wpiFile = wpi.WebPageIndex(file)
        webList.append(wpiFile)

    call = WebpagePriorityQueue(webList, "the")
    print(call.peek(True))
    print(call.poll(True))
    print(call.poll(True))

