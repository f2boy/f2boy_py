import random
import threading
import time
from tkinter import *

WIDTH = 20
LENGTH = 12

LIVE = '#'
DEAD = '-'

# 初始化数据
myList = [([DEAD] * (WIDTH + 2)) for i in range(LENGTH + 2)]
for i in range(1, LENGTH + 1):
    for j in range(1, WIDTH + 1):
        if random.randint(0, 4) == 0:
            myList[i][j] = LIVE


# 计算下一刻的状态
def cal():
    for i in range(1, LENGTH + 1):
        for j in range(1, WIDTH + 1):
            live_no = 0
            if myList[i][j - 1] == LIVE:
                live_no += 1
            if myList[i][j + 1] == LIVE:
                live_no += 1
            if myList[i - 1][j - 1] == LIVE:
                live_no += 1
            if myList[i - 1][j] == LIVE:
                live_no += 1
            if myList[i - 1][j + 1] == LIVE:
                live_no += 1
            if myList[i + 1][j - 1] == LIVE:
                live_no += 1
            if myList[i + 1][j] == LIVE:
                live_no += 1
            if myList[i + 1][j + 1] == LIVE:
                live_no += 1

            if myList[i][j] == LIVE:
                if live_no != 2 and live_no != 3:
                    myList[i][j] = DEAD

            if myList[i][j] == DEAD:
                if live_no == 3:
                    myList[i][j] = LIVE


def confLabel():
    s = ''
    for i in range(1, LENGTH + 1):
        for j in range(1, WIDTH + 1):
            s += myList[i][j]
        s += '\n'
    lb.config(text=s)


class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while 1:
            time.sleep(0.5)
            cal()
            confLabel()


root = Tk()

lb = Label(root, font=("黑体", 8, "bold"))
confLabel()
lb.pack()

MyThread().start()
mainloop()
