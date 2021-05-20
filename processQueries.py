"""
    This program implements a simple web search engine.
    CHANGE THE PATH TO DIRECTORY TO RUN THE CODE!
    Date: March 4, 2021
    Written by: Ngoc Bao Han, Nguyen
    Student ID: 20188974
"""
import WebpagePriorityQueue as wpq
import WebPageIndex as wpi
import os

def readFiles(path):
    """
    This function reads the text files existing within the directory and
    return two list of the files in WebPageIndex format and one of the file names

    :param path: local path to the folder including .py and a data folder
    :return:
    webList: collection of file in WebPageIndex format
    fileName: collection of the file names
    """
    webList = []
    fileName = []
    for file in os.listdir(path):
        if file.endswith(".txt"):
            webList.append(wpi.WebPageIndex(os.path.abspath(path + "/" + file)))
            fileName.append(os.path.basename(file))
        else:
            continue
    return webList, fileName


def ask(path):
    """
    This function raises the search process for user, asking the number of results
    user wants to be displayed and show the results for all the queries in the file
    :param path: path to the current directory
    :return:
    """
    print("__________________WELCOME TO PING! - google-wannabe search engine__________________\n")
    print()
    queryPath = ("queries.txt")
    pages, names = readFiles(path + "/data")
    searchQueue = wpq.WebpagePriorityQueue(pages)
    showCount = int(input("How many result do you want us to show?(Max: 9)"))
    queries = open(path + "/" + queryPath, "r").read().split()
    for query in queries:
        print("_____________new search______________")
        print("Search:", query)
        searchQueue.reheap(query)
        for i in range(showCount):
            if searchQueue.peek(True)[0] > 0:
                item = searchQueue.poll(True)
                rep = item[0]
                foundIn = names[pages.index(item[1])]
            print("Found in:", foundIn,", appears",rep, "times")
        print()


if __name__ == "__main__":
    path = "/Users/mimi/Desktop/20188794_A2"
    ask(path)
