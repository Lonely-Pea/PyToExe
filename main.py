import tkinter as tk
from tkinter import messagebox as msg, filedialog as fdg
from tkinter import ttk

import os
import time

from constant import *
from option import *


# 测试
if __name__ == "__main__":
    window = Window()  # 生成根窗口
    desktop = Desktop(master=window)

    window.mainloop()
