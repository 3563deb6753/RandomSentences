"""
This helper program cleans up text files that have newline characters
in the middle of sentences.  It is helpful to remove unwanted newline
characters because python lists use newline characters to demaracte
elements in list of strings.
"""
import tkinter.filedialog

# This function reads a text file into a list.
# @filename is the filepath chosen by the user
# Returns a list of strings.
def readFile(filename):
    readFile = open(filename, "r")
    text = readFile.readlines()
    readFile.close()
    return text

# This function cleans up the text by replacing newline characters
# with a space if the newline characters appear in the middle of
# a sentence.
# @text is a list of strings
# Returns a string cleanText
def cleanText(text):
    cleanText =""
    for sentence in text:
        if "." not in sentence: 
            cleanText += \
                (sentence.replace("\n"," "))  
        else:
            cleanText += \
                (sentence[0:sentence.index(".")+1] + "\n")
            remaining = sentence[sentence.index(".")+2:]
            cleanText += \
                remaining.replace("\n"," ")
    return cleanText

# Writes the cleaned up text to a new file.
# @text is a string
# @filename is the filepath chosen by the user
def writeFile(text, filename):
    filename += "Clean"
    writeFile = open(filename, "w")
    writeFile.write(text)
    writeFile.close()
    
def main():
    try:
        root = tkinter.Tk()
        root.withdraw()
        filename = tkinter.filedialog.askopenfilename()
    except IOException:
        print("File not found")
    else:
        text = readFile(filename)
        text = cleanText(text)
        writeFile(text,filename)
        print("Complete")

main()