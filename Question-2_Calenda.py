###############

# Student Name: Veasna Kuoy s317557
# Student Name: Ryan Mu s301219

###############


# importing the required libraries and modules  
from tkinter import *           # importing all methods, classes and widgets from the tkinter library  
import calendar                 # importing the calendar module  
from datetime import date       # importing the date module from the datetime library  
  
# defining the necessary functions  
# function to display the Calendar  
def displayCalendar():  
    # get the month and year data from the spin boxes  
    month = int(month_box.get())  
    year = int(year_box.get())  
  
    # using the month() method from the calendar module to  
    # get the month info and storing in the variable  
    output_calendar = calendar.month(year, month)  
  
    # using the delete() method to delete the output  
    calendar_field.delete(1.0, 'end')  
  
    # displaying the resultant calendar  
    calendar_field.insert('end', output_calendar)  
  
# function to reset the entries  
def reset():  
    # using the delete() method to delete the output  
    calendar_field.delete(1.0, 'end')  
  
    # setting the values of the IntVar objects to current month and year  
    month_var.set(current_month)  
    year_var.set(current_year)  
  
    # using the config() method and assigning the  
    # textvariable parameter to different IntVar objects  
    month_box.config(textvariable = month_var)  
    year_box.config(textvariable = year_var)  
  
# function to close the application  
def close():  
    # using the destroy() method to close the application  
    guiWindow.destroy()  
  
# main function  
if __name__ == "__main__":  
    # creating an object of the Tk() class  
    guiWindow = Tk()  
    # setting the title for the main window  
    guiWindow.title("Calendar")  
    # setting the size and position of the main window  
    guiWindow.geometry('500x550+650+250')  
    # disabling the resizable option  
    guiWindow.resizable(0, 0)  
    # setting the background color to #FFFAF0  
    guiWindow.configure(bg="#FFFAF0")  
   
    # creating the objects of the Frame() widget  
    header_frame = Frame(guiWindow, bg = "#FFFAF0")  
    entry_frame = Frame(guiWindow, bg = "#FFFAF0")  
    result_frame = Frame(guiWindow, bg = "#FFFAF0")  
    button_frame = Frame(guiWindow, bg = "#FFFAF0")  
      
    # using the pack() method to set the positions of the frames  
    header_frame.pack(expand = True, fill = "both")  
    entry_frame.pack(expand = True, fill = "both")  
    result_frame.pack(expand = True, fill = "both")  
    button_frame.pack(expand = True, fill = "both")  
  
    # creating the label to display the heading  
    header_label = Label(  
        header_frame,  
        text = "CALENDAR",  
        font = ('verdana','25','bold'),  
        bg = "#EEE8AA",  
        fg = "#191970"
        )  
  
    # using the pack() method to set the position of the label  
    header_label.pack(expand = True, fill = "both")  
  
    # creating the labels to display the details for the month and year  
    month_label = Label(  
        entry_frame,  
        text = "Month:",  
        font = ("consolas", "10", "bold"),  
        bg = "#FFFAF0",  
        fg = "#000000"  
    )  
    year_label = Label(  
        entry_frame,  
        text = "Year:",  
        font = ("consolas", "10", "bold"),  
        bg = "#FFFAF0",  
        fg = "#000000"     
    )  
  
    # using the place() method to set the position of the labels  
    month_label.place(x = 120, y = 20)  
    year_label.place(x = 268, y = 20)  
  
    # creating the objects of the IntVar class  
    month_var = IntVar(entry_frame)  
    year_var = IntVar(entry_frame)  
  
    # storing the current month and year information  
    current_month = date.today().month  
    current_year = date.today().year  
  
    # setting the current month and year to the IntVar objects  
    month_var.set(current_month)  
    year_var.set(current_year)  
  
    # creating the spin boxes to enter month and year  
    month_box = Spinbox(  
        entry_frame,  
        from_ = 1,  
        to = 12,  
        width = "5",  
        textvariable = month_var   
        )  
    year_box = Spinbox(  
        entry_frame,  
        from_ = 0000,  
        to = 3000,  
        width = "6",  
        textvariable = year_var  
    )  
  
    # using the place() method to set the position of the spin boxes  
    month_box.place(x = 175, y = 20)  
    year_box.place(x = 315, y = 20)  
  
    # creating a textbox to display calendar  
    calendar_field = Text(  
        result_frame,  
        width = 20,   
        height= 8,  
        font = ("consolas", "14"),  
        relief = RIDGE,  
        borderwidth = 2    
    )  
  
    # using the pack() method to set the position of the textbox  
    calendar_field.pack(expand = False, fill = None)  
  
    # creating the buttons for the application  
    # DISPLAY BUTTON  
    display_button = Button(  
        button_frame,  
        text = "DISPLAY",  
        bg = "dark violet",  
        fg = "#E0FFFF",  
        command = displayCalendar  
    )  
  
    # RESET BUTTON  
    reset_button = Button(  
        button_frame,  
        text = "RESET",  
        bg = "dark violet",  
        fg = "#E0FFFF",  
        command = reset  
    )  
  
    # CLOSE BUTTON  
    close_button = Button(  
        button_frame,
        text = "CLOSE",  
        bg = "dark violet",  
        fg = "#E0FFFF",  
        command = close  
    )  
  
    # using the place() method to set the positions of the buttons  
    display_button.place(x = 140, y = 0)  
    reset_button.place(x = 230, y = 0)  
    close_button.place(x = 305, y = 0)  
  
    # using the mainloop() method to run the application  
    guiWindow.mainloop() 