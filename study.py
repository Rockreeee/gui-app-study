import time
import threading
import random
import tkinter as tk
import math
import copy

import date

randomNumber = int
book = date.book

class GUI(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.value = 0

    def start(self):
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True) # サイズ
        self.root['bg'] = 'black'
        # StringVarをフィールドに定義する
        self.sv1 = tk.StringVar()
        self.sv2 = tk.StringVar()
        # ラベルの表示 データはStringVarをバインドする
        self.englishLabel = tk.Label(self.root, textvariable=self.sv1, font=(u'Times New Roman', 220), fg="gray", bg='black')
        self.englishLabel.place(relwidth=1.0, rely=0, relheight=0.6)
        self.japaneseLabel = tk.Label(self.root, textvariable=self.sv2, font=('游明朝', 130), fg="gray", bg='black')
        self.japaneseLabel.place(relwidth=1.0, rely=0.6, relheight=0.4)
        #キーイベント
        self.root.bind('<Escape>', self.quit)
        self.root.bind('<space>', self.yes)
        self.root.bind('<Return>', self.tab)

        self.change_value_callback()
        self.root.mainloop()

    # change_valueを別スレッドで実行するコールバック
    def change_value_callback(self):
        th = threading.Thread(target=self.change_value, args=(),daemon=True)
        th.start()

    # StringVarを更新するように変更する
    def change_value(self):
        global randomNumber
        global book
        try:
            while True:
                # StringVarを変更するとGUIスレッドでラベル文字列が更新される
                randomNumber = random.randint(0, len(book) - 1)
                BOOK=copy.copy(book)
                self.sv1.set(BOOK[randomNumber][0])
                self.sv2.set("")
                time.sleep(3)
                self.sv2.set(BOOK[randomNumber][1])
                time.sleep(2)
        except IndexError:
            print('---------err---------')
            self.change_value()
        except ValueError:
            print('---------finish---------')
            self.quit()

    def yes(self, event=None):
        global book
        print('learn word :%s' %book[randomNumber][0])
        book.pop(randomNumber)

    def quit(self, event=None):
        global book
        print('---------Not Learn Words-----------')
        print(book)
        self.root.destroy()

    def tab(self, event=None):
        self.root.attributes('-fullscreen', False)

if __name__ == '__main__':
    gui = GUI()
    gui.start()