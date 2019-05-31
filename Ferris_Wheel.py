from tkinter import *
from tkinter import font
from itertools import cycle
import time
import pygame

intro_chk = 0
'''
image_files  = ['image_700x480/yunah-1.png', 'image_700x480/yunah-2.png', 'image_700x480/yunah-3.png',
                'image_700x480/yunah-4.png', 'image_700x480/yunah-5.png', 'image_700x480/yunah-7.png',
                'image_700x480/yunah-9.png']
'''
#관람차 
image_files1  = ['image_700x480/image-1.png']

#DGSW
image_files2  = ['DGSW/1.png', 'DGSW/2.png', 'DGSW/3.png', 'DGSW/4.png', 'DGSW/5.png',
                 'DGSW/6.png', 'DGSW/7.png', 'DGSW/8.png', 'DGSW/9.png', 'DGSW/10.png',
                 'DGSW/11.png', 'DGSW/12.png', 'DGSW/13.png', 'DGSW/14.png', 'DGSW/15.png',
                 'DGSW/16.png', 'DGSW/17.png', 'DGSW/18.png', 'DGSW/19.png']

# media
image_files3  = ['image_700x480/image3-1.png', 'image_700x480/image2-1.png', 'image_700x480/image2-2.png', 'image_700x480/2.png','image_700x480/3.png','image_700x480/4.png',
					'image_700x480/5.png','image_700x480/7.png','image_700x480/8.png']

# TEAM
image_files4  = ['TEAM/1.png', 'TEAM/2.png', 'TEAM/3.png', 'TEAM/4.png', 'TEAM/5.png']

# Project = DGSW
image_intro  = ['image_700x480/bg1_1.png', 'image_700x480/title.png', 'image_700x480/title_1.png', 'image_700x480/schedule.png']




class App(Canvas):
    def __init__(self, master=None):
        self.master = master
        Canvas.__init__(self, width=800, height=480)
      
        self.init_ui()

    def init_ui(self):

        self.config(bg='White')
        self.grid(column=0, row=0)
        self.create_rectangle(0, 0, 100, 480, width=0, fill='#c0c0c0', outline='#c0c0c0')
        self.bg1 = PhotoImage(file='image_700x480/bg1_1.png')
        self.create_image(101, 0, anchor='nw', image=self.bg1)

# Button1 = 관람차 
        self.photo1 = PhotoImage(file="image_80x40/menu-1.png")
        self.button1 = Button(width=80, height=30, image=self.photo1, bg='#c0c0c0', activebackground='#ffc0c0',
                            borderwidth=0, command=self.click1, relief=FLAT)
        self.button1.configure(width=80, height=30, activebackground='light yellow', highlightthickness=0)
        but1 = self.create_window(10, 100, anchor='nw', window=self.button1)
        def clicka(event):
            print ('event1')
            self.after_cancel(self.photo1)
        self.button1.bind("<Button-1>", clicka)

# Button2 = 대소고
        self.photo2 = PhotoImage(file="image_80x40/menu-2.png")
        self.button2 = Button(width=80, height=30, image=self.photo2, bg='#c0c0c0',
                              activebackground='#c0c0c0', borderwidth=0, command=self.click2, relief=FLAT)
        self.button2.configure(width=80, height=30, activebackground='#c0c0c0', highlightthickness=0)
        but2 = self.create_window(10, 150, anchor='nw', window=self.button2)
        def clickb(event):
            print ('event2')
            self.after_cancel(self.photo2)
        self.button2.bind("<Button-1>", clickb)

# Button3 = Media
        self.photo3 = PhotoImage(file="image_80x40/menu-3.png")
        self.button3 = Button(width=80, height=30, image=self.photo3, bg='#c0c0c0',
                              activebackground='#c0c0c0', borderwidth=0, command=self.click3)
        self.button3.configure(width=80, height=30, activebackground='#c0c0c0', highlightthickness=0)
        but1 = self.create_window(10, 200, anchor='nw', window=self.button3)
        def clickc(event):
            print('event3')
            self.after_cancel(self.photo3)
        self.button3.bind("<Button-1>", clickc)

# Button4 = Team
        self.photo4 = PhotoImage(file="image_80x40/menu-4.png")
        self.button4 = Button(width=80, height=30, image=self.photo4, bg='#c0c0c0',
                          activebackground='#c0c0c0', borderwidth=0, command=self.click4)
        self.button4.configure(width=80, height=30, activebackground='#c0c0c0', highlightthickness=0)
        but1 = self.create_window(10, 250, anchor='nw', window=self.button4)
        def clickd(event):
            print('event4')
            self.after_cancel(self.photo4)
        self.button4.bind("<Button-1>", clickd)

# Button5 = DGSW
        self.photo5 = PhotoImage(file="image_80x40/dgsm.png")
        self.button5 = Button(width=80, height=30, image=self.photo5, bg='#c0c0c0',
                          activebackground='#c0c0c0', borderwidth=0, command=self.click5)
        self.button5.configure(width=80, height=30, activebackground='#c0c0c0', highlightthickness=0)
        but1 = self.create_window(10, 350, anchor='nw', window=self.button5)
        def clicke(event):
            print('event5')
            self.after_cancel(self.photo5)
        self.button5.bind("<Button-1>", clicke)
                
# 관람차 정보
    def click1(self):
        global intro_chk
        intro_chk=1
        pygame.mixer.stop()
        print ('click1')        
        self.bg2 = PhotoImage(file='image_700x480/park_1.png')
        self.lb2 = Label(image=self.bg2) 
        self.lb2.image = self.bg2
        self.lb2.place(x=101,y=0)
        sound_intro2 = pygame.mixer.Sound('wav/park.wav')
        sound_intro2.play()
        intro_chk=1

#DGSW
    def click2(self):
        global intro_chk
        if(intro_chk):
            self.lb2.destroy()
            intro_chk = 0
        pygame.mixer.stop()
        print ('click2')
        self.pictures2 = cycle((PhotoImage(file=image), image) for image in image_files2)
        self.picture_display2 = Label(self)
        self.picture_display2.place(x=101, y=0)
        self.picture_display2.grid(row=0, column=1)
        self.ShowPhoto2()
        sound_intro1 = pygame.mixer.Sound('DGSW/dgsw.wav')
        sound_intro1.play()

    def ShowPhoto2(self):
        img_object2, img_name2 = next(self.pictures2)
        self.picture_display2.config(image=img_object2)
        self.picture_display2.place(relx=1.0, y=2.0, anchor='ne')
        self.photo=self.after(15000, self.ShowPhoto2)

# Media
    def click3(self):
        global intro_chk
        if(intro_chk):
            self.lb2.destroy()
            intro_chk = 0
        pygame.mixer.stop()
        print ('click3')
        self.pictures3 = cycle((PhotoImage(file=image), image) for image in image_files3)
        self.picture_display3 = Label(self)
        self.picture_display3.place(x=101, y=0)
        self.picture_display3.grid(row=0, column=1)
        self.ShowPhoto3()
        sound_intro1 = pygame.mixer.Sound('wav/TopOfTheWorld.wav');  sound_intro1.play()

    def ShowPhoto3(self):
        img_object3, img_name3 = next(self.pictures3)
        self.picture_display3.config(image=img_object3)
        self.picture_display3.place(relx=1.0, y=2.0, anchor='ne')
        self.photo=self.after(5000, self.ShowPhoto3)

# TEAM
    def click4(self):
        global intro_chk
        if(intro_chk):
            self.lb2.destroy()
            intro_chk = 0
        pygame.mixer.stop()
        print ('click4')
        self.pictures4 = cycle((PhotoImage(file=image), image) for image in image_files4)
        self.picture_display4 = Label(self)
        self.picture_display4.place(x=101, y=0)
        self.picture_display4.grid(row=0, column=1)
        self.ShowPhoto4()
        sound_intro1 = pygame.mixer.Sound('TEAM/team.wav')
        sound_intro1.play()

    def ShowPhoto4(self):
        img_object4, img_name4 = next(self.pictures4)
        self.picture_display4.config(image=img_object4)
        self.picture_display4.place(relx=1.0, y=2.0, anchor='ne')
        self.photo=self.after(15000, self.ShowPhoto4)                                     

# Project
    def click5(self):
        global intro_chk
        if(intro_chk):
            self.lb2.destroy()
            intro_chk = 0
        pygame.mixer.stop()
        print ('click5')
        self.pictures5 = cycle((PhotoImage(file=image), image) for image in image_intro)
        self.picture_display5 = Label(self)
        self.picture_display5.place(x=101, y=0)
        self.picture_display5.grid(row=0, column=1)
        self.ShowPhoto5()
        sound_intro1 = pygame.mixer.Sound('wav/intro.wav')
        sound_intro1.play()

    def ShowPhoto5(self):
        img_object5, img_name5 = next(self.pictures5)
        self.picture_display5.config(image=img_object5)
        self.picture_display5.place(relx=1.0, y=2.0, anchor='ne')        
        self.photo=self.after(5000, self.ShowPhoto5)

        

pygame.init()
pygame.mixer.init()
root=Tk()
root.geometry("800x480")
#root.config(cursor='none')
#root.attributes('-fullscreen', True)
my_photo=App(master=root)

root.mainloop()
