import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

def dispPhoto( path ):
    newImg = PIL.Image.open( path ).convert("L").resize((32,32)).resize((700,300), resample=0)
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
root.geometry("800x350")

btn = tk.Button(text="ファイルを開く", command=openFile)
imgLbl = tk.Label()

btn.pack()
imgLbl.pack()
tk.mainloop()