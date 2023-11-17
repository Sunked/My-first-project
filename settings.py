import tkinter as tk
import tkinter.messagebox as tkm

class Calculator:
    """Mini-calculator.
    
    Default calculator, which calculates int values (but not float)
    When an object is created, a window with values appears. 
    If division by 0 or syntax error occurs, the outputed window will be displayed"""
    
    window = tk.Tk()
    window.title("Calculator")
    window.iconphoto(False, tk.PhotoImage(file="CalcIcon.png"))
    window["bg"] = "#3e423f"
    window.geometry("240x260")
    window.resizable(False, False)

    string = "" # string for label manipulation

    def __init__(self) -> None:
        self.calculate = tk.StringVar()
        self.main_string = tk.Label(self.window, 
                                     textvariable=self.calculate,
                                     borderwidth=7,
                                     background="gray",
                                     foreground="white",
                                     width=50,
                                     height=3,
                                     font="Verdana"
                                    )
        # Frames
        self.string1 = tk.Frame(self.window)
        self.string2 = tk.Frame(self.window)
        self.string3 = tk.Frame(self.window)
        self.string4 = tk.Frame(self.window)

        # widgets for string1
        self.plus = tk.Button(self.string1, text="+", width=5, bg="black", fg="#f78400",
                              height=2, font="Verdana", command=self.outputPlus)
        self._1 = tk.Button(self.string1, text="1", width=5, bg="black", fg="white",
                            height=2, font="Verdana", command=self.output1)
        self._2 = tk.Button(self.string1, text="2", width=5, bg="black", fg="white",
                            height=2, font="Verdana", command=self.output2)
        self._3 = tk.Button(self.string1, text="3", width=5, bg="black", fg="white",
                            height=2, font="Verdana", command=self.output3)
        
        # widgets for string2
        self.minus = tk.Button(self.string2, text="-", width=5, bg="black", fg="#f78400",
                               height=2, font="Verdana", command=self.outputMinus)
        self._4 = tk.Button(self.string2, text="4", width=5, bg="black", fg="white",
                            height=2, font="Verdana", command=self.output4)
        self._5 = tk.Button(self.string2, text="5", width=5, bg="black", fg="white",
                            height=2, font="Verdana", command=self.output5)
        self._6 = tk.Button(self.string2, text="6", width=5, bg="black", fg="white",
                            height=2, font="Verdana", command=self.output6)
        
        # widgets for string3
        self.multiply = tk.Button(self.string3, text="*", width=5, bg="black", fg="#f78400",
                               height=2, font="Verdana", command=self.outputMultiply)
        self._7 = tk.Button(self.string3, text="7", width=5, bg="black", fg="white",
                            height=2, font="Verdana", command=self.output7)
        self._8 = tk.Button(self.string3, text="8", width=5, bg="black", fg="white",
                            height=2, font="Verdana", command=self.output8)
        self._9 = tk.Button(self.string3, text="9", width=5, bg="black", fg="white",
                            height=2, font="Verdana", command=self.output9)
        
        # widgets for string4
        self.divide = tk.Button(self.string4, text="/", width=5, bg="black", fg="#f78400",
                               height=2, font="Verdana", command=self.outputDivide)
        self.back = tk.Button(self.string4, text="←", width=5, bg="#69605f", fg="white",
                            height=2, font="Verdana", command=self.outputBack)
        self._0 = tk.Button(self.string4, text="0", width=5, bg="black", fg="white",
                            height=2, font="Verdana", command=self.output0)
        self.enter = tk.Button(self.string4, text="ENTER", width=5, bg="#69605f", fg="white",
                            height=2, font="Verdana", command=self.outputEnter)
        
        # pack widgets
        self.main_string.pack()
       
        self.plus.pack(side="left")
        self._1.pack(side="left")
        self._2.pack(side="left")
        self._3.pack(side="left")
        self.minus.pack(side="left")
        self._4.pack(side="left")
        self._5.pack(side="left")
        self._6.pack(side="left")
        self.multiply.pack(side="left")
        self._7.pack(side="left")
        self._8.pack(side="left")
        self._9.pack(side="left")
        self.divide.pack(side="left")
        self.back.pack(side="left")
        self._0.pack(side="left")
        self.enter.pack(side="left")

        # pack Frames
        self.string1.pack()
        self.string2.pack()
        self.string3.pack()
        self.string4.pack()

        self.window.mainloop()

    def outputPlus(self) -> None:
        self.string += "+"
        self.calculate.set(self.string)

    def output1(self) -> None:
        self.string += "1"
        self.calculate.set(self.string)

    def output2(self) -> None:
        self.string += "2"
        self.calculate.set(self.string)

    def output3(self) -> None:
        self.string += "3"
        self.calculate.set(self.string)

    def outputMinus(self) -> None:
        self.string += "-"
        self.calculate.set(self.string)

    def output4(self) -> None:
        self.string += "4"
        self.calculate.set(self.string)

    def output5(self) -> None:
        self.string += "5"
        self.calculate.set(self.string)

    def output6(self) -> None:
        self.string += "6"
        self.calculate.set(self.string)

    def outputMultiply(self) -> None:
        self.string += "*"
        self.calculate.set(self.string)

    def output7(self) -> None:
        self.string += "7"
        self.calculate.set(self.string)

    def output8(self) -> None:
        self.string += "8"
        self.calculate.set(self.string)

    def output9(self) -> None:
        self.string += "9"
        self.calculate.set(self.string)

    def outputDivide(self) -> None:
        self.string += "/"
        self.calculate.set(self.string)

    def outputBack(self) -> None:
        if len(str(self.string)) == 1:
            self.string = ""
        else:
            self.string = str(self.string)[0:-1]
            self.calculate.set(self.string)

    def output0(self) -> None:
        self.string += "0"
        self.calculate.set(self.string)

    def outputEnter(self) -> None:
        try:
            self.string = eval(self.string)
            self.calculate.set(self.string)
        
        except SyntaxError:
            tkm.showerror("ERROR", "Invalid expression")

        except ZeroDivisionError:
            tkm.showerror("ERROR", "You can't divide by zero")