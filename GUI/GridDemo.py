import tkinter as tk

root = tk.Tk()
root.title("My First App")
root.geometry("500x400")

def displayData() :
    user = uName.get()
    password = psword.get()
    result.config(text=f'Username : {user}\nPassword : {password}')
    
    

tk.Label(root, text='Enter Username : ').grid(row=0, column=0)
uName = tk.Entry(root).grid(row=0, column=1)

tk.Label(root, text='Enter Password : ').grid(row=1, column=0)
psword = tk.Entry(root).grid(row=1, column=1)

tk.Button(root, text='Submit', command=displayData).grid(row=3, column=3)

result = tk.Label(root,text="").grid(row=5, column=5)

root.mainloop()