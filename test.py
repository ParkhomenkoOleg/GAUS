import tkinter as tk
import re


class Maria:
    didWeGetData = False
    data = []


class SimpleTableInput(tk.Frame):
    def __init__(self, parent, rows, columns):
        tk.Frame.__init__(self, parent)

        self._entry = {}
        self.rows = rows
        self.columns = columns

        # register a command to use for validation
        vcmd = (self.register(self._validate), "%P")

        # create the table of widgets
        for row in range(self.rows):
            for column in range(self.columns):
                index = (row, column)
                e = tk.Entry(self, validate="key", validatecommand=vcmd)
                e.grid(row=row, column=column, stick="nsew")
                self._entry[index] = e
        # adjust column weights so they all expand equally
        for column in range(self.columns):
            self.grid_columnconfigure(column, weight=1)
        # designate a final, empty row to fill up any extra space
        self.grid_rowconfigure(rows, weight=1)

    def get(self):
        '''Return a list of lists, containing the data in the table'''
        result = []
        for row in range(self.rows):
            current_row = []
            for column in range(self.columns):
                index = (row, column)
                current_row.append(self._entry[index].get())
            result.append(current_row)
        return result

    def _validate(self, string):
        regex = re.compile(r"(\+|\-)?[0-9.]*$")
        result = regex.match(string)
        return (string == ""
                or (string.count('+') <= 1
                    and string.count('-') <= 1
                    and string.count(',') <= 1
                    and result is not None
                    and result.group(0) != ""))
    # def _validate(self, P):
    #
    #     '''Perform input validation.
    #
    #     Allow only an empty value, or a value that can be converted to a float
    #     '''
    #     if P.strip() == "":
    #         return True
    #
    #     try:
    #         f = float(P)
    #     except ValueError:
    #         self.bell()
    #         return False
    #     return True


class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.table = SimpleTableInput(self, 3, 4)
        self.submit = tk.Button(self, text="Розв'язати", command=self.on_submit)
        self.table.pack(side="top", fill="both", expand=True)
        self.submit.pack(side="bottom")

    def on_submit(self):
        print(self.table.get())
        if self.get_table():
            print("here")
            Maria.didWeGetData = True
            Maria.data = self.table.get()

    def get_table(self):
        isFull = True
        for i in range(len(self.table.get())):
            for j in range(len(self.table.get()[i])):
                if self.table.get()[i][j] == "":
                    isFull = False
        if isFull:
            return self.table.get()
        else:
            return "Error"


def testik():
    root = tk.Tk()
    Example(root).pack(side="top", fill="both", expand=True)
    root.mainloop()


if __name__ == '__main__':
    testik()
