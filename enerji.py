import pyautogui
import time

# not : bütün kordinatlar tamamen sallamadır.

def get_item() :
    pyautogui.displayMousePosition(300,300) # marketi bul
    time.sleep(0.2)
    pyautogui.doubleClick(300,300) # marketi aç
    time.slep(0.2)
    for i in range (1,80) : 
        pyautogui.leftClick(450,700) # marketten item al
        time.sleep(0.7)
    
    
    
def throw_item() : # one item 
    pyautogui.displayMousePosition(750,578) # markter2 bul 
    time.sleep(0.2)
    pyautogui.rightClick(750,15) # tek bir itemi seçme
    time.sleep(0.1)
    pyautogui.moveTo(400,133)  # itemi market 2 üzerine bırakma
    time.sleep(0.1)
    pyautogui.press("enter") # çıkan yazıyı onaylama
    
    

#def throw_item () : # bir çok item
    #pass    
    
    
get_item()
throw_item()