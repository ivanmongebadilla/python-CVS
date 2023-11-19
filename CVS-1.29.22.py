import tkinter
from tkinter import messagebox
from tkinter.ttk import *
import cv2
import PIL.Image, PIL.ImageTk
import time
from threading import Thread
from pywinauto.application import Application
import shutil
import os
from os.path import exists
from tkinter import BOTH, END, LEFT, SINGLE, CENTER


class video_read:
    def __init__(self, mwindow, canvas, Scale1, Scale2, Scale3, Scale4, Label6, Progressbar1):
        self.mwindow = mwindow
        self.canvas = canvas
        self.vid = cv2.VideoCapture(0)
        #self.rectstart_point = (0,0)
        #self.rectend_point = (640, 480)
        self.color = (0, 0, 255)
        self.tickness = 8
        self.scale1 = Scale1
        self.scale2 = Scale2
        self.scale3 = Scale3
        self.scale4 = Scale4
        self.label6 = Label6
        self.progressbar1 = Progressbar1

        self.delay = 15
        self.update_video()

    def update_video(self):
        self.rectstart_point = (Scale1.get(), Scale2.get())
        self.rectend_point = (Scale3.get(), Scale4.get())
        ret, frm = self.vid.read()
        
        if ret:
            frame = cv2.cvtColor(frm, cv2.COLOR_BGR2RGB)
            rect = cv2.rectangle(frame, self.rectstart_point, self.rectend_point, self.color, self.tickness)
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(rect))
            self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)

        self.mwindow.after(self.delay, self.update_video)


    def take_pos_samples(self):
        path = r'C:/Users/gm_i_m01/Documents/python/Computer vision/CVP folder/p/'
        i = 0
        self.sizex = Scale3.get() - Scale1.get()
        self.sizey = Scale4.get() - Scale2.get()
        self.progressbar1['value'] = 0 ##***##

        while (self.sizex>200):
            self.sizex = self.sizex - 50
            self.sizey = self.sizey - 37

        self.label6.place(relx=0.38, rely=0.938, height=29, width=105)
        self.progressbar1.place(relx=0.49, rely=0.938, relwidth=0.26
              , relheight=0.0, height=23)
            
        while (i <= 250):
           ret, photo = self.vid.read()
           #self.mwindow.update_idletasks()
           self.mwindow.update()
           self.progressbar1['value'] = (i+1)/2.5 #((i/100)*100)
           if ret:
               gray = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY) 
               cropimg = gray[self.scale2.get():self.scale4.get(), self.scale1.get():self.scale3.get()]
               resizeimg = cv2.resize(cropimg, (self.sizex, self.sizey))
               cv2.imwrite(path + str(i) + '.png', resizeimg)
           i = i + 1
           #--print("Taking samples")

        self.label6.place_forget()
        self.progressbar1.place_forget()
        #return True

    def take_neg_samples(self):
        path = r'C:/Users/gm_i_m01/Documents/python/Computer vision/CVP folder/n/'
        i = 0
        self.sizex = Scale3.get() - Scale1.get()
        self.sizey = Scale4.get() - Scale2.get()
        self.progressbar1['value'] = 0

        while (self.sizex>200):
            self.sizex = self.sizex - 50
            self.sizey = self.sizey - 37

        self.label6.place(relx=0.38, rely=0.938, height=29, width=105)
        self.progressbar1.place(relx=0.49, rely=0.938, relwidth=0.26
              , relheight=0.0, height=23)
            
        while (i<=250):
           ret, photo = self.vid.read()
           #self.mwindow.update_idletasks()
           self.mwindow.update()
           self.progressbar1['value'] = (i+1)/5 #((i/200)*100)
           
           if ret:
               gray = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
               cropimg = gray[self.scale2.get():self.scale4.get(), self.scale1.get():self.scale3.get()]
               resizeimg = cv2.resize(cropimg, (self.sizex, self.sizey))
               cv2.imwrite(path + str(i) + '.png', resizeimg)
           i = i + 1
           #print("Taking samples")
           
        #h,w = cropimg.shape
        while (i<=500):
            ret, photo = self.vid.read()
            #self.mwindow.update_idletasks()
            self.mwindow.update()
            self.progressbar1['value'] = (i+1)/5 #((i/200)*100)

            if ret:
               gray = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
               resized = cv2.resize(gray, (self.sizex, self.sizey))
               cv2.imwrite(path + str(i) + '.png', resized)
            i = i + 1
            #print("Taking samples")

        self.label6.place_forget()
        self.progressbar1.place_forget()


    def width_hight(self):
        x = (self.sizex * 0.12)
        x = int(x)
        #print (x)
        y = (self.sizey * 0.12)
        y = int (y)
        #print (y)
        return (x, y)

    def deletevid(self):
        self.mwindow.after_cancel(self.mwindow)
        if self.vid.isOpened():
            self.vid.release()        

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()
        

flag3 = False
vision_flag = False
      

def window():
    global root
    global tk_pics
    
    root = tkinter.Tk()
    root.title("Computer Vision Program")
    root.geometry('1000x800')#("600x450+660+210")
    root.minsize(120, 1)
    root.maxsize(1924, 1061)
    root.resizable(1,  1)
    root.configure(background="#d9d9d9")
    #root.protocol( 'WM_DELETE_WINDOW' , close_window)

    global Button1
    global Button2
    global Canvas1
    global Canvas2
    global Canvas3
    global Label2
    global Label3
    global Label4
    global Label5
    global Label6
    global Label7
    global Label8
    global Label9
    global Label10
    global Label11
    global Label12
    global Label13
    global Label14
    global Label15
    global Label16
    global Label17
    global Label18
    global Scale1
    global Scale2
    global Scale3
    global Scale4
    global Button3
    global Button4
    global Button5
    global Button6
    global Button7
    global Button8
    global Button9
    global Button10
    global Button11
    global Button12
    global Button13
    global Button14
    global Progressbar1
    global Spinbox1
    global Spinbox2
    global Spinbox3
    global Spinbox4
    global Spinbox5
    global Spinbox6
    global Spinbox7
    global Spinbox8
    global Spinbox9
    global Entry1
    global Listbox1
    global flag1
    global var2
    global var3
    global var4
    global var5
    global var6
    global var7
    
    flag1 = 0
    
    Button1 = tkinter.Button(root, command = window_two)
    Button1.configure(activebackground="beige")
    Button1.configure(activeforeground="#000000")
    Button1.configure(background="#d9d9d9")
    Button1.configure(compound='left')
    Button1.configure(disabledforeground="#a3a3a3")
    Button1.configure(font="-family {Segoe UI} -size 14 -weight bold")
    Button1.configure(foreground="#000000")
    Button1.configure(highlightbackground="#d9d9d9")
    Button1.configure(highlightcolor="black")
    Button1.configure(pady="0")
    Button1.configure(text='''Create Cascade''')

    Button2 = tkinter.Button(root, command = window_three)
    Button2.configure(activebackground="beige")
    Button2.configure(activeforeground="#000000")
    Button2.configure(background="#d9d9d9")
    Button2.configure(compound='left')
    Button2.configure(disabledforeground="#a3a3a3")
    Button2.configure(font="-family {Segoe UI} -size 14 -weight bold")
    Button2.configure(foreground="#000000")
    Button2.configure(highlightbackground="#d9d9d9")
    Button2.configure(highlightcolor="black")
    Button2.configure(pady="0")
    Button2.configure(text='''Load Cascade''')

    Label2 = tkinter.Label(root)
    Label2.configure(anchor='w')
    Label2.configure(background="#d9d9d9")
    Label2.configure(compound='left')
    Label2.configure(cursor="fleur")
    Label2.configure(disabledforeground="#a3a3a3")
    Label2.configure(font="-family {Segoe UI} -size 13 -weight bold")
    Label2.configure(foreground="#000000")
    Label2.configure(text='''X Start Point''')

    Label3 = tkinter.Label(root)
    Label3.configure(anchor='w')
    Label3.configure(background="#d9d9d9")
    Label3.configure(compound='left')
    Label3.configure(disabledforeground="#a3a3a3")
    Label3.configure(font="-family {Segoe UI} -size 13 -weight bold")
    Label3.configure(foreground="#000000")
    Label3.configure(text='''Y Start Point''')

    Scale1 =  tkinter.Scale(root, from_=0, to=640, resolution=1)
    Scale1.configure(activebackground="beige")
    Scale1.configure(background="#d9d9d9")
    Scale1.configure(foreground="#000000")
    Scale1.configure(highlightbackground="#d9d9d9")
    Scale1.configure(highlightcolor="black")
    Scale1.configure(orient="horizontal")
    Scale1.configure(troughcolor="#d9d9d9")
    Scale1.set(0)

    Scale2 =  tkinter.Scale(root, from_=0, to=480, resolution=1)
    Scale2.configure(activebackground="beige")
    Scale2.configure(background="#d9d9d9")
    Scale2.configure(foreground="#000000")
    Scale2.configure(highlightbackground="#d9d9d9")
    Scale2.configure(highlightcolor="black")
    Scale2.configure(orient="horizontal")
    Scale2.configure(troughcolor="#d9d9d9")
    Scale1.set(0)

    Label4 = tkinter.Label(root)
    Label4.configure(anchor='w')
    Label4.configure(background="#d9d9d9")
    Label4.configure(compound='left')
    Label4.configure(disabledforeground="#a3a3a3")
    Label4.configure(font="-family {Segoe UI} -size 13 -weight bold")
    Label4.configure(foreground="#000000")
    Label4.configure(text='''X End Point''')

    Scale3 =  tkinter.Scale(root, from_=0, to=640, resolution=1)
    Scale3.configure(activebackground="beige")
    Scale3.configure(background="#d9d9d9")
    Scale3.configure(foreground="#000000")
    Scale3.configure(highlightbackground="#d9d9d9")
    Scale3.configure(highlightcolor="black")
    Scale3.configure(orient="horizontal")
    Scale3.configure(troughcolor="#d9d9d9")
    Scale3.set(640)

    Label5 = tkinter.Label(root)
    Label5.configure(anchor='w')
    Label5.configure(background="#d9d9d9")
    Label5.configure(compound='left')
    Label5.configure(disabledforeground="#a3a3a3")
    Label5.configure(font="-family {Segoe UI} -size 13 -weight bold")
    Label5.configure(foreground="#000000")
    Label5.configure(text='''Y End Point''')

    Scale4 =  tkinter.Scale(root, from_=0, to=480, resolution=1)
    Scale4.configure(activebackground="beige")
    Scale4.configure(background="#d9d9d9")
    Scale4.configure(foreground="#000000")
    Scale4.configure(highlightbackground="#d9d9d9")
    Scale4.configure(highlightcolor="black")
    Scale4.configure(orient="horizontal")
    Scale4.configure(troughcolor="#d9d9d9")
    Scale4.set(480)

    Canvas1 = tkinter.Canvas(root, width = 640, height = 480)
    #Canvas1.configure(background="#d9d9d9")
    #Canvas1.configure(borderwidth="2")
    #Canvas1.configure(insertbackground="black")
    #Canvas1.configure(relief="ridge")
    #Canvas1.configure(selectbackground="#c4c4c4")
    #Canvas1.configure(selectforeground="black")

    Button3 = tkinter.Button(root, command = tk_pos_smpls)
    Button3.configure(activebackground="beige")
    Button3.configure(activeforeground="#000000")
    Button3.configure(background="#d9d9d9")
    Button3.configure(compound='left')
    Button3.configure(disabledforeground="#a3a3a3")
    Button3.configure(font="-family {Segoe UI} -size 12 -weight bold")
    Button3.configure(foreground="#000000")
    Button3.configure(highlightbackground="#d9d9d9")
    Button3.configure(highlightcolor="black")
    Button3.configure(pady="0")
    Button3.configure(text='''Take Positive Samples''')

    Button4 = tkinter.Button(root, command = tk_neg_smpls)
    Button4.configure(activebackground="beige")
    Button4.configure(activeforeground="#000000")
    Button4.configure(background="#d9d9d9")
    Button4.configure(compound='left')
    Button4.configure(disabledforeground="#a3a3a3")
    Button4.configure(font="-family {Segoe UI} -size 12 -weight bold")
    Button4.configure(foreground="#000000")
    Button4.configure(highlightbackground="#d9d9d9")
    Button4.configure(highlightcolor="black")
    Button4.configure(pady="0")
    Button4.configure(text='''Take Negative Samples''')

    Button5 = tkinter.Button(root, command = next_win)
    Button5.configure(activebackground="beige")
    Button5.configure(activeforeground="#000000")
    Button5.configure(background="#d9d9d9")
    Button5.configure(compound='left')
    Button5.configure(disabledforeground="#a3a3a3")
    Button5.configure(font="-family {Segoe UI} -size 12 -weight bold")
    Button5.configure(foreground="#000000")
    Button5.configure(highlightbackground="#d9d9d9")
    Button5.configure(highlightcolor="black")
    Button5.configure(pady="0")
    Button5.configure(text='''Next''')

    #Progressbar1 = Progressbar(root, mode = 'indeterminate')
    Progressbar1 = Progressbar(root)
    Progressbar1.configure(length="260")
    
    Label6 = tkinter.Label(root)
    Label6.configure(background="#d9d9d9")
    Label6.configure(foreground="#000000")
    Label6.configure(font="TkDefaultFont")
    Label6.configure(relief="flat")
    Label6.configure(anchor='w')
    Label6.configure(justify='left')
    Label6.configure(text='''Taking samples...''')
    Label6.configure(compound='left')

    Label7 = tkinter.Label(root)
    Label7.configure(anchor='w')
    Label7.configure(background="#d9d9d9")
    Label7.configure(compound='left')
    Label7.configure(disabledforeground="#a3a3a3")
    Label7.configure(foreground="#000000")
    Label7.configure(text='''Positive Samples Usage:''')

    Label8 = tkinter.Label(root)
    Label8.configure(anchor='w')
    Label8.configure(background="#d9d9d9")
    Label8.configure(compound='left')
    Label8.configure(disabledforeground="#a3a3a3")
    Label8.configure(foreground="#000000")
    Label8.configure(text='''Number of Stages:''')
    
    var1 = tkinter.IntVar()
    var1.set(100)
    Spinbox1 = tkinter.Spinbox(root, from_=1, to=100, textvariable = var1)
    Spinbox1.configure(activebackground="#f9f9f9")
    Spinbox1.configure(background="white")
    Spinbox1.configure(buttonbackground="#d9d9d9")
    Spinbox1.configure(disabledforeground="#a3a3a3")
    Spinbox1.configure(font="TkDefaultFont")
    Spinbox1.configure(foreground="black")
    Spinbox1.configure(highlightbackground="black")
    Spinbox1.configure(highlightcolor="black")
    Spinbox1.configure(insertbackground="black")
    Spinbox1.configure(selectbackground="#c4c4c4")
    Spinbox1.configure(selectforeground="black")

    var2 = tkinter.IntVar()
    var2.set(15)
    Spinbox2 = tkinter.Spinbox(root, from_=1, to=20, textvariable = var2)
    Spinbox2.configure(activebackground="#f9f9f9")
    Spinbox2.configure(background="white")
    Spinbox2.configure(buttonbackground="#d9d9d9")
    Spinbox2.configure(disabledforeground="#a3a3a3")
    Spinbox2.configure(font="TkDefaultFont")
    Spinbox2.configure(foreground="black")
    Spinbox2.configure(highlightbackground="black")
    Spinbox2.configure(highlightcolor="black")
    Spinbox2.configure(insertbackground="black")
    Spinbox2.configure(selectbackground="#c4c4c4")
    Spinbox2.configure(selectforeground="black")

    Label9 = tkinter.Label(root)
    Label9.configure(anchor='w')
    Label9.configure(background="#d9d9d9")
    Label9.configure(compound='left')
    Label9.configure(disabledforeground="#a3a3a3")
    Label9.configure(font="-family {Segoe UI} -size 16 -weight bold")
    Label9.configure(foreground="#000000")
    Label9.configure(text="A new widnow will be open in 5 seconds and will automatically \n close when the proccess is finished, \n please do not move anything)")

    Label10 = tkinter.Label(root)
    Label10.configure(anchor='w')
    Label10.configure(background="#d9d9d9")
    Label10.configure(compound='left')
    Label10.configure(disabledforeground="#a3a3a3")
    Label10.configure(font="-family {Segoe UI} -size 36 -weight bold")
    Label10.configure(foreground="#000000")
    Label10.configure(text="5")

    Button6 = tkinter.Button(root, command = learning_file_selection)
    Button6.configure(activebackground="beige")
    Button6.configure(activeforeground="#000000")
    Button6.configure(background="#d9d9d9")
    Button6.configure(compound='left')
    Button6.configure(disabledforeground="#a3a3a3")
    Button6.configure(font="-family {Segoe UI} -size 12 -weight bold")
    Button6.configure(foreground="#000000")
    Button6.configure(highlightbackground="#d9d9d9")
    Button6.configure(highlightcolor="black")
    Button6.configure(pady="0")
    Button6.configure(text='''Start Vision System''')

    Button7 = tkinter.Button(root, command = w_window)
    Button7.configure(activebackground="beige")
    Button7.configure(activeforeground="#000000")
    Button7.configure(background="#d9d9d9")
    Button7.configure(compound='left')
    Button7.configure(disabledforeground="#a3a3a3")
    Button7.configure(font="-family {Segoe UI} -size 12 -weight bold")
    Button7.configure(foreground="#000000")
    Button7.configure(highlightbackground="#d9d9d9")
    Button7.configure(highlightcolor="black")
    Button7.configure(pady="0")
    Button7.configure(text='''Go Home''')

    Canvas2 = tkinter.Canvas(root, width = 640, height = 480)

    Button8 = tkinter.Button(root, command = stop_vision_system)
    Button8.configure(activebackground="beige")
    Button8.configure(activeforeground="#000000")
    Button8.configure(background="#d9d9d9")
    Button8.configure(compound='left')
    Button8.configure(disabledforeground="#a3a3a3")
    Button8.configure(font="-family {Segoe UI} -size 12 -weight bold")
    Button8.configure(foreground="#000000")
    Button8.configure(highlightbackground="#d9d9d9")
    Button8.configure(highlightcolor="black")
    Button8.configure(pady="0")
    Button8.configure(text='''Stop Vision System''')

    Label11 = tkinter.Label(root)
    Label11.configure(anchor='w')
    Label11.configure(background="#d9d9d9")
    Label11.configure(compound='left')
    Label11.configure(disabledforeground="#a3a3a3")
    Label11.configure(font="-family {Segoe UI} -size 16 -weight bold")
    Label11.configure(foreground="#000000")
    Label11.configure(text="Label Inspection Vision System")

    Label12 = tkinter.Label(root)
    Label12.configure(anchor='w')
    Label12.configure(background="#d9d9d9")
    Label12.configure(compound='left')
    Label12.configure(disabledforeground="#a3a3a3")
    Label12.configure(foreground="#000000")
    Label12.configure(text='''File Name:''')

    Entry1 = tkinter.Entry(root)
    Entry1.configure(background="white")
    Entry1.configure(disabledforeground="#a3a3a3")
    Entry1.configure(font="TkFixedFont")
    Entry1.configure(foreground="#000000")
    Entry1.configure(insertbackground="black")

    Button9 = tkinter.Button(root, command = list_box_selection )
    Button9.configure(activebackground="beige")
    Button9.configure(activeforeground="#000000")
    Button9.configure(background="#d9d9d9")
    Button9.configure(compound='left')
    Button9.configure(disabledforeground="#a3a3a3")
    Button9.configure(font="-family {Segoe UI} -size 12 -weight bold")
    Button9.configure(foreground="#000000")
    Button9.configure(highlightbackground="#d9d9d9")
    Button9.configure(highlightcolor="black")
    Button9.configure(pady="0")
    Button9.configure(text='''Start Vision System''')

    Button10 = tkinter.Button(root, command = w_window)
    Button10.configure(activebackground="beige")
    Button10.configure(activeforeground="#000000")
    Button10.configure(background="#d9d9d9")
    Button10.configure(compound='left')
    Button10.configure(disabledforeground="#a3a3a3")
    Button10.configure(font="-family {Segoe UI} -size 12 -weight bold")
    Button10.configure(foreground="#000000")
    Button10.configure(highlightbackground="#d9d9d9")
    Button10.configure(highlightcolor="black")
    Button10.configure(pady="0")
    Button10.configure(text='''Go Back''')

    Listbox1 = tkinter.Listbox(root, selectmode = SINGLE)
    Listbox1.configure(background="white")
    Listbox1.configure(disabledforeground="#a3a3a3")
    Listbox1.configure(font="TkFixedFont")
    Listbox1.configure(foreground="#000000")

    Label13 = tkinter.Label(root)
    Label13.configure(anchor='w')
    Label13.configure(background="#d9d9d9")
    Label13.configure(compound='left')
    Label13.configure(disabledforeground="#a3a3a3")
    Label13.configure(foreground="#000000")
    Label13.configure(text="Scale Factor:")

    Label14 = tkinter.Label(root)
    Label14.configure(anchor='w')
    Label14.configure(background="#d9d9d9")
    Label14.configure(compound='left')
    Label14.configure(disabledforeground="#a3a3a3")
    Label14.configure(foreground="#000000")
    Label14.configure(text="Min Neighbors:")

    Label15 = tkinter.Label(root)
    Label15.configure(anchor='w')
    Label15.configure(background="#d9d9d9")
    Label15.configure(compound='left')
    Label15.configure(disabledforeground="#a3a3a3")
    Label15.configure(foreground="#000000")
    Label15.configure(text="Min Size:")

    Label16 = tkinter.Label(root)
    Label16.configure(anchor='w')
    Label16.configure(background="#d9d9d9")
    Label16.configure(compound='left')
    Label16.configure(disabledforeground="#a3a3a3")
    Label16.configure(foreground="#000000")
    Label16.configure(text="Max Size:")

    var2 = tkinter.DoubleVar()
    var2.set(1.05)
    Spinbox3 = tkinter.Spinbox(root, from_=1.01, to=5.00, increment=0.01, textvariable = var2)
    Spinbox3.configure(activebackground="#f9f9f9")
    Spinbox3.configure(background="white")
    Spinbox3.configure(buttonbackground="#d9d9d9")
    Spinbox3.configure(disabledforeground="#a3a3a3")
    Spinbox3.configure(font="TkDefaultFont")
    Spinbox3.configure(foreground="black")
    Spinbox3.configure(highlightbackground="black")
    Spinbox3.configure(highlightcolor="black")
    Spinbox3.configure(insertbackground="black")
    Spinbox3.configure(selectbackground="#c4c4c4")
    Spinbox3.configure(selectforeground="black")

    var3 = tkinter.IntVar()
    var3.set(6)
    Spinbox4 = tkinter.Spinbox(root, from_=1, to=25, increment=1, textvariable = var3)
    Spinbox4.configure(activebackground="#f9f9f9")
    Spinbox4.configure(background="white")
    Spinbox4.configure(buttonbackground="#d9d9d9")
    Spinbox4.configure(disabledforeground="#a3a3a3")
    Spinbox4.configure(font="TkDefaultFont")
    Spinbox4.configure(foreground="black")
    Spinbox4.configure(highlightbackground="black")
    Spinbox4.configure(highlightcolor="black")
    Spinbox4.configure(insertbackground="black")
    Spinbox4.configure(selectbackground="#c4c4c4")
    Spinbox4.configure(selectforeground="black")

    var4 = tkinter.IntVar()
    var4.set(30)
    Spinbox5 = tkinter.Spinbox(root, from_=1, to=640, increment=1, textvariable = var4)
    Spinbox5.configure(activebackground="#f9f9f9")
    Spinbox5.configure(background="white")
    Spinbox5.configure(buttonbackground="#d9d9d9")
    Spinbox5.configure(disabledforeground="#a3a3a3")
    Spinbox5.configure(font="TkDefaultFont")
    Spinbox5.configure(foreground="black")
    Spinbox5.configure(highlightbackground="black")
    Spinbox5.configure(highlightcolor="black")
    Spinbox5.configure(insertbackground="black")
    Spinbox5.configure(selectbackground="#c4c4c4")
    Spinbox5.configure(selectforeground="black")

    var5 = tkinter.IntVar()
    var5.set(30)
    Spinbox6 = tkinter.Spinbox(root, from_=1, to=480, increment=1, textvariable = var5)
    Spinbox6.configure(activebackground="#f9f9f9")
    Spinbox6.configure(background="white")
    Spinbox6.configure(buttonbackground="#d9d9d9")
    Spinbox6.configure(disabledforeground="#a3a3a3")
    Spinbox6.configure(font="TkDefaultFont")
    Spinbox6.configure(foreground="black")
    Spinbox6.configure(highlightbackground="black")
    Spinbox6.configure(highlightcolor="black")
    Spinbox6.configure(insertbackground="black")
    Spinbox6.configure(selectbackground="#c4c4c4")
    Spinbox6.configure(selectforeground="black")

    var6 = tkinter.IntVar()
    var6.set(0)
    Spinbox7 = tkinter.Spinbox(root, from_=1, to=640, increment=1, textvariable = var6)
    Spinbox7.configure(activebackground="#f9f9f9")
    Spinbox7.configure(background="white")
    Spinbox7.configure(buttonbackground="#d9d9d9")
    Spinbox7.configure(disabledforeground="#a3a3a3")
    Spinbox7.configure(font="TkDefaultFont")
    Spinbox7.configure(foreground="black")
    Spinbox7.configure(highlightbackground="black")
    Spinbox7.configure(highlightcolor="black")
    Spinbox7.configure(insertbackground="black")
    Spinbox7.configure(selectbackground="#c4c4c4")
    Spinbox7.configure(selectforeground="black")

    var7 = tkinter.IntVar()
    var7.set(0)
    Spinbox8 = tkinter.Spinbox(root, from_=1, to=480, increment=1, textvariable = var7)
    Spinbox8.configure(activebackground="#f9f9f9")
    Spinbox8.configure(background="white")
    Spinbox8.configure(buttonbackground="#d9d9d9")
    Spinbox8.configure(disabledforeground="#a3a3a3")
    Spinbox8.configure(font="TkDefaultFont")
    Spinbox8.configure(foreground="black")
    Spinbox8.configure(highlightbackground="black")
    Spinbox8.configure(highlightcolor="black")
    Spinbox8.configure(insertbackground="black")
    Spinbox8.configure(selectbackground="#c4c4c4")
    Spinbox8.configure(selectforeground="black")

    Button11 = tkinter.Button(root, command = main_window)
    Button11.configure(activebackground="beige")
    Button11.configure(activeforeground="#000000")
    Button11.configure(background="#d9d9d9")
    Button11.configure(compound='left')
    Button11.configure(disabledforeground="#a3a3a3")
    Button11.configure(font="-family {Segoe UI} -size 12 -weight bold")
    Button11.configure(foreground="#000000")
    Button11.configure(highlightbackground="#d9d9d9")
    Button11.configure(highlightcolor="black")
    Button11.configure(pady="0")
    Button11.configure(text='''Lot# Detection''')

    Button12 = tkinter.Button(root, command = main_window)
    Button12.configure(activebackground="beige")
    Button12.configure(activeforeground="#000000")
    Button12.configure(background="#d9d9d9")
    Button12.configure(compound='left')
    Button12.configure(disabledforeground="#a3a3a3")
    Button12.configure(font="-family {Segoe UI} -size 12 -weight bold")
    Button12.configure(foreground="#000000")
    Button12.configure(highlightbackground="#d9d9d9")
    Button12.configure(highlightcolor="black")
    Button12.configure(pady="0")
    Button12.configure(text='''Label Detection''')

    Button13 = tkinter.Button(root, command = bottle_detection)
    Button13.configure(activebackground="beige")
    Button13.configure(activeforeground="#000000")
    Button13.configure(background="#d9d9d9")
    Button13.configure(compound='left')
    Button13.configure(disabledforeground="#a3a3a3")
    Button13.configure(font="-family {Segoe UI} -size 12 -weight bold")
    Button13.configure(foreground="#000000")
    Button13.configure(highlightbackground="#d9d9d9")
    Button13.configure(highlightcolor="black")
    Button13.configure(pady="0")
    Button13.configure(text='''Bottle Detection''')

    Canvas3 = tkinter.Canvas(root)
    #Canvas2.place(relx=0.19, rely=0.063, relheight=0.6, relwidth=0.64)

    Label17 = tkinter.Label(root)
    Label17.configure(anchor='w')
    Label17.configure(background="#d9d9d9")
    Label17.configure(compound='left')
    Label17.configure(disabledforeground="#a3a3a3")
    Label17.configure(font="-family {Segoe UI} -size 16 -weight bold")
    Label17.configure(foreground="#000000")

    Label18 = tkinter.Label(root)
    Label18.configure(anchor='w')
    Label18.configure(background="#d9d9d9")
    Label18.configure(compound='left')
    Label18.configure(disabledforeground="#a3a3a3")
    Label18.configure(foreground="#000000")
    Label18.configure(text="Scale Factor:")

    var8 = tkinter.IntVar()
    var8.set(0)
    Spinbox9 = tkinter.Spinbox(root, from_=1, to=30, increment=1, textvariable = var8)
    Spinbox9.configure(activebackground="#f9f9f9")
    Spinbox9.configure(background="white")
    Spinbox9.configure(buttonbackground="#d9d9d9")
    Spinbox9.configure(disabledforeground="#a3a3a3")
    Spinbox9.configure(font="TkDefaultFont")
    Spinbox9.configure(foreground="black")
    Spinbox9.configure(highlightbackground="black")
    Spinbox9.configure(highlightcolor="black")
    Spinbox9.configure(insertbackground="black")
    Spinbox9.configure(selectbackground="#c4c4c4")
    Spinbox9.configure(selectforeground="black")

    Button14 = tkinter.Button(root, command = done_adj)
    Button14.configure(activebackground="beige")
    Button14.configure(activeforeground="#000000")
    Button14.configure(background="#d9d9d9")
    Button14.configure(compound='left')
    Button14.configure(disabledforeground="#a3a3a3")
    Button14.configure(font="-family {Segoe UI} -size 12 -weight bold")
    Button14.configure(foreground="#000000")
    Button14.configure(highlightbackground="#d9d9d9")
    Button14.configure(highlightcolor="black")
    Button14.configure(pady="0")
    Button14.configure(text='''Next''')
    
    w_window()

    root.mainloop()

def w_window():
    clear_window()
    global flag3
    
    flag3 = False
    Button11.place(relx=0.64, rely=0.163, height=84, width=187)
    Button12.place(relx=0.64, rely=0.363, height=84, width=187)
    Button13.place(relx=0.64, rely=0.563, height=84, width=187)

def main_window():
    clear_window()
    flag1 = 0
    Button1.place(relx=0.35, rely=0.156, height=74, width=217)
    Button2.place(relx=0.35, rely=0.489, height=74, width=217)

def window_two():
    global vid_strm
    
    clear_window()
    Label2.place(relx=0.05, rely=0.044, height=41, width=124)
    Label3.place(relx=0.05, rely=0.2, height=41, width=124)
    Scale1.place(relx=0.05, rely=0.111, relheight=0.093, relwidth=0.177)
    Scale2.place(relx=0.05, rely=0.267, relheight=0.093, relwidth=0.177)
    Label4.place(relx=0.05, rely=0.378, height=41, width=124)
    Scale3.place(relx=0.05, rely=0.444, relheight=0.093, relwidth=0.177)
    Label5.place(relx=0.05, rely=0.533, height=41, width=124)
    Scale4.place(relx=0.05, rely=0.6, relheight=0.093, relwidth=0.177)
    Canvas1.place(relx=0.283, rely=0.044)#, relheight=0.918
            #, relwidth=0.672)
    Button3.place(relx=0.15, rely=0.813, height=64, width=187)
    Button4.place(relx=0.42, rely=0.813, height=64, width=187)
    Button4["state"] = "disable"
    Button5.place(relx=0.69, rely=0.813, height=64, width=187)
    Button5["state"] = "disable"
    #scales[0] = Scale1
    #scales[1] = Scale2
    #scales[2] = Scale3
    #scales[3] = Scale4
           

    vid_strm = video_read(root, Canvas1, Scale1, Scale2, Scale3, Scale4, Label6, Progressbar1)

def window_three():
    clear_window()
    global flag3
    Listbox1.delete(0,END)
    casfile_path = r'C:\Users\gm_i_m01\Documents\python\Computer vision\CVP folder\CascadeFiles'

    for file in os.listdir(casfile_path):
        Listbox1.insert(END, file)
    

    Listbox1.place(relx=0.31, rely=0.013, relheight=0.69, relwidth=0.374)
    Button9.place(relx=0.6, rely=0.788, height=74, width=177)
    Button10.place(relx=0.27, rely=0.788, height=74, width=177)

def list_box_selection():
    global flag3
    cascade_path = "C:/Users/gm_i_m01/Documents/python/Computer vision/CVP folder/CascadeFiles/" + Listbox1.get(Listbox1.curselection())
    if flag3 == False:
        adjust_bottle_detection(cascade_path)
        #start_vision_system(cascade_path)
    elif flag3 == True:
        adjust_bottle_detection(cascade_path)
        #start_bottle_detection(cascade_path)

def learning_file_selection():
    global flag3
    cascade_path = "C:/Users/gm_i_m01/Documents/python/Computer vision/CVP folder/CascadeFiles/" + Entry1.get() + ".xml"
    if flag3 == False:
        adjust_bottle_detection(cascade_path)
        #start_vision_system(cascade_path)
    elif flag3 == True:
        adjust_bottle_detection(cascade_path)
        #start_bottle_detection(cascade_path)

def tk_pos_smpls():
    Button3["state"] = "disable"
    Button4["state"] = "disable"
    Button5["state"] = "disable"
    vid_strm.take_pos_samples()
    Button3["state"] = "normal"
    Button4["state"] = "normal"

def tk_neg_smpls():
    Button3["state"] = "disable"
    Button4["state"] = "disable"
    Button5["state"] = "disable"
    vid_strm.take_neg_samples()
    Button3["state"] = "normal"
    Button4["state"] = "normal"
    Button5["state"] = "normal"
    Label7.place(relx=0.69, rely=0.688, height=32, width=134)
    Label8.place(relx=0.69, rely=0.725, height=31, width=134)
    Spinbox1.place(relx=0.83, rely=0.694, relheight=0.025
                    , relwidth=0.045)
    Spinbox2.place(relx=0.831, rely=0.733, relheight=0.025
                    , relwidth=0.045)
    Label12.place(relx=0.69, rely=0.763, height=32, width=134)
    Entry1.place(relx=0.83, rely=0.768, height=20, relwidth=0.134)

def next_win():
    if Entry1.get() == "":
        messagebox.showerror("Error", "Please add a file name")            
    else:
        global width
        global hight
        #global vid_strm
        width, hight = vid_strm.width_hight()
        #del vid_strm ##MAYBE DO NOT DELETE IT
        vid_strm.deletevid()
        clear_window()

        Label9.configure(text="A new window will be open in 5 seconds and will automatically \n close when the proccess is finished, \n please do not move anything)")
        Label9.place(relx=0.03, rely=0.125, height=341, width=934)
        Label10.place(relx=0.49, rely=0.65, height=81, width=44)
        v = 5
        
        while (v >= 0):
            root.update()
            Label10.configure(text=str(v))
            v = v - 1
            time.sleep(1)

        file_created = haar_cascade_trainer()
        clear_window()
        if file_created == True:
            Label9.configure(text= "Training Proccess Completed")
            Label9.place(relx=0.03, rely=0.125, height=341, width=934)
            Button6.place(relx=0.32, rely=0.825, height=64, width=177)
            Button7.place(relx=0.59, rely=0.825, height=64, width=177)
        else:
            Label9.configure(text= "There has been an error, try again")
            Label9.place(relx=0.03, rely=0.125, height=341, width=934)
            Button7.place(relx=0.59, rely=0.825, height=64, width=177)

def adjust_bottle_detection(cascade_path):
    clear_window()
    path_cascade = cascade_path
    Label2.place(relx=0.05, rely=0.044, height=41, width=124)
    Label3.place(relx=0.05, rely=0.2, height=41, width=124)
    Scale1.place(relx=0.05, rely=0.111, relheight=0.093, relwidth=0.177)
    Scale2.place(relx=0.05, rely=0.267, relheight=0.093, relwidth=0.177)
    Label4.place(relx=0.05, rely=0.378, height=41, width=124)
    Scale3.place(relx=0.05, rely=0.444, relheight=0.093, relwidth=0.177)
    Label5.place(relx=0.05, rely=0.533, height=41, width=124)
    Scale4.place(relx=0.05, rely=0.6, relheight=0.093, relwidth=0.177)
    Canvas1.place(relx=0.283, rely=0.044)
    Label18.place(relx=0.05, rely=0.688, height=32, width=104)
    Spinbox9.place(relx=0.15, rely=0.695, relheight=0.025, relwidth=0.045)
    Button14.place(relx=0.42, rely=0.813, height=64, width=187)

    global adj_flag
    global adj_vision
    adj_flag = True
    color = (0, 0, 255)
    tickness = 8 

    adj_vision = cv2.VideoCapture(0)
    while adj_flag:
        rec_startpoint = (Scale1.get(), Scale2.get())
        rec_endpoint = (Scale3.get(), Scale4.get())
        root.update()
        ret, frame = adj_vision.read()
        if ret:
            RGBframe = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            rect = cv2.rectangle(RGBframe, rec_startpoint, rec_endpoint, color, tickness) 
            pic = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(rect))
            Canvas1.create_image(0, 0, image = pic, anchor = tkinter.NW)
        else:
            break

    start_bottle_detection(path_cascade, adj_vision, rec_startpoint, rec_endpoint)

def done_adj():
    global adj_flag
    if adj_flag == True:
        adj_flag = False
        #adj_vision.release()         
            
def start_bottle_detection(cascade_path, adj_vision, rec_startpoint, rec_endpoint):#(cascade_path):
    clear_window()
    global Label18
    global photo

    Canvas3.place(relx=0.19, rely=0.063, relheight=0.6, relwidth=0.64)
    photo_cap = adj_vision#cv2.VideoCapture(0)
    wx, hx = rec_startpoint
    wy, hy = rec_endpoint

    for x in range(3):
        ret, image = photo_cap.read()
        if ret:
            cv_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            cropimg = cv_img[hx:hy, wx:wy]
            photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cropimg))
            Canvas3.create_image(0, 0, image=photo, anchor=tkinter.NW)
        root.update()
        time.sleep(3)

    #root.update()
    
    #imagepath = r'C:\Users\gm_i_m01\Documents\python\Computer vision CNN\CasesCNN\test1.png'
    #cascadepath = r'C:\Users\gm_i_m01\Documents\python\Computer vision CNN\cases\classifier\cascade.xml'

    #bottlecascade = cv2.CascadeClassifier(cascadepath)

    #image = cv2.imread(imagepath)
    #cropimg = image[80:500, 300:700]
    #gray = cv2.cvtColor(cropimg, cv2.COLOR_BGR2GRAY)

    #bottles = bottlecascade.detectMultiScale(
    #    gray,
    #    scaleFactor=1.1,
    #    minNeighbors=14,
    #    minSize=(100,100),
    #    maxSize=(150,150)
    #    )

    #print("Found {0} bottles!".format(len(bottles)))

    #if len(bottles)< 6:
    #    x = 6 - len(bottles)
    #    Label17.configure(text = "MISSING " + str(x) + " BOTTLES!!")
    #    Label17.place(relx=0.19, rely=0.688, height=41, width=634)
        #print ("MISSING " + str(x) + " BOTTLES!!")


    #for (x, y, w, h) in bottles:
    #    cv2.rectangle(cropimg, (x, y), (x+w, y+h), (0, 255, 0), 2)

    #cv_img = cv2.cvtColor(cropimg, cv2.COLOR_BGR2RGB)
    #photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img))
    #Canvas3.create_image(0, 0, image=photo, anchor=tkinter.NW)
    #Canvas3.place(relx=0.19, rely=0.063, relheight=0.6, relwidth=0.64)

def start_vision_system(cascade_path):
    clear_window() 
    Label11.place(relx=0.36, rely=0.05, height=61, width=264)
    Canvas2.place(relx=0.27, rely=0.138, relheight=0.6, relwidth=0.64)
    Button8.place(relx=0.4, rely=0.838, height=64, width=207)
    Spinbox3.place(relx=0.14, rely=0.544, relheight=0.025, relwidth=0.045)
    Label13.place(relx=0.04, rely=0.538, height=32, width=84)
    Label14.place(relx=0.04, rely=0.575, height=31, width=94)
    Label15.place(relx=0.04, rely=0.613, height=32, width=64)
    Label16.place(relx=0.04, rely=0.65, height=32, width=94)
    Spinbox4.place(relx=0.14, rely=0.584, relheight=0.025, relwidth=0.045)
    Spinbox5.place(relx=0.14, rely=0.62, relheight=0.025, relwidth=0.045)
    Spinbox6.place(relx=0.2, rely=0.62, relheight=0.025, relwidth=0.045)
    Spinbox7.place(relx=0.14, rely=0.656, relheight=0.025, relwidth=0.045)
    Spinbox8.place(relx=0.2, rely=0.655, relheight=0.025, relwidth=0.045)
    
    global vision
    global vision_flag

    vision_flag = True

    detectionCascade = cv2.CascadeClassifier(cascade_path)

    vision = cv2.VideoCapture(0)
    while vision_flag:
        root.update()
        ret, frame = vision.read()
        #print("Im running...")

        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            detection = detectionCascade.detectMultiScale(
                gray,
                scaleFactor = var2.get(),#1.05,
                minNeighbors = var3.get(),#6,
                minSize = (var4.get(), var5.get()),#(100, 100),
                maxSize = (var6.get(), var7.get()),
                flags = cv2.CASCADE_SCALE_IMAGE
            )
            
            for (x, y, w, h) in detection:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 8)
                
            RGBframe = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pic = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(RGBframe))
            Canvas2.create_image(0, 0, image = pic, anchor = tkinter.NW)
        else:
            break

def stop_vision_system():
    global vision_flag
    if vision_flag == True:
        vision_flag = False
        vision.release()
    w_window()

def bottle_detection():
    global flag3
    flag3 = True
    main_window()
    
#def go_home():
#    main_window()

def haar_cascade_trainer():
    posimg = str(Spinbox1.get())
    stgsnum = str(Spinbox2.get())
    negnum = "200"
    cstnwid = str(width)
    csthig = str(hight)
    fe = False

    src_path = r"C:\Users\gm_i_m01\Documents\python\Computer vision\CVP folder\classifier\cascade.xml"
    dst_path = r'C:/Users/gm_i_m01/Documents/python/Computer vision/CVP folder/CascadeFiles/'
    file_name = Entry1.get() + ".xml"
    final_dest = dst_path + file_name
    
    
    tit = 'Cascade Trainger GUI (Version 3.3.1)'
    app = Application(backend='uia').start(r'C:\Program Files\Cascade Trainer GUI\Cascade-Trainer-GUI.exe').connect(title=tit , timeout=100)
    #--app = Application(backend='uia').connect(title=tit , timeout=100)
    #app[tit].restore()
    
    #### SELECT FOLDER ####
    app[tit]['Edit'].set_text(r"C:/Users/gm_i_m01/Documents/python/Computer vision/CVP folder")

    #### POSITIVE IMAGE USAGE ####
    app[tit]['UpDown'].click_input()
    app[tit]['UpDown'].type_keys('^a')
    #app[tit]['UpDown'].type_keys('{DELETE}')
    app[tit]['UpDown'].type_keys(posimg)

    #### NEGATIVE IMAGE COUNT ####
    app[tit]['UpDown3'].click_input()
    app[tit]['UpDown3'].type_keys('^a')
    #app[tit]['UpDown3'].type_keys('{DELETE}')
    app[tit]['UpDown3'].type_keys(negnum)

    #### COMMON TAB ####
    app[tit]['TabItem2'].click_input()

    #### NUMBER OF STAGES ####
    app[tit]['UpDown2'].click_input()
    app[tit]['UpDown2'].type_keys('^a')
    app[tit]['UpDown2'].type_keys(stgsnum)

    #### CASCADE TAB ####
    app[tit]['Cascade'].click_input()

    #### SAMPLES SIZES ####
    app[tit]['UpDown'].click_input()
    app[tit]['UpDown'].type_keys('^a')
    app[tit]['UpDown'].type_keys(cstnwid)
    app[tit]['UpDown2'].click_input()
    app[tit]['UpDown2'].type_keys('^a')
    app[tit]['UpDown2'].type_keys(csthig)
    
    #### START ####
    app[tit]['Start'].click_input()

    #### WAIT FOR PROCESS ####
    while (app[tit]['Cascade classifier training completed!'].exists() == False):
        pass

    #### PROCESS COMPLETED OK AND CLOSE
    app[tit]['OK EnterButton'].click_input()
    app[tit].close()
    app[tit]['Yes EnterButton'].click_input()

    if exists(src_path):
        shutil.copy(src_path, final_dest)
        fe = True
    else:
        fe = False
    #flag1 = 1
    print ("Process completed")

    return fe


def clear_window():
    Button1.place_forget()
    Button2.place_forget()
    Button3.place_forget()
    Button4.place_forget()
    Button5.place_forget()
    Button6.place_forget()
    Button7.place_forget()
    Button8.place_forget()
    Button9.place_forget()
    Button10.place_forget()
    Button11.place_forget()
    Button12.place_forget()
    Button13.place_forget()
    Button14.place_forget()
    Canvas1.place_forget()
    Canvas2.place_forget()
    Canvas3.place_forget()
    Label2.place_forget()
    Label3.place_forget()
    Label4.place_forget()
    Label5.place_forget()
    Scale1.place_forget()
    Scale2.place_forget()
    Scale3.place_forget()
    Scale4.place_forget()
    Label7.place_forget()
    Label8.place_forget()
    Label9.place_forget()
    Label10.place_forget()
    Label11.place_forget()
    Label12.place_forget()
    Label13.place_forget()
    Label14.place_forget()
    Label15.place_forget()
    Label16.place_forget()
    Label17.place_forget()
    Label18.place_forget()
    Spinbox1.place_forget()
    Spinbox2.place_forget()
    Spinbox3.place_forget()
    Spinbox4.place_forget()
    Spinbox5.place_forget()
    Spinbox6.place_forget()
    Spinbox7.place_forget()
    Spinbox8.place_forget()
    Spinbox9.place_forget()
    Entry1.place_forget()
    Listbox1.place_forget()
    #print ("Button forget")

    

    
    
global vid_strm
window()
if vid_strm == None:
    del vid_strm

    
