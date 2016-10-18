import speech
import sys
import os
import numpy as np
import pyttsx


counter = 0

while True:
    print "Talk:"

    phrase = speech.input()
    

    print phrase
    
    if phrase == "Friday":
        speech.say("Yes sir!, at your service!")
    if phrase == "What's up" or phrase == "Kamusta":
        speech.say("My system seems to be good sir!,thank you, how about you sir, How's the day?? ")
    if phrase == ("I'm fine") or phrase ==("Well I'm fine") or phrase == ("I'm good") or phrase == ("I'm ok"):
        speech.say(" I'm glad to know that your fine sir! ")
    if phrase == ("Good evening") or phrase == ("Good Evening"):
        os.system("C:\Users\ellen\Desktop\scripts\Greetings.vbs")
    if phrase == ("Translate good morning in tagalog"):
        os.system("C:\Users\ellen\Desktop\scripts\GoodMorning_Tagalog.vbs")
    if phrase == ("Translate good evening in tagalog"):
        os.system("C:\Users\ellen\Desktop\scripts\GoodNight_Tagalog.vbs")
    if phrase == ("Translate good afternoon in tagalog"):
        os.system("C:\Users\ellen\Desktop\scripts\GoodAfternoon_Tagalog.vbs")
    if phrase == ("Thanks") or phrase == ("Thank you"):
        speech.say("My pleasure, anything else sir-?")
    if phrase == ("Friday open documents") or phrase == ("Friday Show documents") or phrase == ("Friday Open documents"):
        speech.say("Opening Documents")
        os.system("C:\Users\ellen\AppData\Roaming\Microsoft\Windows\Libraries\Documents.library-ms")
    if phrase == ("Friday open downloads") or phrase == ("Friday Show downloads") or phrase == ("Friday Open downloads"):
        speech.say("Opening Downloads")
        os.system("start C:\Users\ellen\downloads")
    if phrase == ("Anong oras na"):
        os.system("C:\Users\ellen\Desktop\scripts\Clock.vbs")
        
    if phrase == ("Friday open notepad plus plus") or phrase == ("Friday Open notepad plus plus"):
        speech.say("Opening Notepad++")
        os.system("start notepad++.exe ")
    if phrase == ("Friday open notepad") or phrase == ("Friday Open notepad"):
        speech.say("Opening Notepad")
        os.system("C:\\Users\\ellen\\Desktop\\scripts\\notepad.vbs ")
    if phrase == ("Friday open calculator") or phrase == ("Friday Open calculator"):
        speech.say("Opening Calculator")
        os.system("C:\Users\ellen\Desktop\scripts\calculator.vbs")
    if phrase == ("Friday Open Command prompt") or phrase == ("Friday open Command prompt"):
        speech.say("Opening Command prompt")
        os.system("C:\Users\ellen\Desktop\scripts\cmd.vbs")

    if 'plus' in phrase or 'Plus' in phrase:
        Token = phrase.split(" plus ")

        if Token[0] == "One":
            First = '1'
                
        elif Token[0] == "Two" or Token[0] == "To":
            First = '2'

        elif Token[0] == "Three" or Token[0] == "Tree":
            First = '3'
                
        elif Token[0] == "Four" or Token[0] == "For":
            First = '4'
                
        elif Token[0] == "Five":
            First = '5'
                
        elif Token[0] == "Six":
            First = '6'

        elif Token[0] == "Seven":
            First = '7'
                
        elif Token[0] == "Eight":
            First = '8'
 
        elif Token[0] == "Nine":
            First = '9'
                
        elif Token[0] == "Ten":
            First = '10'

        else:
            First = Token[0]

        if Token[1] == "one":
            Second = '1'
                
        elif Token[1] == "two" or Token[1] == "to":
            Second = '2'


        elif Token[1] == "three" or Token[1] == "tree":
            Second = '3'
                
        elif Token[1] == "four" or Token[1] == "for" :
            Second = '4'
                
        elif Token[1] == "five" :
            Second = '5'
                
        elif Token[1] == "six":
            Second = '6'

        elif Token[1] == "seven":
            Second = '7'
                
        elif Token[1] == "eight":
            Second = '8'
                
        elif Token[1] == "nine":
            Second = '9'
                
        elif Token[1] == "ten":
            Second = '10'

        else:
            Second = Token[1]

        
        try: 
            result = int(First) + int(Second)
            print result
            if result == 10:
                speech.say("TEN")
            else:
                speech.say(result)
                
                
            
        except ValueError:
            print ""

    if '-' in phrase or 'Minus' in phrase or 'minus' in phrase:
        Token = phrase.split(" -")

        
        
        if Token[0] == "One":
            First = '1'
                
        elif Token[0] == "Two" or Token[0] == "To":
            First = '2'

        elif Token[0] == "Three" or Token[0] == "Tree":
            First = '3'
                
        elif Token[0] == "Four" or Token[0] == "For":
            First = '4'
                
        elif Token[0] == "Five":
            First = '5'
                
        elif Token[0] == "Six":
            First = '6'

        elif Token[0] == "Seven":
            First = '7'
                
        elif Token[0] == "Eight":
            First = '8'
 
        elif Token[0] == "Nine":
            First = '9'
                
        elif Token[0] == "Ten":
            First = '10'

        else:
            First = Token[0]

        if Token[1] == "one":
            Second = '1'
                
        elif Token[1] == "two" or Token[1] == "to":
            Second = '2'


        elif Token[1] == "three" or Token[1] == "tree":
            Second = '3'
                
        elif Token[1] == "four" or Token[1] == "for" :
            Second = '4'
                
        elif Token[1] == "five" :
            Second = '5'
                
        elif Token[1] == "six":
            Second = '6'

        elif Token[1] == "seven":
            Second = '7'
                
        elif Token[1] == "eight":
            Second = '8'
                
        elif Token[1] == "nine":
            Second = '9'
                
        elif Token[1] == "ten":
            Second = '10'

        else:
            Second = Token[1]
            
        try: 
            result = long(First) - long(Second)
            speech.say(result)
            print result
            
        except ValueError:
            print ""
            
    if 'times' in phrase or 'Times' in phrase:
        Token = phrase.split(" times ")

        
        if Token[0] == "One":
            First = '1'
                
        elif Token[0] == "Two" or Token[0] == "To":
            First = '2'

        elif Token[0] == "Three" or Token[0] == "Tree":
            First = '3'
                
        elif Token[0] == "Four" or Token[0] == "For":
            First = '4'
                
        elif Token[0] == "Five":
            First = '5'
                
        elif Token[0] == "Six":
            First = '6'

        elif Token[0] == "Seven":
            First = '7'
                
        elif Token[0] == "Eight":
            First = '8'
 
        elif Token[0] == "Nine":
            First = '9'
                
        elif Token[0] == "Ten":
            First = '10'

        else:
            First = Token[0]

        if Token[1] == "one":
            Second = '1'
                
        elif Token[1] == "two" or Token[1] == "to":
            Second = '2'


        elif Token[1] == "three" or Token[1] == "tree":
            Second = '3'
                
        elif Token[1] == "four" or Token[1] == "for" :
            Second = '4'
                
        elif Token[1] == "five" :
            Second = '5'
                
        elif Token[1] == "six":
            Second = '6'

        elif Token[1] == "seven":
            Second = '7'
                
        elif Token[1] == "eight":
            Second = '8'
                
        elif Token[1] == "nine":
            Second = '9'
                
        elif Token[1] == "ten":
            Second = '10'

        else:
            Second = Token[1]
            
        try: 
            result = long(First) * long(Second)
            speech.say(result)
            print result
            
        except ValueError:
            print ""
    #("C:\Users\ellen\Documents")
    if 'Divided by' in phrase or 'divided by' in phrase:
        Token = phrase.split(" divided by ")

        
        if Token[0] == "One":
            First = '1'
                
        elif Token[0] == "Two" or Token[0] == "To":
            First = '2'

        elif Token[0] == "Three" or Token[0] == "Tree":
            First = '3'
                
        elif Token[0] == "Four" or Token[0] == "For":
            First = '4'
                
        elif Token[0] == "Five":
            First = '5'
                
        elif Token[0] == "Six":
            First = '6'

        elif Token[0] == "Seven":
            First = '7'
                
        elif Token[0] == "Eight":
            First = '8'
 
        elif Token[0] == "Nine":
            First = '9'
                
        elif Token[0] == "Ten":
            First = '10'

        else:
            First = Token[0]

        if Token[1] == "one":
            Second = '1'
                
        elif Token[1] == "two" or Token[1] == "to":
            Second = '2'


        elif Token[1] == "three" or Token[1] == "tree":
            Second = '3'
                
        elif Token[1] == "four" or Token[1] == "for" :
            Second = '4'
                
        elif Token[1] == "five" :
            Second = '5'
                
        elif Token[1] == "six":
            Second = '6'

        elif Token[1] == "seven":
            Second = '7'
                
        elif Token[1] == "eight":
            Second = '8'
                
        elif Token[1] == "nine":
            Second = '9'
                
        elif Token[1] == "ten":
            Second = '10'

        else:
            Second = Token[1]
            
        try: 
            result = float(First) / float(Second)
            speech.say(result)
            print result
            
        except ValueError:
            print ""    
    print "You said {0}".format(phrase)

    
        
    
    if phrase == "ayoko na":
        break
