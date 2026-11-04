import tkinter as tk
import random

root = tk.Tk()
root.title("My First App")
root.geometry("400x300")
root.configure(bg="white")

count = 0
colors = ["white", "black", "gray", "lightgray", "darkgray",
          "blue", "lightblue", "navy", "cyan", "skyblue", "royalblue",
          "green", "lightgreen", "darkgreen", "forestgreen", "lime",
          "red", "pink", "darkred", "crimson", "salmon", "coral",
          "yellow", "orange", "gold", "darkorange", "khaki",
          "purple", "violet", "plum", "orchid", "magenta",
          "brown", "chocolate", "tan", "sienna"]

def magic() : 
    global count
    count += 1
    color = random.choice(colors)
    btn.config(text=f'Clicked {count} Times !!!', bg=color,fg="white")

btn = tk.Button(root,text="Click ME",font=("Arial",18),command=magic)    
btn.pack(pady=100,padx=20)
root.mainloop()


'''
Create something usefull like raddar system as sir said for diwali vacation
'''