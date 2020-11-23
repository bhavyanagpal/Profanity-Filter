
import os
import json
import re


file=open("article.txt","r", encoding="utf-8")
text=file.read()
file.close()



class Wordfilter:
    def __init__(self):
        # json is in same directory as this class, given by __location__.

        #creates a list of flag words from json file

        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))
        with open(os.path.join(__location__, 'text.json')) as self.f:
            self.blacklist = json.loads(self.f.read())

    def blacklisted(self, string):

        #checks for flag words in a string and prints flag words. Returns boolean value whether there are flag words in the article or not

        test_string = string.lower().replace('0','o').replace('1','l').replace('!','i').replace(" ","").replace("$","s")
        flag=0
        for badword in self.blacklist:
            if badword in test_string:
                flag=flag+1
                print(badword)
                
        if flag>0:
            print("The article is NSFW!!")
            return True
        print("The article looks clean")    
        return False

    def addWord(self, word):

        # adds a word to the json file in the list of flag words

        self.blacklist.extend([word.lower()])
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        with open(os.path.join(__location__, 'text.json'),"w") as f:
            json.dump(self.blacklist,f)

    def removeWord(self, word):

        #removes a word from the json file
        
        self.blacklist = [x for x in self.blacklist if x != word]
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        with open(os.path.join(__location__, 'text.json'),"w") as f:
            json.dump(self.blacklist,f)


wordfilter=Wordfilter()

print(wordfilter.blacklisted(text))       