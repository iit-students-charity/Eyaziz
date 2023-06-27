from tkinter import *
from tkinter import messagebox as mb
import easygui
import sintax


def button_select():
    input_file = easygui.fileopenbox(filetypes=["*.txt"])
    sintax.parsing(way=input_file)
    mb.showinfo("Успешно", "Парсинг завершен")


def button_entry():
    sintax.parsing(text=inputFileName.get())
    mb.showinfo("Успешно", "Парсинг завершен")


window = Tk()
window['bg'] = '#ffe4c4'
window.title("Синтаксический анализ предложения")
window.wm_attributes('-alpha', 1)
window.geometry('500x500')
window.resizable(height=False, width=False)

Label(borderwidth=1, relief="sunken", text='Введите текст или выберите файл', bg='#ffe4c4').pack()
inputFileName = Entry(window, width=45)
inputFileName.pack()
Button(window, text="Выбрать", bg='#7fffd4', command=button_select).place(x=20, y=70)
Button(window, text="Ввести", bg='#7fffd4', command=button_entry).place(x=120, y=70)

window.mainloop()

# print(word_analyze.tag.mood)          # наклонение (повелительное, изъявительное)
# print(word_analyze.tag.transitivity)  # переходность (переходный, непереходный)
# print(word_analyze.tag.voice)         # залог (действительный, страдательный)
