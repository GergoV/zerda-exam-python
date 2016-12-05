# EXAM: Python Basics

### Getting Started
 - Fork this repository under your own account
 - Clone the forked repository to your computer
 - Commit your progress frequently and with descriptive commit messages
 - All your answers and solutions should go in this repository

### What can I use?
- You can use any resource online, but **please work individually**
- **Don't just copy-paste** your answers and solutions, use your own words instead.


# Tasks
## 1-5. Complete the tasks seen in the first-fifth.py files! (~120 mins)
### Acceptance criteria
The application is accepted if:
- The solution works according to specification [1p each]
- Has proper error handling where the specification says it [1p each]
- Has the correct loops, methods, filters [1p each]
- The code is clean, without unnecessary repetition, and with descriptive names [1p each]
- You commit frequently, after each task, with descriptive commit messages [1p]
- The solution follows [styleguide](https://github.com/greenfox-academy/teaching-materials/blob/master/styleguide/python.md) [1p]

## 6. Question time! (~30 mins) [6p]

### Explain the algorithm seen in `third.py`. Use a flowchart, structogram or pseudo code. [2p]
#### Your answer:

See Python_exam_flowchart.png included.

(In brief:
  - Get a string and a letter as input
  - Check if string is really a string, if no: return 0
  - Set a counter to 0;
  - Iterate letters of string
  - Check if current letter is letter we're looking for; if so, increase counter;
  - Return count of occurences.)

### How can you create a graphical user interface and draw a rectangle on it in python? What are the tools needed for it? [2p]
#### Your answer:

Python has various modules for graphics. Tkinter is a basic one suitable for this task.

Tkinter module has to be installed alongside python to be able to work.

To create simple graphics, tkinter module has to be imported. You need to set up a windows object (Tk()), then create a canvas widget and draw a rectangle on canvas widget with proper tkinter function.

Finally, all has to be put in the main loop to be displayed in the window.

Example use:

from tkinter import * # import tkinter

root = Tk() # instantiate window

canvas = Canvas(root, width=200, height=100) # set up canvas with given width, heigt
canvas.pack() # pack canvas

canvas.create_rectangle(50, 25, 150, 75, fill="blue") # create rectangle, coordinates are corners

mainloop() # display all by putting canvas in main loop

### What does V stand for in MVC? [2p]
#### Your answer:

View. The component of the program that is responsible for displaying the software's output and the user interface.
