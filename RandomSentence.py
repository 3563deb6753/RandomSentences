"""
This program generates random sentences from a text file.
And displays them in a graphical window
"""
import random
import tkinter.filedialog
from functools import partial 

# This function reads a file into a list of strings.
# String elements are separated by the newline character.
# @filename is the filepath of the file.
# Returns a list of strings.  
def readFile(filename):
    readFile = open(filename, "r")
    text = readFile.readlines()
    readFile.close()
    return text

    
# This function gets a random sentence within a normal size range.
# @text is a list of strings
# @display_text is a tkinter variable string that holds the label text
def getSentence(text, display_text):
    sentence=""
    while len(sentence) < 50 or len(sentence) > 281:
        randomNum = random.randint(1, len(text)-1)
        sentence = text[randomNum]
    display_text.set(sentence) #set the sentence as the window label's text


def createWindow():
    my_window = tkinter.Tk()
    my_window.geometry("1400x280")
    my_window.title("")
    
    my_button = tkinter.Button(my_window,text="again")
    my_button.config(font=("Courier", 24))
    my_button.pack() 
    
    display_text = tkinter.StringVar(value="default")
    my_Label = tkinter.Label(my_window, textvariable=display_text)
    my_Label.config(wraplength=1300)
    my_Label.config(font=("Courier", 24))
    my_Label.pack()
    
    return my_window, display_text, my_button

def getFile():
    try:
        filename = tkinter.filedialog.askopenfilename()
        return filename
    except IOError:
        print("file not found")

def main():
    my_window, display_text, my_button = createWindow() 
    my_window.withdraw() #hide the window while getting the file
    filename = getFile()
    text = readFile(filename)
    getSentence(text, display_text)
    my_button.config(command=partial(getSentence, text, display_text))
    my_window.deiconify() #show the window
    my_window.mainloop() #keep the window until closed by user
 

    
main()