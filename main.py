from tkinter import *
import openform

def write_openform(parsedDict, outputPath):
  with open(outputPath, "w") as text_file:
    text_file.write(openform.build(parsedDict))

class OpenformInputFrame(Frame):
  def __init__(self, master, **kwargs):
    '''
      openform 변수를 다루기 위한 Label-Entry 쌍 입니다. 
      Frame의 subclass로 같은 option을 사용할 수 있으며 추가로 몇가지 옵션이 더 있습니다.

      text: label의 text입니다.  
      Var: entry의 Var class입니다. default - StringVar
      openform_path: required. save시에 변경할 openform파일 경로입니다.
      label_options: label 생성시에 넘기는 options. 사용시엔 text를 명시해 주세요.
      label_grid_options: label grid에 넘기는 options. default - { 'column': 0, 'row': 0 }
      entry_options: etnry 생성시에 넘기는 options
      entry_grid_options: entry grid에 넘기는 options. default - { 'column': 1, 'row': 0 }
      
    '''


    # required
    openform_path = kwargs.pop('openform_path')

    self.openform_path = openform_path

    self.entry_options = kwargs.pop('entry_options', {})
    self.entry_grid_options = kwargs.pop('entry_grid_options', {
      'column': 1,
      'row': 0
    })

    self.label_options = kwargs.pop('label_options', {
      'text': kwargs.pop('text', '')
    })
    self.label_grid_options = kwargs.pop('label_grid_options', {
      'column': 0,
      'row': 0
    })

    self.Var = kwargs.pop('Var', StringVar)

    super().__init__(master, **kwargs)

    # 하위 컴포넌트 그리기
    self.render()

  def render(self):
    self.label = Label(self, **self.label_options)
    self.label.grid(**self.label_grid_options)
    self.entry = Entry(self, **self.entry_options)
    self.entry.grid(**self.entry_grid_options)
  
# 왼쪽 프레임
class FormFrame(Frame):
  def __init__(self, *args, **kwargs):
    '''변수 input들이 담기는 Frame입니다'''

    super().__init__(*args, **kwargs)

    # 하위 컴포넌트 그리기
    self.render()
    
  def render(self):
    self.create_forms()

  def create_forms(self):
    label_column_minsize = 200

    labelFrame1 = LabelFrame(self, text='Properties')
    labelFrame1.pack(padx=5, pady=5)
    ofInput11 = OpenformInputFrame(labelFrame1, openform_path='', text='Density')
    ofInput11.columnconfigure(0, minsize=label_column_minsize)
    ofInput11.pack()
    ofInput12 = OpenformInputFrame(labelFrame1, openform_path='', text='Viscosity')
    ofInput12.columnconfigure(0, minsize=label_column_minsize)
    ofInput12.pack()
    ofInput13 = OpenformInputFrame(labelFrame1, openform_path='', text='Surface tension coefficient')
    ofInput13.columnconfigure(0, minsize=label_column_minsize)
    ofInput13.pack()

    labelFrame2 = LabelFrame(self, text='Nozzle Spec')
    labelFrame2.pack(padx=5, pady=5)
    ofInput21 = OpenformInputFrame(labelFrame2, openform_path='', text='Nozzle radius')
    ofInput21.columnconfigure(0, minsize=label_column_minsize)
    ofInput21.pack()
    ofInput22 = OpenformInputFrame(labelFrame2, openform_path='', text='Rotating speed')
    ofInput22.columnconfigure(0, minsize=label_column_minsize)
    ofInput22.pack()
    ofInput23 = OpenformInputFrame(labelFrame2, openform_path='', text='Nozzle velocity')
    ofInput23.columnconfigure(0, minsize=label_column_minsize)
    ofInput23.pack()
    ofInput24 = OpenformInputFrame(labelFrame2, openform_path='', text='Nozzle velocity')
    ofInput24.columnconfigure(0, minsize=label_column_minsize)
    ofInput24.pack()

    labelFrame3 = LabelFrame(self, text='Solution Control')
    labelFrame3.pack(padx=5, pady=5)
    ofInput31 = OpenformInputFrame(labelFrame3, openform_path='', text='Start time')
    ofInput31.columnconfigure(0, minsize=label_column_minsize)
    ofInput31.pack()
    ofInput32 = OpenformInputFrame(labelFrame3, openform_path='', text='End time')
    ofInput32.columnconfigure(0, minsize=label_column_minsize)
    ofInput32.pack()
    ofInput33 = OpenformInputFrame(labelFrame3, openform_path='', text='Time step')
    ofInput33.columnconfigure(0, minsize=label_column_minsize)
    ofInput33.pack()
    ofInput43 = OpenformInputFrame(labelFrame3, openform_path='', text='Write interval')
    ofInput43.columnconfigure(0, minsize=label_column_minsize)
    ofInput43.pack()


# 오른쪽 프레임
class ControlFrame(Frame):
  def __init__(self, *args, **kwargs):
    '''Button 같은 컨트롤 UI들이 담기는 Frame입니다'''
    
    super().__init__(*args, **kwargs)

    # 하위 컴포넌트 그리기
    self.render()

  def render(self):
    self.create_buttons()

  def create_buttons(self):
    Button(self, text="Run", width=6).pack(side=BOTTOM)
    Button(self, text="Mesh", width=6).pack(side=BOTTOM)

# Main Application 입니다.
class Application(Tk):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    
    # 하위 컴포넌트 그리기
    self.render()

  def render(self):
    FormFrame(self).pack(side=LEFT, padx=5, pady=5)
    ControlFrame(self).pack(side=LEFT, fill=Y, padx=10, pady=10)
    
    # Entry(self).grid(column=1)
    # self.JetR = tk.DoubleVar()
    # self.label = tk.Label(self, text="JetR"e)
    # self.label.pack(side='left')
    # self.JetREntry = tk.Entry(self)
    # self.JetREntry['textvariable'] = self.JetR
    # self.JetREntry.pack(side='left')

    # self.hFixedVal = tk.DoubleVar()
    # self.label = tk.Label(self, text="hFixedVal")
    # self.label.pack(side='left')
    # self.hFixedValEntry = tk.Entry(self)
    # self.hFixedValEntry['textvariable'] = self.hFixedVal
    # self.hFixedValEntry.pack(side='left')

    # self.UsMagFixedVal = tk.DoubleVar()
    # self.label = tk.Label(self, text="UsMagFixedVal")
    # self.label.pack(side='left')
    # self.UsMagFixedValEntry = tk.Entry(self)
    # self.UsMagFixedValEntry['textvariable'] = self.UsMagFixedVal
    # self.UsMagFixedValEntry.pack(side='left')
    
    # self.txt.grid(row=0, column=1)
    # btn = Button(root, text="OK", width=15)
    # btn.grid(row=1, column=1)
    # self.hi_there = tk.Button(self)
    # self.hi_there["text"] = "Hello World\n(click me)"
    # self.hi_there["command"] = self.say_hi
    # self.hi_there.pack(side="top")

    # self.saveBtn = tk.Button(self, text="저장", fg="black",
    #                       command=self.save)
    # self.saveBtn.pack(side="bottom")

  # def say_hi(self):
  #   print("hi there, everyone!")

  # def save(self):
  #   inputDict = {}
  #   inputDict['JetR'] = self.JetR.get()
  #   inputDict['hFixedVal'] = self.hFixedVal.get()
  #   inputDict['UsMagFixedVal'] = self.UsMagFixedVal.get()
  #   # print(inputDict)

  #   # transportProperties가 저장될 위치를 지정한다.
  #   write_openform(inputDict, './transportProperties')


app = Application()
app.mainloop()