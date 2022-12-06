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
def escape():
    click(x_buttonX,x_buttonY)
    click(battlecats_iconX,battlecats_iconY)
i=0
battlecats_iconX = 340
battlecats_iconY = 20
skip_loreX = 1640
skip_loreY = 936
play_homescreenX = 920
play_homescreenY = 641
#have empire_of_cats, play_homescreen,and chapter1 be the same and click nothing on the normal menu
empire_of_catsX = 920
empire_of_catsY = 641
chapter1X = 920
chapter2Y = 641
catfoodX = 1404
catfoodY = 975
watchmediaX = 1001
watchmediaY = 238
no_mediaX = 1287
no_mediaY = 571
resume_buttonX = 1061
resume_buttonY = 662
ok_buttonX =1163
ok_buttonY=663
x_buttonX = 1790
x_buttonY = 80

    
while keyboard.is_pressed('q')==False:

    print("--------------------------------------")
    print("Checking if app crashed or not")
    battlecats= pyautogui.locateOnScreen('battlecats.png',region=(10,100,600,600),confidence=.8)
    if(battlecats!=None):
        print("app crashed")
        click(battlecats_iconX,battlecats_iconY) # battle cats app
        time.sleep(10)
        click(skip_loreX,skip_loreY) # skip lore
        time.sleep(3)
        click(play_homescreenX,play_homescreenY) #play button
        time.sleep(2)
        click(empire_of_catsX,empire_of_catsY) #empire of cats
        time.sleep(2)            
        click(chapter1X,chapter1Y)  #chapter 1
        time.sleep(2)            
   
    
 
    click(catfoodX,catfoodY) #catfood icon
    print("Clicked catfood")
    time.sleep(1)
    click(watchmediaX,watchmediaY)   #ad button
    print("Watching ad")
    time.sleep(1)
    print("checking for no media")
    media= pyautogui.locateOnScreen('nomedia.png',region=(500,20,1300,1050),confidence=.8)
    if(media!=None):
        print("No media found waiting for 10 seconds")
        click(no_mediaX,no_mediaY)   #clicks ok button on the nomedia screen
        time.sleep(10)
        click(catfoodX,catfoodY)    #clicks catfood icon( since it brought you to the main menu)
        print("--------------------------------------")
        print("Clicks catfood")
        time.sleep(1)
        click(watchmediaX,watchmediaY)    #clicks ad button
        print("Watching Ad")
        time.sleep(1)
    time.sleep(17)
    escape()
    time.sleep(.2)
    keyboard2.press(Key.esc)
    keyboard2.release(Key.esc)
    print("First Escape Pressed")
    nextbutton=pyautogui.locateOnScreen('okbutton.png',region=(500,20,1300,1050),confidence=.5)
    print("looking for the OK button")
    if (nextbutton!=None):
        print("Found the OK button")
        click(ok_buttonX,ok_buttonY)
        time.sleep(1)
    elif(nextbutton==None):
        print("didn't find the ok button, checking again in 14 seconds")
        time.sleep(14)
        escape()
        print("Seconds escape pressed")
        time.sleep(2)
        print("Looking for the OK button")
        nextbutton=pyautogui.locateOnScreen('okbutton.png',region=(500,20,1300,1050),confidence=.5)
        if(nextbutton!=None):
            print("Found the OK button")
            time.sleep(1)
            click(ok_buttonX,ok_buttonY)
            time.sleep(2)
        elif(nextbutton==None):
            print("Didn't find the OK button, checking again in 16 seconds")
            time.sleep(16)
            escape()
            print("Third Escape Pressed")
            time.sleep(2)
            print("looking for OK button")
            nextbutton=pyautogui.locateOnScreen('okbutton.png',region=(500,20,1300,1050),confidence=.5)
            if(nextbutton!=None):
                click(ok_buttonX,ok_buttonY)  # clicks ok button
                print("Should've clicked the OK button")
                time.sleep(2)
            elif(nextbutton==None):
                print("Didn't find the OK button, checking again in 14 seconds")
                time.sleep(14)
                escape()
                print("Fourth escape pressed")
                time.sleep(2)
                click(ok_buttonX,ok_buttonY)
                print("Should've clicked the ok button")
                time.sleep(5)
                
