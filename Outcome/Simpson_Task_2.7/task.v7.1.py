from tkinter import *
import random

def quit():
    main_window.destroy()


def generate_random():
    count_items["count_dice"] += 1
    bg_colour = "red"

    # random number 1
    random_number1 = random.randint(1, 10)
    # random number2
    random_number2 = random.randint(1, 10)

    if random_number1 == 6 and random_number2 == 6:
        bg_colour = "green"
        print("WE GET DOUBLE 6. ")
    # create labels
    Label(main_window, text=random_number1, bg=bg_colour, width=12).grid(column=0, row=1, sticky=E)
    Label(main_window, text=random_number2, bg=bg_colour, width=12).grid(column=1, row=1, sticky=E)
    Label(main_window, text="roll count =", width=12).grid(column=0, row=2, sticky=E)
    Label(main_window, text= count_items["count_dice"], width=12)  .grid(column=1, row=2, sticky=W)


def main():
    Button(main_window, text="Quit", command=quit, width=12).grid(column=0, row=0)
    Button(main_window, text="Random", command=generate_random, width=12).grid(column=1, row=0)
    Label(main_window, text="").grid(column=0, row=1, sticky=E)
    Label(main_window, text="").grid(column=1, row=1, sticky=E)
    Label(main_window, text="").grid(column=0, row=2, sticky=E)
    Label(main_window, text="").grid(column=1, row=2, sticky=E)
    main_window.mainloop()

def reset():
    def quit():
        main_window.destroy()
    def generate_random():
        count_items["count_dice"] += 1
        bg_colour = "red"

        # random number 1
        random_number1 = random.randint(1, 10)
        # random number2
        random_number2 = random.randint(1, 10)

        if random_number1 == 6 and random_number2 == 6:
            bg_colour = "green"
            print("EITHER NUMBER IS NOT 4. ")
        # create labels
        Label(main_window, text=random_number1, bg=bg_colour, width=12).grid(column=0, row=1, sticky=E)
        Label(main_window, text=random_number2, bg=bg_colour, width=12).grid(column=1, row=1, sticky=E)
        Label(main_window, text="roll count =", width=12).grid(column=0, row=2, sticky=E)
        Label(main_window, text= count_items["count_dice"], width=12)  .grid(column=1, row=2, sticky=W)


    def main1():
        Button(main_window, text="Quit", command=quit, width=12).grid(column=0, row=0)
        Button(main_window, text="Random", command=generate_random, width=12).grid(column=1, row=0)
        Label(main_window, text="").grid(column=0, row=1, sticky=E)
        Label(main_window, text="").grid(column=1, row=1, sticky=E)
        Label(main_window, text="").grid(column=0, row=2, sticky=E)
        Label(main_window, text="").grid(column=1, row=2, sticky=E)
        main_window.mainloop()
        count_items = {"count_dice":0}
        main_window = Tk()
        main1()

    
count_items = {"count_dice":0}
main_window = Tk()
main()
