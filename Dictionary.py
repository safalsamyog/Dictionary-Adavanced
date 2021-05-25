from tkinter import *
from tkinter import messagebox as msg
from bs4 import BeautifulSoup
import requests
#import time
#importing all required library
_window=Tk()
_window.title("English to Nepali Dictionary App")
_window.geometry("660x660")
_window.config(bg="black")
mess=StringVar()


    
def dd():
    a=mess.get()
    contents=requests.get("https://www.englishnepalidictionary.com/?q=%s"%a).content
    soup=BeautifulSoup(contents,"lxml")

    dd=soup.find('div',class_="search-result")
    result=dd.h3.text
    msg.showinfo("Your Result",result)
    
          

        
     
f1=Frame(_window,bg="#1B1464",borderwidth=4)
f1.pack(side=LEFT,fill="y")
l1=Label(f1,text="English to Nepali Dictionary App",font="serif 9 bold",bg="#0984e3",width=36,height=3)
l1.pack(side=TOP,fill=BOTH)
but_q=Button(f1,text="Quit",borderwidth=5,bg="#d35400",fg="white",font="serif 12 bold",cursor="circle",command=f1.quit)
but_q.pack(side=BOTTOM,fill="both")

#working in window

l2=Label(_window,text="Word",font="serif 9 bold",fg="black",bg="#009432",relief=GROOVE)
l2.place(x=300,y=12,height=60,width=110)
e2=Entry(_window,relief=GROOVE,bg="#e74c3c",fg="white",font="serif 9 bold",textvariable=mess)
e2.place(x=420,y=12,height=60,width=200)

send=Button(_window,text="Search",cursor="heart",bg="#3742fa",relief=GROOVE,fg="white",font="serif 12 bold",command=dd)
send.place(x=390,y=120,height=35,width=180)
lb=Label(_window,text="Dictionary App made by Safal",relief=RAISED,bg="red",fg="white",font="serif 15 bold",cursor="pirate")
lb.pack(side=BOTTOM,fill="both",pady=9,padx=2)




if __name__=='__main__':
    
    _window.mainloop()
    #making window to run unlimited loop until quit