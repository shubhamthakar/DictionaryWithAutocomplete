import pandas as pd
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("400x130")
root.title("Dictionary")
frame = LabelFrame(root,text="", padx=5, pady=5, bg="light blue", bd=5)
frame.grid(row=0, column=0, padx=10, pady=10)
lab1 = Label(frame, text="Word", bg="light blue", font =80)
lab1.grid(row=0, column=0, padx = 25)
e = Entry(frame, bg="pink", font=80)
e.grid(row=0, column=1, padx=10, pady=10, columnspan=4)

def button_click():
    wrd = e.get()
    e.delete(0,END)
    meaning = t.search(wrd)
    if(meaning==-1):
        suggested = t.autocomplete(wrd)
        if suggested:
            msg = "Word not found.\nDid you mean: "
            for i in suggested:
                msg=msg+i+", "
            messagebox.showinfo("Not Found",msg)
        else:
            messagebox.showinfo("Not Found","Word not found.")
    else:
        messagebox.showinfo("Meaning",meaning)

button1 = Button(frame, text="Search", command=button_click, bg="dark blue", fg="white", font=80)
button1.grid(row=1, column=1,ipadx=10, padx=5)
button_quit = Button(frame,text="Exit", command=root.quit, bg="dark blue", fg="white", font=80)
button_quit.grid(row=1, column=2, ipadx = 10, padx=8)

class Node():
    def __init__(self):
        self.isEndofWord = False
        self.dict = {}
        self.meaning = ""

class Tries():
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return Node()

    def getIndex(self, ch):
        return ord(ch)-ord('a')

    def insert(self, word, meaning):
        root = self.root
        len1 = len(word)
        for i in range (0,len1):
            key = self.getIndex(word[i])
            if key not in root.dict:
                root.dict[key] = self.getNode()
            root = root.dict.get(key)
        root.isEndofWord = True
        root.meaning = meaning

    def autocomplete(self, word):
        root = self.root
        len1 = len(word)
        arr = []
        prefix =""
        for i in range (0,len1):
            key = self.getIndex(word[i])
            if key not in root.dict:
                break
            if root.dict[key].isEndofWord:
                arr.append(word[:(i+1)])
            prefix = prefix + word[i]
            root = root.dict.get(key)
        queue = []
        queue.append(root)
        suffixarr = []
        suffixele = None
        while(1):
            if (len(queue)==0):
                return(arr)
            for i in range(0,len(queue)):
                for keyi, valuei in queue[i].dict.items():
                    if valuei.isEndofWord:
                        if len(suffixarr) >0:
                            suffix = suffixarr[i]+chr(97+keyi)
                        else:
                            suffix = chr(keyi +97)
                        arr.append((prefix+suffix))
                        if (len(arr)==4):
                            return(arr)
            for i in range (0,len(queue)):
                rootele = queue.pop(0)
                if len(suffixarr) > 0:
                    suffixele = suffixarr.pop(0)
                for keyi,valuei in rootele.dict.items():
                    queue.append(valuei)
                    if suffixele == None:
                        suffixarr.append(chr(keyi+97))
                    else:
                        suffixarr.append((suffixele + chr(keyi+97)))

    def search(self, word):
        root = self.root
        len1 = len(word)
        for i in range (0,len1):
            key = self.getIndex(word[i])
            if key not in root.dict:
                return -1
                #print("Did you mean :")
                #self.autocomplete(word)
            root = root.dict.get(key)
        if root.isEndofWord == False:
            return -1
        else:
            return root.meaning.strip()

    def delete(self, word):
        root = self.root
        len1 = len(word)
        for i in range (0,len1):
            key = self.getIndex(word[i])
            if key not in root.dict:
                print("Word is not present")
                return -1
            root = root.dict.get(key)
        root.isEndofWord = False
        root.meaning = ""

t = Tries()
df = pd.read_csv('word_list.csv')
df1 = df.to_numpy()
for i in df1:
    t.insert(i[0],i[1])
root.mainloop()