# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 17:57:41 2020

@author: Funmi
"""


#IMPORTING PACKAGES
import wikipedia as wk
import webbrowser

#PICKING A RANDOM ARTICLE
article = wk.random(1)

#SUMMARY OF THE ARTICLE
summary = wk.summary(article)

#ARTICLE URL
article_load = wk.page(article).url

#TO OPEN URL(not supported by repl.it)
article_open = webbrowser.open(article_load, new = 2)

#FUNCTION TO PROMPT USER INPUT
def wiki4all():
    userInput1 = input("Hey there!!! Will you like to read an article on {}? \n\nType Y for 'YES', or N for 'NO', or Q to QUIT--->".format(article)).lower().strip()
    if (userInput1 == "y") or (userInput1 == "yes"):
        print("\n\n")
        print("There you go.....", "\n", "\n", summary, "\n")
        
        userInput2 = input("That was just to summarize!!! \nWould you like to read further? \n\nType Y for 'YES', or N for 'NO', or Q to QUIT--->").lower().strip()
        if (userInput2 == "y") or (userInput2 == "yes"):
            article_open
            #print("\n")
            #print("Please click on link below " + "\n" + article_load)
        else:
            print("\n")
            print("I guess my job ends here. GOODBYE!!!")
    elif (userInput1 == "q") or (userInput1 == "quit"):
        print("\n")
        print("Ooopsss!! I quit :(")
    elif (userInput1 == "n") or (userInput1 == "no"):
        print("Hmmnnnn....\n")
        wiki4all()
    else:
        print("\n")
        print("I'm sorry, I do not recognize this input.\n\nKindly type Y for 'YES', or N for 'NO', or Q to QUIT in the next prompt.\n")
        wiki4all()

wiki4all()