import easygui 
import os
import time

msg = "Load application..."
title = "Muhindi Njenga's Application Starter"


choices = ['Google Chrome',"Iexplore","Codeblocks"]

reply = easygui.buttonbox(msg, title, choices=choices)


if reply == "Google Chrome":
    time.sleep(2)
    os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
    print("opening chrome ...")
elif reply == "Iexplore":
    time.sleep(2)
    os.startfile("C:\Program Files\Internet Explorer\iexplore.exe")
    print('opening Explore ...')
elif reply == "Codeblocks":
    time.sleep(2)
    os.startfile("C:\Program Files\CodeBlocks\codeblocks.exe")
    print('opening codeblocks ...')
else:
    time.sleep(2)
    print("Done")
    
