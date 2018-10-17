# imports
from tkinter import *


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        # change title of windows
        self.master.title("Osu! Minus Weeb")

        # allow widget to take the full space of the window
        self.pack(fill=BOTH, expand=1)

        prices_text = Text(root, height=10, width=40)

        change_seasonal = False
        change_song_skin = False

        seasonal_image_box = Checkbutton(root, text="Seasonal Images", variable=change_seasonal)
        seasonal_image_box.pack()

        song_skin_box = Checkbutton(root, text="Ignore Song Skin?", variable=change_song_skin)
        song_skin_box.pack()

        # create a button
        get_data_button = Button(self, text="Get new prices", command=lambda: self.update_text(prices_text))

        # put button on spot on window
        get_data_button.pack(side="top", fill='x', expand=True, padx=10, pady=10)

    def update_text(self, text):
        prices = []
        # text delete expects a string representation of the floated value of the number of lines of text starting at 1
        text.delete('1.0', str(float(len(prices)) + 1))
        for price in prices:
            text.insert(END, str(price[0]) + ": " + str(price[1]) + "\n")
        text.pack(fill='x', padx=10, pady=10)

    def client_exit(self):
        exit()


root = Tk()

# size of the window
root.geometry("350x500")

app = Window(root)
root.mainloop()
