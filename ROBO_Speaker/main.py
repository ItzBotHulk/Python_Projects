from gtts import gTTS 
  
import os 

print("This is a ROBO Speaker .");

while True:
    x = input("Write what you want to speak : ")
    if x == "s":
        break;
    mytext = f"{x}"
    
    language = 'en'
    
    myobj = gTTS(text=mytext, lang=language, slow=False) 
    
    myobj.save("output.mp3") 
    
    os.system("start output.mp3") 
    