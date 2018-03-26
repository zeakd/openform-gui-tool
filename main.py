from tkinter import *
from string import Template

def saveFoamFiles(valueDict):
  """
  주어진 초안은 세개의 파일을 다루고 있습니다. 더 수정하는 파일이 생길경우 tmpl파일과 dest를 각각 추가해주십시오.
  또한 같은 파일 속에서 variable이 늘어날 경우 tmpl파일을 수정해야합니다.
  """
  writeTemplateTo('./templates/controlDict.tmpl', './dest/controlDict', valueDict)
  writeTemplateTo('./templates/physicalParameters.tmpl', './dest/physicalParameters', valueDict)
  writeTemplateTo('./templates/transportProperties.tmpl', './dest/transportProperties', valueDict)

def writeTemplateTo(tmplPath, destPath, keyDict):
  """
  tmplPath의 template 파일을 읽어들여 keyDict로 채우고 destPath에 파일을 생성합니다.
  """

  with open(tmplPath, 'r') as tmplFile:
    tmpl = Template(tmplFile.read())

  with open(destPath, 'w') as destFile:
    print(tmpl.substitute(keyDict), file=destFile)

class Application(Tk):
  """
  Main Application 입니다.
  """

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    self.variables = {}

    # template에 필요한 variables 생성
    # 배열로 초기화할 경우 벡터로 간주하여 처리합니다.
    self.variables["rhol"] = DoubleVar()
    self.variables["mul"] = DoubleVar()
    self.variables["sigma"] = DoubleVar()
    self.variables["JetR"] = DoubleVar()
    self.variables["UMagFixedVal"] = DoubleVar()
    self.variables["NozzleMotionDir"] = [DoubleVar(), DoubleVar(), DoubleVar()]
    self.variables["Omega"] = [DoubleVar(), DoubleVar(), DoubleVar()]
    self.variables["startTime"] = DoubleVar()
    self.variables["endTime"] = DoubleVar()    
    self.variables["deltaT"] = DoubleVar()
    self.variables["writeInterval"] = IntVar()

    # render를 새로할 경우 clear 필요.
    self.labelFrames = []

    self.render()

  def renderMainFrame(self):
    """
    Variables가 그려지는 메인 프레임을 생성, 추가합니다.
    """
    self.MainFrame = Frame(self)
    self.MainFrame.pack(side=LEFT, fill=BOTH, expand=1)

  def renderButtonsFrame(self):
    """
    버튼들이 모인 프레임을 생성, 추가합니다.
    """
    self.ButtonsFrame = Frame(self)
    self.ButtonsFrame.pack(side=LEFT, fill=BOTH)
    self.runButton = Button(self.ButtonsFrame, text='Run', command=self.run)
    self.runButton.pack(side=BOTTOM)
    self.meshButton = Button(self.ButtonsFrame, text='Mesh')
    self.meshButton.pack(side=BOTTOM)

  def renderLabelFrameToMain(self, label, variables):
    """
    메인프레임에 LabelFrame과 그의 variables를 추가합니다.
    """

    # variable의 label의 최소 크기
    variableLabelColumnMinsize=200

    # main frame 안에 들어가는 label Frame 생성
    labelFrame = LabelFrame(self.MainFrame, text=label)

    # column 설정
    labelFrame.columnconfigure(0, minsize=variableLabelColumnMinsize)
    labelFrame.columnconfigure(1, weight=1)

    # label frame 을 pack.
    labelFrame.pack(fill=X)

    # label frame 안에 들어가는 변수들의 UI 생성 (Label, Entry)
    # ex)
    # ┌──────────────────────────────────────────┐
    # │ ┌───LableFrame─────────────────────────┐ │
    # │ │                  ┌─────────────────┐ │ │
    # │ │      Label       │     Variable    │ │ │
    # │ │                  └─────────────────┘ │ │
    # │ │                ● ● ●                 │ │
    # │ └──────────────────────────────────────┘ │
    # └──────────────────────────────────────────┘
    #
    # variables는 반드시 list로 받는다.
    for index, variable in enumerate(variables):

      # variable의 형태 정의
      (label, Var) = variable

      # 좌측 Label 생성 
      l = Label(labelFrame, text=label)
      l.grid(row=index+1, column=0)

      # 우측 entry(variables)의 frame 생성
      entryFrame = Frame(labelFrame)
      entryFrame.grid(row=index+1, column=1, sticky=N+W+E+S)

      # 주어진 variable이 list일 경우.
      if (isinstance(Var, list)):
        for v in Var:
          e = Entry(entryFrame)
          e['textvariable'] = v
          e.pack(side=LEFT, fill=X, expand=1)

      # 단일 variable일 경우
      else:
        e = Entry(entryFrame)
        e['textvariable'] = Var
        e.pack(side=LEFT, fill=X, expand=1)

    # 관리를 위한 단순 추가.
    self.labelFrames.append(labelFrame)

  # app을 그리는 로직.
  def render(self):
    self.renderMainFrame()
    self.renderButtonsFrame()
    
    self.renderLabelFrameToMain('Properties', [
      ('Density', self.variables["rhol"]),
      ('Viscosity', self.variables["mul"]),
      ('Surface tension coefficient', self.variables["sigma"])
    ])

    self.renderLabelFrameToMain('Nozzle Spec', [
      ('Nozzle radius', self.variables["JetR"]),
      ('Rotating speed', self.variables["Omega"]),
      ('Nozzle velosity', self.variables["UMagFixedVal"]),
      ('Nozzle direction', self.variables["NozzleMotionDir"])
    ])

    self.renderLabelFrameToMain('Solution Control', [
      ('Start time', self.variables["startTime"]),
      ('End time', self.variables["endTime"]),
      ('Time step', self.variables["deltaT"]),
      ('Writing interval', self.variables["writeInterval"])
    ])

  def save(self):
    """
    self.variables를 순회하여 template에 적합한 dict를 생성한후 FOAM의 파일을 생성한다.
    """

    # template에 전달될 dictionary
    valueDict = {}
    
    for key, value in self.variables.items():
      # Variables가 list일 때는 순회하여 벡터로 만든다.
      if isinstance(value, list):
        valueDict[key] = "(" + " ".join([str(v.get()) for v in value]) + ")"

      # 단일 variables일 경우 단순히 추가한다.
      else:
        valueDict[key] = value.get()
    
    # template을 통해 foam파일을 저장한다.
    saveFoamFiles(valueDict)

  def run(self):
    self.save()

if __name__ == '__main__':
  app = Application()
  app.mainloop()