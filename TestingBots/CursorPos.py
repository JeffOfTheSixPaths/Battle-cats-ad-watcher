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
#pyautogui.displayMousePosition()
#click(3115,187) X Button
#time.sleep(1)
click(2875,821)#Catfood
time.sleep(1)
win32api.SetCursorPos((2586,315))


    
