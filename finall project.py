from tkinter import *
from tkinter import messagebox
import os
qn=0
qr=[]
mark=0
import pyttsx3
def speak(a):
    eg=pyttsx3.init()
    eg.say(a)
    eg.runAndWait()
def brou():
    import webbrowser
    webbrowser.open("https://project20ver.blogspot.com/")
    speak("#2.0ver Online Support")
def qu():
    os.system("qu.pdf")
def liv():
    os.system("li.mp4")
def div():
    os.system("di.mp4")
def tuv():
    os.system("tu.mp4")
def tov():
    os.system("to.mp4")
def stv():
    os.system("st.mp4")
def li():
    os.system("li.pdf")
def di():
    os.system("di.pdf")
def tu():
    os.system("tu.pdf")
def to():
    os.system("to.pdf")
def st():
    os.system("st.pdf")
def Final(mark):
    gui=Tk()
    gui.attributes('-fullscreen',True)
    gui.configure(bg="sky blue")
    gui.minsize(200,200)
    b=Label(gui,text="#2.0ver RESULT_SET_1",bg="sky blue",fg="red",font="ArialBlack 40 bold")
    b.place(x=405,y=10)
    lable=Label(gui,text="YOUR GOT MARK : ",bg="sky blue",fg="blue",font="ArialBlack 20 bold")
    lable.place(x=80,y=150)
    speak("you have got mark")
    speak(mark)
    lable=Label(gui,text="YOUR CORRECT ANSWERED QUESTIONS ARE : ",bg="sky blue",fg="blue",font="ArialBlack 20 bold")
    lable.place(x=80,y=350)
    lable=Label(gui,text=qr,bg="sky blue",fg="GREEN",font="ArialBlack 20 bold")
    lable.place(x=750,y=350)
    marks=len(qr)*10
    lable=Label(gui,text=marks,bg="sky blue",fg="black",font="ArialBlack 20 bold")
    lable.place(x=350,y=150)
    lable=Button(gui,text="Back",bg="Blue",fg="white",font=("Comic Sans MS",18),command=gui.destroy)
    lable.place(x=80,y=610)
def q(d):
    if d not in qr:
        qr.append(d)
def marks2d():
    gui=Tk()
    gui.attributes('-fullscreen',True)
    gui.configure(bg="sky blue")
    gui.minsize(200,200)
    b=Label(gui,text="#2.0ver TEST_SET_1",bg="sky blue",fg="red",font="ArialBlack 40 bold")
    b.place(x=405,y=10)
    out=StringVar()
    f1=open("11.txt")
    f=f1.read()
    lable=Label(gui,text=f,bg="sky blue",fg="black",font="ArialBlack 15 bold")
    lable.place(x=40,y=150)
    f1=open("12.txt")
    f=f1.read()
    lable=Label(gui,text=f,bg="sky blue",fg="black",font="ArialBlack 15 bold")
    lable.place(x=720,y=150)
    
    lable=Button(gui,text=" a ",bg="white",fg="blue",font=("Comic Sans MS",15),command=lambda: q("11"))
    lable.place(x=80,y=290)
    lable=Button(gui,text=" b ",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=80,y=350)
    lable=Button(gui,text=" c ",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=80,y=410)
    lable=Button(gui,text=" d ",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=80,y=470)
    
    lable=Button(gui,text=" a ",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=780,y=290)
    lable=Button(gui,text=" b ",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=780,y=350)
    lable=Button(gui,text=" c ",bg="white",fg="blue",font=("Comic Sans MS",15),command=lambda: q("12"))
    lable.place(x=780,y=410)
    lable=Button(gui,text=" d ",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=780,y=470)
    
    lable=Button(gui,text="Next",command=lambda: ns2(mark),bg="blue",fg="light green",font=("Comic Sans MS",20))
    lable.place(x=1200,y=600)
    lable=Button(gui,text="Back",bg="Blue",fg="white",font=("Comic Sans MS",18),command=gui.destroy)
    lable.place(x=80,y=610)
def ns2(ma):
    gui=Tk()
    gui.attributes('-fullscreen',True)
    gui.configure(bg="sky blue")
    gui.minsize(200,200)
    b=Label(gui,text="#2.0ver TEST_SET_1",bg="sky blue",fg="red",font="ArialBlack 40 bold")
    b.place(x=405,y=10)
    out=StringVar()
    f1=open("13.txt")
    f=f1.read()
    lable=Label(gui,text=f,bg="sky blue",fg="black",font="ArialBlack 15 bold")
    lable.place(x=40,y=150)
    f1=open("14.txt")
    f=f1.read()
    lable=Label(gui,text=f,bg="sky blue",fg="black",font="ArialBlack 15 bold")
    lable.place(x=730,y=150)
    lable=Button(gui,text=" a ",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=80,y=290)
    lable=Button(gui,text=" b ",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=80,y=350)
    lable=Button(gui,text=" c ",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=80,y=410)
    lable=Button(gui,text=" d ",bg="white",fg="blue",font=("Comic Sans MS",15),command=lambda: q("13"))
    lable.place(x=80,y=470)
    
    lable=Button(gui,text=" a ",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=780,y=290)
    lable=Button(gui,text=" b ",bg="white",fg="blue",font=("Comic Sans MS",15),command=lambda: q("14"))
    lable.place(x=780,y=350)
    lable=Button(gui,text=" c ",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=780,y=410)
    lable=Button(gui,text=" d ",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=780,y=470)
    
    lable=Button(gui,text="Next",bg="blue",fg="light green",font=("Comic Sans MS",20),command=lambda: q5q62(mark))
    lable.place(x=1200,y=600)
    lable=Button(gui,text="Back",bg="Blue",fg="white",font=("Comic Sans MS",18),command=gui.destroy)
    lable.place(x=80,y=610)
def q5q62(mark):
    gui=Tk()
    gui.attributes('-fullscreen',True)
    gui.configure(bg="sky blue")
    gui.minsize(200,200)
    b=Label(gui,text="#2.0ver TEST_SET_1",bg="sky blue",fg="red",font="ArialBlack 40 bold")
    b.place(x=405,y=10)
    out=StringVar()
    f1=open("15.txt")
    f=f1.read()
    lable=Label(gui,text=f,bg="sky blue",fg="black",font="ArialBlack 15 bold")
    lable.place(x=40,y=150)
    f1=open("16.txt")
    f=f1.read()
    q2=StringVar()
    q2.set(f)
    lable=Label(gui,text=f,bg="sky blue",fg="black",font="ArialBlack 15 bold")
    lable.place(x=730,y=150)
    lable=Button(gui,text=" a ",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=80,y=290)
    lable=Button(gui,text=" b ",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=80,y=350)
    lable=Button(gui,text=" c ",bg="white",fg="blue",font=("Comic Sans MS",15),command=lambda: q("15"))
    lable.place(x=80,y=410)
    lable=Button(gui,text=" d ",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=80,y=470)
    
    lable=Button(gui,text=" a ",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=780,y=290)
    lable=Button(gui,text=" b ",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=780,y=350)
    lable=Button(gui,text=" c ",bg="white",fg="blue",font=("Comic Sans MS",15),command=lambda: q("16"))
    lable.place(x=780,y=410)
    lable=Button(gui,text=" d ",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=780,y=470)

    
    lable=Button(gui,text="Next",bg="blue",fg="light green",font=("Comic Sans MS",20),command=lambda: q7q82(mark))
    lable.place(x=1200,y=600)
    lable=Button(gui,text="Back",bg="Blue",fg="white",font=("Comic Sans MS",18),command=gui.destroy)
    lable.place(x=80,y=610)
def q7q82(mark):
    gui=Tk()
    gui.attributes('-fullscreen',True)
    gui.configure(bg="sky blue")
    gui.minsize(200,200)
    b=Label(gui,text="#2.0ver TEST_SET_1",bg="sky blue",fg="red",font="ArialBlack 40 bold")
    b.place(x=405,y=10)
    out=StringVar()
    f1=open("17.txt")
    f=f1.read()
    lable=Label(gui,text=f,bg="sky blue",fg="black",font="ArialBlack 15 bold")
    lable.place(x=40,y=150)
    f1=open("18.txt")
    f=f1.read()
    q2=StringVar()
    q2.set(f)
    lable=Label(gui,text=f,bg="sky blue",fg="black",font="ArialBlack 15 bold")
    lable.place(x=730,y=150)
    
    lable=Button(gui,text=" a ",bg="white",fg="blue",font=("Comic Sans MS",15),command=lambda: q("17"))
    lable.place(x=80,y=290)
    lable=Button(gui,text=" b ",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=80,y=350)
    lable=Button(gui,text=" c ",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=80,y=410)
    lable=Button(gui,text=" d ",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=80,y=470)
    
    lable=Button(gui,text=" a ",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=780,y=290)
    lable=Button(gui,text=" b ",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=780,y=350)
    lable=Button(gui,text=" c ",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=780,y=410)
    lable=Button(gui,text=" d ",bg="white",fg="blue",font=("Comic Sans MS",15),command=lambda: q("18"))
    lable.place(x=780,y=470)
    
    lable=Button(gui,text="Next",bg="blue",fg="light green",font=("Comic Sans MS",20),command=lambda: q9q102(mark))
    lable.place(x=1200,y=600)
    lable=Button(gui,text="Back",bg="Blue",fg="white",font=("Comic Sans MS",18),command=gui.destroy)
    lable.place(x=80,y=610)
def q9q102(mark):
    gui=Tk()
    gui.attributes('-fullscreen',True)
    gui.configure(bg="sky blue")
    gui.minsize(200,200)
    b=Label(gui,text="#2.0ver TEST_SET_1",bg="sky blue",fg="red",font="ArialBlack 40 bold")
    b.place(x=405,y=10)
    out=StringVar()
    f1=open("19.txt")
    f=f1.read()
    lable=Label(gui,text=f,bg="sky blue",fg="black",font="ArialBlack 15 bold")
    lable.place(x=40,y=150)
    f1=open("20.txt")
    f=f1.read()
    q2=StringVar()
    q2.set(f)
    lable=Label(gui,text=f,bg="sky blue",fg="black",font="ArialBlack 15 bold")
    lable.place(x=730,y=150)
    lable=Button(gui,text=" a ",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=80,y=290)
    lable=Button(gui,text=" b ",bg="white",fg="blue",font=("Comic Sans MS",15),command=lambda: q("19"))
    lable.place(x=80,y=350)
    lable=Button(gui,text=" c ",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=80,y=410)
    lable=Button(gui,text=" d ",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=80,y=470)
    
    lable=Button(gui,text=" a ",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=780,y=290)
    lable=Button(gui,text=" b ",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=780,y=350)
    lable=Button(gui,text=" c ",bg="white",fg="blue",font=("Comic Sans MS",15),command=lambda: q("20"))
    lable.place(x=780,y=410)
    lable=Button(gui,text=" d ",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=780,y=470)

    
    lable=Button(gui,text="Finish",bg="blue",fg="light green",font=("Comic Sans MS",20),command=lambda: Final(mark))
    lable.place(x=1200,y=600)
    lable=Button(gui,text="Back",bg="Blue",fg="white",font=("Comic Sans MS",18),command=gui.destroy)
    lable.place(x=80,y=610)
def marksd():
    gui=Tk()
    gui.attributes('-fullscreen',True)
    gui.configure(bg="sky blue")
    gui.minsize(200,200)
    b=Label(gui,text="#2.0ver TEST_SET_1",bg="sky blue",fg="red",font="ArialBlack 40 bold")
    b.place(x=405,y=10)
    out=StringVar()
    f1=open("1.txt")
    f=f1.read()
    lable=Label(gui,text=f,bg="sky blue",fg="black",font="ArialBlack 15 bold")
    lable.place(x=40,y=150)
    f1=open("2.txt")
    f=f1.read()
    lable=Button(gui,text="a. 5.0",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=80,y=290)
    lable=Button(gui,text="b. 6",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=80,y=350)
    lable=Button(gui,text="c. 5",bg="white",fg="blue",font=("Comic Sans MS",15),command=lambda: q("1"))
    lable.place(x=80,y=410)
    lable=Button(gui,text="d. 4.0",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=80,y=470)
    
    lable=Label(gui,text=f,bg="sky blue",fg="black",font="ArialBlack 15 bold")
    lable.place(x=720,y=150)
    
    lable=Button(gui,text="a. 6",bg="white",fg="blue",font=("Comic Sans MS",15),command=lambda: q("2"))
    lable.place(x=780,y=290)
    lable=Button(gui,text="b. 4",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=780,y=350)
    lable=Button(gui,text="c. 6.0",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=780,y=410)
    lable=Button(gui,text="d. 5.0",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=780,y=470)
    
    lable=Button(gui,text="Next",command=lambda: ns(mark),bg="blue",fg="light green",font=("Comic Sans MS",20))
    lable.place(x=1200,y=600)
    lable=Button(gui,text="Back",bg="Blue",fg="white",font=("Comic Sans MS",18),command=gui.destroy)
    lable.place(x=80,y=610)
def ns(ma):
    gui=Tk()
    gui.attributes('-fullscreen',True)
    gui.configure(bg="sky blue")
    gui.minsize(200,200)
    b=Label(gui,text="#2.0ver TEST_SET_1",bg="sky blue",fg="red",font="ArialBlack 40 bold")
    b.place(x=405,y=10)
    out=StringVar()
    f1=open("3.txt")
    f=f1.read()
    lable=Label(gui,text=f,bg="sky blue",fg="black",font="ArialBlack 15 bold")
    lable.place(x=40,y=150)
    f1=open("4.txt")
    f=f1.read()
    lable=Label(gui,text=f,bg="sky blue",fg="black",font="ArialBlack 15 bold")
    lable.place(x=730,y=150)
    lable=Button(gui,text="a. m < n",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=80,y=290)
    lable=Button(gui,text="b. False",bg="white",fg="blue",font=("Comic Sans MS",15),command=lambda: q("3"))
    lable.place(x=80,y=350)
    lable=Button(gui,text="c. True",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=80,y=410)
    lable=Button(gui,text="d. No",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=80,y=470)

    lable=Button(gui,text="a. True",bg="white",fg="blue",font=("Comic Sans MS",15),command=lambda: q("4"))
    lable.place(x=780,y=290)
    lable=Button(gui,text="b. False",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=780,y=350)
    lable=Button(gui,text="c. Yes",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=780,y=410)
    lable=Button(gui,text="d. No",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=780,y=470)
    
    lable=Button(gui,text="Next",bg="blue",fg="light green",font=("Comic Sans MS",20),command=lambda: q5q6(mark))
    lable.place(x=1200,y=600)
    lable=Button(gui,text="Back",bg="Blue",fg="white",font=("Comic Sans MS",18),command=gui.destroy)
    lable.place(x=80,y=610)
def q5q6(mark):
    gui=Tk()
    gui.attributes('-fullscreen',True)
    gui.configure(bg="sky blue")
    gui.minsize(200,200)
    b=Label(gui,text="#2.0ver TEST_SET_1",bg="sky blue",fg="red",font="ArialBlack 40 bold")
    b.place(x=405,y=10)
    out=StringVar()
    f1=open("5.txt")
    f=f1.read()
    lable=Label(gui,text=f,bg="sky blue",fg="black",font="ArialBlack 15 bold")
    lable.place(x=40,y=150)
    f1=open("6.txt")
    f=f1.read()
    q2=StringVar()
    q2.set(f)
    lable=Label(gui,text=f,bg="sky blue",fg="black",font="ArialBlack 15 bold")
    lable.place(x=730,y=150)
    user=StringVar()
    lable=Button(gui,text="a. m or n",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=780,y=290)
    lable=Button(gui,text="b. False",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=780,y=350)
    lable=Button(gui,text="c. True",bg="white",fg="blue",font=("Comic Sans MS",15),command=lambda: q("6"))
    lable.place(x=780,y=410)
    lable=Button(gui,text="d. mn",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=780,y=470)

    lable=Button(gui,text="a. m and n",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=80,y=290)
    lable=Button(gui,text="b. False",bg="white",fg="blue",font=("Comic Sans MS",15),command=lambda: q("5"))
    lable.place(x=80,y=350)
    lable=Button(gui,text="c. True",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=80,y=410)
    lable=Button(gui,text="d. mn",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=80,y=470)

    
    lable=Button(gui,text="Next",bg="blue",fg="light green",font=("Comic Sans MS",20),command=lambda: q7q8(mark))
    lable.place(x=1200,y=600)
    lable=Button(gui,text="Back",bg="Blue",fg="white",font=("Comic Sans MS",18),command=gui.destroy)
    lable.place(x=80,y=610)
def q7q8(mark):
    gui=Tk()
    gui.attributes('-fullscreen',True)
    gui.configure(bg="sky blue")
    gui.minsize(200,200)
    b=Label(gui,text="#2.0ver TEST_SET_1",bg="sky blue",fg="red",font="ArialBlack 40 bold")
    b.place(x=405,y=10)
    out=StringVar()
    f1=open("7.txt")
    f=f1.read()
    lable=Label(gui,text=f,bg="sky blue",fg="black",font="ArialBlack 15 bold")
    lable.place(x=40,y=150)
    f1=open("8.txt")
    f=f1.read()
    q2=StringVar()
    q2.set(f)
    lable=Label(gui,text=f,bg="sky blue",fg="black",font="ArialBlack 15 bold")
    lable.place(x=730,y=150)
    user=StringVar()
    lable=Button(gui,text="a. not m defined",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=80,y=290)
    lable=Button(gui,text="b. False",bg="white",fg="blue",font=("Comic Sans MS",15),command=lambda: q("7"))
    lable.place(x=80,y=350)
    lable=Button(gui,text="c. True",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=80,y=410)
    lable=Button(gui,text="d. Not",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=80,y=470)

    
    lable=Button(gui,text="a. not n",bg="white",fg="blue",font=("Comic Sans MS",15),command=lambda: q("8"))
    lable.place(x=780,y=290)
    lable=Button(gui,text="b. False",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=780,y=350)
    lable=Button(gui,text="c. True",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=780,y=410)
    lable=Button(gui,text="d. Not defined",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=780,y=470)

    
    lable=Button(gui,text="Next",bg="blue",fg="light green",font=("Comic Sans MS",20),command=lambda: q9q10(mark))
    lable.place(x=1200,y=600)
    lable=Button(gui,text="Back",bg="Blue",fg="white",font=("Comic Sans MS",18),command=gui.destroy)
    lable.place(x=80,y=610)
def q9q10(mark):
    gui=Tk()
    gui.attributes('-fullscreen',True)
    gui.configure(bg="sky blue")
    gui.minsize(200,200)
    b=Label(gui,text="#2.0ver TEST_SET_1",bg="sky blue",fg="red",font="ArialBlack 40 bold")
    b.place(x=405,y=10)
    out=StringVar()
    f1=open("9.txt")
    f=f1.read()
    lable=Label(gui,text=f,bg="sky blue",fg="black",font="ArialBlack 15 bold")
    lable.place(x=40,y=150)
    f1=open("10.txt")
    f=f1.read()
    q2=StringVar()
    q2.set(f)
    lable=Label(gui,text=f,bg="sky blue",fg="black",font="ArialBlack 15 bold")
    lable.place(x=730,y=150)
    lable=Button(gui,text="a. 91",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=80,y=290)
    lable=Button(gui,text="b. 20",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=80,y=350)
    lable=Button(gui,text="c. 47",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=80,y=410)
    lable=Button(gui,text="d. 43",bg="white",fg="blue",font=("Comic Sans MS",15),command=lambda: q("9"))
    lable.place(x=80,y=470)

    
    lable=Button(gui,text="a. 45",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=780,y=290)
    lable=Button(gui,text="b. 159",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=780,y=350)
    lable=Button(gui,text="c. 95",bg="white",fg="blue",font=("Comic Sans MS",15))
    lable.place(x=780,y=410)
    lable=Button(gui,text="d. 135",bg="white",fg="blue",font=("Comic Sans MS",15),command=lambda: q("10"))
    lable.place(x=780,y=470)

    
    lable=Button(gui,text="Finish",bg="blue",fg="light green",font=("Comic Sans MS",20),command=lambda: Final(mark))
    lable.place(x=1200,y=600)
    lable=Button(gui,text="Back",bg="Blue",fg="white",font=("Comic Sans MS",18),command=gui.destroy)
    lable.place(x=80,y=610)
from PIL import Image, ImageTk
speak("you have choice a great #2.over by aman singh")
speak("welcome to the #2.0ver")
n=-1
gn=Tk()
gn.attributes('-fullscreen',True)
gn.configure(bg="black")
gn.minsize(200,200)
Image=Image.open("am.jpg")
Photo=ImageTk.PhotoImage(Image)
lable=Button(image = Photo,command=gn.destroy)
lable.place(x=42,y=23)
b=Label(gn,text="Click on DVD",bg="green",fg="WHITE",font="ArialBlack 20 bold")
b.place(x=600,y=0)
gn,mainloop()
speak("welcome to the Log in window")
from os import system , name
if __name__ == "__main__":
    from PIL import Image, ImageTk
    gui=Tk()
    gui.configure(bg="blue")
    gui.title("WELCOME #2.0ver")
    gui.attributes('-fullscreen',True)
    def enter():
        speak("you have entered")
        global n
        i=output_lab.get()
        speak(i)
        j="NA98D389N9"
        if i==j:
            out.set("sucessfull")
            n=0
            speak("log in sucessfull")
            gui.destroy()
        else:
            speak("log in falid")
            messagebox.showwarning("Warning #2.0ver","""Invalid I.D.
Please check online
on clicking WEB SUPPORT""")
            speak("for online support on clicking WEB SUPPORT")
    Image=Image.open("login.png")
    Photo = ImageTk.PhotoImage(Image)
    lable=Label(image = Photo)
    lable.place(x=0,y=0)
    b=Label(gui,text="WELCOME TO #2.0ver",bg="BLACK",fg="red",font="ArialBlack 28 bold")
    b.place(x=475,y=15)
    b=Label(gui,text="SERVICES ID",bg="DARK BLUE",fg="RED",font="Arial 25 bold")
    b.place(x=370,y=300)
    user=StringVar()
    output_lab=Entry(gui,textvariable=user,bg="blue",fg="YELLOW",font=("Comic Sans MS",20))
    output_lab.place(x=605,y=300)
    out=StringVar()
    b=Label(gui,textvariable=out,bg="DARK blue",fg="YELLOW",font=("Comic Sans MS",20))
    b.place(x=580,y=450)
    b1=Button(gui,text="Log In",command=enter,fg="WHITE",font="ArialBlack 20 bold",bg="DARK blue")
    b1.place(x=625,y=400)
    b1=Button(gui,text="WEB SUPPORT",command=brou,fg="YELLOW",font="ArialBlack 15 bold",bg="blue")
    b1.place(x=605,y=480)
    b=Label(gui,text="Please Enter the product Data",bg="DARK blue",fg="LIGHT green",font="Arial 20")
    b.place(x=510,y=570)
    labl=Button(gui,text="EXIT",bg="WHITE",fg="BLACK",font=("Comic Sans MS",18),command=gui.destroy)
    labl.place(x=70,y=670)
    gui.mainloop()
if n==0:
    g=Tk()
    g.attributes('-fullscreen',True)
    from PIL import Image, ImageTk
    Image=Image.open("main.png")
    Photo = ImageTk.PhotoImage(Image)
    lable=Label(g,image=Photo)
    lable.place(x=0,y=0)
    b=Label(g,text="#2.0ver MAIN_MENU",bg="DARK BLUE",fg="red",font="ArialBlack 28 bold")
    b.place(x=500,y=10)
    def learn():
        global n
        n=2
        speak("you have choice learning option")
        g.destroy()
    lablell=Button(g,text="LEARNING",bg="blue",fg="WHITE",font=("Comic Sans MS",25),command=learn)
    lablell.place(x=40,y=490)
    def mock():
        global n
        n=1
        speak("you have choice mock option")
        g.destroy()
    def game():
        speak("you have choice game option")
        os.system("fg.py")
    lablemock=Button(g,text="MOCK TEST",bg="BLUE",fg="WHITE",font=("Comic Sans MS",25),command=mock)
    lablemock.place(x=553,y=490)
    lable=Button(g,text="GAMES ",bg="blue",fg="WHITE",font=("Comic Sans MS",25),command=game)
    lable.place(x=1100,y=490)
    f1=open("aman.txt")
    f=f1.read()
    lable=Label(g,text=f,bg="DARK BLUE",fg="white",font=("Comic Sans MS",15))
    lable.place(x=460,y=600)
    lableEx=Button(g,text="EXIT",bg="WHITE",fg="BLACK",font=("Comic Sans MS",16),command=g.destroy)
    lableEx.place(x=100,y=600)
    g.mainloop()
    if n==1:
        from PIL import Image, ImageTk
        gui=Tk()
        gui.attributes('-fullscreen',True)
        gui.configure(bg="WHITE")
        Image=Image.open("mock.png")
        Photo=ImageTk.PhotoImage(Image)
        lable=Label(gui,image = Photo)
        lable.place(x=0,y=0)
        a=Label(gui,text="MOCK TEST #2.0",bg="BLACK",fg="WHITE",font="ArialBlack 45 bold")
        a.place(x=440,y=15)
        a=Button(gui,text="MCQ Test Set 1",bg="blue",fg="red",font="ArialBlack 30 bold",command=marksd)
        a.place(x=74,y=150)
        a=Button(gui,text="MCQ Test Set 2",bg="blue",fg="red",font="ArialBlack 30 bold",command=marks2d)
        a.place(x=74,y=250)
        a=Button(gui,text="More Questions",bg="SKY blue",fg="RED",font="ArialBlack 20 bold",command=qu)
        a.place(x=74,y=350)
        a=Button(gui,text=" Exit ",bg="WHITE",fg="BLACK",font="ArialBlack 18 bold",command=gui.destroy)
        a.place(x=74,y=600)
        gui.mainloop()
    if n==2:
        from PIL import Image, ImageTk
        gui=Tk()
        gui.attributes('-fullscreen',True)
        gui.configure(bg="sky blue")
        b=Label(gui,text="#2.0ver Syllabus",bg="sky blue",fg="red",font="ArialBlack 40 bold")
        b.place(x=450,y=10)
        Image=Image.open("leaning.png")
        Photo=ImageTk.PhotoImage(Image)
        lable=Label(image = Photo)
        lable.place(x=0,y=0)
        lable=Label(gui,text="""
----------------------  TOKENS  ----------------------""",bg="sky blue",fg="green"
                ,font="ArialBlack 18 bold")
        lable.place(x=50,y=70)
        a=Button(gui,text="1) Tokens_Explainion_Video",fg="blue",font="Arial 17",command=tov)
        a.place(x=100,y=170)
        a=Button(gui,text="2) Notes_for_tokens",fg="blue",font="Arial 17",command=to)
        a.place(x=450,y=170)
        lable=Label(gui,text="----------------------  LIST MANIPULATION ---------------------",bg="sky blue",fg="red",font="ArialBlack 18 bold")
        lable.place(x=35,y=230)
        a=Button(gui,text="1) Lists_Explainion_Video",fg="blue",font="Arial 17",command=liv)
        a.place(x=100,y=280)
        a=Button(gui,text="2) Notes_for_List",fg="blue",font="Arial 17",command=li)
        a.place(x=450,y=280)
        lable=Label(gui,text="----------------------  TUPLES  ----------------------",bg="sky blue",fg="GREEN",font="ArialBlack 20 bold")
        lable.place(x=50,y=350)
        a=Button(gui,text="1) Tuples_Explainion_Video",fg="blue",font="Arial 17",command=tuv)
        a.place(x=100,y=400)
        a=Button(gui,text="2) Notes_for_Tuples",fg="blue",font="Arial 17",command=tu)
        a.place(x=450,y=400)
        lable=Label(gui,text="------------------  STRING MANIPULATION  -----------------",bg="sky blue",fg="RED",font="ArialBlack 18 bold")
        lable.place(x=50,y=450)
        a=Button(gui,text="1) Strings_Explainion_Video",fg="blue",font="Arial 17",command=stv)
        a.place(x=100,y=500)
        a=Button(gui,text="2) Notes_for_Strings",fg="blue",font="Arial 17",command=st)
        a.place(x=450,y=500)
        lable=Label(gui,text="----------------------  Dictionaries   ----------------------",bg="sky Blue",fg="green",font="ArialBlack 20 bold")
        lable.place(x=50,y=550)
        a=Button(gui,text="1) Dictionaries_Explainion_Video",fg="blue",font="Arial 15",command=div)
        a.place(x=100,y=600)
        a=Button(gui,text="2) Notes_for_Dictionaries",fg="blue",font="Arial 17",command=di)
        a.place(x=450,y=600)
        a=Button(gui,text="Exit",bg="blue",fg="White",font="Arial 20",command=gui.destroy)
        a.place(x=20,y=700)
        gui.mainloop()
