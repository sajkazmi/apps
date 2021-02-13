from tkinter import *

#window setup
window = Tk()
window.geometry('250x400+300+300')
window.resizable(0,0)
window.title('Syed Sajeel')


#variables
first_operand = 0
second_operand = 0

#digit function
def result_commands(command_var):
    res = results.get()
    if command_var=='' or res in 'Cannot use more than one operator' or res == '+' or res in 'Division by zero not allowed':
        results.set(command_var)
    else:
        if '=' in res or res in 'Syntax Error':
            results.set(command_var)
        else:
            results.set(res + command_var)

#operator function
def operator_control(op_value):
    global first_operand
    res = results.get()
    if '=' in res:
        res = res.replace('=','')
    if res == '' or res in 'Cannot use more than one operator' or res in 'Division by zero not allowed':
        results.set(op_value)
    else:
        try:
            first_operand = int(res)
            if res in 'Syntax Error':
                results.set(op_value)
            else:
                res = res + op_value
                results.set(res)
        except ValueError:
            results.set('Cannot use more than one operator')


#output function
def show_results():
    global first_operand
    res = results.get()
    if '=' in res:
        pass
    else:
        try:
            if '+' in res:
                second_operand = int(res.split('+')[1])
                res = str(first_operand + second_operand)
            if '-' in res:
                second_operand = int(res.split('-')[1])
                res = str(first_operand - second_operand)
            if '*' in res:
                second_operand = int(res.split('*')[1])
                res = str(first_operand * second_operand)
            if '/' in res:
                second_operand = int(res.split('/')[1])
                res = str(int(first_operand / second_operand))


            res = "=" + res
            results.set(res)
        except ZeroDivisionError:
            results.set('Division by zero not allowed')







#label on the top
results = StringVar()
lbl = Label(window, textvariable=results, font='Raleway', background='white', fg='black', anchor=SE)
lbl.pack( expand=True, fill='both')



#button row 1
btnrow1 = Frame(window, bg='brown')
btnrow1.pack(expand=True, fill = 'both')

btn1 = Button(btnrow1,text='1', command=lambda:result_commands('1'), font='Raleway', bd=0)
btn1.pack(side='left',expand=True, fill='both')

btn2 = Button(btnrow1,text='2', command=lambda:result_commands('2' ), font='Raleway', bd=0)
btn2.pack(side= 'left',expand=True, fill='both')

btn3 = Button(btnrow1,text='3', command=lambda:result_commands('3'), font='Raleway', bd=0)
btn3.pack(side= 'left',expand=True, fill='both')

btn4 = Button(btnrow1,text='+', command=lambda: operator_control('+'),
              font='Raleway', bd=0)
btn4.pack(side= 'left',expand=True, fill='both')


#button row 2
btnrow2 = Frame(window, )
btnrow2.pack(expand=True, fill = 'both')

btn1 = Button(btnrow2,text='4', command=lambda:result_commands('4'), font='Raleway', bd=0)
btn1.pack(side='left',expand=True, fill='both')

btn2 = Button(btnrow2,text='5', command=lambda:result_commands('5'), font='Raleway', bd=0)
btn2.pack(side= 'left',expand=True, fill='both')

btn3 = Button(btnrow2,text='6', command=lambda:result_commands('6'), font='Raleway', bd=0)
btn3.pack(side= 'left',expand=True, fill='both')

btn4 = Button(btnrow2,text='-', command=lambda: operator_control('-'), font='Raleway', bd=0)
btn4.pack(side= 'left',expand=True, fill='both')


#button row 3
btnrow3 = Frame(window , bg='green')
btnrow3.pack(expand=True, fill = 'both')

btn1 = Button(btnrow3,text='7', command=lambda:result_commands('7'), font='Raleway', bd=0)
btn1.pack(side='left',expand=True, fill='both')

btn2 = Button(btnrow3,text='8', command=lambda:result_commands('8'), font='Raleway', bd=0)
btn2.pack(side= 'left',expand=True, fill='both')

btn3 = Button(btnrow3,text='9', command=lambda:result_commands('9'), font='Raleway', bd=0)
btn3.pack(side= 'left',expand=True, fill='both')

btn4 = Button(btnrow3,text='*', command=lambda: operator_control('*'), font='Raleway', bd=0)
btn4.pack(side= 'left',expand=True, fill='both')

#button row 4
btnrow4 = Frame(window, bg='yellow')
btnrow4.pack(expand=True, fill = 'both')



btn1 = Button(btnrow4, command=lambda:result_commands(''), text='Clear',font='Raleway', bd=0)
btn1.pack(side='left',expand=True, fill='both')

btn2 = Button(btnrow4,text='0', command=lambda:result_commands('0'),font='Raleway', bd=0)
btn2.pack(side= 'left',expand=True, fill='both')

btn3 = Button(btnrow4,text='/', command=lambda: operator_control('/'),font='Raleway', bd=0)
btn3.pack(side= 'left',expand=True, fill='both')

btn4 = Button(btnrow4,text='=', command=lambda:show_results(), font='Raleway', bd=0)
btn4.pack(side= 'left',expand=True, fill='both')






mainloop()