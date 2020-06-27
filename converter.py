from tkinter import *
import tkinter as tk
from tkinter.ttk import Progressbar
from time import sleep
from random import randint as ri
import webbrowser

#Feeding Unit Values.
calci={"Kilometer":["*1","*1000","*100000","*(1e+6)","*(1e+9)","*(1e+12)","/1.609","*1094","*3281","*39370","/1.852",0],
       "Meter":["/1000","*1","*100","*1000","*(1e+6)","*(1e+9)","/1609","*1.094","*3.281","*39.37","/1852",1],
       "Centimeter":["/100000","/100","*1","*10","*10000","*(1e+7)","/160934","/91.44","/30.48","/2.54","/185200",2],
       "Millimeter":["/(1e+6)","/1000","*10","*1","*1000","*(1e+6)","/(1.609e+6)","/914","/305","/25.4","/(1.852e+6)",3],
       "Micrometer":["/(1e+9)","/(1e+6)","/(1e-4)","/1000","*1","*1000","/(1.609e+9)","/914400","/304800","/25400","/(1.852e+9)",4],
       "Nanometer":["/(1e+12)","/(1e+9)","/(1e+7)","/(1e+6)","/1000","*1","/(1.609e+12)","/(9.144e+8)","/(3.048e+8)","/(2.54e+7)","/(1.852e+12)",5],
       "Mile":["*1.609","*1609","*160934","*(1.609e+6)","*(1.609e+9)","*(1.609e+12)","*1","*1760","*5280","*63360","/1.151",6],
       "Yard":["/1094","/1.094","*91.44","*914","*914400","*(9.144e+8)","/1760","*1","*3","*36","/2025",7],
       "Foot":["/3281","/3.281","*30.48","*305","*304800","*(3.048e+8)","/5280","/3","*1","*12","/6076",8],
       "Inch":["/39370","/39.37","*2.54","*25.4","*25400","*(2.54e+7)","/63360","/36","/12","*1","/72913",9],
       "Nautical Mile":["*1.852","*1852","*185200","*(1.852e+6)","*(1.852e+9)","*(1.852e+12)","*1.151","*2025","*6076","*72913","*1",10]       
       }

#To center a window to the screen.
def center(screen,width,height):
        wid=screen.winfo_screenwidth()  #To get screen dimensions
        high=screen.winfo_screenheight()
        x=(wid//2)-(width//2)
        y=(high//2)-(height/2)
        screen.geometry("%dx%d+%d+%d"%(width,height,x,y))

#To shift from into window to converter.
def shift():
    wind.withdraw()
    user1=length()

#Intro window.
class intro():

    def __init__(self):
        
        wind.deiconify()                            #Used to open the hidden window.
        #wind.geometry("500x230")
        wind.resizable(0,0)
        wind.configure(bg="#008080")                #Light blue background.
        wind.title("Krishna's Unit Converter")
        icon=PhotoImage(file=r"convert.png")        #window icon.
        wind.iconphoto(False,icon)

        center(wind,500,230)


        entry=Label(wind,bg="#008080",fg="white",text="Welcome to Krishna's Unit Converter!",font=("Footlight MT Light",15,"bold"))
        entry.place(x=70,y=30,width=390,height=30)

        self.load=Progressbar(wind,orient=HORIZONTAL,length=250,mode='determinate')     #Loading bar.

        self.start=Button(wind,bg="#f5f5f5",fg="black",text="START",command=self.loading)
        self.start.place(x=200,y=90,width=80,height=30)            

        follow=Label(wind,bg="#008080",fg="white",text="Follow Me On",font=("Helvetica",12,"bold"))
        follow.place(x=186,y=150,width=104,height=20)

        #Follow links
        self.git=PhotoImage(file=r'git.png')
        github=Button(wind,image=self.git,bg="white",relief=FLAT,command=lambda:self.links("https://www.github.com/pavankrish16"),cursor="hand2")
        github.place(x=110,y=190,width=30,height=30)

        self.instag=PhotoImage(file=r'ins.png')
        insta=Button(wind,image=self.instag,bg="#008080",relief=FLAT,command=lambda:self.links("https://www.instagram.com/itzme_pavan/"),cursor="hand2")
        insta.place(x=190,y=190,width=30,height=30)


        self.fcb=PhotoImage(file=r'fb.png')
        fb=Button(wind,image=self.fcb,bg="white",relief=FLAT,command=lambda:self.links("https://www.facebook.com/pavankrishn16/"),cursor="hand2")
        fb.place(x=270,y=190,width=30,height=30)

        self.tweet=PhotoImage(file=r'twitter.png')
        twitter=Button(wind,image=self.tweet,bg="white",relief=FLAT,command=lambda:self.links("https://www.twitter.com/pavankrish16"),cursor="hand2")
        twitter.place(x=350,y=190,width=30,height=30)

    def links(self,url):  #Opening author links in browser.  
        webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito").open(url)

    def loading(self):  #Loding the loadbar.
    
        self.start.place(x=0,y=0,width=0,height=0)  #Removing start button.
        self.load.place(x=120,y=100)
        wind.update()        #To remove self.start button when loading self.starts.
    
        c=0
        while(c<=110):
            self.load['value']=c
            wind.update_idletasks()
            sleep(0.2)
            c+=10
        if(c>100):
            shift()
            




class length():

    def __init__(self):

        win.deiconify()
        #win.geometry("350x500")
        win.resizable(0,0)
        win.title("Converter")
        icon=PhotoImage(file=r'convert.png')
        win.iconphoto(False,icon)
        center(win,350,500)

        upr=Label(win,bg="#add8e6",width=400,height=250)
        upr.place(x=0,y=0)

        lwr=Label(win,bg="#189AB4",width=400,height=250,bd=0)
        lwr.place(x=0,y=250)
        
        #Input Entry
        self.inp_stg=StringVar()
        self.inp=Entry(win,bg="#add8e6",fg="white",font=("Helvetica",14),text=self.inp_stg,bd=1)
        self.inp.place(x=120,y=100,width=116,height=40)
        self.inp.bind('<KeyRelease>',self.operation)
        self.inp.bind('<BackSpace>',self.operation)

        #Laoding the menu box.
        self.user=["Kilometer","Meter","Centimeter","Millimeter","Micrometer","Nanometer","Mile","Yard","Foot","Inch","Nautical Mile"]

        self.lb=Listbox(win,selectmode=SINGLE,height=0)
        for i in range(len(self.user)):
            self.lb.insert(i,self.user[i])
        self.lb.bind('<<ListboxSelect>>',self.option) 

        #Input Unit Display.
        self.disp=Label(win,text="Kilometer",bg="white",fg="black")
        self.disp.place(x=120,y=160,width=100,height=20)

        self.down=PhotoImage(file=r"down.png")
        scroll_upr=Button(win,image=self.down,width=14,height=18,bd=0,command=lambda:self.select(0))
        scroll_upr.place(x=220,y=160)

        #Output Entry
        self.opt_stg=StringVar()
        self.opt=Entry(win,bg="#189AB4",fg="black",font=("Helvetica",14),text=self.opt_stg,bd=1)
        self.opt.place(x=120,y=350,width=116,height=40)
        self.opt.bind('<Key>',self.operation)


        self.lb1=Listbox(win,selectmode=SINGLE,height=0)
        for i in range(len(self.user)):
            self.lb1.insert(END,self.user[i])
        self.lb1.bind('<<ListboxSelect>>',self.option)

        #Output unit display.
        self.disp1=Label(win,text="Meter",bg="#ffffff",fg="black")
        self.disp1.place(x=120,y=410,width=100,height=20)

        scroll_dwn=Button(win,image=self.down,width=14,height=18,bd=0,command=lambda:self.select(1),bg="#f5f5f5")
        scroll_dwn.place(x=220,y=410)

    
    def operation(self,event):          #Converting the user input.
        
        global calci,exp_in,operator,exp_out,exp
        self.inp_unit=self.disp['text']
        self.opt_unit=self.disp1['text']
    
        try:
            widget=event.widget
        
            if(widget==self.inp):
                index=calci[self.opt_unit][-1]
                operator=calci[self.inp_unit][index]
                
                if(event.char>='0' and event.char<='9'):
                    exp_in=self.inp_stg.get()
                    #exp_in+=event.char
                    exp_out=str(eval(exp_in+operator))
                    self.opt_stg.set(exp_out)
                
                elif((event.char=='\b') or (len(self.inp_stg.get())<len(exp_in))):
                    win.update()
                    exp_in=self.inp_stg.get()
                    
                    if(exp_in==''):
                        exp_out=""
                        self.opt_stg.set("0")
                    elif(exp_in[-1]=='.'):
                        self.opt_stg.set(str(eval(exp_in[:-1]+operator)))
                    else:
                        print(exp_in)
                        exp_out=str(eval(exp_in+operator))
                        self.opt_stg.set(exp_out)

            elif(widget==self.opt):
                index=calci[self.inp_unit][-1]
                operator=calci[self.opt_unit][index]
            
                if(event.char>='0' and event.char<='9'):
                    exp_out=self.opt_stg.get()
                    exp_in=str(eval(exp_out+operator))
                    self.inp_stg.set(exp_in)
                    
                elif(event.char=='\b'):
                    exp_out=self.opt_stg.get()
                    
                    if(exp_out==''):
                        exp_in=""
                        self.inp_stg.set("0")
                        
                    elif(exp_out[-1]=='.'):
                        self.opt_stg.set(str(eval(exp_in[:-1]+operator)))

                    else:
                        exp_in=str(eval(exp_out+operator))
                        self.inp_stg.set(exp_in)
            
        except Exception:
            print("UnWorthyError")

    def select(self,c):          #Button Selection.
        global x,y
    
        if(c==0):
            self.disp1['fg']="black"
            y=0
        
            if(x==0):
                self.disp['fg']="white"
                x=200
                self.lb.place(x=120,y=0,width=100,height=200)
                self.disp1.place(height=20)
                self.disp.place(height=0)
            else:
                x=0
                self.disp['fg']="black"
                self.disp.place(height=20)
                self.lb.place(x=120,y=0,width=100,height=0)

            self.lb1.place(x=120,y=250,height=0)
        
        else:
            self.disp['fg']="black"
            x=0
            
            if(y==0):
                self.disp1['fg']="white"
                y=200
                self.disp1.place(height=0)
                self.disp.place(height=20)
                self.lb1.place(x=120,y=251,width=100,height=200)
            else:
                self.disp1['fg']="black"
                y=0
                self.lb1.place(x=120,y=251,width=100,height=0)
                self.disp1.place(height=20)

            self.lb.place(x=120,y=0,height=0)

    def option(self,event):              #Listbox Activation
        global x,y,exp_in,calci,operator,exp_out
    
        try:
            widget=event.widget
            picked=widget.get(widget.curselection())

            if(x==200):     #When self.user clicks button to activate menu list.
                self.disp['text']=picked
                self.disp['fg']="black"
            else:
                self.disp1['text']=picked
                self.disp1['fg']="black"

            x,y=0,0
            self.disp.place(height=20)
            self.disp1.place(height=20)
            self.lb.place(x=120,y=0,width=100,height=0)
            self.lb1.place(x=120,y=251,width=100,height=0)
            
            self.inp_unit=self.disp['text']
            op_unit=self.disp1['text']

            
            if(widget==self.lb):        
         
                if((self.inp_unit==op_unit) and (self.inp_unit!=self.user[6])):
                    op_unit=self.user[6]
                    self.disp1['text']=op_unit
                elif((self.inp_unit==op_unit)):
                    index=ri(1,3)+ri(1,2)
                    op_unit=self.user[index]
                    self.disp1['text']=op_unit
            else:
                
                if((self.inp_unit==op_unit) and (self.inp_unit!=self.user[6])):
                    ip_unit=self.user[6]
                    self.disp['text']=ip_unit
                elif((self.inp_unit==op_unit)):
                    index=ri(1,3)+ri(1,2)
                    ip_unit=self.user[index]
                    self.disp['text']=ip_unit

            if(exp_in!=''):
                index=calci[self.disp1['text']][-1]
                operator=calci[self.disp['text']][index]
                exp_in=self.inp_stg.get()
                exp_out=str(eval(exp_in+operator))
                self.opt_stg.set(exp_out)

        
        except Exception:
            print("Unworthy Error")
    


if __name__ == "__main__":      #Main function to intilaise the program.
    
    #global variable.
    exp=''
    exp_in=''
    exp_out=''
    operator=0
    x=0
    y=0

    abc=Tk()
    abc.withdraw()

    win=Toplevel(abc)
    win.withdraw()

    wind=Toplevel(abc)
    wind.withdraw()
    
    initial = intro()
