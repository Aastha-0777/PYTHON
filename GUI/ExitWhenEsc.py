import tkinter as tk

root = tk.Tk()
root.title("My First App")
root.geometry("500x400")

def key_pressed(event): 
    if event.keysym == "Escape" :
        root.destroy()


keyboard = tk.Label(root, text="Press Esc key to Exit...")
keyboard.pack(pady=10)

root.bind("<Key>", key_pressed)

root.mainloop()