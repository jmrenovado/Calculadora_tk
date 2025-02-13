
import tkinter as tk

root = tk.Tk()
root.configure(background='#333333')
root.title('Calculadora')
root.geometry('386x168')

equation = tk.StringVar()

def press(num): 
    equation.set(equation.get() + str(num))
   
    
def equalpress():
    try:
        total = str(eval(equation.get()))
        equation.set(total)
    except(SyntaxError, ZeroDivisionError):
        equation.set('error')
        
def clear():
    equation.set('')
    
def exit_app():
    root.quit()
    
Expression_entry = tk.Entry(root, textvariable=equation, font=('Arial', 18))
Expression_entry .grid(row=0, columnspan=4, sticky='nswe')

# Configurar las filas y columnas para que se expandan
for i in range(6):
    root.rowconfigure(i, weight=1)
for i in range(4):
    root.columnconfigure(i, weight=1)
    
button_font = ('Arial', 18)

btn7 = tk.Button(root, text=' 7 ', fg='#fff', background='#666', command=lambda: press(7), font=button_font)
btn7.grid(row=1, column=0, sticky='nswe')

btn8 = tk.Button(root, text=' 8 ', fg='#fff', background='#666', command=lambda: press(8), font=button_font)
btn8.grid(row=1, column=1, sticky='nswe')

btn9 = tk.Button(root, text=' 9 ', fg='#fff', background='#666', command=lambda: press(9), font=button_font)
btn9.grid(row=1, column=2, sticky='nswe')

btn4 = tk.Button(root, text=' 4 ', fg='#fff', background='#666', command=lambda: press(4), font=button_font)
btn4.grid(row=2, column=0, sticky='nswe')

btn5 = tk.Button(root, text=' 5 ', fg='#fff', background='#666', command=lambda: press(5), font=button_font)
btn5.grid(row=2, column=1, sticky='nswe')

btn6 = tk.Button(root, text=' 6 ', fg='#fff', background='#666', command=lambda: press(6), font=button_font)
btn6.grid(row=2, column=2, sticky='nswe')

btn1 = tk.Button(root, text=' 1 ', fg='#fff', background='#666', command=lambda: press(1), font=button_font)
btn1.grid(row=3, column=0, sticky='nswe')

btn2 = tk.Button(root, text=' 2 ', fg='#fff', background='#666', command=lambda: press(2), font=button_font)
btn2.grid(row=3, column=1, sticky='nswe')

btn3 = tk.Button(root, text=' 3 ', fg='#fff', background='#666', command=lambda: press(3), font=button_font)
btn3.grid(row=3, column=2, sticky='nswe')

btn0 = tk.Button(root, text=' 0 ', fg='#fff', background='#666' , command=lambda: press(0), font=button_font)
btn0.grid(row=4, column=0, sticky='nswe', columnspan=2)

decimal = tk.Button(root, text=' . ', fg='#fff', background='#666', command=lambda: press('.'), anchor='center', font=button_font) # se pasa entre comillas para que lo tome como un string 
decimal.grid(row=4, column=2, sticky='nswe') #columnspan=2

plus = tk.Button(root, text=' + ', fg='#fff', background='#fe9727', command=lambda: press('+'), font=button_font)
plus.grid(row=1, column=3, sticky='nswe')

minus = tk.Button(root, text=' - ', fg='#fff', background='#fe9727', command=lambda: press('-'), font=button_font)
minus.grid(row=2, column=3, sticky='nswe')

multiply = tk.Button(root, text=' * ', fg='#fff', background='#fe9727', command=lambda: press('*'), font=button_font)
multiply.grid(row=3, column=3, sticky='nswe')

divide = tk.Button(root, text=' / ', fg='#fff', background='#fe9727', command=lambda: press('/'), font=button_font)
divide.grid(row=4, column=3, sticky='nswe')

equal = tk.Button(root, text=' = ', fg='#fff', background='#fe9727', command=equalpress, font=button_font)
equal.grid(row=5, column=3, sticky='nswe')

clear = tk.Button(root, text=' Clear ', fg='#fff', background='#999', command=clear, font=button_font)
clear.grid(row=5, column=2, sticky='nswe')

exit_button = tk.Button(root, text='Salir', fg='#fff', background='#999', command=root.quit, font=button_font)
exit_button.grid(row=5, column=0, sticky='nswe', columnspan=2)


root.mainloop()