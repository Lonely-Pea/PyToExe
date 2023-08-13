"""
生成exe的相关方法
安装pyinstaller和nuitka

"""
import os
from constant import *


def make_file(file_from_path, file_output_path="", file_icon_path="", tool="pyinstaller",
              module="Basic", if_python=False, one_file=(False, True), if_cmd=(False, False)):
    text = ""
    if tool == COMBOBOX_TEXT[1][1]:  # pyinstaller
        text += COMBOBOX_TEXT[1][1]
        if one_file[1]:
            text += " %s" % PYINSTALLER_TEXTS[1]
        if if_cmd[1]:
            text += " %s" % PYINSTALLER_TEXTS[4]
        if file_icon_path != "":
            text += " %s \"%s\"" % (PYINSTALLER_TEXTS[2], file_icon_path)
        text += " \"%s\"" % file_from_path
    elif tool == COMBOBOX_TEXT[1][0]:  # nuitka
        text += COMBOBOX_TEXT[1][0]
        if one_file[0]:
            text += " %s" % NUITKA_TEXTS[5]
        if if_cmd:
            text += " %s" % NUITKA_TEXTS[1]
        if if_python:
            text += " %s" % NUITKA_TEXTS[0]
        if module == COMBOBOX_TEXT[0][1]:
            text += " %s%s" % (NUITKA_TEXTS[3], "tk-inter")
        if module == COMBOBOX_TEXT[0][2]:
            text += " %s%s" % (NUITKA_TEXTS[3], COMBOBOX_TEXT[0][2])
        if file_icon_path != "":
            text += " %s\"%s\"" % (NUITKA_TEXTS[4], file_icon_path)
        text += " %s\"%s\"" % (NUITKA_TEXTS[2], file_output_path)
        text += " \"%s\"" % file_from_path
    return text


def install_pyinstaller_and_nuitka():
    os.system(INSTALL_TEXT[0])
    os.system(INSTALL_TEXT[1])
