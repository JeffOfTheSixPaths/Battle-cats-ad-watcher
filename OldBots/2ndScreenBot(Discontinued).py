from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
from pynput.keyboard import Key, Controller
keyboard2 = Controller()

time.sleep(2)
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
i=0

while True: 
    if(keyboard.is_pressed('q'))== True:
       break;
    while keyboard.is_pressed('q')==False:
        click(2875,821)#Clicks The Catfood Button on the homescreen
        print("-------------------------------------------------------")
        print(" Pressed The Cat Food")
        time.sleep(1)
        click(2586,315)#Clicks "Watch Media" Button
        print("Watching ad")
        time.sleep(17)
        keyboard2.press(Key.esc)
        keyboard2.release(Key.esc)
        print("First Esc")
        time.sleep(2)
        nextbutton=pyautogui.locateOnScreen('okbutton.png',region=(1920,20,1200,1000),confidence=.6)
        print("First OK Check")
        if (nextbutton!=None):  
            click(2706,592)#Clicks the OK Button after The first Escape check
            time.sleep(1)
        elif(nextbutton==None):
            time.sleep(15)
            keyboard2.press(Key.esc)
            keyboard2.release(Key.esc)
            print("Seconds Escape")
            time.sleep(1)
            nextbutton=pyautogui.locateOnScreen('okbutton.png',region=(1920,20,1200,1000),confidence=.6)
            if(nextbutton!=None):
                print("Found OK button and now resetting")
                time.sleep(1)
                click(2706,592)#Clicks on the Ok Button
                time.sleep(5)
            elif(nextbutton==None):
                print("Did not find OK button, sleeping for 30 seconds")
                time.sleep(30)
                print("Third escape")
                keyboard2.press(Key.esc)
                keyboard2.release(Key.esc)
                time.sleep(.5)
                click(2875,821) #Clicks x button
                time.sleep(1)
                click(2706,592)#Clicks Ok button
                print("Should be reset")
                time.sleep(5)
