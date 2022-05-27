#-*- codin:uft-8 -*-
import numpy as np
import openpyxl
import glob
import pandas as pd
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import tkinter.simpledialog as simpledialog
import sys
import random
import matplotlib.pyplot as plt
import csv

class Cointoss():
    def __init__(self):
        self.DAY=[
            "月曜日",
            "火曜日",
            "水曜日",
            "木曜日",
            "金曜日"
        ]
        self.TEXT=[
            "表",
            "裏",
            "勝ち",
            "負け"
        ]
        self.text2=[
            "lot数",
            0.5,
            "指値",
            60,
            "逆指値",
            -50,
        ]
        self.path="cointoss.xlsx"

 
    def main(self):
        root=tk.Tk()
        root.geometry('500x400')
        root.title("コイントス")
        tk.Button(root,text="+",command=lambda:self.add_currency(root,nb,currency,tabs)).place(x=400,y=0)

        with open('settings.txt','r') as f:
            currency=f.read().splitlines()
            f.close()
        
        tabs=[]
        count=0
        nb=ttk.Notebook(width=400,height=320)
        for i in currency:
            tabs.append(tk.Frame(nb))
            nb.add(tabs[count],text=i,padding=3)
            count+=1
        nb.place(x=80,y=0)

        for i in tabs:
#########################################################################
# 曜日，コイントス，勝ち負け                                               #
#########################################################################
            for j in range(len(self.DAY)):
                tk.Label(i,text=self.DAY[j]).place(x=0,y=(j+2)*50-25)
            for j in range(len(self.TEXT)):
                tk.Label(i,text=self.TEXT[j]).place(x=(j+1.4)*50,y=20)
########################################################################
# チェックボックスの生成                                                 #
########################################################################      
        bln={}
        chk={}         
        for j in range(len(self.TEXT)):
            for k in range(len(self.DAY)):
                bln[j*len(self.DAY)+k]=tk.BooleanVar()
                chk[j*len(self.DAY)+k]=tk.Checkbutton(root,variable=bln[j*len(self.DAY)+k],text="")
                chk[j*len(self.DAY)+k].place(x=(j+3)*50,y=(k+2)*50)
#########################################################################
# ボタンの配置                                                           #
#########################################################################
        tk.Button(root,text="入力",command=lambda:self.insert(),width=6).place(x=20,y=50)
        tk.Button(root,text="リセット",command=lambda:self.reset(bln),width=6).place(x=20,y=100)
        tk.Button(root,text="閉じる",command=lambda:root.destroy(),width=6).place(x=20,y=150)
        tk.Button(root,text="詳細変更",command=lambda:self.change(),width=6).place(x=20,y=200)
        weeks=tk.IntVar()
        edit=ttk.Entry(root,textvariable=weeks,width=2)
        edit.place(x=20,y=20)
        tk.Label(root,text="週").place(x=55,y=20)
        tk.Button(root,text=">",command=lambda:self.upper(edit),height=1,width=1).place(x=38,y=19)
        tk.Button(root,text="<",command=lambda:self.down(edit),height=1,width=1).place(x=2,y=19)

        print(nb.index("end"))

        root.mainloop()




##########################################################################
# 関数置き場                                                              #
##########################################################################
    def add_currency(self,root,nb,currency,tabs):
        cur=simpledialog.askstring("Input Box","追加したい通貨を入力してください",)
        currency.append(cur)
        tabs.append(tk.Frame(nb))
        nb.add(tabs[currency.index(cur)],text=cur)
    
        with open('settings.txt','a') as f:
            print(cur,file=f)
            f.close()

    def upper(self,edit): 
        a=int(edit.get())
        edit.delete(0,tk.END)
        edit.insert(tk.END,str(a+1))
        
    def down(self,edit):
        a=int(edit.get())
        if a!=0:
            edit.delete(0,tk.END)
            edit.insert(tk.END,str(a-1))

#    def insert(self):
#        for i in glob.glob("*.xlsx"):
#            if i==self.path:
                
    def reset(self,bln):
        for i in range(len(bln)):
            bln[i].set(False)

#    def change(self):

            



cointoss=Cointoss()
cointoss.main()