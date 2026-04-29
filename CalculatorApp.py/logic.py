

import math
import tkinter as tk
import memory 

memory = 0


def click(display, value, ):
    global memory
    
    if value == "=":
        try:
            expression = display.get()
            expression = expression.replace("×","*").replace("÷","/").replace("^","**")
    
            result = eval(expression)

            display.delete(0, tk.END)
            display.insert(tk.END,str(result))
        except:
            display.delete(0,tk.END)
            display.insert(tk.END, "ERROR")

    #to prevent crashes
        if expression == "":
         return


        if expression[-1] in "+-*/":
            display.delete(0, tk.END)
            display.insert(tk.END, "ERROR")
            return
        try:
            result = eval(expression)
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except:
            display.delete(0, tk.END)
            display.insert(tk.END, "ERROR")
    
    elif value == "√":
        try:
            result = math.sqrt(float(display.get()))
            display.delete(0,tk.END)
            display.insert(tk.END,str(result))
        except:
            display.delete(0,tk.END)
            display.insert(tk.END,"ERROR")
    
    elif value == "x^y":
        display.insert(tk.END,"^")
        


    elif value == "x²":
        try:
            result = float(display.get()) ** 2
            display.delete(0,tk.END)
            display.insert(tk.END, str(result))
        except:
            display.delete(0, tk.END)
            display.insert(tk.END, "ERROR")

    elif value == "C":
        display.delete(0,tk.END)
        

#Adding memory fuction to buttons
    elif value == "MS":
        try:
            memory = float(display.get())
            display.delete(0,tk.END)
            display.insert(tk.END,"MEMORY STORED")
        except:
            memory = 0

    elif value == "M+":
        try:
            memory += float(display.get())
        except:
            pass

    elif value == "M-":
        try:
            memory -= float(display.get())
        except:
            pass

    elif value == "MR":
        display.delete(0,tk.END)
        display.insert(tk.END, str(memory))

    elif value == "MC":
        memory = 0
        display.delete(0,tk.END)
        display.insert(tk.END,"MEMORY CLEARED")
        
    elif value in "+-×÷":
        current = display.get()

        if current == "":  #can not click the operator first
            return
    
        if current[-1] in "+-×÷": #double operators not allowed
            return

        display.insert(tk.END, value)
    else:
        display.insert(tk.END, value)

 





    


