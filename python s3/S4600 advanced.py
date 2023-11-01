# Opgave:
# Skab denne liste med comprehension: [10, 15, 20, 25, 30, 35]
# Skriv din kode her

# dictionary_comprehension = {i: i * i for i in range(3)}
# list_comprehension = [10 + i * 5 for i in range(6)]
# set_comprehension = {i%5 for i in range(10)}
# generator_comprehension = (2 * i + 5 for i in range(10))
# print(f'{dictionary_comprehension = }')
# print(f'{list_comprehension = }')
# print(f'{set_comprehension = }')
# print(f'{generator_comprehension = }')

# list_comprehension = [i if i < 4 else 40 + (i - 4) for i in range(10)]
# print(f'{list_comprehension = }')

# # Opgave:
# # Skab denne dictionary med comprehension: {3: 33, 4: 44, 5: 55, 6: 66}
# dictionary_comprehension = {i: 11 * i for i in range(3, 7)}
# print(f'{dictionary_comprehension = }')
# # Skriv din kode her

# import random
#
# # Funktion der returnerer et tilfældigt tal mellem 1 og 10
# def random_number():
#     return random.randint(1, 100)
#
# # Funktion der udskriver en besked baseret på input
# def print_message(message):
#     print(f"Besked: {message}")
#
# # Funktion der tjekker om et tal er lige eller ulige
# def even_or_odd(num):
#     if num % 2 == 0:
#         return "Lige"
#     else:
#         return "Ulige"
#
# # Funktion der finder det største af tre tal
# def find_largest(a, b, c):
#     largest = max(a, b, c)
#     return largest
#
# # Simpelt program der bruger tidligere funktioner
# def main.py():
#     num = random_number()
#     print_message("Dette er en tilfældig besked.")
#     print(f"Det tilfældige tal er: {num}")
#     print(f"Tallet er {even_or_odd(num)}.")
#
#     a, b, c = 12, 8, 15
#     print(f"Af tallene {a}, {b}, og {c}, er det største: {find_largest(a, b, c)}")
#
# # Kør programmet
# if __name__ == "__main__":
#     main.py()
#
#
# nr = 7
# plus = nr.__add__(18)
# print(plus)

# Opgave:
# # Add a magic function to the Dog class so that "huge_dog > tiny_dog" is interpreted in a sensible way.
#
# class Dog:
#     def __init__(self, size):
#         self.size = size
#
#     def __gt__(self, other):
#         return self.size > other.size
#
#
#
# huge_dog = Dog(80)
# tiny_dog = Dog(25)
#
# # Uncomment this in order to test your solution!
# if huge_dog > tiny_dog:
#     print("Du løste opgaven! :)")

# def some_function():
#     return 1, 2, 3, 4, 5, 6, 7, 8
#
# result, result1, result2, *result3, result4, result5 = some_function()
# print(result3)

# concatenate_keys.py
# def concatenate(**kwargs):
#     result = ""
#     # Iterating over the keys of the Python kwargs dictionary
#     for arg in kwargs:
#         result += arg
#     return result
#
# print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!")

# def concatenate_keys(**kwargs):
#     result = "          "
#     # Iterating over the keys of the Python kwargs dictionary
#     for arg in kwargs:
#         result += arg
#     return result
#
# print(concatenate_keys(a="Real", b="Python", c="Is", d="Great", e="!"))
#
# exempel = ("abcdef")
# exempel_tuple = ("abcdef",)
# for s in exempel:
#     print("String: ", s)
# for t in exempel_tuple:
#     print("Tuple: ", t)

# for i, j, k, l, m, in zip(range(1, 23), "abcde", ["one", "two", "three", "four", "five"], ["six", "seven", "eight", "nine", "ten", "eleven"], [11, 12, 13, 14, 15]):
# #     print(i, j, k, l, m, end="   ")

# def lamba_function(n):
#     return lambda x: x ** n
#
# square = lamba_function(2)
# triple = lamba_function(3)
#
# print(square(5))
# print(triple(5))

# class Dummy:
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __repr__(self):
#         return f"{self.a=}  {self.b=}"
#
# dummy1 = Dummy(5, 1)
# dummy2 = Dummy(2, 4)
# dummies = [dummy1, dummy2]
# print("before", dummies)
# dummies.sort(key=lambda x: x.a, reverse=False)
# print("after", dummies)

# fullybfgfgererfe functional calculator gui

# # Program to demonstrate conditional operator
# a, b, c = 1, 2, 3
#
# min = a if a < b elif b < c else c
# print(min)
#
# max = a if a > b else b
# print(max)

# def get_verdi():
#     yield "Ord1"
#     yield "Ord2"
#     yield 123
#
# def exempel_get_verdi():
#     gen = get_verdi()
#     # print(gen)
#     print(next(gen))
#
# exempel_get_verdi()

# def get_verdi():
#     yield "Ord1"
#     yield "Ord2"
#     yield 123
#
# def exempel_get_verdi():
#     for x in get_verdi():
#         print(x)

# exempel_get_verdi()

# import itertools
#
# class Generator:
#     def __init__(self, stop: str):
#         self.start = "Ord1"
#         self.stop = stop
#
#     def __iter__(self) -> Iterator[str]:
#         curr = ord(self.start)
#         stop_ord = ord(self.stop)
#         while curr <= stop_ord:
#             yield "Ord" + str(curr - ord('O') + 1)
#             curr += 1
#
# def range_example():
#     for char in Generator('Ord7'):
#         print(char)
#         if char == 'Ord6':
#             break
#
# range_example()

# from typing import Iterator
#
#
# Test = "testing"
#
#
# class Generator:
#     def __init__(self, stop: int):
#         self.start = 0
#         self.stop = stop
#
#     def __iter__(self) -> Iterator[int]:
#         curr = self.start
#         while curr < self.stop:
#             yield curr
#             curr += 1
#
# def range_example():
#     for n in Generator(5):
#         print(n)
#         if n == 3:
#             break
#
# print(Test, range_example())


# import csv as csv_reader
#
# csv_gen = csv_reader("some_csv.txt")
# row_count = 0
#
# for row in csv_gen:
#     row_count += 1
#
# print(f"Row count is {row_count}")
#
# def infinite_sequence():
#     num = 0
#     while True:
#         yield num
#         num += 1
#
# gen = infinite_sequence()
# print(next(gen))
# print(next(gen))
# for some_iterator in [3, 12, 4]:
#     print("in a for loop", next(gen))

#Asyncio python test
# import time
# import asyncio
#
#
#
# async def do_work(s: str, delay_s: float = 1.0):
#     print(f"{s} started")
#     await asyncio.sleep(delay_s)
#     print(f"{s} Færdiggjort")
#
#
# from multiprocessing import Pool
#
# def f(x):
#     return x*x
#
#
# if __name__ == '__main__':
#     with Pool(2) as p:
#         print(p.map(f, [1, 3, 5]))

# from multiprocessing import Process
# import os
#
# def info(title):
#     print(title)
#     print('module name:', __name__)
#     print('parent process:', os.getppid())
#     print('process id:', os.getpid())
#
# def f(name):
#     info('function f')
#     print('hello', name)
#
# if __name__ == '__main__':
#     info('main.py line')
#     p = Process(target=f, args=('bob',))
#     p.start()
#     p.join()

# import multiprocessing as mp
#
# def foo(q):
#     q.put('Hej')
#
# if __name__ == '__main__':
#     ctx = mp.get_context('spawn')
#     q = ctx.Queue()
#     p = ctx.Process(target=foo, args=(q,))
#     p.start()
#     print(q.get())
#     p.join()

# from multiprocessing import Process, Queue
#
# def f(q):
#     q.put([42, None, 'hello'])
#
# if __name__ == '__main__':
#     q = Queue()
#     p = Process(target=f, args=(q,))
#     p.start()
#     print(q.get())    # prints "[42, None, 'hello']"
#     p.join()

# from multiprocessing import Process, Lock
#
# def f(l, i):
#     l.acquire()
#     try:
#         print('hello world', i)
#     finally:
#         l.release()
#
# if __name__ == '__main__':
#     lock = Lock()
#
#     for num in range(10):
#         Process(target=f, args=(lock, num)).start()
# from multiprocessing import Process, Lock
#
# def f(l, i):
#     l.acquire()
#     try:
#         print('Bruger nr:', i, "Scannet for trusler")
#     finally:
#         l.release()
#
# if __name__ == '__main__':
#     lock = Lock()
#
#     for num in range(100):
#         Process(target=f, args=(lock, num)).start()

# from multiprocessing import Pool, TimeoutError
# import time
# import os
#
# def f(x):
#     return x*x
#
# if __name__ == '__main__':
#     # start 4 worker processes
#     with Pool(processes=4) as pool:
#
#         # print "[0, 1, 4,..., 81]"
#         print(pool.map(f, range(10)))
#
#         # print same numbers in arbitrary order
#         for i in pool.imap_unordered(f, range(10)):
#             print(i)
#
#         # evaluate "f(20)" asynchronously
#         res = pool.apply_async(f, (20,))      # runs in *only* one process
#         print(res.get(timeout=1))             # prints "400"
#
#         # evaluate "os.getpid()" asynchronously
#         res = pool.apply_async(os.getpid, ()) # runs in *only* one process
#         print(res.get(timeout=1))             # prints the PID of that process
#
#         # launching multiple evaluations asynchronously *may* use more processes
#         multiple_results = [pool.apply_async(os.getpid, ()) for i in range(4)]
#         print([res.get(timeout=1) for res in multiple_results])
#
#         # make a single worker sleep for 10 seconds
#         res = pool.apply_async(time.sleep, (10,))
#         try:
#             print(res.get(timeout=1))
#         except TimeoutError:
#             print("We lacked patience and got a multiprocessing.TimeoutError")
#
#         print("For the moment, the pool remains available for more work")
#
#     # exiting the 'with'-block has stopped the pool
# #     print("Now the pool is closed and no longer available")
# #
# import time
#
# def f(t0, array):
#     t_offest = time.time() - t0
#     dt = array[1, 0] - array[0, 0]
#     while True:
#         t = time.perf_counter_ns() - t_offest*1E9
#         i = int(t/dt)
#         if i >= len(array):
#             break
#         array[i, 1] += 1
#     return array
#
# for i in range(nprocesses):
#     inarrays.append(np.copy(array))
#
# p = Pool(processes=nthreads)
# t0 = time.time()
# outarrays = p.starmap(f, [(t0, array)
#                             for array in inarrays], chunksize=1)
#
# import os
# current_dir = os.getcwd()  # What is the program's current directory?
# current_dir

# from PIL import Image
# img = Image.open("../Python s2/DKEMPIRE.jpg")
# img.show()

# from PIL import Image
#
# # Load the image
# img = Image.open("../Python s2/DKEMPIRE.jpg")
#
# # Convert the image to grayscale
# img_gray = img.convert('L')
#
# # Define ASCII characters for different pixel intensity levels
# ascii_chars = "@%#*+=-:. "
#
# # Resize the image (to reduce the size of ASCII representation)
# width, height = img_gray.size
# aspect_ratio = height/width
# new_width = 100
# new_height = int(aspect_ratio * new_width * 0.55)
# resized_img = img_gray.resize((new_width, new_height))
#
# # Generate ASCII representation
# ascii_img = ""
# pixels = resized_img.load()
# for i in range(new_height):
#     for j in range(new_width):
#         pixel_value = pixels[j, i]
#         ascii_img += ascii_chars[pixel_value // 25]
#     ascii_img += '\n'
#
# print(ascii_img)
#
# from IPython.display import Image
# Image(filename="../Python s2/DKEMPIRE.jpg")


# import sys
# from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget, QLabel
# from PyQt5.QtCore import QTimer
# import PyQt5.QtGui
# import datetime
#
# # Oversættelse af dage og måneder
# oversaettelse = {
#     "Mon": "Mandag",
#     "Tue": "Tirsdag",
#     "Wed": "Onsdag",
#     "Thu": "Torsdag",
#     "Fri": "Fredag",
#     "Sat": "Lørdag",
#     "Sun": "Søndag",
#     "Jan": "Januar",
#     "Feb": "Februar",
#     "Mar": "Marts",
#     "Apr": "April",
#     "May": "Maj",
#     "Jun": "Juni",
#     "Jul": "Juli",
#     "Aug": "August",
#     "Sep": "September",
#     "Oct": "Oktober",
#     "Nov": "November",
#     "Dec": "December"
# }
#
# def oversaet_dag(dag):
#     return oversaettelse.get(dag, "Ukendt")
#
# def oversaet_maaned(maaned):
#     return oversaettelse.get(maaned, "Ukendt")
#
# def vis_dato_og_tid():
#     x = datetime.datetime.now()
#     oversat_dag = oversaet_dag(x.strftime("%a"))
#     oversat_maaned = oversaet_maaned(x.strftime("%b"))
#     formateret_dato_og_tid = f"{x.strftime('%X')} {oversat_dag} {x.strftime('%d')} {oversat_maaned} {x.strftime('%Y')} Uge nr: {x.strftime('%U')}"
#     return formateret_dato_og_tid
#
# class RundetKnapEksempel(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#         layout = QVBoxLayout()
#
#
#         logo_label = QLabel(self)
#         pixmap = PyQt5.QtGui.QPixmap('../Python s2/DKEMPIRE.jpg')
#         logo_label.setPixmap(pixmap)
#         layout.addWidget(logo_label)
#
#         self.label = QLabel("Tryk på knappen for at vise klokkeslættet", self)
#         layout.addWidget(self.label)
#
#         self.knap = QPushButton("Vis Klokkeslæt", self)
#         self.knap.setStyleSheet(
#             """
#             QPushButton {
#                 background-color: red;
#                 border: none;
#                 color: white;
#                 padding: 12px 24px;
#                 border-radius: 12px;
#                 transition: background-color 0.5s;
#             }
#             """
#         )
#         self.knap.clicked.connect(self.on_button_click)
#
#         layout.addWidget(self.knap)
#         self.setLayout(layout)
#
#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.opdater_knapfarve)
#         self.hovered = False
#
#     def opdater_knapfarve(self):
#         if self.hovered:
#             self.knap.setStyleSheet(
#                 """
#                 QPushButton {
#                     background-color: green;
#                     border: none;
#                     color: white;
#                     padding: 12px 24px;
#                     border-radius: 12px;
#                     transition: background-color 0.5s;
#                 }
#                 """
#             )
#         else:
#             self.knap.setStyleSheet(
#                 """
#                 QPushButton {
#                     background-color: red;
#                     border: none;
#                     color: white;
#                     padding: 12px 24px;
#                     border-radius: 12px;
#                     transition: background-color 0.5s;
#                 }
#                 """
#             )
#
#     def enterEvent(self, event):
#         self.hovered = True
#         self.opdater_knapfarve()
#
#     def leaveEvent(self, event):
#         self.hovered = False
#         self.opdater_knapfarve()
#
#     def on_button_click(self):
#         output_text = vis_dato_og_tid()
#         self.label.setText(output_text)
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#
#     eksempel = RundetKnapEksempel()
#     eksempel.setWindowTitle('Klokkeslæt 2.0')
#     eksempel.setGeometry(300, 300, 400, 250)  # Justér vinduehøjden til at rumme logoet
#     eksempel.show()
#
#     sys.exit(app.exec_())


# import time
# from datetime import datetime
#
#
# def time_stub():
#     now = time.time()
#     print("seconds since 01.01.1970: ", now)
#     readable = datetime.fromtimestamp(now, tz=None)
#     print("transform into readable format: ", read

# import time
# from datetime import datetime
#
#
# def time_stub():
#     now = time.time()
#     print("seconds since 01.01.1970: ", now)
#     readable = datetime.fromtimestamp(now, tz=None)
#     print("transform into readable format: ", read

# import time
# from datetime import datetime
#
#
# def time_stub():
#     now = time.time()
#     print("seconds since 01.01.1970: ", now)
#     readable = datetime.fromtimestamp(now, tz=None)
#     print("transform into readable format: ", read

# import time
# from datetime import datetime
#
#
# def time_stub():
#     now = time.time()
#     print("seconds since 01.01.1970: ", now)
#     readable = datetime.fromtimestamp(now, tz=None)
#     print("transform into readable format: ", read

# import time
# from datetime import datetime
#
#
# def time_stub():
#     now = time.time()
#     print("seconds since 01.01.1970: ", now)
#     readable = datetime.fromtimestamp(now, tz=None)
#     print("transform into readable format: ", read

# import time
# from datetime import datetime
#
#
# def time_stub():
#     now = time.time()
#     print("seconds since 01.01.1970: ", now)
#     readable = datetime.fromtimestamp(now, tz=None)
#     print("transform into readable format: ", read

# import time
# from datetime import datetime
#
#
# def time_stub():
#     now = time.time()
#     print("seconds since 01.01.1970: ", now)
#     readable = datetime.fromtimestamp(now, tz=None)
#     print("transform into readable format: ", read

# import time
# from datetime import datetime
#
#
# def time_stub():
#     now = time.time()
#     print("seconds since 01.01.1970: ", now)
#     readable = datetime.fromtimestamp(now, tz=None)
#     print("transform into readable format: ", read

# import time
# from datetime import datetime
#
#
# def time_stub():
#     now = time.time()
#     print("seconds since 01.01.1970: ", now)
#     readable = datetime.fromtimestamp(now, tz=None)
#     print("transform into readable format: ", read

# import time
# from datetime import datetime
#
#
# def time_stub():
#     now = time.time()
#     print("seconds since 01.01.1970: ", now)
#     readable = datetime.fromtimestamp(now, tz=None)
#     print("transform into readable format: ", read

# import time
# from datetime import datetime
#
#
# def time_stub():
#     now = time.time()
#     print("seconds since 01.01.1970: ", now)
#     readable = datetime.fromtimestamp(now, tz=None)
#     print("transform into readable format: ", read

# import time
# from datetime import datetime
#
#
# def time_stub():
#     now = time.time()
#     print("seconds since 01.01.1970: ", now)
#     readable = datetime.fromtimestamp(now, tz=None)
#     print("transform into readable format: ", read

# import time
# from datetime import datetime
#
#
# def time_stub():
#     now = time.time()
#     print("seconds since 01.01.1970: ", now)
#     readable = datetime.fromtimestamp(now, tz=None)
#     print("transform into readable format: ", read

# import time
# from datetime import datetime
#
#
# def time_stub():
#     now = time.time()
#     print("seconds since 01.01.1970: ", now)
#     readable = datetime.fromtimestamp(now, tz=None)
#     print("transform into readable format: ", read

# import time
# from datetime import datetime
#
#
# def time_stub():
#     now = time.time()
#     print("seconds since 01.01.1970: ", now)
#     readable = datetime.fromtimestamp(now, tz=None)
#     print("transform into readable format: ", read

# import time
# from datetime import datetime
#
#
# def time_stub():
#     now = time.time()
#     print("seconds since 01.01.1970: ", now)
#     readable = datetime.fromtimestamp(now, tz=None)
#     print("transform into readable format: ", read

# import time
# from datetime import datetime
#
#
# def time_stub():
#     now = time.time()
#     print("seconds since 01.01.1970: ", now)
#     readable = datetime.fromtimestamp(now, tz=None)
#     print("transform into readable format: ", read

# import time
# from datetime import datetime
#
#
# def time_stub():
#     now = time.time()
#     print("seconds since 01.01.1970: ", now)
#     readable = datetime.fromtimestamp(now, tz=None)
#     print("transform into readable format: ", read

# import time
# from datetime import datetime
#
#
# def time_stub():
#     now = time.time()
#     print("seconds since 01.01.1970: ", now)
#     readable = datetime.fromtimestamp(now, tz=None)
#     print("transform into readable format: ", read
# import cProfile, pstats, io
# from pstats import SortKey
# pr = cProfile.Profile()
# pr.enable()
# # ... do something ...
# pr.disable()
# s = io.StringIO()
# sortby = SortKey.CUMULATIVE
# ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
# ps.print_stats()
# print(s.getvalue())

# import cProfile
# import pstats
# import math
# import numpy as np
#
# def test_np():
#     for i in range(88888):
#         x = np.sqrt(i)*np.sin(i)
#
# def test_math():
#     for i in range(99999):
#         x = math.sqrt(i)*math.sin(i)
#
# def test():
#     test_np()
#     test_math()
#
#
# with cProfile.Profile() as pr:
#     test()
# stats = pstats.Stats(pr)
# stats.sort_stats(pstats.SortKey.TIME)
# stats.print_stats()
# stats.dump_stats(filename='needs_profiling.prof')

# time stub

# import time
# from datetime import datetime
#
# def time_stub():
#     now = time.time()
#     print("seconds since 01.01.1970: ", now)
#     readable = datetime.fromtimestamp(now, tz=None)
#     print("transform into readable format: ", readable)
#
# time_stub()

# import json
# import requests
#
# read_from_file = False
# def json_stub():
#     if read_from_file:
#         with open("insert_filename_here.json", 'r') as f:
#             dic = json.loads(f.read())  # invoke json.loads() on the contents of the file, as opposed to the file path of that JSON
#         print(dic)
#     else:  # read from web
#         r = requests.get('https://jsonplaceholder.typicode.com/users')
#         print(r.json()[0])
#
# json_stub()

# Json colored text

import json


class Corlors:


    class Fg:
        BLACK = '\033[30m'
        RED = '\033[31m'
        GREEN = '\033[32m'
        YELLOW = '\033[33m'
        BLUE = '\033[34m'
        MAGENTA = '\033[35m'
        CYAN = '\033[36m'
        WHITE = '\033[37m'
        RESET = '\033[39m'


    class Bg:
        BLACK = '\033[40m'
        RED = '\033[41m'
        GREEN = '\033[42m'
        YELLOW = '\033[43m'
        BLUE = '\033[44m'
        MAGENTA = '\033[45m'
        CYAN = '\033[46m'
        WHITE = '\033[107m'
        RESET = '\033[49m'


    # HEADER = '\033[95m'
    # BLUE = '\033[94m'
    # GREEN = '\033[92m'
    # WARNING = '\033[93m'
    # RED = '\033[91m'
    # END = '\033[0m'
    # YELLOW = '\033[33m'
    # UNDERLINE = '\033[4m'
    # BOLD = '\033[1m'

def colorloop():

    color = [Corlors.Fg.RED, Corlors.Fg.GREEN, Corlors.Fg.YELLOW, Corlors.Fg.BLUE, Corlors.Fg.MAGENTA, Corlors.Fg.CYAN, Corlors.Fg.WHITE, Corlors.Fg.RESET]
    color_bg = [Corlors.Bg.RED, Corlors.Bg.GREEN, Corlors.Bg.YELLOW, Corlors.Bg.BLUE, Corlors.Bg.MAGENTA, Corlors.Bg.CYAN, Corlors.Bg.WHITE, Corlors.Bg.RESET]


    print("Forgrundsfarver Og Baggrundsfarver:")
    for bg_color in color_bg:
        for fg_color in color:
            print(f"{fg_color}{bg_color}Hello World{Corlors.Fg.RESET}{Corlors.Bg.RESET}", end="   ")
        print("")

colorloop()
# print(" ")
# for color_bg in color_bg:
#     print(color_bg + "Hello World" + Corlors.Bg.RESET, end="   ")
