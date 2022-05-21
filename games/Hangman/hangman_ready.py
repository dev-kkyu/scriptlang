import math
from tkinter import * # Import tkinter
from random import *
    
class Hangman:
    def __init__(self):
        self.hiddenWord = list(words[randint(0, len(words) - 1)])
        self.guessWord = []
        self.guessWord.append(['*' for i in range(len(self.hiddenWord))])
        self.nCorrectChar = 0
        self.nMissChar = 0
        self.nMissedLetters = []
        self.finished = 0
        self.setWord()
        self.draw()


    def draw(self):
        # 한꺼번에 지울 요소들을 "hangman" tag로 묶어뒀다가 일괄 삭제.
        canvas.delete("hangman")

        # 인자 : (x1,y1)=topleft, (x2,y2)=bottomright, start=오른쪽이 0도(반시계방향), extent=start부터 몇도까지인지
        #    style='pieslice'|'chord'|'arc'
        canvas.create_arc(20, 200, 100, 240, start = 0, extent = 180, style='chord', tags = "hangman") # Draw the base
        canvas.create_line(60, 200, 60, 20, tags = "hangman")  # Draw the pole
        canvas.create_line(60, 20, 160, 20, tags = "hangman") # Draw the hanger
        
        radius = 20 # 반지름
        canvas.create_line(160, 20, 160, 40, tags = "hangman") # Draw the hanger

        # Draw the circle
        canvas.create_oval(140, 40, 180, 80, tags = "hangman") # Draw the hanger

        # Draw the left arm (중심(160,60)에서 45도 움직인 지점의 x좌표는 cos로, y좌표는 sin으로 얻기)
        x1 = 160 - radius * math.cos(math.radians(45))
        y1 = 60 + radius * math.sin(math.radians(45))
        x2 = 160 - (radius+60) * math.cos(math.radians(45))
        y2 = 60 + (radius+60) * math.sin(math.radians(45))

        canvas.create_line(x1, y1, x2, y2, tags = "hangman")

        x1 = 160 + radius * math.cos(math.radians(45))
        y1 = 60 + radius * math.sin(math.radians(45))
        x2 = 160 + (radius+60) * math.cos(math.radians(45))
        y2 = 60 + (radius+60) * math.sin(math.radians(45))

        canvas.create_line(x1, y1, x2, y2, tags = "hangman")

        canvas.create_line(160, 80, 160, 140, tags = "hangman") # Draw the hanger

        x1 = 160
        y1 = 140
        x2 = 160 - 60 * math.cos(math.radians(45))
        y2 = 140 + 60 * math.sin(math.radians(45))

        canvas.create_line(x1, y1, x2, y2, tags = "hangman")

        x1 = 160
        y1 = 140
        x2 = 160 + 60 * math.cos(math.radians(45))
        y2 = 140 + 60 * math.sin(math.radians(45))

        canvas.create_line(x1, y1, x2, y2, tags = "hangman")

        canvas.create_text(200, 210, text= "정답",font=('맑은 고딕', 15))
        canvas.create_text(200, 240, text= "게임을 계속하려면 Enter를 누르세요",font=('맑은 고딕', 15)) 
    
    def setWord(self):
        self.hiddenWord = list(words[randint(0, len(words) - 1)])
        self.guessWord = []
        self.guessWord.append(['*' for i in range(len(self.hiddenWord))])
        self.nCorrectChar = 0
        self.nMissChar = 0
        self.nMissedLetters = []
        self.finished = 0
    
    def guess(self, spel):
        for i in self.guessWord:
            if spel == i: break
        else: return

        for i in self.nMissedLetters:
            if spel == i: break
        else: return

        count = self.nCorrectChar
        for i, x in enumerate(self.hiddenWord):
            if spel == x:
                self.guessWord[i] = spel
                self.nCorrectChar += 1
            if self.nCorrectChar == len(self.hiddenWord):
                finished = 1
                break
            if count == self.nCorrectChar:
                self.nMissChar += 1
                self.nMissedLetters.append(spel)
                if self.nMissChar == 7:
                    finished = 2
                    break
                
            
        
        
# Initialize words, get the words from a file
infile = open("hangman.txt", "r")
words = infile.read().split()
    
window = Tk() # Create a window
window.title("행맨") # Set a title

def processKeyEvent(event):  
    global hangman
    if event.char >= 'a' and event.char <= 'z':
        canvas.guess(event.char)
        pass
    elif event.keycode == 13:
        if canvas.finished != 0:
            canvas.setWord()
        pass
    
width = 400
height = 280    
# 선, 다각형, 원등을 그리기 위한 캔버스를 생성
canvas = Canvas(window, bg = "white", width = width, height = height)
canvas.pack()

hangman = Hangman()

# Bind with <Key> event
canvas.bind("<Key>", processKeyEvent)
# key 입력 받기 위해 canvas가 focus 가지도록 함.
canvas.focus_set()

window.mainloop() # Create an event loop