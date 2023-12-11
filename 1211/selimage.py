import tkinter as tk
import tkinter.filedialog as fd

def openFile():
    path = fd.askopenfilename()

root = tk.Tk()
root.geometry("400x350")

btn = tk.Button(text="ファイルを開く", command=openFile)
imgLbl = tk.Label()

btn.pack()
imgLbl.pack()
tk.mainloop()