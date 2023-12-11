import tkinter as tk

root = tk.Tk()
#横200縦100
root.geometry("200x100")

lbl = tk.Label(text="LABEL")
btb = tk.Button(text="PUSH")
#ラベルを設置
lbl.pack()
btb.pack()
tk.mainloop()