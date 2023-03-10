# Import the required Libraries
import tkinter.dialog
from tkinter import *
from tkinter import ttk, messagebox as mb, dialog
from tkinter import filedialog as fd

import solver
from calculationFromFile import calculation_from_file
from test import Example, Maria


class Oleh:
    didWeGetPath = False
    path = ""

def hehe():
    # # Create an instance of Tkinter frame
    # win = Tk()
    #
    # # Set the geometry of Tkinter frame
    # win.geometry("100x100")
    #
    # def display_text():
    #     global entry
    #     string = entry.get()
    #     label.configure(text=string)
    #
    # # Initialize a Label to display the User Input
    # label = Label(win, text="", font=("Courier 22 bold"))
    # label.pack()
    #
    # # Create an Entry widget to accept User Input
    # entry = Entry(win, width=40)
    # entry.focus_set()
    # entry.pack()
    #
    # # Create a Button to validate Entry Widget
    # ttk.Button(win, text="Okay", width=20, command=display_text).pack(pady=20)
    # mb.showinfo("Information", "Informative message")
    if mb.askyesno(title="Важливе питання", message="Чи хочете ви розв'язати рівняння методом Гауса у форматі файла?"):
        print("ФОРМАТ ФАЙЛУ")

        def callback():
            global name
            name = fd.askopenfilename()
            print(name)
            Oleh.didWeGetPath = True
            Oleh.path = name

        errmsg = 'Error!'
        tkinter.Button(text='Відкрити файл',
                       command=callback).pack(fill=tkinter.X)

        tkinter.mainloop()
        while not Oleh.didWeGetPath:
            pass

        result = calculation_from_file(name)
        win = Tk()
        win.geometry("400x400")
        label = Label(win, text=result, font=("Courier 22 bold"))
        label.pack()
        tkinter.mainloop()
        exit()
    elif mb.askyesno(title="Друге важливе питання",
                     message="Чи хочете ви розв'язати рівняння методом Гауса у візуальному форматі?"):
        print("not hehe")
        root = tkinter.Tk()
        Example(root).pack(side="top", fill="both", expand=True)
        root.mainloop()


        while not Maria.didWeGetData:
            pass

        pre_result = Maria.data
        for i in range(len(pre_result)):
            for j in range(len(pre_result[i])):
                pre_result[i][j] = float(pre_result[i][j])
        result = solver.solve(pre_result)




        win = Tk()
        win.geometry("400x400")
        label = Label(win, text=result, font=("Courier 22 bold"))
        label.pack()
        tkinter.mainloop()
        exit()
    else:
        mb.showwarning(title="Попередження",
                       message="На жаль, більше немає форматів. Якщо хочете спробувати знову, то перезапустіть "
                               "програму.")
        exit()
    # d = MyDialog(tkinter.dialog.Dialog)
    # print(d.result)
    # win.mainloop()


if __name__ == '__main__':
    hehe()
