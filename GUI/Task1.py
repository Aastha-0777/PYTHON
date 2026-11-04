import tkinter as tk

root = tk.Tk()
root.title("My First App")
root.geometry("500x400")
# root.configure(bg="lightblue")

def add_two_nums():
    no1 = int(entry1.get())
    no2 = int(entry2.get())
    result.configure(text=f'Sum = {no1+no2}')
    

tk.Label(root,text="Enter Number 1").pack(pady=3)
entry1 = tk.Entry(root)
entry1.pack(pady=10)

tk.Label(root,text="Enter Number 2").pack(pady=3)
entry2 = tk.Entry(root)
entry2.pack(pady=10)


tk.Button(root,text="Submit",command=add_two_nums).pack(pady=10)
result = tk.Label(root,text="")
result.pack(pady=10)
root.mainloop()

# root.configure(bg="lightblue")
# root.mainloop()