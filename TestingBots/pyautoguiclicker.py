from pyautogui import *
import pyautogui
from win32 import win32api
import win32.lib.win32con as win32con

#pyautogui.click(1470,1033)
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

click(1070,1033)
