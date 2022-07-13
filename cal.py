from tkinter import Tk, E, W, END, messagebox
from tkinter.ttk import Label, Button, Entry, Style

# nums collects entered numbers in box
nums = []
# op collect required operator
operator = ''

def calculating(ent_operator):
    global nums, operator
    try:
        nums.append(float(ent_exp.get()))
        operator = ent_operator
    except ValueError:
        messagebox.showerror('Invalid input', 'You may forgot to fill the box, or did not enter a number!')
    else:
        lbl_ans['text'] = str(nums[0]) + ' ' + operator
        lbl_ans.grid(
            row=0,
            column=0,
        )

        ent_exp.delete(0, END)

        if len(nums) == 2:
            if operator == '+':
                res = nums[0] + nums[1]
                nums.clear()
                lbl_ans['text'] = res
                lbl_ans.grid(
                    row=0,
                    column=0,
                )


win_cal = Tk()
win_cal.title('Calculater')
win_cal.config(bg='#3F4E4F')

lbl_ans = Label(
    master=win_cal,
    text='ans',
    background='#3F4E4F',
    foreground='white',
    font=('Arial', 14)
)
lbl_ans.grid(
    row=0,
    column=0,
)

ent_exp = Entry(
    master=win_cal,
    justify='center',
    font=('Helvetica', 12),
)
ent_exp.grid(
    row=1,
    column=0,
    columnspan=4,
    sticky=(W,E)
)

# designe buttons
style = Style()
style.theme_use('alt')
style.configure('TButton', background = '#2C3639', foreground = 'white', width = 10, borderwidth=2, focusthickness=3, focuscolor='none')
style.configure('TButton', font=('Helvetica', 14))
style.map('TButton', background=[('active','gray')]) 

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

btn_percent = Button(
    master=win_cal,
    text='%',
)
btn_percent.grid(
    row=2,
    column=0,
    ipady=10,
)


btn_erase = Button(
    master=win_cal,
    text='🔙'
)
btn_erase.grid(
    row=2,
    column=3,
    ipady=10,
)

btn_CE = Button(
    master=win_cal,
    text='CE',
)
btn_CE.grid(
    row=2,
    column=1,
    ipady=10,
)

btn_C = Button(
    master=win_cal,
    text='C',
)
btn_C.grid(
    row=2,
    column=2,
    ipady=10,
)

btn_reverse = Button(
    master=win_cal,
    text='1/x',
)
btn_reverse.grid(
    row=3,
    column=0,
    ipady=10,
)

btn_square = Button(
    master=win_cal,
    text=f'{"x"}\u00b2',
)
btn_square.grid(
    row=3,
    column=1,
    ipady=10,
)
btn_rad = Button(
    master=win_cal,
    text='√x'
)
btn_rad.grid(
    row=3,
    column=2,
    ipady=10,
)

btn_div = Button(
    master=win_cal,
    text='÷',
)
btn_div.grid(
    row=3,
    column=3,
    ipady=10,
)

btn_mul = Button(
    master=win_cal,
    text='×'
)
btn_mul.grid(
    row=4,
    column=3,
    ipady=10,
)

btn_min = Button(
    master=win_cal,
    text='-',
)
btn_min.grid(
    row=5,
    column=3,
    ipady=10,
)

btn_plus = Button(
    master=win_cal,
    text='+',
    command=lambda: calculating('+')
)
btn_plus.grid(
    row=6,
    column=3,
    ipady=10,
)

btn_eq = Button(
    master=win_cal,
    text='=',
    command=lambda: calculating(operator)
)
win_cal.bind('<Return>', lambda *args: calculating(operator))
btn_eq.grid(
    row=7,
    column=3,
    ipady=10,
)

btn_cross10 = Button(
    master=win_cal,
    text='×10',
)
btn_cross10.grid(
    row=7,
    column=0,
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

win_cal.mainloop()