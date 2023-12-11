import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

def dispPhoto( path ):
    newImg = PIL.Image.open( path ).convert("L").resize((300,300))
    #デスクトップアプリ用に変換
    imgData = PIL.ImageTk.PhotoImage( newImg )
    imgLbl.configure(image=imgData)
    #imageプロパティに設定
    imgLbl.image = imgData

def openFile():
    path = fd.askopenfilename()
    if path:
        dispPhoto( path )

root = tk.Tk()
root.geometry("400x350")

btn = tk.Button(text="ファイルを開く", command=openFile)
imgLbl = tk.Label()

btn.pack()
imgLbl.pack()
tk.mainloop()