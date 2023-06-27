from tkinter import *
from tkinter import messagebox as mb
import easygui
import semantic_analysis as s


def button_select():
    input_file = easygui.fileopenbox(filetypes=["*.txt"])
    s.semantic_analysis(way=f'{input_file}')
    mb.showinfo("Successful", "Parsing completed")


def button_entry():
    s.semantic_analysis(text=inputText.get())
    mb.showinfo("Successful", "Parsing completed")

def instruction():
    def close():
        instructionWindow.destroy()

    instructionWindow = Toplevel()
    instructionWindow['bg'] = '#ffe4c4'
    instructionWindow.geometry('500x500')
    instructionWindow.title("Инструкция")
    instructionWindow.resizable(False, False)
    Label(instructionWindow, text="To use the app:",font="Arial 10", bg='#ffe4c4').place(x=55, y=0)
    Label(instructionWindow, text="1)Enter the text", font="Arial 10", bg='#ffe4c4').place(x=0, y=20)
    Label(instructionWindow, text="2)Click the button 'Input'", font="Arial 10", bg='#ffe4c4').place(x=0, y=40)
    Label(instructionWindow, text="OR", font="Arial 10", bg='#ffe4c4').place(x=75, y=60)
    Label(instructionWindow, text="1)Click the button 'Open'", font="Arial 10", bg='#ffe4c4').place(x=0, y=80)
    Label(instructionWindow, text="2)Select the desired file", font="Arial 10", bg='#ffe4c4').place(x=0, y=100)
    Label(instructionWindow, text="All analysis is saved in a file\n 'semantic_analysis'", font="Arial 10",
          bg='#ffe4c4').place(x=0, y=120)

    closeButton = Button(instructionWindow, text='OK', font="Arial 10", command=close)
    closeButton.place(x=90, y=160)

window = Tk()
window['bg'] = '#ffe4c4'
window.title("Semantic Sentence Analysis")
window.wm_attributes('-alpha', 1)
window.geometry('500x500')
window.resizable(height=False, width=False)

Label(borderwidth=1, text='Enter text or select a file', bg='#ffe4c4').pack()
inputText = Entry(window, width=45)
inputText.pack()
Button(window, text="Open", bg='#7fffd4', command=button_select).place(x=20, y=70)
Button(window, text="Input", bg='#7fffd4', command=button_entry).place(x=85, y=70)
Button(window, text="Help", bg='#7fffd4', command=instruction).place(x=140, y=70)
window.mainloop()
