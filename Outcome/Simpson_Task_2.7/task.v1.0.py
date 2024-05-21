from tkinter import *
import random


def quit():
    main_window.destroy()


def generate_random():
    random_number = random.randint(1, 10)
    Label(main_window, text=random_number) .grid(column=0, row=2, sticky=E)


def main():
    Button(main_window, text="Quit", command=quit)  .grid(column=0, row=0)
    Button(main_window, text="Random", command=generate_random)  .grid(column=1, row=0)
    main_window.mainloop()


main_window = Tk()
main()
