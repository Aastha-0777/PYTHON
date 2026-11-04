import tkinter as tk

root = tk.Tk()
root.title("My First App")
root.geometry("500x400")

def display_name():
    name = entry.get()
    result.configure(text="Hello " +name)
    

tk.Label(root,text="Enter your Name").pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=10)

tk.Button(root,text="Submit",command=display_name).pack(pady=10)
result = tk.Label(root,text="")
result.pack(pady=10)
root.mainloop()

# root.configure(bg="lightblue")
# root.mainloop()