import tkinter as tk
import random
def dispLabel():
    lst = ["大吉","中吉","小吉","吉","凶","大凶"]
    #リストの中からランダムで要素を抽出
    lbl.configure(text=random.choice(lst))
    # i = random.randint(0, len(lst)-1)
    # lbl.configure(text=lst[i])

root = tk.Tk()
#横200縦100
root.geometry("200x100")

lbl = tk.Label(text="LABEL")
btb = tk.Button(text="PUSH",command=dispLabel)
#ラベルを設置
lbl.pack()
btb.pack()
tk.mainloop()