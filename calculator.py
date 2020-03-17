import tkinter
from tkinter import Button


# 画面を表示
root = tkinter.Tk()


# ウィンドウの名前
root.title('簡易電卓')


# 表示画面
val = tkinter.StringVar()
label = tkinter.Label(root, textvariable=val, fg='#ffffff', bg='#000000', anchor='e', height=4, font=('', 20))
label.grid(row=0, column=0, columnspan=4, sticky='EW')


# 文字の入力
def func(v):
    val.set(val.get() + v)


# Cの機能
def clear():
    value = val.get()
    if value == 'SyntaxError' or value == 'NameError' or value == 'ZeroDivisionError':
        value = ''
    value = value[:-1]
    val.set(value)


# ACの機能
def all_clear():
    val.set('')
    

# =の機能
def result():
    try:
        value = val.get()
        value = value.replace('÷', '/')
        value = value.replace('×', '*')
        val.set(eval(value))  # evalは第一引数を式として認識する
    except SyntaxError:
        val.set('SyntaxError')
    except NameError:
        val.set('NameError')
    except ZeroDivisionError:
        val.set('ZeroDivisionError')


# 1行目
btn_ac = Button(root, text='AC', command=all_clear, width=10, height=4)
btn_ac.grid(row=1, column=0)
btn_7 = Button(root, text='7', command=lambda: func('7'), width=10, height=4)
btn_7.grid(row=2, column=0)
btn_4 = Button(root, text='4', command=lambda: func('4'), width=10, height=4)
btn_4.grid(row=3, column=0)
btn_1 = Button(root, text='1', command=lambda: func('1'), width=10, height=4)
btn_1.grid(row=4, column=0)
btn_0 = Button(root, text='0', command=lambda: func('0'), width=10, height=4)
btn_0.grid(row=5, column=0)


# 2行目
btn_c = Button(root, text='C', command=clear, width=10, height=4)
btn_c.grid(row=1, column=1)
btn_8 = Button(root, text='8', command=lambda: func('8'), width=10, height=4)
btn_8.grid(row=2, column=1)
btn_5 = Button(root, text='5', command=lambda: func('5'), width=10, height=4)
btn_5.grid(row=3, column=1)
btn_2 = Button(root, text='2', command=lambda: func('2'), width=10, height=4)
btn_2.grid(row=4, column=1)
btn_00 = Button(root, text='00', command=lambda: func('00'), width=10, height=4)
btn_00.grid(row=5, column=1)


# 3行目
btn_power = Button(root, text='^', command=lambda: func('^'), width=10, height=4)
btn_power.grid(row=1, column=2)
btn_9 = Button(root, text='9', command=lambda: func('9'), width=10, height=4)
btn_9.grid(row=2, column=2)
btn_6 = Button(root, text='6', command=lambda: func('6'), width=10, height=4)
btn_6.grid(row=3, column=2)
btn_3 = Button(root, text='3', command=lambda: func('3'), width=10, height=4)
btn_3.grid(row=4, column=2)
btn_pt = Button(root, text='.', command=lambda: func('.'), width=10, height=4)
btn_pt.grid(row=5, column=2)



#4行目
btn_div = Button(root, text='÷', command=lambda: func('÷'), width=10, height=4)
btn_div.grid(row=1, column=3)
btn_mul = Button(root, text='×', command=lambda: func('×'), width=10, height=4)
btn_mul.grid(row=2, column=3)
btn_sub = Button(root, text='-', command=lambda: func('-'), width=10, height=4)
btn_sub.grid(row=3, column=3)
btn_add = Button(root, text='+', command=lambda: func('+'), width=10, height=4)
btn_add.grid(row=4, column=3)
btn_eq = Button(root, text='=', command=result, width=10, height=4)
btn_eq.grid(row=5, column=3)


root.mainloop()