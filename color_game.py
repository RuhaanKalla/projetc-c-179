# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 11:49:58 2022

@author: Dell
"""

from tkinter import*
import random
root = Tk()
root.title("color game")
root.geometry("500x500")
root.config(bg = "white")

label_score = Label(root , text = "Score : 0" , font = "arial 15" , bg = "white" , fg = "black")
label_score.place(relx = 0.2 , rely = 0.3 , anchor = CENTER)

label = Label(root , font = "arial 25" , bg = "white" , fg = "black")
label.place(relx = 0.5 , rely = 0.4 , anchor = CENTER)

input_value = Entry(root)
input_value.place(relx = 0.5 , rely = 0.5 , anchor = CENTER)

class game:
    def __init__(self):
        self._score = 0
        
    def updateGame(self):
        self.text = ["GREEN" , "BLUE" , "RED" , "YELLOW" , "ORANGE" , "PURPLE" , "CYAN" , "AQUA" , "GREY"]
        self.random_no_for_text = random.randint(0 , 8)
        self.color = ["green" , "blue" , "red" , "yellow" ,"orange" , "purple" , "cyan" , "aqua" , "grey"]
        self.random_no_for_color = random.randint(0 , 8)
        label["text"] = self.text[self.random_no_for_text]
        label["fg"] = self.color[self.random_no_for_color]
        
    def _updateScore(self,input_value):
        if(input_value == self.color[self.random_no_for_color]):
            print(self.color[self.random_no_for_color])
            self._score = self._score + random.randint(0,10)
            label_score["text"] = "Score : " + str(self._score)
            
    def get_user_value(self , input_value):
        self._updateScore(input_value)
        
obj = game()

def get_input():
    value = input_value.get()
    obj.get_user_value(value)
    obj.updateGame()
    input_value.delete(0 , END)
    
btn_start = Button(root , text = "Start" , command = obj.updateGame , bg = "SpringGreen4" , fg = "white" , relief = FLAT , padx = 5 , pady = 5 , font = "arial 15") 
btn_start.place(relx = 0.6 , rely = 0.7 , anchor = CENTER)

btn_check = Button(root , text = "Check" , command = get_input , bg = "IndianRed1" , fg = "white" , relief = FLAT , padx = 10 , pady = 1 , font = "arial 15")
btn_check.place(relx = 0.4 , rely = 0.7 , anchor = CENTER) 

root.mainloop()      
        
        
