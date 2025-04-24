from tkinter import *
import calendar


def showCal():
    try:
        fetch_year = int(year_field.get())
        new_gui = Tk()
        new_gui.config(background="black")
        new_gui.title("CALANDER")
        new_gui.geometry("550x600")
        cal_content = calendar.calendar(fetch_year)
        cal_year = Label(new_gui, text=cal_content, font="Consolas 10 bold")
        cal_year.grid(row=5, column=1, padx=20)
        new_gui.mainloop()
    except ValueError:
        print("Niepoprawna wartość w polu rok")


if __name__ == "__main__":
    gui = Tk()
    gui.config(background="white")
    gui.title("CALANDER")
    gui.geometry("250x200")
    cal = Label(gui, text="CALANDER", bg="dark blue",
                font=("times", 28, "italic"))
    cal.grid(row=0, column=0, columnspan=2)
    year = Label(gui, text="Enter Year", bg="light green")
    year.grid(row=1, column=0)
    year_field = Entry(gui)
    year_field.grid(row=1, column=1)
    Show = Button(gui, text="Show calander", fg="Black", bg="Red",
                  command=showCal, font=("Arial", 12, 'bold'))
    Show.grid(row=2, column=0, columnspan=2)
    Exit = Button(gui, text="Exit", fg="Black", bg="Red", command=exit)
    Exit.grid(row=3, column=0, columnspan=2)
    gui.mainloop()
