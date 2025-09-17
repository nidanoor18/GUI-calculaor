import tkinter as tk     #python gui-library

#function to handle press button - refers to user clicking on one of the calculator’s buttons in the GUI—like 1,2,+,etc.

def press(num):   
 global expression,is_on  #global → allows modification of the variable outside the function scope.
 if not is_on:   # ignore button presses when OFF
        return
 expression+=str(num) 
  #+= → appends the new button value to the existing expression.
   #str(num) → ensures both numbers and operators are treated as strings.
 equation.set(expression)   #updates the Entry widget so user sees new expression on calculator display

#Function to evaluate the final expression when user clicks "=" button
 
def equalpress():
     #attempts to run code that could raise an error.
     if not is_on:   # ignore button presses when OFF
        return
     try:   
        global expression  #equalpress() also modifies expression-that's why global is used again.
       #eval(expression) → takes the string in expression (like "2+3*4") and calculates the result (here, 14).
        total_val= str(eval(expression))  #converts result to string for display

        #equation is a Tkinter StringVar() linked to the Entry widget (calculator display).
        equation.set(total_val)  #updates display with result
        #set(value) → updates the value of the StringVar, which in turn updates all linked widget automatically.
        
        expression= total_val  #After showing the result, we store it back in expression.This allows further calculations without clearing the previous result.

    #Error Handling

   #specific error handling for division by zero 
     except ZeroDivisionError:  
        equation.set("Error (Div by 0)")  #displays error message on calculator display
        expression=""  #resets expression to empty string, allowing user to start fresh.

     except:  #generic exception handler for any other errors (like syntax errors)
        equation.set("Error") 
        expression="" 

    #Function to clear display when user clicks "C" button  

def clear():
      global expression  #modifies expression variable  
      expression=""
      equation.set("")  #clears the Entry widget display

    #Function to backspace (delete the last character)
def backspace():
    global expression
    expression = expression[:-1]  # slice remove last character
    equation.set(expression)

    #Function for OFF button
def TurnOff():
    global expression, is_on
    is_on = False
    expression=""     # clear the stored expression
    equation.set(" ")      # clear the display
    entry_field.config(bg="#669db3", fg="white")

    #Function to "TURN ON" again
def TurnOn():
     global is_on
     is_on = True
     entry_field.config(bg="white", fg="#152130")  #restore original screen


      #Main GUI window setup

window=tk.Tk()  #creates main application window
window.title("GUI Calculator") #sets window title
window.geometry("500x700") #sets window size
      #window.resizable(False,False) → prevents user from resizing window

      # Define global variables
   
expression=""  #string that stores the current calculation
equation=tk.StringVar()    #StringVar() → special Tkinter variable for text
    #Automatically updates the Entry widget when equation.set() is called.

    #CREATE ENTRY WIDGET (CALCULATOR DISPLAY) i.e, the place where numbers and results appear

    #In Tkinter, Entry is a widget (a GUI element).It allows the user (or the program) to enter or display text.

# In  calculator, you’re not typing directly — instead, you update the Entry field using equation.set()
#So in this calculator, the Entry field is the screen/display.

# Entry = class from Tkinter (like a blueprint to create text boxes).
# tk.Entry(...) = creates one object (an actual text box in your program).
# entry_field = variable that stores a reference to Entry object, so you can configure it later.
 
entry_field= tk.Entry(window,     #Creates an Entry widget inside the main window
textvariable=equation,          # Links the Entry field to the Tkinter variable equation (StringVar()).Whatever value you put in equation.set("123") → shows in the Entry field.
font=("Seougi UI",32,"bold"),
bd=12,           #sets border width inside the widget.Creates spacing between the text and the widget edges.
insertwidth=2,  #Controls the width of the text cursor (blinking line).     
borderwidth=8,    #Thickness of the outer border of the widget.
relief="sunken",    #gives a  effect to the border.
justify="right",  #aligns text to the right side of the Entry field

bg="#1E1E2E", fg="#F8F8F2"  )     # modern dark screen



entry_field.grid(row=0,column=0,columnspan=4,padx=10, pady=15, sticky="nsew") #places the Entry widget in the window using grid layout manager in row 0, spanning 2 columns 
#row=0, column=0 ->top-left corner.
#columnspan=2 → spans across 2 columns .By default, a widget takes up 1 column. but widget will stretch across 2 columns in the grid.

#.grid() places the Entry on the window using a grid layout.Tkinter uses a grid layout manager to arrange widgets (like buttons, labels, entries) in a table-like structure with rows and columns.
#Each widget is placed at a specific (row, column) location.

#BUTTON LAYOUT
 
buttons = [
    ('C',1,0), ('⌫',1,1), ('OFF',1,2), ('ON',1,3),
    ('7',2,0), ('8',2,1), ('9',2,2), ('/',2,3),
    ('4',3,0), ('5',3,1), ('6',3,2), ('*',3,3),
    ('1',4,0), ('2',4,1), ('3',4,2), ('-',4,3),
    ('0',5,0), ('.',5,1), ('%',5,2), ('+',5,3),
    ('=',6,0,4)   # full-width row for equal button
]

#loop
for b in buttons:    
    if len(b) == 3:
        text, row, col = b
        colspan = 1
    elif len(b) == 4:
        text, row, col, colspan = b
    else:
        continue

       # === Create buttons inside the loop ===
    if text == "=":
        btn = tk.Button(window, text=text, padx=2, pady=2, bd=8,
                        fg="black", bg="#FFD6E0", activebackground="#FF9980",relief="flat",
                        font=('Ariel', 26, 'bold'), command=equalpress)

    elif text in ["+", "-", "*", "/", "%"]:
        btn = tk.Button(window, text=text, padx=2, pady=2, bd=8,
                        fg="black", bg="#f2e1ec", activebackground="#FF8C94",relief="flat",
                        font=('Ariel', 22, 'bold'), command=lambda t=text: press(t))

    elif text == "C":
        btn = tk.Button(window, text=text, padx=20, pady=20, bd=8,
                        fg="white",bg="#DAC5E3", activebackground="#BFA2D4",relief="flat",
                        font=('Ariel', 25, 'bold'), command=clear)

    elif text == "⌫":
        btn = tk.Button(window, text=text, padx=20, pady=20, bd=8,
                        fg="white", bg="#DAC5E3", activebackground="#BFA2D4",relief="flat",
                        font=('Ariel', 25, 'bold'), command=backspace)

    elif text == "OFF":
        btn = tk.Button(window, text=text, padx=20, pady=20, bd=8,
                        fg="white",bg="#C1E1C1", activebackground="#A3C9A8",relief="flat",
                        font=('Ariel', 22, 'bold'), command=TurnOff)

    elif text == "ON":
        btn = tk.Button(window, text=text, padx=20, pady=20, bd=8,
                         fg="white", bg="#C1E1C1", activebackground="#A3C9A8",relief="flat",
                        font=('Ariel', 22, 'bold'), command=TurnOn)

    else:
        btn = tk.Button(window, text=text, padx=20, pady=20, bd=8,
                        fg="black", bg="white", activebackground="#ccb6c4",relief="flat",
                        font=('Ariel', 22, 'bold'), command=lambda t=text: press(t))


    # === Place the button in grid (also inside the loop!) ===
    btn.grid(row=row, column=col, columnspan=colspan, sticky="nsew",padx=6,pady=6)


# sticky="nsew" → makes button expand to fill the grid cell in all directions (north, south, east, west)

# EVEN GRID (all rows/cols same size)
for i in range(4):
    window.grid_columnconfigure(i, weight=1, uniform="col")
for i in range(7):
    window.grid_rowconfigure(i, weight=1, uniform="row")

#RUN TKINTER MAIN LOOP
window.mainloop()

# Starts the event loop.

# Keeps the GUI window open and responsive to user actions (clicks, typing, etc.).

# Program will stay running until the window is closed.

