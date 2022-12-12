import tkinter as tk


class mathOperation():
    def __init__(self, operationType, firstNumber, secondNumber, executeOnOperation,clearTextOnChange=False):
        self.operationType=operationType
        self.firstNumber=firstNumber
        self.secondNumber=secondNumber
        self.executeOnOperation=executeOnOperation
        self.clearTextOnChange=clearTextOnChange

def clear():
    oper.operationType=None
    oper.firstNumber="0"
    oper.secondNumber="0"
    oper.executeOnOperation=None
    oper.clearTextOnChange=False
    textMain.delete(0, "end")
    textMain.insert(0, "0")

def getAnswer(operationType):
    oper.secondNumber=float(textMain.get())
    checkDecimal()
    if operationType==None: 
        pass

    else:
        if oper.operationType=="+":
            answer=oper.firstNumber+oper.secondNumber
        if oper.operationType=="-":
            answer=oper.firstNumber-oper.secondNumber
        if oper.operationType=="*":
            answer=oper.firstNumber*oper.secondNumber
        if oper.operationType=="/":
            if oper.secondNumber==0:
                textMain.insert("end", "Cannot Divide by Zero")
                answer=0
            else:
                answer=oper.firstNumber/oper.secondNumber
        oper.firstNumber=answer
        checkDecimal()
        textMain.delete(0, "end")
        textMain.insert(0, oper.firstNumber)
        oper.clearTextOnChange=True
        oper.executeOnOperation=None

def setOperationType(operationType):
    checkDecimal()
    if oper.operationType==operationType:
        oper.secondNumber=float(textMain.get())
        getAnswer(operationType)
        oper.executeOnOperation==True
   
    else:
        checkDecimal()
        oper.operationType=operationType
        oper.firstNumber=float(textMain.get())
        oper.executeOnOperation=True
    oper.clearTextOnChange=True



def insertNum(number):
    if textMain.get()=="0" and number!=".":
        oper.clearTextOnChange=True
    if oper.clearTextOnChange==True:
        textMain.delete(0, "end")
    if number=="." and "." in textMain.get():
        pass
    else:
        textMain.insert("end", number)
        oper.clearTextOnChange=False

def checkDecimal():
    checkDig=str(oper.firstNumber)
    if checkDig[-2:]==".0":
        oper.firstNumber=int(oper.firstNumber)
    checkDig=str(oper.secondNumber)
    if checkDig[-2:]==".0":
        oper.secondNumber=int(oper.secondNumber)

def keySort(key):
    operationsList=["+","-","/","*"]
    numbersList=[]
    for i in range (9):
        numbersList.append(str(i))
        numbersList.append(".")
    if key.char in operationsList:
        setOperationType(key.char)
    elif key.char in numbersList:
        insertNum(key.char)

def keyBackspace(x):
    if len(textMain.get())<=1:
        textMain.delete(0, "end")
        textMain.insert(0, "0")
    else:
        data=textMain.get()
        data=data[:-1]
        textMain.delete(0, "end")
        textMain.insert(0, data)

oper=mathOperation(None, "0", "0", False)

root = tk.Tk()
root.title("Calculator")
root.geometry("225x200")
root.resizable(False, False)
numberFrame=tk.Frame(root)
textMainFrame=tk.Frame(root)
textMain=tk.Entry(textMainFrame, justify="right", font="TkDefaultFont 14", width=14)
buttonModulus=tk.Button(numberFrame, text="%", command="")
buttonDivision=tk.Button(numberFrame, text=" /", command=lambda: setOperationType("/"))
buttonMultiplication=tk.Button(numberFrame, text=" *", command=lambda: setOperationType("*"))
buttonSubtraction=tk.Button(numberFrame, text=" - ", command=lambda: setOperationType("-"))
buttonAddition=tk.Button(numberFrame, text="\n+\n", command=lambda: setOperationType("+"))
buttonEquals=tk.Button(numberFrame, text="\n=\n", command=lambda: getAnswer(oper.operationType))
buttonClear=tk.Button(numberFrame, text="C", command=lambda: clear())
buttonNumOne=tk.Button(numberFrame, text="1", command=lambda: insertNum("1"))
buttonNumTwo=tk.Button(numberFrame, text="2", command=lambda: insertNum("2"))
buttonNumThree=tk.Button(numberFrame, text="3", command=lambda: insertNum("3"))
buttonNumFour=tk.Button(numberFrame, text="4", command=lambda: insertNum("4"))
buttonNumFive=tk.Button(numberFrame, text="5", command=lambda: insertNum("5"))
buttonNumSix=tk.Button(numberFrame, text="6", command=lambda: insertNum("6"))
buttonNumSeven=tk.Button(numberFrame, text="7", command=lambda: insertNum("7"))
buttonNumEight=tk.Button(numberFrame, text="8", command=lambda: insertNum("8"))
buttonNumNine=tk.Button(numberFrame, text="9", command=lambda: insertNum("9"))
buttonNumZero=tk.Button(numberFrame, text="     0     ", command=lambda: insertNum("0"))
buttonDecimal=tk.Button(numberFrame, text=".", command=lambda: insertNum("."))

textMain.grid(row=0)
buttonClear.grid(row=0, column=0)
buttonDivision.grid(row=0, column=1)
buttonMultiplication.grid(row=0, column=2)
buttonSubtraction.grid(row=0, column=3)
buttonAddition.grid(row=1, column=3, rowspan=2)
buttonNumOne.grid(row=3, column=0)
buttonNumTwo.grid(row=3, column=1)
buttonNumThree.grid(row=3, column=2)
buttonNumFour.grid(row=2, column=0)
buttonNumFive.grid(row=2, column=1)
buttonNumSix.grid(row=2, column=2)
buttonNumSeven.grid(row=1, column=0)
buttonNumEight.grid(row=1, column=1)
buttonNumNine.grid(row=1, column=2)
buttonNumZero.grid(row=4, column=0, columnspan=2)
buttonDecimal.grid(row=4, column=2)
buttonEquals.grid(row=3, column=3, rowspan=2)
textMainFrame.pack()
numberFrame.pack()

root.bind("<BackSpace>", keyBackspace)
root.bind("<KP_Enter>", getAnswer)
root.bind("<KP_Decimal>", keySort)
root.bind("<Key>", keySort)

textMain.insert(0, "0")
root.mainloop()
