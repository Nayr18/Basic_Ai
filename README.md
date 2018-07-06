# Windows OS based Offline Speech Recognition Artificial Intelligence

This is a basic natural language UI written in python. It uses windows' speech API, so it only works with windows operating system.
Compared to google speech API, windows speech recognition works in offline. The python program uses the resources of windows speech recognition module which performs speech to text conversion. 

The program acts like a personal assistant (a virtual) just like JARVIS, but in this program i named it FRIDAY.

THE THINGS FRIDAY CAN DO:
   - Open applications with audible feedback (example command: "Friday, open notepad ++"  FRIDAY: "Opening Notepad++ . . ."
   - Open folders with audible feedback
   - Answer questions 
   - Can perform as a speech based calculator with audible answer
   
CAN BE REPROGRAMMED TO PERFORM:
  - Face recognition using webcam and greet every recognized person with their names
  - Alarm Clock
  - Search internet
  - Realtime translator
  
  
 Requirements:
 speech
 numpy
 pyttsx
 pywin32
 
 install:
   1.download the code.
   2. install required libraries (pip install speech, pip install pyttsx, pip install pywin32)
   3. restart pc.
   4. run the code.
   
   initial test.
   -use microphone, speak "Friday" if there's audible feedback means it works.
   
   changing code.
   i've used my own directory for opening application so change it.
   example: os.system("start C:\Users\ellen\downloads") change to start os.system("start [your directory]\downloads")
   
   i've used vbs scripts to play audible feedback.
   example. i want to ask friday what is the day today, so i need to write vbs script that will read the current date
   based on the system's time.
   
   create new text file. save as checkDay.vbs write:
   
         Set Sapi = Wscript.CreateObject("SAPI.SpVoice")
         Sapi.speak "To day is"+ weekdayname(weekday(date))
         
  edit the friday.py:
         
         if phrase == ("What's the day today"):
        os.system("[your directory]\checkDay.vbs")
 
 
 To improve speech recognition, open windows (find "speech recognition")
 Select "setup microphone" and "Train your computer to better understand you"
 
 gmail: ryanpontillasiraola18@gmail.com
 fb:  facebook.com/RYNPRL
 

   
   

              

