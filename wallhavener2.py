from tkinter import *

class App():
  def __init__(self, master):
    frame = Frame(master)
    frame.pack()

    master.title("Just my example")
    self.label = Label(frame, text="Type very long text:")

    self.entry = Entry(frame)

    self.button = Button(frame,
                         text="Quit", fg="red", width=20,
                         command=frame.quit)


    self.slogan = Button(frame,
                         text="Hello", width=20,
                         command=self.write_slogan)

    self.label.grid(row=0, column=0)
    self.entry.grid(row=0, column=1)
    self.slogan.grid(row=1, column=0)
    self.button.grid(row=1, column=1)

  def write_slogan(self):
    print ("Tkinter is easy to use!")

root = Tk()
app = App(root)
root.mainloop()
