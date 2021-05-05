"""
GUI for Logical expander
Created on Apr 29, 2021
Version 1.6 
latest update: May 4, 2021
author: David Wiser
"""
from tkinter import *
from tkinter import ttk
from LogicConverter import *
from re import sub

''' initiallize'''
root = Tk()
root.title("First Order Logic Expander")
Welcome = Label(root, text='Welcome to the logic expander')

''' Variables'''
global expression
global UD
global expDisplay
out = ""
expression = ""
UD = ""
expDisplay = ""

'''textbox'''
global labelExp2
global labelUD2
textbox = Frame(root, height=200, width=200)
labelUD = ttk.Label(textbox, text="UD: ").grid(column=0,row=0)
labelUD2 = ttk.Label(textbox, text=UD).grid(column=0,row=1)
labelExp = ttk.Label(textbox, text='Expression:').grid(column=0,row=2)
labelExp2 = ttk.Label(textbox, text=expression).grid(column=0,row=3)

''' output display'''
output = Frame(root)
labelOUT = ttk.Label(output, text="output: ").grid(column=0,row=0)

'''functions'''
#convertion function
def conv_str2Log(string):
    outputstr = string
    outputstr = sub('&',u'\u2227',outputstr)
    #outputstr = sub('|',u'\u2228',outputstr)
    #outputstr = sub('$',u'\u2192',outputstr)
    outputstr = sub('%',u'\u2294',outputstr)
    outputstr = sub('~',u'\u00AC',outputstr)
    outputstr = sub('@',u'\u2200',outputstr)
    #outputstr = sub('\\',u'\u2203',outputstr)
    return outputstr

#functions for the different button commands
def and_bt():
    """adds an and (&) to the expression"""
    temp = '&'
    global expression
    global expDisplay
    expDisplay += u'\u2227'
    expression += temp
    labelExp2 = ttk.Label(textbox, text=expDisplay).grid(column=0,row=3)
    return None

def or_bt():
    """adds an or (|) to the expression"""
    temp = '|'
    global expression
    global expDisplay
    expDisplay += u'\u2228'
    expression += temp
    labelExp2 = ttk.Label(textbox, text=expDisplay).grid(column=0,row=3)
    return None

def exists_bt():
    """adds an exisits (\\) to the expression"""
    temp = '\\'
    global expression
    global expDisplay
    expDisplay += u'\u2203'
    expression += temp
    labelExp2 = ttk.Label(textbox, text=expDisplay).grid(column=0,row=3)
    return None

def forall_bt():
    """adds a forall (@) to the expression"""
    temp = '@'
    global expression
    global expDisplay
    expDisplay += u'\u2200'
    expression += temp
    labelExp2 = ttk.Label(textbox, text=expDisplay).grid(column=0,row=3)
    return None

def leftpar_bt():
    """adds a ( to the expression"""
    temp = '('
    global expression
    global expDisplay
    expDisplay += temp
    expression += temp
    labelExp2 = ttk.Label(textbox, text=expDisplay).grid(column=0,row=3)
    return None

def rightpar_bt():
    """adds a ) to the expression"""
    temp = ')'
    global expression
    global expDisplay
    expDisplay += temp
    expression += temp
    labelExp2 = ttk.Label(textbox, text=expDisplay).grid(column=0,row=3)
    return None

def if_bt():
    """adds an if ($) to the expression"""
    temp = '$'
    global expression
    global expDisplay
    expDisplay += u'\u2192'
    expression += temp
    labelExp2 = ttk.Label(textbox, text=expDisplay).grid(column=0,row=3)
    return None

def iff_bt():
    """adds an iff (%) to the expression"""
    temp = '%'
    global expression
    global expDisplay
    expDisplay += u'\u2194'
    expression += temp
    labelExp2 = ttk.Label(textbox, text=expDisplay).grid(column=0,row=3)
    return None

def neg_bt():
    """adds a negaion (~) to the expression"""
    temp = '~'
    global expression    
    global expDisplay
    expDisplay += u'\u00AC'
    expression += temp
    labelExp2 = ttk.Label(textbox, text=expDisplay).grid(column=0,row=3)
    return None

def x_bt():
    """adds a x to the expression"""
    temp = 'x'
    global expression
    global expDisplay
    expDisplay += temp
    expression += temp
    labelExp2 = ttk.Label(textbox, text=expDisplay).grid(column=0,row=3)
    return None

def y_bt():
    """adds a y to the expression"""
    temp = 'y'
    global expression
    global expDisplay
    expDisplay += temp
    expression += temp
    labelExp2 = ttk.Label(textbox, text=expDisplay).grid(column=0,row=3)
    return None

def z_bt():
    """adds a z to the expression"""
    temp = 'z'
    global expression
    global expDisplay
    expDisplay += temp
    expression += temp
    labelExp2 = ttk.Label(textbox, text=expDisplay).grid(column=0,row=3)
    return None

#backspace buttons
def bsUD_bt():
    global UD
    if (len(UD) >= 1):
        UD = UD[0:-1]
        labelUD2 = ttk.Label(textbox, text=UD).grid(column=0,row=1)
    return None
def bsExp_bt():
    global expression
    global expDisplay
    if (len(expression) >= 1):
        expression = expression[0:-1]
        expDisplay = expDisplay[0:-1]
        labelExp2 = ttk.Label(textbox, text=expDisplay).grid(column=0,row=3)
    return None

#other important button commands
def run():
    """
    Performs the conversion drom a FOL expression into the expansion method format. 
    
    Utilizes the Logic Converter file for the input checker and converter functions

    Returns None.
    """
    global out
    global expression
    if inputChecker(expression):
        out = converter(expression, UD)
        out2= conv_str2Log(out)
        labelOUT2 = ttk.Label(output, text=out2).grid(column=0,row=1)
    else :
        labelOUT2 = ttk.Label(output, text='invalid input').grid(column=0,row=1)
    return None

def reset():
    global expression
    global UD
    global expDisplay
    global labelExp2
    global labelUD2
    # expression = ""
    # expDisplay = ""
    # UD = ""
    temp = "  "
    temp2 ="  "
    for i in range(len(expression)):
        bsExp_bt()
        temp += " "
    for j in range(len(UD)):
        bsUD_bt()
        temp2 += " "
    labelExp2 = ttk.Label(textbox, text=temp).grid(column=0,row=3)
    labelUD2 = ttk.Label(textbox, text=temp2).grid(column=0,row=1)
    return None

#shortcut functions
def pressand(event):
    and_bt()
    return None
def pressor(event):
    or_bt()
    return None
def pressexists(event):
    exists_bt()
    return None
def pressforall(event):
    forall_bt()
    return None
def pressleftpar(event):
    leftpar_bt()
    return None
def pressrightpar(event):
    rightpar_bt()
    return None
def pressif(event):
    if_bt()
    return None
def pressiff(event):
    iff_bt()
    return None
def pressneg(event):
    neg_bt()
    return None
def pressx(event):
    x_bt()
    return None
def pressy(event):
    y_bt()
    return None
def pressz(event):
    z_bt()
    return None

#entry boxes
def enterS(event):
    global expression
    global expDisplay
    txt = inputS.get()
    expression += txt
    txt2 = conv_str2Log(txt)
    expDisplay += txt2
    inputS.delete(0,'end')
    labelExp2 = ttk.Label(textbox, text=expDisplay).grid(column=0,row=3)
    return None
def enterUD(event):
    global UD
    txt = inputUD.get()
    UD += txt
    inputUD.delete(0,'end')
    labelUD2 = ttk.Label(textbox, text=UD).grid(column=0,row=1)
    return None



'''Keyboard'''
#create the buttons
keys = Frame(root, height=200, width=200)
ab = ttk.Button(keys, text=u'\u2227', command=and_bt)
ob = ttk.Button(keys, text=u'\u2228', command=or_bt)
Eb = ttk.Button(keys, text=u'\u2203', command=exists_bt)
Ab = ttk.Button(keys, text=u'\u2200', command=forall_bt)
lpb = ttk.Button(keys, text='(', command=leftpar_bt)
rpb = ttk.Button(keys, text=')', command=rightpar_bt)
ib = ttk.Button(keys, text=u'\u2192', command=if_bt)
bb = ttk.Button(keys, text=u'\u2194', command=iff_bt)
nb = ttk.Button(keys, text=u'\u00AC', command=neg_bt)
xb = ttk.Button(keys, text='x', command=x_bt)
yb = ttk.Button(keys, text='y', command=y_bt)
zb = ttk.Button(keys, text='z', command=z_bt)

#format layout
ab.grid(column=0,row=0)
ob.grid(column=1,row=0)
Eb.grid(column=0,row=1)
Ab.grid(column=1,row=1)
lpb.grid(column=0,row=2)
rpb.grid(column=1,row=2)
ib.grid(column=2,row=1)
bb.grid(column=2,row=2)
nb.grid(column=2,row=0)
xb.grid(column=0,row=3)
yb.grid(column=1,row=3)
zb.grid(column=2,row=3)

#shortcuts
root.bind("&", pressand)
root.bind("|", pressor)
root.bind("\\", pressexists)
root.bind("@", pressforall)
root.bind("(", pressleftpar)
root.bind(")", pressrightpar)
root.bind("$", pressif)
root.bind("%", pressiff)
root.bind("~", pressneg)
root.bind("x", pressx)
root.bind("y", pressy)
root.bind("z", pressz)

'''Other aspects of interface'''
other = Frame(root)
#run btn
ttk.Button(other, text='run', command=run).grid(column=0,row=5)

#entry for expression
inputS = ttk.Entry(other)
inputS.grid(column=0, row=1, columnspan=2)
inputS.bind("<Return>", enterS)

#entry for UD
inputUD = ttk.Entry(other)
inputUD.grid(column=0, row=3, columnspan=2)
inputUD.bind("<Return>", enterUD)

#Reset button
ttk.Button(other, text='reset', command=reset).grid(column=1,row=5)

#backspace buttons
ttk.Button(other, text='backspace UD', command=bsUD_bt).grid(column=0,row=6)
ttk.Button(other, text='backspace expression', command=bsExp_bt).grid(column=1,row=6)

#formatting
Label(other, text="").grid(column=0,row=0, columnspan=2)
Label(other, text="").grid(column=0,row=2, columnspan=2)
Label(other, text="").grid(column=0,row=4, columnspan=2)



'''final grid'''
#set window
#mainframe = ttk.Frame(root, padding="3 3 12 12")
#mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
#root.columnconfigure(0, weight=1)
#root.rowconfigure(0, weight=1)
root.geometry("600x300")
Welcome.grid(column=0, row=0, columnspan=2)
keys.grid(column=0, row=1)
textbox.grid(column=1, row=1)
other.grid(column=0, row=2, columnspan=2)
output.grid(column=0, row=3, columnspan=2)

root.mainloop()