import tkinter as tk

root = tk.Tk()

frame1 = tk.Frame(root, width=200, height=200, bg="red")
frame1.pack()

frame2 = tk.Frame(root, width=100, height=100, bg="yellow")
frame2.pack()

frame3 = tk.Frame(root, width=50, height=50, bg="blue")
frame3.pack()

root.mainloop()