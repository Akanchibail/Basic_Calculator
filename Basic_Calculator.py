from tkinter import *
from tkinter import ttk

# Variables color0 to color4 store different color codes
color0 = "white"    # White background
color1 = "black"    # Black font
color2 = "#ff843d"  # Orange 
color3 = "#334acc"  # Blue
color4 = "#d8dae6"  # Ash

# Create window
window = Tk() #Creates the main application window.
window.title('Basic Calculator') #Sets the title of the window to "Basic Calculator".
window.geometry('260x315') #Defines the window size as 260 pixels width and 315 pixels height
window.resizable(height=False, width=False) #Disables resizing of the window to keep the calculator's layout fixed
window.configure(bg=color0) #Sets the window background color to color0 (white)

style = ttk.Style(window) #Creates a style object that allows us to apply themes to widget
style.theme_use("clam") #Sets the theme of the application to "clam" (a predefined Tkinter theme).

ttk.Separator(window, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=280) #Creates a horizontal line (separator).
#Places the separator at row 0, spanning one column, and extends its width using padx.

# Display frame
frame_score = Frame(window, width=300, height=56, bg=color1, pady=0, padx=0)  #Creates a section (frame) within the main window.
frame_score.grid(row=1, column=0, sticky=NW) #This frame holds the calculator's display (where numbers appear).

# Buttons frame
frame_buttons = Frame(window, width=300, height=340, bg=color0, pady=0, padx=0) #This frame holds the buttons (digits, operations, etc.).
frame_buttons.grid(row=2, column=0, sticky=NW) #Places the frames inside the window at specified positions

#Function to Enter Numbers and Operators
def entering_values(number): #Defines a function that takes number as input.
    global all_values #Declares all_values as a global variable so it can be accessed outside the function.

    all_values = all_values + str(number) #Concatenates the pressed number & operator to the all_values string.
    text_value.set(all_values) #Updates the calculator display with the new value.

#Function to Clear the Display
def clear_screen():
    global all_values

    all_values =""  #updates all_values to empty 
    text_value.set("") #Clears the all_values string and resets the display.

#Function to Calculate the Result
def calculate():
    global all_values

    result = str(eval(all_values)) #Uses Python’s eval() function to evaluate mathematical expressions.
    text_value.set(result) #Updates the display with the calculated result.
    all_values = "" #Resets all_values after displaying the result.

all_values ="" #Stores the entered numbers and operations as a string.
text_value=StringVar() #StringVar is a Tkinter variable that holds text for UI updates.
                
# Creating the Display Screen
app_screen = Label(frame_score, width=16, height=2, textvariable=text_value,padx=7, anchor="e", bd=0, 
                   justify=RIGHT, font=("Ivy 18"), bg=color1, fg=color0) #Creates a label inside frame_score to display user input

app_screen.place(x=0, y=0)

#Creating Buttons
# Row 1 - Clear, Percentage, Divide
#Creates a button inside frame_buttons & Calls the clear_screen function when clicked.
b_1 = Button(frame_buttons, text="C",command=lambda:clear_screen(), width=11, height=2, bg=color4, fg=color1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE,)
b_1.place(x=0, y=0) #Positions the button using absolute coordinates.

b_2 = Button(frame_buttons,command=lambda:entering_values("%"), text="%", width=5, height=2, bg=color0, fg=color1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)

b_3 = Button(frame_buttons, command=lambda:entering_values("/"),text="/", width=5, height=2, bg=color2, fg=color2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)

# Row 2 - Numbers 7, 8, 9, Multiply
b_4 = Button(frame_buttons, command=lambda:entering_values("7"),text="7", width=5, height=2, bg=color0, fg=color1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)

b_5 = Button(frame_buttons, command=lambda:entering_values("8"),text="8", width=5, height=2, bg=color0, fg=color1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=52)

b_6 = Button(frame_buttons,command=lambda:entering_values("9"), text="9", width=5, height=2, bg=color0, fg=color1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=52)

b_7 = Button(frame_buttons,command=lambda:entering_values("*"), text="*", width=5, height=2, bg=color2, fg=color2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=52)

# Row 3 - Numbers 4, 5, 6, Minus
b_8 = Button(frame_buttons, command=lambda:entering_values("4"),text="4", width=5, height=2, bg=color0, fg=color1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)

b_9 = Button(frame_buttons,command=lambda:entering_values("5"), text="5", width=5, height=2, bg=color0, fg=color1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=104)

b_10 = Button(frame_buttons,command=lambda:entering_values("6"), text="6", width=5, height=2, bg=color0, fg=color1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=104)

b_11 = Button(frame_buttons, command=lambda:entering_values("-"),text="-", width=5, height=2, bg=color2, fg=color2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_11.place(x=177, y=104)

# Row 4 - Numbers 1, 2, 3, Plus
b_12 = Button(frame_buttons, command=lambda:entering_values("1"),text="1", width=5, height=2, bg=color0, fg=color1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)

b_13 = Button(frame_buttons, command=lambda:entering_values("2"),text="2", width=5, height=2, bg=color0, fg=color1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=156)

b_14 = Button(frame_buttons,command=lambda:entering_values("3"), text="3", width=5, height=2, bg=color0, fg=color1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=156)

b_15 = Button(frame_buttons,command=lambda:entering_values("+"), text="+", width=5, height=2, bg=color2, fg=color2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=156)

# Row 5 - Number 0, Decimal, Equals
b_16 = Button(frame_buttons, command=lambda:entering_values("0"),text="0", width=11, height=2, bg=color0, fg=color1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=208)

b_17 = Button(frame_buttons,command=lambda:entering_values("."), text=".", width=5, height=2, bg=color0, fg=color1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_17.place(x=118, y=208)

b_18 = Button(frame_buttons, text="=",command=lambda:calculate(), width=5, height=2, bg=color2, fg=color2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_18.place(x=177, y=208)

#Centering the Window
window.update()  # Update the window to get correct dimensions

#Get the window size & Get screen size.
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()  
screen_height = window.winfo_screenheight()

#Centers the window horizontally & Centers the window vertically.
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")  # Apply positioning & Moves the window to the center.

#Starts the Tkinter event loop, keeping the application running until the user closes it.
window.mainloop()
