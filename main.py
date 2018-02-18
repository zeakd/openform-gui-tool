import tkinter as tk
import openform

class Application(tk.Frame):
  def __init__(self, master=None):
    super().__init__(master)
    self.pack()
    self.create_widgets()

  def create_widgets(self):
    self.JetR = tk.DoubleVar()
    self.label = tk.Label(self, text="JetR")
    self.label.pack(side='left')
    self.JetREntry = tk.Entry(self)
    self.JetREntry['textvariable'] = self.JetR
    self.JetREntry.pack(side='left')

    self.hFixedVal = tk.DoubleVar()
    self.label = tk.Label(self, text="hFixedVal")
    self.label.pack(side='left')
    self.hFixedValEntry = tk.Entry(self)
    self.hFixedValEntry['textvariable'] = self.hFixedVal
    self.hFixedValEntry.pack(side='left')

    self.UsMagFixedVal = tk.DoubleVar()
    self.label = tk.Label(self, text="UsMagFixedVal")
    self.label.pack(side='left')
    self.UsMagFixedValEntry = tk.Entry(self)
    self.UsMagFixedValEntry['textvariable'] = self.UsMagFixedVal
    self.UsMagFixedValEntry.pack(side='left')
    
    # self.txt.grid(row=0, column=1)
    # btn = Button(root, text="OK", width=15)
    # btn.grid(row=1, column=1)
    # self.hi_there = tk.Button(self)
    # self.hi_there["text"] = "Hello World\n(click me)"
    # self.hi_there["command"] = self.say_hi
    # self.hi_there.pack(side="top")

    self.saveBtn = tk.Button(self, text="저장", fg="black",
                          command=self.save)
    self.saveBtn.pack(side="bottom")

  # def say_hi(self):
  #   print("hi there, everyone!")

  def save(self):
    inputDict = {}
    inputDict['JetR'] = self.JetR.get()
    inputDict['hFixedVal'] = self.hFixedVal.get()
    inputDict['UsMagFixedVal'] = self.UsMagFixedVal.get()
    # print(inputDict)

    # transportProperties가 저장될 위치를 지정한다.
    write_openform(inputDict, './transportProperties')


def write_openform(parsedDict, outputPath):
  with open(outputPath, "w") as text_file:
    text_file.write(openform.build(parsedDict))

root = tk.Tk()
app = Application(master=root)
app.mainloop()