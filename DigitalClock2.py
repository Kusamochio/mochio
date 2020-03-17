# デジタル時計

from datetime import datetime
import tkinter
import time


root = tkinter.Tk()
root.title('DigitalClock')

canvas = tkinter.Canvas(root, width=400, height=200, background='#000000')
canvas.pack()


try:
    while True:
        now = datetime.now()
        text = '{0:0>2d}:{1:0>2d}:{2:0>2d}'.format(now.hour, now.minute, now.second)

        canvas.create_rectangle(0, 0, 400, 200, outline='#000000', fill='#000000')
        canvas.create_text(200, 100, text=text, fill='#ffffff', font=('', 70))
        canvas.update()
        time.sleep(0.1)
except:
    pass       