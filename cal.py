from math import sqrt
from tkinter import Tk, E, W, END, messagebox
from tkinter.ttk import Label, Button, Entry, Style

from click import command

# nums collects entered numbers in entry box
nums = []
# operator collect required operator
operator = ''

def calculating_main_four(ent_operator):
    """Calculates plus, minuse, multiplication and division"""
    global nums, operator

    try:
        nums.append(float(ent_exp.get()))
        if ent_operator != '=': operator = ent_operator
    except ValueError:
        if ent_exp.get() == '' and lbl_ans['text'] != 'Ans':
            try:
                nums.append(float(lbl_ans['text']))
            except ValueError:
                messagebox.showerror('Invalid input', 'You may forgot to fill the box, or did not enter a number!')
            else:
                if ent_operator != '=': operator = ent_operator
                lbl_ans['text'] = str(lbl_ans['text']) + ' ' + operator
                lbl_ans.grid(
                    row=0,
                    column=0,
                )
        else:
            messagebox.showerror('Invalid input', 'You may forgot to fill the box, or did not enter a number!')
    else:
        if len(nums) == 1:    
            lbl_ans['text'] = str(nums[0]) + ' ' + operator
            lbl_ans.grid(
                row=0,
                column=0,
            )
        ent_exp.delete(0, END)

        if len(nums) >= 2:
            if '*' == operator:
                res = nums[0] * nums[1]
                nums.clear()
                operator = ''
                lbl_ans['text'] = res
                lbl_ans.grid(
                    row=0,
                    column=0,
                )
            if '+' == operator:
                res = nums[0] + nums[1]
                nums.clear()
                operator = ''
                lbl_ans['text'] = res
                lbl_ans.grid(
                    row=0,
                    column=0,
                )
            if '-' == operator:
                res = nums[0] - nums[1]
                nums.clear()
                operator = ''
                lbl_ans['text'] = res
                lbl_ans.grid(
                    row=0,
                    column=0,
                )
            if '÷' == operator:
                try:
                    res = nums[0] / nums[1]
                except ZeroDivisionError as e:
                    messagebox.showerror('Division by zero', e)
                    nums.clear()
                else:
                    nums.clear()
                    operator = ''
                    lbl_ans['text'] = res
                    lbl_ans.grid(
                        row=0,
                        column=0,
                    )

def square():
    """Calculates square of the number"""
    global nums

    try:
        nums.append(float(ent_exp.get()))
    except ValueError:
        if ent_exp.get() == '' and lbl_ans['text'] != 'Ans':
            nums.append(float(lbl_ans['text']))
            try:
                lbl_ans['text'] = nums[0] ** 2
            except OverflowError as e:
                messagebox.showerror('Overflow', e)
                nums.clear()
                ent_exp.delete(0, END)
            else:
                lbl_ans.grid(
                    row=0,
                    column=0,
                )
                nums.clear()
                ent_exp.delete(0, END)
        else:
            messagebox.showerror('Invalid input', 'You may forgot to fill the box, or did not enter a number!')
    else:
        try:
            res = nums[0] ** 2
        except OverflowError as e:
            messagebox.showerror('Overflow', e)
            nums.clear()
            ent_exp.delete(0, END)
        else:
            lbl_ans['text'] = res
            lbl_ans.grid(
                row=0,
                column=0,
            )
            nums.clear()
            ent_exp.delete(0, END)

def reverse():
    """1/x : Reverse the number"""
    global nums

    try:
        nums.append(float(ent_exp.get()))
    except ValueError:
        if ent_exp.get() == '' and lbl_ans['text'] != 'Ans':
            nums.append(float(lbl_ans['text']))
            try:
                lbl_ans['text'] = 1/nums[0]
            except ZeroDivisionError as e:
                messagebox.showerror('Division by zero', e)
                nums.clear()
                ent_exp.delete(0, END)
            else:
                lbl_ans.grid(
                    row=0,
                    column=0,
                )
                nums.clear()
                ent_exp.delete(0, END)
        else:
            messagebox.showerror('Invalid input', 'You may forgot to fill the box, or did not enter a number!')
    else:
        try:
            res = 1/nums[0]
        except ZeroDivisionError as e:
            messagebox.showerror('Division by zero', e)
            nums.clear()
            ent_exp.delete(0, END)
        else:
            lbl_ans['text'] = res
            lbl_ans.grid(
                row=0,
                column=0,
            )
            nums.clear()
            ent_exp.delete(0, END)

def radical():
    """Calculates square root of the number"""
    global nums

    try:
        nums.append(float(ent_exp.get()))
    except ValueError:
        if ent_exp.get() == '' and lbl_ans['text'] != 'Ans':
            nums.append(float(lbl_ans['text']))
            try:
                lbl_ans['text'] = sqrt(nums[0])
            except Exception as e:
                messagebox.showerror('Square root of negative number', e)
                nums.clear()
                ent_exp.delete(0, END)
            else:
                lbl_ans.grid(
                    row=0,
                    column=0,
                )
                nums.clear()
                ent_exp.delete(0, END)
        else:
            messagebox.showerror('Invalid input', 'You may forgot to fill the box, or did not enter a number!')
    else:
        try:
            res = sqrt(nums[0])
        except Exception as e:
            messagebox.showerror('Square root of negative number', e)
            nums.clear()
            ent_exp.delete(0, END)
        else:
            lbl_ans['text'] = res
            lbl_ans.grid(
                row=0,
                column=0,
            )
            nums.clear()
            ent_exp.delete(0, END)

win_cal = Tk()
win_cal.title('Calculater')
win_cal.config(bg='#3F4E4F')

lbl_ans = Label(
    master=win_cal,
    text='Ans',
    background='#3F4E4F',
    foreground='white',
    font=('Arial', 16),
)
lbl_ans.grid(
    row=0,
    column=0,
    columnspan=4,
    pady=5,
)

ent_exp = Entry(
    master=win_cal,
    justify='center',
    font=('Helvetica', 20),
)
ent_exp.grid(
    row=1,
    column=0,
    columnspan=4,
    sticky=(W,E),
    pady=(0,5)
)

about_style = Style()
about_style.theme_use('alt')
about_style.configure('a.TButton', background = '#47B5FF', foreground = '#06283D',  borderwidth=5, focusthickness=3, focuscolor='none')
about_style.map('a.TButton', background=[('active','#D6D5A8')])

btn_about = Button(
    master=win_cal,
    text='About',
    style='a.TButton',
    command=lambda: messagebox.showinfo('About',
                                        'This is a simple calculater developed by Erfan Arefmehr. \
                                        Wait for the scientific version!'),
)
btn_about.grid(
    row=7,
    column=0,
    ipady=10,
)


# designe buttons
style = Style()
style.theme_use('alt')
style.configure('TButton', background = '#1B2430', foreground = 'white', width = 10, borderwidth=5, focusthickness=3, focuscolor='none')
style.configure('TButton', font=('Helvetica', 14))
style.map('TButton', background=[('active','#D6D5A8')]) 

# create number buttons from 0 to 9
buttons_list = [
    Button(
        master=win_cal,
        text=n,
        command=lambda c=n: ent_exp.insert(20, buttons_list[9-c].cget("text"))
    )
    for n in range(10)
]
buttons_list.reverse()

# rows start from i and columns start from j
i=4
j=3

# arrange number buttons in 6 rows and 3 columns
for button in buttons_list:
    j -= 1
    if j == -1:
        i += 1
        j=2
    if buttons_list[-1] == button:
        j=1
    style = Style
    button.grid(
        row=i,
        column=j,
        ipady=10,
    )

btn_pi = Button(
    master=win_cal,
    text='𝝅',
    command=lambda: ent_exp.insert(0, '3.14')
)
btn_pi.grid(
    row=2,
    column=0,
    ipady=10,
)

erase_style = Style()
erase_style.theme_use('alt')
erase_style.configure('W.TButton', background = 'red', foreground = 'white',  borderwidth=5, focusthickness=3, focuscolor='none')
erase_style.map('W.TButton', background=[('active','#D6D5A8')])

btn_erase = Button(
    master=win_cal,
    text='🔙',
    style='W.TButton',
    command=lambda: ent_exp.delete(len(ent_exp.get())-1, END),
)
win_cal.bind('<BackSpace>', lambda *args: ent_exp.delete(len(ent_exp.get())-1, END))
btn_erase.grid(
    row=2,
    column=3,
    ipady=10,
)

btn_CE = Button(
    master=win_cal,
    text='CE',
    command=lambda: ent_exp.delete(0, END),
)
btn_CE.grid(
    row=2,
    column=1,
    ipady=10,
)

def btn_C_func():
    ent_exp.delete(0, END)
    lbl_ans['text'] = 'Ans'
    lbl_ans.grid(
        row=0,
        column=0,
    )


btn_C = Button(
    master=win_cal,
    text='C',
    command=btn_C_func
)
btn_C.grid(
    row=2,
    column=2,
    ipady=10,
)

btn_reverse = Button(
    master=win_cal,
    text='1/x',
    command=reverse,
)
btn_reverse.grid(
    row=3,
    column=0,
    ipady=10,
)

btn_square = Button(
    master=win_cal,
    text=f'{"x"}\u00b2',
    command=square
)
btn_square.grid(
    row=3,
    column=1,
    ipady=10,
)
btn_rad = Button(
    master=win_cal,
    text='√x',
    command=radical,
)
btn_rad.grid(
    row=3,
    column=2,
    ipady=10,
)

btn_div = Button(
    master=win_cal,
    text='÷',
    command=lambda: calculating_main_four('÷'),

)
btn_div.grid(
    row=3,
    column=3,
    ipady=10,
)

btn_mul = Button(
    master=win_cal,
    text='×',
    command=lambda: calculating_main_four('*'),
)
btn_mul.grid(
    row=4,
    column=3,
    ipady=10,
)

btn_min = Button(
    master=win_cal,
    text='-',
    command=lambda: calculating_main_four('-')
)
btn_min.grid(
    row=5,
    column=3,
    ipady=10,
)

btn_plus = Button(
    master=win_cal,
    text='+',
    command=lambda: calculating_main_four('+')
)
btn_plus.grid(
    row=6,
    column=3,
    ipady=10,
)

eq_style = Style()
eq_style.theme_use('alt')
eq_style.configure('eq.TButton', background = '#1B2430', foreground = 'white', width = 10, borderwidth=5, focusthickness=3, focuscolor='none')
eq_style.configure('eq.TButton', font=('Helvetica', 14))
eq_style.map('eq.TButton', background=[('active','green')])

btn_eq = Button(
    master=win_cal,
    text='=',
    style='eq.TButton',
    command=lambda: calculating_main_four('='),
)
win_cal.bind('<Return>', lambda *args: calculating_main_four('='))
btn_eq.grid(
    row=7,
    column=3,
    ipady=10,
)

btn_dot = Button(
    master=win_cal,
    text='.',
    command=lambda: ent_exp.insert(30, btn_dot.cget('text'))
)
btn_dot.grid(
    row=7,
    column=2,
    ipady=10,
)

win_cal.bind('<Escape>', lambda *args: win_cal.destroy())
win_cal.mainloop()