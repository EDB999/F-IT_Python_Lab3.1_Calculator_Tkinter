from tkinter import *


class Main(Frame):

    def __init__(self, root_init):
        super().__init__(root_init)
        self.build()

    def build(self):
        self.formula = ""

        self.label = Label(text=self.formula, bg="#323232", foreground="#FFF",
                           font=("Times New Roman", 16, "bold"))

        self.label.place(x=11, y=50)

        btns = ["C", "x^2", "Back", "/",
                "7", "8", "9", "*",
                "4", "5", "6", "-",
                "1", "2", "3", "+",
                "+/-", "0", "%", "="
                ]
        x = 10
        y = 140

        for btn in btns:

            com = lambda x=btn: self.calculateLogic(x)

            Button(text=btn, bg="#898989", foreground="#FFF",
                   font=("Times New Roman", 16),
                   command=com).place(x=x, y=y, width=115, height=79)

            x += 117
            if x > 400:
                x = 10
                y += 81

    def calculateLogic(self, operation):
        if operation == "C":
            self.formula = ""
        elif operation == "x^2":
            self.formula = str((eval(self.formula)) ** 2)
        elif operation == "Back":
            self.formula = self.formula[0:-1]
        elif operation == "=":
            self.formula = str(eval(self.formula))
        elif operation == "+/-":
            self.formula = str((eval(self.formula)) * -1)
        else:
            if self.formula == "0":
                self.formula = ""
            self.formula += operation

        self.update()

    def update(self):
        if self.formula == "":
            self.formula = ""

        self.label.configure(text=self.formula, bg="#323232")


if __name__ == '__main__':
    root = Tk()

    root["bg"] = "#323232"
    root.geometry("485x550+200+200")
    root.title("Calculator")
    root.resizable(False, False)

    app = Main(root)

    app.pack()

    root.mainloop()
