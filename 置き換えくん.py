import tkinter
import tkinter.ttk
from tkinter import filedialog
from tkinter import messagebox
import os

tki = tkinter.Tk()
tki.geometry("350x230")
tki.title(u"置き換えくん")
tki.resizable(False, False)

def openfile(event):
 file_name = filedialog.askopenfilename()
 tktbox1.insert(tkinter.END, file_name)

def replace(event):
  if not os.path.isfile(tktbox1.get()):
    return messagebox.showerror("エラー", "対象のファイルが存在しません")
  if tktbox2.get() == "":
    return messagebox.showerror("エラー", "置き換え元を指定してください")
  c = ""
  try:
    with open(tktbox1.get(), "r", encoding="utf-8") as f:
      c = f.read()
    with open(tktbox1.get(), "w", encoding="utf-8") as f:
      f.write(c.replace(tktbox2.get(), tktbox3.get()))
    messagebox.showinfo("成功", "置き換えに成功しました")
  except Exception as e:
    messagebox.showerror("エラー", f"エラーが発生しました\n{e}")

lbl = tkinter.Label(tki, text="ファイル内の特定の文字列を別の文字列に置き換えてくれます。")
lbl.place(x=13, y=13)

lbl = tkinter.Label(tki, text="対象のファイル")
lbl.place(x=13, y=50)
tktbox1 = tkinter.Entry(tki, text="", width=40)
tktbox1.place(x=13, y=75)
btn1 = tkinter.Button(tki, text="参照")
btn1.place(x=265, y=75)
btn1.bind("<Button-1>", openfile)

lbl = tkinter.Label(tki, text="置き換え元")
lbl.place(x=13, y=112)
tktbox2 = tkinter.Entry(tki, text="", width=10)
tktbox2.place(x=13, y=137)
lbl = tkinter.Label(tki, text="置き換え先")
lbl.place(x=85, y=112)
tktbox3 = tkinter.Entry(tki, text="", width=10)
tktbox3.place(x=85, y=137)

border = tkinter.ttk.Separator(tki, orient="horizontal")
border.place(x=0, y=177, width=350)

btn1 = tkinter.Button(tki, text="置き換える")
btn1.place(x=265, y=190)
btn1.bind("<Button-1>", replace)

tki.mainloop()