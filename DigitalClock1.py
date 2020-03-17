# デジタル時計

from datetime import datetime
import tkinter


def clock(window, size, fg, bg):
    canvas = tkinter.Canvas(window, width=size*2, height=size, background=bg)  # ウィンドウ(キャンバス)を作成
    canvas.pack()


    # 時間を表示するための関数
    def draw_time(time):
        x, y = size, size / 2
        font = ('', int(size/3))
        text = '{0:0>2d}:{1:0>2d}:{2:0>2d}'.format(time.hour, time.minute, time.second)
        canvas.delete('T')
        canvas.create_text(x, y, text=text, fill=fg, font=font, tag='T')
        canvas.update()

    
    # 現在の時刻を取得し、draw_time()を呼び出し
    def draw():
        now = datetime.now()
        draw_time(now)


    return draw


def main():
    root = tkinter.Tk()
    root.title('DigitalClock')
    draw_clock = clock(root, size=200, fg='#ffffff', bg='#000000')
    def update():
        try:
            draw_clock()
            root.after(100, update)  # after(<間隔>, <実行する関数>)　間隔はミリ秒(1/1000秒)で入力
        except KeyboardInterrupt:
            root.destroy()

    update()
    root.mainloop()


if __name__ == '__main__':
    main()


