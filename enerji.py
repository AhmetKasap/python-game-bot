import pyautogui
import time

'''
bot dışında karekteri silah satıcısına bırak => item al => simyacıyıya git => itemleri simyacı üzerine bırak => 
işlem bittikten sonra tekrar silah satıcısına git => işlemler tekrarlansın.
''' 


def start(x,y): 
    pyautogui.leftClick()(x,y)
    

def get_item() :
    pyautogui.displayMousePosition(300,300) # silah satıcısı kordinantı
    time.sleep(0.2)
    pyautogui.leftClick()(300,300)
    time.sleep(0.1)
    pyautogui.press('enter') # silah satıcısını aç
    time.slep(0.2)
    for i in range (1,80) : 
        pyautogui.leftClick(450,700) # marketten 80 tane item al # envanterin ilk 10 satırına 10 adet enerji parçası önceden koy
        time.sleep(0.7)
    
    
def alchemistry_go(): # silah satıcısından simyacıya gidiş   #güncellenecek
    pass

def gun_market() : # simyacıdan silah satıcısına gidiş.   #güncellenecek
    pass

def throw_item () : #itemleri tek tek simyacı üzerine bırakıp enerji parçası üretme
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
    y2 = 250
    y3 = 300
    y4 = 350
    y5 = 400
    y6 = 450
    y7 = 500
    y8 = 550
    y9 = 600
    
    
    for i in range (1,2) : 
    
        for i in range (1,9) : 
            pyautogui.leftClick(x1,y1) # itemi seçme
            pyautogui.mouseDown() 
            pyautogui.moveTo(400,133) # itemi simyacı üzerine bırakma
            pyautogui.mouseUp()
            time.sleep(0.1)
            pyautogui.press("enter") # çıkan yazıyı onaylama
            y1 = y1 + 50 
            
        for i in range (1,9) : 
            pyautogui.leftClick(x1,y1) # itemi seçme
            pyautogui.mouseDown() 
            pyautogui.moveTo(400,133) # itemi simyacı üzerine bırakma
            pyautogui.mouseUp()
            time.sleep(0.1)
            pyautogui.press("enter") # çıkan yazıyı onaylama
            y1 = y1 + 50 
            
        for i in range (1,9) : 
            pyautogui.leftClick(x1,y1) # itemi seçme
            pyautogui.mouseDown() 
            pyautogui.moveTo(400,133) # itemi simyacı üzerine bırakma
            pyautogui.mouseUp()
            time.sleep(0.1)
            pyautogui.press("enter") # çıkan yazıyı onaylama
            y1 = y1 + 50 
            
        for i in range (1,9) : 
            pyautogui.leftClick(x1,y1) # itemi seçme
            pyautogui.mouseDown() 
            pyautogui.moveTo(400,133) # itemi simyacı üzerine bırakma
            pyautogui.mouseUp()
            time.sleep(0.1)
            pyautogui.press("enter") # çıkan yazıyı onaylama
            y1 = y1 + 50 
            
        for i in range (1,9) : 
            pyautogui.leftClick(x1,y1) # itemi seçme
            pyautogui.mouseDown() 
            pyautogui.moveTo(400,133) # itemi simyacı üzerine bırakma
            pyautogui.mouseUp()
            time.sleep(0.1)
            pyautogui.press("enter") # çıkan yazıyı onaylama
            y1 = y1 + 50 
        
        pyautogui.leftClick(750,15) # 2. envanteri aç ve işlem döngüsü 2. defa çalışsın.
        
        
start(500,500) # girilen cordinat ile oyuna tıkla / başla
time.sleep(1)
for i in range (1,15):     
    get_item()
    go_alchemistry()
    throw_item()
    gun_market()
    

def end () : # 10 veya 20 paket enerji parçası yapıldıktan sonra bunu depoya aktarmak lazım. İlk aşamada el ile yapılabilir.
    time.sleep(5400)