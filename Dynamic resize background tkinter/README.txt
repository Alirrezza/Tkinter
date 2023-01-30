This is small piece of code for resizing the program window in a way
the background image covers all of the window screen in each size!!!

You can find lots of cods on the internet about "How to Dynamically Resize Background Images" but
thier problems are so clear for avoiding them!!!! One of the best tutorial I have seen about resizing dynamiclly is:
-->  https://steemit.com/python/@codemy/dynamically-resize-background-images-python-tkinter-gui-tutorial-148 <--
but the main problem of that is about using global variables and the 'resizer' function which is not flexible.

Finally I figured out to pass my variables to function by reference ,instead of value ! and this article helped me alot:
https://www.geeksforgeeks.org/pass-by-reference-vs-value-in-python/