import tkinter as tk
import mainBody
## from casioplot import *

 # create main window
root = tk.Tk()

root.title("Russian Roulette")
label = tk.Label(root,
            text="Welcome to Russian Roulette!!",
            foreground="white",
            background="black",
            width=30,
            height=5
            )

label.pack()
button = tk.Button(
        text="Spin",
        width=25,
        height=5,
        bg="Blue",
        fg="yellow",
    )
button.pack()

label = tk.Label(root, text="Name")
label.pack()


def handle_click(event):
    print("Spin was clicked!")


button.bind("<Button-1>", handle_click)

root.mainloop()
