from tkinter import*
w=Tk()
w.title("child table game")
w.config(bg="powder blue")
w.minsize(width=600,height=600)

def f(i,j):
    l[(i-1)*10+j-1]["text"]=str(i*j)
    l[(i - 1) * 10 + j - 1]["bg"] = "black"
    l[(i - 1) * 10 + j - 1]["state"]="disable"
def start():
    for i in range(1,11):
        for j in range(1,11):
            l[(i - 1) * 10 + j - 1]["text"] = "?"
            l[(i - 1) * 10 + j - 1]["state"] = "active"
            l[(i - 1) * 10 + j - 1]["bg"] = "white"
for i in range(1,11):
    b=Label(w,text=str(i),font="arial 10 bold",bg="#123456")
    b.grid(row=0,column=i,pady=5,padx=5,ipadx=10,ipady=10,sticky="nswe")
for i in range(1,11):
    b=Label(w,text=str(i),font="arial 10 bold",bg="#123456")
    b.grid(row=i,column=0,pady=5,padx=5,ipadx=10,ipady=10,sticky="nswe")
m=Button(w,text='Start',font="arial 10 bold",bg="yellow",command=lambda :start())
m.grid(row=0,column=0,padx=5,pady=5,ipadx=10,ipady=10,sticky="nswe")
l=[]   #list is made b/c, b is local and we want to change the text of button...so we will take a global list sothat we could reach address of buftton which we click
for i in range(1,11):
    for j in range(1,11):
        l.append(Button(w,text='?',font="arial 10 bold",command=lambda x=(i,j):f(x[0],x[1])))
        l[-1].grid(row=i,column=j,padx=5,pady=5,ipadx=10,ipady=10,sticky="nswe")
for i in range(11):
    w.grid_columnconfigure(i,weight=1)
for i in range(11):
    w.grid_rowconfigure(i,weight=1)

w.mainloop()