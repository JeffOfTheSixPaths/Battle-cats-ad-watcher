from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con


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
                    i=2
                    print(i)
                    time.sleep(30)
                    while(i==2):
                        xbutton2= pyautogui.locateOnScreen('xbutton2.png',region=(500,20,1300,1050),confidence=.65,grayscale=True)
                        xbutton=pyautogui.locateOnScreen('xbutton.png',region=(500,20,1300,1050),confidence=.65,grayscale=True)
                        xbutton3=pyautogui.locateOnScreen('xbutton3.png',region=(500,20,1300,1050),confidence=.65,grayscale=True)
                        if ((xbutton!=None or xbutton2!=None or xbutton3!=None) and i==2):
                           
                            click(1732,98)
                            i=3
                            print(i)
                            time.sleep(1)
                            
                            while(i==3):
                                nextbutton=pyautogui.locateOnScreen('okbutton.png',region=(500,20,1300,1050),confidence=.6)
                                if (nextbutton!=None and i==3):
                                    click(1163,663)
                        
                                    i=0
                                    print(i)
                                    time.sleep(10)
                      
       
