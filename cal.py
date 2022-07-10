from tkinter import Tk, E, W
from tkinter.ttk import Label, Button, Entry, Style

win_cal = Tk()
win_cal.title('Calculater')
win_cal.config(bg='#231955')

lbl_ans = Label(
    master=win_cal,
    text='ans',
    background='#231955',
    foreground='#F9F9C5',
    font=('Arial', 12)
)
lbl_ans.grid(
    row=0,
    column=0,
)

ent_exp = Entry(
    master=win_cal,
    justify='center',
)
ent_exp.grid(
    row=1,
    column=0,
    columnspan=4,
    sticky=(W,E)
)

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
# arrange buttons in 6 rows and 3 columns
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
    )

btn_cross10 = Button(
    master=win_cal,
    text='*10',
)
btn_cross10.grid(
    row=7,
    column=0,
)

btn_dot = Button(
    master=win_cal,
    text='.',
)
btn_dot.grid(
    row=7,
    column=2,
)

win_cal.mainloop()