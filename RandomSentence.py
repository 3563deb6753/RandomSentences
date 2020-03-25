"""
This program generates 10 random sentences from a text file.
"""
import random
import tkinter.filedialog

# This function reads a file into a list of strings.
# String elements are separated by the newline character.
# @filename is the filepath of the file.
# Returns a list of strings.  
def readFile(filename):
    readFile = open(filename, "r")
    text = readFile.readlines()
    readFile.close()
    return text
    
# This function gets a random sentence.
# @text is a list of strings
# Returns a string.
def getSentence(text):
    randomNum = random.randint(1, len(text)-1)
    return text[randomNum]

def main():
    try:
        root = tkinter.Tk()
        root.withdraw()
        filename = tkinter.filedialog.askopenfilename()
    except IOError:
        print("file not found")
    else:
        text = readFile(filename)
        for x in range(10):  # number of random sentences generated
            sentence = getSentence(text)
            if len(sentence) >50 and len(sentence) < 281: 
                print(sentence)
    
main()