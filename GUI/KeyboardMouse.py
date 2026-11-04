import tkinter as tk

root = tk.Tk()
root.title("My First App")
root.geometry("500x400")

def key_pressed(event): 
    keyboard.config(text=f'You Pressed : {event.keysym}')

def mouse_clicked(event): 
    mouse.config(text=f'You Clicked at : {event.x}, {event.y}')


keyboard = tk.Label(root, text="Press any key...")
keyboard.pack(pady=10)

mouse = tk.Label(root, text="Click anywhere...")
mouse.pack(pady=10)

root.bind("<Key>", key_pressed)
root.bind("<Button-1>", mouse_clicked)

root.mainloop()