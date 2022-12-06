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
#1163 Y:  663
#
#


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
        click(1404,975)
        print("-------------------------------------------------------")
        print(" Pressed The Cat Food")
        time.sleep(1)
        click(1001,238)
        print("Watching ad")
        time.sleep(15)
        keyboard2.press(Key.esc)
        keyboard2.release(Key.esc)
        print("First Esc")
        time.sleep(2)
        nextbutton=pyautogui.locateOnScreen('okbutton.png',region=(500,20,1300,1050),confidence=.6)
        print("First OK Check")
        if (nextbutton!=None):  
            click(1163,663)
            time.sleep(1)
        elif(nextbutton==None):
            time.sleep(20)
            keyboard2.press(Key.esc)
            keyboard2.release(Key.esc)
            print("Seconds Escape")
            time.sleep(1)
            nextbutton=pyautogui.locateOnScreen('okbutton.png',region=(500,20,1300,1050),confidence=.6)
            if(nextbutton!=None):
                print("Found OK button and now resetting")
                time.sleep(1)
                click(1163,663)
                time.sleep(5)
            elif(nextbutton==None):
                print("Did not find OK button, sleeping for 30 seconds")
                time.sleep(30)
                print("Third escape")
                keyboard2.press(Key.esc)
                keyboard2.release(Key.esc)
                time.sleep(1)
                click(1163,663)
                print("Should be reset")
                time.sleep(5)
