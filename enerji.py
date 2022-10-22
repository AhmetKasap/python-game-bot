import pyautogui
import time

def start(x,y): 
    pyautogui.leftClick(x,y)
    

def get_item() :
    pyautogui.moveTo(680,363) #silah satıcısı kordinantı
    time.sleep(0.1)
    pyautogui.click(button='left', clicks=1) #silah satıcısına tıkla
    time.sleep(0.1)
    pyautogui.moveTo(680, 300) #silah satıcısını aç
    pyautogui.click(button='left', clicks=1) #marketi aça tıkla
    for i in range (1,80) : # item al
        pyautogui.leftClick(450,700) 
        time.sleep(0.7)
    
    
def go_alchemistry () :
    for i in range (1,45): #4.5 sn
        pyautogui.press('s')
    
    for i in range (1,10):  # 1 sn
        pyautogui.press('e')
        
    for i in range (1,120): # 12sn 
        pyautogui.press('w')
    
    for i in range (1,20):  # 2 sn 
        pyautogui.press('q')
    
    for i in range (1,20):  # 2 sn 
        pyautogui.press('w')

def go_market () :
    for i in range (1,30): #3 sn
        pyautogui.press('s')
    
    for i in range (1,15):  # 1.5 sn
        pyautogui.press('q')
        
    for i in range (1,70): # 7sn 
        pyautogui.press('w')
    
    for i in range (1,3):  # 0.3 sn 
        pyautogui.press('e')
    
    for i in range (1,65):  # 6.5 sn 
        pyautogui.press('w')
        
    for i in range (1,2):  # 0.2 sn 
        pyautogui.press('e')
        
    for i in range (1,15):  # 1.5 sn 
        pyautogui.press('w')

def throw_item () : 
    pyautogui.displayMousePosition(750,578) # simyacıyı kordinantı
    time.sleep(0.2)
    
    # +65 her seferinde
    x1 = 970
    
    x2 = 1035 
    x3 = 1095
    x4 = 1160
    x5 = 1225
    
    # +50 her seferinde 
    y1 = 200
    
    #y2 = 250
    #y3 = 300
    #y4 = 350
    #y5 = 400
    #y6 = 450
    #y7 = 500
    #y8 = 550
    #y9 = 600
    
    
    for i in range (1,2) : 
    
        for i in range (1,9) : 
            pyautogui.moveTo(x1, y1) #item kordinantı
            time.sleep(0.5)
            pyautogui.click(button='left', clicks=1)
            time.sleep(0.5)
            pyautogui.moveTo(680, 363)  
            time.sleep(0.5)
            pyautogui.click(button='left', clicks=1)
            time.sleep(0.5)
            y1 = y1 + 50 
            
        for i in range (1,9) : 
            pyautogui.moveTo(x2, y1)
            time.sleep(0.5)
            pyautogui.click(button='left', clicks=1)
            time.sleep(0.5)
            pyautogui.moveTo(680, 363)  
            time.sleep(0.5)
            pyautogui.click(button='left', clicks=1)
            time.sleep(0.5)
            y1 = y1 + 50 
            
        for i in range (1,9) : 
            pyautogui.moveTo(x3, y1)
            time.sleep(0.5)
            pyautogui.click(button='left', clicks=1)
            time.sleep(0.5)
            pyautogui.moveTo(680, 363)  
            time.sleep(0.5)
            pyautogui.click(button='left', clicks=1)
            time.sleep(0.5)
            y1 = y1 + 50 
            
        for i in range (1,9) : 
            pyautogui.moveTo(x4, y1)
            time.sleep(0.5)
            pyautogui.click(button='left', clicks=1)
            time.sleep(0.5)
            pyautogui.moveTo(680, 363)  
            time.sleep(0.5)
            pyautogui.click(button='left', clicks=1)
            time.sleep(0.5)
            y1 = y1 + 50 
            
        for i in range (1,9) : 
            pyautogui.moveTo(x5, y1)
            time.sleep(0.5)
            pyautogui.click(button='left', clicks=1)
            time.sleep(0.5)
            pyautogui.moveTo(680, 363)  
            time.sleep(0.5)
            pyautogui.click(button='left', clicks=1)
            time.sleep(0.5)
            y1 = y1 + 50 
        
        pyautogui.leftClick(750,15) # 2. envanteri aç ve işlem döngüsü 2. defa çalışsın.
        
        
start(500,500) 
time.sleep(1)
for i in range (1,15):     
    get_item()
    go_alchemistry()
    throw_item()
    go_market()
    

