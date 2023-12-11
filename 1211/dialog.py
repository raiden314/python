import tkinter as tk

root = tk.Tk()
#横200縦100
root.geometry("200x100")

lbl = tk.Label(text="LABEL")
#ラベルを設置
lbl.pack()
tk.mainloop()