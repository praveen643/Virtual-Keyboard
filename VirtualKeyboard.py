#Virtual Keyboard project
#press enter on virtual keyboard to get full text after running program
#text will get print on running window


"""impoerting GUI Package"""
from tkinter import *


root = Tk()

avar = 1
bvar = 1

def shiftf():
    global bvar
    bvar = bvar+1
    return bvar


def minusf():
    if bvar % 2 == 0:
        print("_", end="")
    else:
        print("-", end="")


def plusf():
    if bvar % 2 == 0:
        print("+", end="")
    else:
        print("=", end="")


def opbrf():
    if bvar % 2 == 0:
        print("{", end="")
    else:
        print("[", end="")


def clbrf():
    if bvar % 2 == 0:
        print("}", end="")
    else:
        print("]", end="")


def bcslashf():
    if bvar % 2 == 0:
        print("|", end="")
    else:
        print("\\", end="")


def quesf():
    if bvar % 2 == 0:
        print("?", end="")
    else:
        print("/", end="")


def colmf():
    if bvar % 2 == 0:
        print(":", end="")
    else:
        print(";", end="")


def aphf():
    if bvar % 2 == 0:
        print('"', end="")
    else:
        print("'", end="")


def grf():
    if bvar % 2 == 0:
        print("<", end="")
    else:
        print(",", end="")


def lessf():
    if bvar % 2 == 0:
        print(">", end="")
    else:
        print(".", end="")


def tildf():
    print("~", end="")


def onef():
    print(int("1"), end="")


def twof():
    print(int("2"), end="")


def threef():
    print(int("3"), end="")


def fourf():
    print(int("4"), end="")


def fivef():
    print(int("5"), end="")


def sixf():
    print(int("6"), end="")


def sevenf():
    print(int("7"), end="")


def eightf():
    print(int("8"), end="")


def ninef():
    print(int("9"), end="")


def zerof():
    print(int("0"), end="")


def backf():
    print("\b", end="")


def tabf():
    print("    ", end="")


def enterf():
    print("\n", end="")


def space():
    print(" ", end="")


def capsf():
    global avar
    avar = avar+1
    return avar


def af():
    global avar
    if avar % 2 == 0:
        print("A", end="")
    else:
        print("a", end="")


def bf():
    global avar
    if avar % 2 == 0:
        print("B", end="")
    else:
        print("b", end="")


def cf():
    global avar
    if avar % 2 == 0:
        print("C", end="")
    else:
        print("c", end="")


def df():
    global avar
    if avar % 2 == 0:
        print("D", end="")
    else:
        print("d", end="")


def ef():
    global avar
    if avar % 2 == 0:
        print("E", end="")
    else:
        print("e", end="")


def ff():
    global avar
    if avar % 2 == 0:
        print("F", end="")
    else:
        print("f", end="")


def gf():
    global avar
    if avar % 2 == 0:
        print("G", end="")
    else:
        print("g", end="")


def hf():
    global avar
    if avar % 2 == 0:
        print("H", end="")
    else:
        print("h", end="")


def iff():
    global avar
    if avar % 2 == 0:
        print("I", end="")
    else:
        print("i", end="")


def jf():
    global avar
    if avar % 2 == 0:
        print("J", end="")
    else:
        print("j", end="")


def kf():
    global avar
    if avar % 2 == 0:
        print("K", end="")
    else:
        print("k", end="")


def lf():
    global avar
    if avar % 2 == 0:
        print("L", end="")
    else:
        print("l", end="")


def mf():
    global avar
    if avar % 2 == 0:
        print("M", end="")
    else:
        print("m", end="")


def nf():
    global avar
    if avar % 2 == 0:
        print("N", end="")
    else:
        print("n", end="")


def of():
    global avar
    if avar % 2 == 0:
        print("O", end="")
    else:
        print("o", end="")


def pf():
    global avar
    if avar % 2 == 0:
        print("P", end="")
    else:
        print("p", end="")


def qf():
    global avar
    if avar % 2 == 0:
        print("Q", end="")
    else:
        print("q", end="")


def rf():
    global avar
    if avar % 2 == 0:
        print("R", end="")
    else:
        print("r", end="")


def sf():
    global avar
    if avar % 2 == 0:
        print("S", end="")
    else:
        print("s", end="")


def tf():
    global avar
    if avar % 2 == 0:
        print("T", end="")
    else:
        print("t", end="")


def uf():
    global avar
    if avar % 2 == 0:
        print("U", end="")
    else:
        print("u", end="")


def vf():
    global avar
    if avar % 2 == 0:
        print("V", end="")
    else:
        print("v", end="")


def wf():
    global avar
    if avar % 2 == 0:
        print("W", end="")
    else:
        print("w", end="")


def xf():
    global avar
    if avar % 2 == 0:
        print("X", end="")
    else:
        print("x", end="")


def yf():
    global avar
    if avar % 2 == 0:
        print("Y", end="")
    else:
        print("y", end="")


def zf():
    global avar
    if avar % 2 == 0:
        print("Z", end="")
    else:
        print("z", end="")

"""formate or templete keyboard"""


display = Label(root, text="VIRTUAL KEYBOARD\n", fg="red", bg="BLUE")
display.config(font=("Courier", 50))
display.pack()

frame = Frame(root)
frame.pack(side=TOP)

tild = Button(frame, text="~", bg="black", fg="white", command=tildf)
tild.pack(side=LEFT)

one = Button(frame, text="1", bg="black", fg="white", command=onef)
one.pack(side=LEFT)


two = Button(frame, text="2", bg="black", fg="white", command=twof)
two.pack(side=LEFT)


three = Button(frame, text="3", bg="black", fg="white", command=threef)
three.pack(side=LEFT)


four = Button(frame, text="4", bg="black", fg="white", command=fourf)
four.pack(side=LEFT)


five = Button(frame, text="5", bg="black", fg="white", command=fivef)
five.pack(side=LEFT)


six = Button(frame, text="6", bg="black", fg="white", command=sixf)
six.pack(side=LEFT)


seven = Button(frame, text="7", bg="black", fg="white", command=sevenf)
seven.pack(side=LEFT)


eight = Button(frame, text="8", bg="black", fg="white", command=eightf)
eight.pack(side=LEFT)

nine = Button(frame, text="9", bg="black", fg="white", command=ninef)
nine.pack(side=LEFT)

zero = Button(frame, text="0", bg="black", fg="white", command=zerof)
zero.pack(side=LEFT)


minus = Button(frame, text="-  _", bg="black", fg="white", command=minusf)
minus.pack(side=LEFT)


plus = Button(frame, text="=  +", bg="black", fg="white", command=plusf)
plus.pack(side=LEFT)


backspace = Button(frame, text="backspace", bg="black", fg="white", command=backf)
backspace.pack(side=LEFT)

frame1 = Frame(root)
frame1.pack()

tab = Button(frame1, text="Tab", bg="black", fg="white", command=tabf)
tab.pack(side=LEFT)

q = Button(frame1, text="Q", bg="black", fg="white", command=qf)
q.pack(side=LEFT)

w = Button(frame1, text="W", bg="black", fg="white", command=wf)
w.pack(side=LEFT)

e = Button(frame1, text="E", bg="black", fg="white", command=ef)
e.pack(side=LEFT)

r = Button(frame1, text="R", bg="black", fg="white", command=rf)
r.pack(side=LEFT)

t = Button(frame1, text="T", bg="black", fg="white", command=tf)
t.pack(side=LEFT)

y = Button(frame1, text="Y", bg="black", fg="white", command=yf)
y.pack(side=LEFT)

u = Button(frame1, text="U", bg="black", fg="white", command=uf)
u.pack(side=LEFT)


i = Button(frame1, text="I", bg="black", fg="white", command=iff)
i.pack(side=LEFT)


o = Button(frame1, text="O", bg="black", fg="white", command=of)
o.pack(side=LEFT)


p = Button(frame1, text="P", bg="black", fg="white", command=pf)
p.pack(side=LEFT)


opbr = Button(frame1, text="{  [", bg="black", fg="white", command=opbrf)
opbr.pack(side=LEFT)


clbr = Button(frame1, text="}  ]", bg="black", fg="white", command=clbrf)
clbr.pack(side=LEFT)


slash = Button(frame1, text="\\  |", bg="black", fg="white", command=bcslashf)
slash.pack(side=LEFT)

frame2 = Frame(root)
frame2.pack()

caps = Button(frame2, text="CapsLK", bg="black", fg="white", command=capsf)
caps.pack(side=LEFT)

a = Button(frame2, text="A", bg="black", fg="white", command=af)
a.pack(side=LEFT)


s = Button(frame2, text="S", bg="black", fg="white", command=sf)
s.pack(side=LEFT)


d = Button(frame2, text="D", bg="black", fg="white", command=df)
d.pack(side=LEFT)


f = Button(frame2, text="F", bg="black", fg="white", command=ff)
f.pack(side=LEFT)


g = Button(frame2, text="G", bg="black", fg="white", command=gf)
g.pack(side=LEFT)


h = Button(frame2, text="H", bg="black", fg="white", command=hf)
h.pack(side=LEFT)


j = Button(frame2, text="J", bg="black", fg="white", command=jf)
j.pack(side=LEFT)


k = Button(frame2, text="K", bg="black", fg="white", command=kf)
k.pack(side=LEFT)


le = Button(frame2, text="L", bg="black", fg="white", command=lf)
le.pack(side=LEFT)


semic = Button(frame2, text=";  :", bg="black", fg="white", command=colmf)
semic.pack(side=LEFT)


aph = Button(frame2, text="'  "+'"', bg="black", fg="white", command=aphf)
aph.pack(side=LEFT)


enter = Button(frame2, text="ENTER", bg="black", fg="white", command=enterf)
enter.pack(side=LEFT)

frame3 = Frame(root)
frame3.pack()

shift = Button(frame3, text="Shift", bg="black", fg="white", command=shiftf)
shift.pack(side=LEFT)

z = Button(frame3, text="Z", bg="black", fg="white", command=zf)
z.pack(side=LEFT)


x = Button(frame3, text="X", bg="black", fg="white", command=xf)
x.pack(side=LEFT)


c = Button(frame3, text="C", bg="black", fg="white", command=cf)
c.pack(side=LEFT)


v = Button(frame3, text="V", bg="black", fg="white", command=vf)
v.pack(side=LEFT)


b = Button(frame3, text="B", bg="black", fg="white", command=bf)
b.pack(side=LEFT)


n = Button(frame3, text="N", bg="black", fg="white", command=nf)
n.pack(side=LEFT)


m = Button(frame3, text="M", bg="black", fg="white", command=mf)
m.pack(side=LEFT)


co = Button(frame3, text=",  <", bg="black", fg="white", command=grf)
co.pack(side=LEFT)


stop = Button(frame3, text=".  >", bg="black", fg="white", command=lessf)
stop.pack(side=LEFT)


sl = Button(frame3, text="/  ?", bg="black", fg="white", command=quesf)
sl.pack(side=LEFT)


shift = Button(frame3, text="Shift", bg="black", fg="white", command=shiftf)
shift.pack(side=LEFT)


up = Button(frame3, text="up", bg="black", fg="white")
up.pack(side=LEFT)

frame4 = Frame(root)
frame4.pack()

exi = Button(frame4, text="exit", bg="black", fg="white", command=root.quit)
exi.pack(side=LEFT)


space = Button(frame4, text=" ", bg="black", fg="white", command=space)
space.pack(side=LEFT)


left = Button(frame4, text="Left", bg="black", fg="white")
left.pack(side=LEFT)


down = Button(frame4, text="Down", bg="black", fg="white")
down.pack(side=LEFT)


right = Button(frame4, text="Right", bg="black", fg="white")
right.pack(side=LEFT)

copy = Button(root, text="copyright", fg="black")
copy.pack(side=RIGHT)
copy.config(font=("courier", 1))




menu1 = Menu(root)
root.config(menu=menu1)
submenu = Menu(menu1)
menu1.add_cascade(label="file", menu=submenu)
submenu.add_command(label="copyright", command=copy)


root.mainloop()

