from tkinter import *
import tkinter as tk
import logic 


#import logic
#widgets = GUI Elements: buttons, textboxes, labels, images
#windows = serves as a container to hold or contain these widgets
#label = an area widget that holds text and/or an image within a window


#adding size and title to the app
window = tk.Tk() #Instantiate an instance of a window
window.geometry("350x450") 
window.resizable(False,False)
window.title("Calculator")

#adding colors 
window.configure(bg="black")

#adding a icon and configuring the background color
icon = PhotoImage(file="CalculatorPart2.py/pi.png")
window.iconphoto(True,icon)
window.config(background="black")



#adding frame
frame = tk.Frame(window, bg="black")
frame.grid(row=0, column=0, sticky="nsew")


#Adding Display
display=tk.Entry(frame, font=("Arial",20), justify="right")
display.grid(row=0,column=0,columnspan=5, sticky="nsew", padx=8, pady=2, ipady=12 )

#Adding memory buttons
memory_buttons = ["M+","M-","MR","MS","MC"]
for i, btn in enumerate(memory_buttons):
     Button(frame, text=btn,command=lambda value=btn: button_clicked(value)).grid(row=1, column=i, sticky="nsew", padx=4,pady=4)

#buttons click
def button_clicked(value):
    logic.click(display, value)

#adding numbers and signs as buttons
button_values = [
        ["7","8","9","+"],
        ["4","5","6","-"],
        ["1","2","3","×"],
        ["0",".","x²","÷"],
        ["C","x^y","√","=" ]
]


#style fuctions
def get_button_style(value):
     operators = {"+","-","×","÷","="}
     if value in operators:
          return {"bg": "orange", "fg": "white"}
     elif value == "C":
          return {"bg": "red", "fg": "white"}
     elif value.startswith("M"):
          return {"bg": "green", "fg": "black"}
     else:
          return {"bg": "blue", "fg": "white"}



for r, row in enumerate(button_values):
     for c, val in enumerate(row):
          
          style = get_button_style(val)


          button = tk.Button(
               frame,
               text=val,
               font=("Arial", 18),
               command=lambda value=val: button_clicked(value),
               bd=5,
               relief="raise", 
               **style
          )
          button.grid(row=r+2, column=c, columnspan=1, sticky="nsew", padx=4, pady=4)

          if val in {"=","÷","×","-","+"}:
               button = tk.Button(
                    frame,
                    text=val,
                    font=("Ariel", 18),
                    command=lambda value=val: button_clicked(value),
                    **style
               )
               button.grid(row=r+2, column=c, columnspan=2, sticky="nsew", padx=4, pady=4)

for i in range(5):
     frame.columnconfigure(i, weight=1, uniform="col")
for i in range(7):
     frame.rowconfigure(i, weight=1, uniform="row")

frame.grid()

window.mainloop() #display window on screen and will listen for events