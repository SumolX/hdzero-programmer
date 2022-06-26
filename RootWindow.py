#from msilib.schema import Font
import os
import tkinter as tk
from tkinter import HORIZONTAL, VERTICAL, ttk
from Download import LoadGithubFirmwareRequest

version = "0.1"


class UI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.CreateRootWindow()
        self.CreateSeparator()
        self.CreateLabel()
        self.CreateLoadButton()
        self.CreateDetectButton()
        self.CreateDefineTargetButton()
        self.CreateFlashButton()

    def CreateRootWindow(self):
        titleString = "HDZero Programmer"+" v"+version
        iconPath = 'Data/HDZero_16.ico'
        windowX = 720
        windowY = 720
        offsetX = (self.winfo_screenwidth() - windowX)/2
        offsetY = (self.winfo_screenheight() - windowY)/2
        self.geometry('%dx%d+%d+%d' % (windowX, windowY, offsetX, offsetY))
        self.resizable(False, False)
        self.title(titleString)
        if os.path.exists(iconPath):
            self.iconbitmap(iconPath)

    def CreateSeparator(self):
        sep_hor1 = ttk.Separator(self, orient=HORIZONTAL)
        sep_hor1.anchor = 'NW'
        sep_hor1.place(width=720, height=1, x=0, y=400)
        sep_hor2 = ttk.Separator(self, orient=HORIZONTAL)
        sep_hor2.anchor = 'NW'
        sep_hor2.place(width=720, height=1, x=0, y=690)
        sep_ver1 = ttk.Separator(self, orient=VERTICAL)
        sep_ver1.anchor = 'NW'
        sep_ver1.place(width=1, height=400, x=300, y=0)

    def LoadGithubButtonCommand(self):
        LoadGithubFirmwareRequest()

    def CreateLoadButton(self):
        buttonLoadGithubString = "Load Firmware[Github]"
        LoadGithubButton = ttk.Button(self, text=buttonLoadGithubString,
                                      command=self.LoadGithubButtonCommand)
        LoadGithubButton.anchor = 'NW'
        LoadGithubButton.place(x=310, y=370)

        buttonLoadLocalString = "Load Firmware[Local]"
        reloadButton = ttk.Button(self, text=buttonLoadLocalString,
                                  command=self.LoadGithubButtonCommand)
        reloadButton.anchor = 'NW'
        reloadButton.place(x=460, y=370)

    def CreateFlashButton(self):
        buttonFlashString = "Flash"
        FlashButton = ttk.Button(self, text=buttonFlashString,
                                 command=self.LoadGithubButtonCommand)
        FlashButton.anchor = 'NW'
        FlashButton.place(x=610, y=370)

    def CreateDetectButton(self):
        buttonDetectString = "Detect"
        DetectButton = ttk.Button(self, text=buttonDetectString,
                                  command=self.LoadGithubButtonCommand)
        DetectButton.anchor = 'NW'
        DetectButton.place(x=110, y=370)

    def CreateDefineTargetButton(self):
        buttonDefineTargetString = "Define Target"
        DefineTargetButton = ttk.Button(self, text=buttonDefineTargetString,
                                        command=self.LoadGithubButtonCommand)
        DefineTargetButton.anchor = 'NW'
        DefineTargetButton.place(x=630, y=692)

    def CreateLabel(self):
        targetLabelString = "Target"
        targetLabel = tk.Label(self, text=targetLabelString, bg="dimgray",
                               fg="white", font=("Consolas", 15, "bold"))
        targetLabel.anchor = 'NW'
        targetLabel.place(x=110, y=10)

        firmwareLabelString = "Firmware"
        firmwareLabel = tk.Label(self, text=firmwareLabelString, bg="dimgray",
                                 fg="white", font=("Consolas", 15, "bold"))
        firmwareLabel.anchor = 'NW'
        firmwareLabel.place(x=460, y=10)

        messageLabelString = "Message"
        messageLabel = tk.Label(self, text=messageLabelString, bg="dimgray",
                                fg="white", font=("Consolas", 15, "bold"))
        messageLabel.anchor = 'NW'
        messageLabel.place(x=10, y=410)

        statusLabelString = "Status"
        statusLabel = tk.Label(self, text=statusLabelString, bg="dimgray",
                               fg="white", font=("Consolas", 10, "bold"))
        statusLabel.anchor = 'NW'
        statusLabel.place(x=5, y=695)


def UI_mainloop():
    UI().mainloop()
