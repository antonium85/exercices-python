import time
from tkinter import *
    
tk=Tk()
canvas=Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_polygon(10,10,10,60,50,35,fill='magenta')

"""
for x in range(0, 60):
    canvas.move(1,5,5)
    tk.update()
    time.sleep(0.05)
"""

def bouger_triangle(evenement):
    if evenement.keysym == 'Up':
        canvas.move(1,0,-3)
    elif evenement.keysym == 'Down':
        canvas.move(1,0,3)
    elif evenement.keysym == 'Left':
        canvas.move(1,-3,0)
    else:
        canvas.move(1,3,0)

canvas.bind_all('<KeyPress-Up>',bouger_triangle)
canvas.bind_all('<KeyPress-Down>',bouger_triangle)
canvas.bind_all('<KeyPress-Left>',bouger_triangle)
canvas.bind_all('<KeyPress-Right>',bouger_triangle)

tk.mainloop()