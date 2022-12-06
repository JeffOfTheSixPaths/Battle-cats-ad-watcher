import pyautogui

nextbutton=pyautogui.locateOnScreen('okbutton.png',region=(500,20,1300,1050),confidence=.5)
print("looking for the OK button")
print(nextbutton)
if (nextbutton!=None):
    print("Found the OK button")
    
elif(nextbutton==None):
    print("didn't find the ok button, checking again in 20 seconds")

