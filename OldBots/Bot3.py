from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
from pynput.keyboard import Key, Controller
keyboard2 = Controller()

#500,20,1300,1050- region
#X: 1404 Y:  975- catfood
#X: 1001 Y:  238 - watch button
#X: 1732 Y:   98
#1061 Y:  662- resume button
#1287 Y:  571- no media available



time.sleep(2)
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
i=0
battlecatsX = 129
battlecatsY = 358
catfoodX = 1404
catfoodY = 975
watchmediaX = 1001
watchmediaY = 238
no_mediaX = 1287
no_mediaY = 571
resume_buttonX = 1061
resume_bottonY = 662

while True:
    
        
    if(keyboard.is_pressed('q'))== True:
       break;
    while keyboard.is_pressed('q')==False:
        battlecats= pyautogui.locateOnScreen('battlecats.png',region=(10,100,600,600),confidence=.8)
        print("---------------------------------------------------------------")
        print("Checking if game crashed")
        if(battlecats!=None):
            print("Game crashed")
            click(129,358)#reopens BattleCats by PONOS
       
        
        click(1404,975)#Clicks catfood.png
        print("Clicked Catfood")
        time.sleep(1)
        click(1001,238)#Clicks the watch ad thing
        print("Watching Advertisment")
        time.sleep(1)
        media= pyautogui.locateOnScreen('nomedia.png',region=(500,20,1300,1050),confidence=.8)
        print("Checking if there's media")
        if(media!=None):
            click(1287,571)#nomedia.png location
            print("No media, waiting 10 seconds and then trying again")
            time.sleep(10)
            click(1404,975)#Clicks catfood.png
            print("Clicked Catfood")
            time.sleep(1)
            click(1001,238)#Clicks the ad watching thing
            time.sleep(1)
        else:
            print("No nomedia button located. Continuing like normal")
        time.sleep(16)
        keyboard2.press(Key.esc)
        keyboard2.release(Key.esc)
        print("First Escape Pressed")
        time.sleep(2)
        resume=pyautogui.locateOnScreen('resume.png',region=(687,390,605,400),confidence=.6)
        print("Looking for ResumeButton")
        if(resume!=None):
            print("Found ResumeButton")
            click(1061,662)#Clicks the Resume button for those shorter ads
        nextbutton=pyautogui.locateOnScreen('okbutton.png',region=(500,20,1300,1050),confidence=.6)
        print("Looking for OK button")
        if (nextbutton!=None):
            print("Found Ok button. Resetting program")
            click(1163,663)#Clicks the Ok button
            time.sleep(1)
        elif(nextbutton==None):
            time.sleep(20)
            keyboard2.press(Key.esc)
            keyboard2.release(Key.esc)
            print("Second Escape Pressed")
            time.sleep(2)
            nextbutton=pyautogui.locateOnScreen('okbutton.png',region=(500,20,1300,1050),confidence=.6)
            print("Looking for Ok button")
            if(nextbutton!=None):
                print("Found The OK Button")
                time.sleep(1)
                click(1163,663)#Clicks the OK button
                time.sleep(2)
            elif(nextbutton==None):
                print("Could not find OK button. Sleeping for 30 seconds")
                time.sleep(30)
                keyboard2.press(Key.esc)
                keyboard2.release(Key.esc)
                print("Third Escape Pressed")
                time.sleep(2)
                click(1163,663)
                time.sleep(2)
        
        '''
        catfood= pyautogui.locateOnScreen('catfood.png',region=(500,20,1300,1050),confidence=.5)
        if(catfood!=None and i==0):
            click(1404,975)
            
            i=1
            print(i)
            time.sleep(1)
        while(i==1):
             
            
            watchbutton=pyautogui.locateOnScreen('watch.png',region=(500,20,1300,1050),confidence=.5)
            if(watchbutton!=None and i==1):
                click(1001,238)
                counter= 0
                i=2
                print(i)
                time.sleep(6)
        while(i==2):
            
                
          
            xbutton6=pyautogui.locateOnScreen('xbutton6.png',region=(500,20,1300,1050),confidence=.8,grayscale=True)
            xbutton2= pyautogui.locateOnScreen('xbutton2.png',region=(500,20,1300,1050),confidence=.8,grayscale=True)
            xbutton=pyautogui.locateOnScreen('xbutton.png',region=(500,20,1300,1050),confidence=.8,grayscale=True)
            xbutton3=pyautogui.locateOnScreen('xbutton3.png',region=(500,20,1300,1050),confidence=.8,grayscale=True)
            if ((xbutton!=None or xbutton2!=None or xbutton3!=None or xbutton6!=None) and i==2):
                time.sleep(2)

           
        

                keyboard2.press(Key.esc)
                keyboard2.release(Key.esc)
                time.sleep(3)
                click(1732,98)
                keyboard2.press(Key.esc)
                keyboard2.release(Key.esc)
                time.sleep(3)
                keyboard2.press(Key.esc)
                keyboard2.release(Key.esc)
                i=3
                print(i)
                time.sleep(1)

        while(i==3):
            
                
          
            nextbutton=pyautogui.locateOnScreen('okbutton.png',region=(500,20,1300,1050),confidence=.6)
            if (nextbutton!=None and i==3):
                click(1163,663)
                

        

                i=0
                #print(i)
                time.sleep(3)
         '''   
