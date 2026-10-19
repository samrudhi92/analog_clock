import tkinter as tk
import time
import math


root = tk.Tk()
root.title("Analog Clock")


canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

def clock():
    canvas.delete("all")

    canvas.create_oval(50, 50, 350, 350, width=4)


    for i in range(1, 13):
        angle = math.radians(i * 30 - 90)

        x = 200 + 125 * math.cos(angle)
        y = 200 + 125 * math.sin(angle)

        canvas.create_text(
            x, y,
            text=str(i),
            font=("Arial", 16, "bold")
        )

    t = time.localtime()

    hour = t.tm_hour % 12
    minute = t.tm_min
    second = t.tm_sec

   
    angle = math.radians((hour + minute / 60) * 30 - 90)
    x = 200 + 80 * math.cos(angle)
    y = 200 + 80 * math.sin(angle)

    canvas.create_line(200, 200, x, y, width=6)

 
    angle = math.radians((minute + second / 60) * 6 - 90)
    x = 200 + 110 * math.cos(angle)
    y = 200 + 110 * math.sin(angle)

    canvas.create_line(200, 200, x, y, width=4)

    
    angle = math.radians(second * 6 - 90)
    x = 200 + 125 * math.cos(angle)
    y = 200 + 125 * math.sin(angle)

    canvas.create_line(200, 200, x, y, fill="red", width=2)

   
    canvas.create_oval(195, 195, 205, 205, fill="black")

  
    root.after(1000, clock)


clock()


root.mainloop()