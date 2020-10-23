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
        st =""
        for i in range (0,len1):
            key = self.getIndex(word[i])
            if key not in root.dict:
                break
            st = st + word[i]
            root = root.dict.get(key)
        for keyi, valuei in root.dict.items():
            if valuei.isEndofWord :
                print(st,end="")
                suffix = chr(keyi+97)
                print(suffix)
        for keyi, valuei in root.dict.items():
            for keyj, valuej in valuei.dict.items():
                if valuej.isEndofWord:
                    print(st,end="")
                    suffix = chr(97+keyi)+chr(97+keyj)
                    print(suffix)

    def search(self, word):
        root = self.root
        len1 = len(word)
        for i in range (0,len1):
            key = self.getIndex(word[i])
            if key not in root.dict:
                print("The word you entered does not exist")
                print("Did you mean :")
                self.autocomplete(word)
                return -1
            root = root.dict.get(key)
        if root.isEndofWord == False:
            print("The word you entered does not exist")
            print("Did you mean :")
            self.autocomplete(word)
            return -1
        else:
            print(root.meaning)
            return 1

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
words = ["language", "computer", "map"]
meanings = ["the method of human communication", 
"A computer is a machine that can be instructed to carry out sequences of arithmetic logical operations automatically via computer programming",
"a diagrammatic representation of an area", ]
for i in range (0,len(words)):
    t.insert(words[i], meanings[i])

t.search("langua")
t.search("languaf")
t.search("computers")
t.search("m")