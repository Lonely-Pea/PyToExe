import tkinter as tk
from tkinter import messagebox as msg, filedialog as fdg
from tkinter import ttk

import os
import time
import random

from threading import Thread

from constant import *
from function import *


class Window(tk.Tk):  # 根窗口
    def __init__(self):
        super().__init__()

        # 变量
        self.screenwidth = self.winfo_screenwidth()
        self.screenheight = self.winfo_screenheight()
        self.x = (self.screenwidth - WINDOW_WIDTH) / 2
        self.y = (self.screenheight - WINDOW_HEIGHT) / 2
        self.size = "%dx%d+%d+%d" % (WINDOW_WIDTH, WINDOW_HEIGHT, self.x, self.y)

        # 设置
        self.set()

        # 刷新
        self.update()

    def set(self):  # 设置窗口
        self.title(WINDOW_TITLE)
        self.geometry(self.size)
        self.resizable(False, False)
        self.iconbitmap(WINDOW_ICON_PATH)


class Desktop(tk.Frame):  # 根窗口界面
    def __init__(self, master):
        super().__init__(master)

        # 变量
        self.master = master

        self.combobox1_var = tk.StringVar()
        self.combobox2_var = tk.StringVar()

        self.combobox1_var.set(COMBOBOX_TEXT[0][0])
        self.combobox2_var.set(COMBOBOX_TEXT[1][0])

        self.checkbutton1_1_var = tk.IntVar()
        self.checkbutton1_2_var = tk.IntVar()
        self.checkbutton1_3_var = tk.IntVar()
        self.checkbutton2_1_var = tk.IntVar()
        self.checkbutton2_2_var = tk.IntVar()

        self.checkbutton1_1_var.set(1)
        self.checkbutton1_2_var.set(0)
        self.checkbutton1_3_var.set(0)
        self.checkbutton2_1_var.set(0)
        self.checkbutton2_2_var.set(0)

        self.file_from_path_var = tk.StringVar()
        self.file_output_path_var = tk.StringVar()
        self.file_icon_path_var = tk.StringVar()

        self.console_order_var = tk.StringVar()

        # 设置
        self.set_place()
        self.combobox()
        self.checkbutton()
        self.change_checkbutton_frame(tool=self.combobox2_var.get())
        self.sidebar()
        self.entry_file()
        self.console_order_entry()
        self.install()
        self.info()

    def combobox(self):
        combobox1 = ttk.Combobox(self, textvariable=self.combobox1_var, values=COMBOBOX_TEXT[0], state="readonly")
        combobox1.place(x=OPTION_GAP, y=OPTION_GAP, width=COMBOBOX_WIDTH, height=COMBOBOX_HEIGHT)
        combobox2 = ttk.Combobox(self, textvariable=self.combobox2_var, values=COMBOBOX_TEXT[1], state="readonly")
        combobox2.place(x=OPTION_GAP * 2 + COMBOBOX_WIDTH, y=OPTION_GAP, width=COMBOBOX_WIDTH, height=COMBOBOX_HEIGHT)

        combobox2.bind("<<ComboboxSelected>>",
                       lambda event: self.change_checkbutton_frame(tool=self.combobox2_var.get()))

    def checkbutton(self):
        global frame1, frame2
        frame_x = OPTION_GAP
        frame_y = OPTION_GAP * 2 + BUTTON_HEIGHT
        frame_width = WINDOW_WIDTH - OPTION_GAP * 2 - BUTTON_WIDTH
        frame_height = OPTION_GAP * 3 + BUTTON_HEIGHT * 2

        frame1 = tk.Frame(self)
        frame2 = tk.Frame(self)

        frame1_checkbutton_1 = ttk.Checkbutton(frame1, text=CHECKBUTTON_TEXT[0][0], variable=self.checkbutton1_1_var)
        frame1_checkbutton_1.place(x=OPTION_GAP, y=OPTION_GAP, width=CHECKBUTTON_WIDTH, height=CHECKBUTTON_HEIGHT)
        frame1_checkbutton_2 = ttk.Checkbutton(frame1, text=CHECKBUTTON_TEXT[0][1], variable=self.checkbutton1_2_var)
        frame1_checkbutton_2.place(x=OPTION_GAP * 2 + CHECKBUTTON_WIDTH, y=OPTION_GAP, width=CHECKBUTTON_WIDTH,
                                   height=CHECKBUTTON_HEIGHT)
        frame1_checkbutton_3 = ttk.Checkbutton(frame1, text=CHECKBUTTON_TEXT[0][2], variable=self.checkbutton1_3_var)
        frame1_checkbutton_3.place(x=OPTION_GAP, y=OPTION_GAP * 2 + CHECKBUTTON_HEIGHT, width=CHECKBUTTON_WIDTH,
                                   height=CHECKBUTTON_HEIGHT)

        frame2_checkbutton_1 = ttk.Checkbutton(frame2, text=CHECKBUTTON_TEXT[1][0], variable=self.checkbutton1_1_var)
        frame2_checkbutton_1.place(x=OPTION_GAP, y=OPTION_GAP, width=CHECKBUTTON_WIDTH, height=CHECKBUTTON_HEIGHT)
        frame2_checkbutton_2 = ttk.Checkbutton(frame2, text=CHECKBUTTON_TEXT[1][1], variable=self.checkbutton1_2_var)
        frame2_checkbutton_2.place(x=OPTION_GAP * 2 + CHECKBUTTON_WIDTH, y=OPTION_GAP, width=CHECKBUTTON_WIDTH,
                                   height=CHECKBUTTON_HEIGHT)

    def change_checkbutton_frame(self, tool):
        frame_x = OPTION_GAP
        frame_y = OPTION_GAP * 2 + BUTTON_HEIGHT
        frame_width = WINDOW_WIDTH - OPTION_GAP * 2 - BUTTON_WIDTH
        frame_height = OPTION_GAP * 3 + BUTTON_HEIGHT * 2
        if tool == COMBOBOX_TEXT[1][0]:
            frame1.place(x=frame_x, y=frame_y, width=frame_width, height=frame_height)
            frame2.place(x=WINDOW_WIDTH, y=frame_y, width=frame_width, height=frame_height)
        elif tool == COMBOBOX_TEXT[1][1]:
            frame2.place(x=frame_x, y=frame_y, width=frame_width, height=frame_height)
            frame1.place(x=WINDOW_WIDTH, y=frame_y, width=frame_width, height=frame_height)
        else:
            msg.showerror(title="错误", message="发生了未知的错误，且程序无法处理！")
            self.master.quit()

    def set_place(self):
        self.place(x=0, y=0, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

    def sidebar(self):
        """
        别问为什么没有button2，问就是写代码的时候删掉了，因为其他变量涉及的地方有点多，于是就没改后面的变量

        """
        global button_3
        frame = tk.Frame(self)
        frame.place(x=WINDOW_WIDTH - OPTION_GAP * 2 - BUTTON_WIDTH, y=0, width=OPTION_GAP * 2 + BUTTON_WIDTH,
                    height=BUTTON_HEIGHT * 4 + OPTION_GAP * 5)

        button_1 = ttk.Button(frame, text="关于", cursor="hand2", command=lambda: self.make_toplevel_about())
        button_1.place(x=OPTION_GAP, y=OPTION_GAP, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        button_3 = ttk.Button(frame, text="生成", cursor="hand2", command=lambda: self.make_exe())
        button_3.place(x=OPTION_GAP, y=OPTION_GAP * 2 + BUTTON_HEIGHT, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        button_4 = ttk.Button(frame, text="打开文件夹", cursor="hand2", command=lambda: self.open_output_dic())
        button_4.place(x=OPTION_GAP, y=OPTION_GAP * 3 + BUTTON_HEIGHT * 2, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

    def make_toplevel_about(self):
        global toplevel_about
        try:
            toplevel_about.destroy()
        except:
            pass
        toplevel_about = ToplevelAbout(master=self.master)

    def make_toplevel_info(self):
        global toplevel_info
        try:
            toplevel_info.destroy()
        except:
            pass
        toplevel_info = ToplevelInfo(master=self.master)

    def entry_file(self):  # 获取文件基本信息框架
        """
        文件导入地址
        文件导出地址
        文件图标地址(可不填)
        软件名称(可不填)

        """

        frame_x = OPTION_GAP
        frame_y = BUTTON_HEIGHT * 4 + OPTION_GAP * 4
        frame_width = OPTION_GAP * 6 + ENTRY_WIDTH + BUTTON_WIDTH * 2 + LABEL_WIDTH
        frame_height = BUTTON_HEIGHT * 3 + OPTION_GAP * 4

        label_x = OPTION_GAP
        entry_x = OPTION_GAP * 2 + LABEL_WIDTH
        button_x = OPTION_GAP * 3 + LABEL_WIDTH + ENTRY_WIDTH
        button_x_ = button_x + OPTION_GAP + BUTTON_WIDTH

        frame = tk.Frame(self)
        frame.place(x=frame_x, y=frame_y, width=frame_width, height=frame_height)

        label_1 = tk.Label(frame, text="文件导入地址：", anchor="w")
        label_1.place(x=label_x, y=OPTION_GAP, width=LABEL_WIDTH, height=LABEL_HEIGHT)
        label_2 = tk.Label(frame, text="文件导出地址(nuitka)：", anchor="w")
        label_2.place(x=label_x, y=OPTION_GAP * 2 + LABEL_HEIGHT, width=LABEL_WIDTH, height=LABEL_HEIGHT)
        label_3 = tk.Label(frame, text="文件图标地址(可不填)：", anchor="w")
        label_3.place(x=label_x, y=OPTION_GAP * 3 + LABEL_HEIGHT * 2, width=LABEL_WIDTH, height=LABEL_HEIGHT)

        entry_1 = ttk.Entry(frame, textvariable=self.file_from_path_var)
        entry_1.place(x=entry_x, y=OPTION_GAP, width=ENTRY_WIDTH, height=ENTRY_HEIGHT)
        entry_2 = ttk.Entry(frame, textvariable=self.file_output_path_var)
        entry_2.place(x=entry_x, y=OPTION_GAP * 2 + ENTRY_HEIGHT, width=ENTRY_WIDTH, height=ENTRY_HEIGHT)
        entry_3 = ttk.Entry(frame, textvariable=self.file_icon_path_var)
        entry_3.place(x=entry_x, y=OPTION_GAP * 3 + ENTRY_HEIGHT * 2, width=ENTRY_WIDTH, height=ENTRY_HEIGHT)

        button_1 = ttk.Button(frame, text="浏览", cursor="hand2", command=lambda: self.choose_file_from())
        button_1.place(x=button_x, y=OPTION_GAP, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        button_1_ = ttk.Button(frame, text="清空", cursor="hand2", command=lambda: self.file_from_path_var.set(""))
        button_1_.place(x=button_x_, y=OPTION_GAP, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

        button_2 = ttk.Button(frame, text="浏览", cursor="hand2", command=lambda: self.choose_file_output())
        button_2.place(x=button_x, y=OPTION_GAP * 2 + BUTTON_HEIGHT, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        button_2_ = ttk.Button(frame, text="清空", cursor="hand2", command=lambda: self.file_output_path_var.set(""))
        button_2_.place(x=button_x_, y=OPTION_GAP * 2 + BUTTON_HEIGHT, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

        button_3 = ttk.Button(frame, text="浏览", cursor="hand2", command=lambda: self.choose_file_icon())
        button_3.place(x=button_x, y=OPTION_GAP * 3 + BUTTON_HEIGHT * 2, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        button_3_ = ttk.Button(frame, text="清空", cursor="hand2", command=lambda: self.file_icon_path_var.set(""))
        button_3_.place(x=button_x_, y=OPTION_GAP * 3 + BUTTON_HEIGHT * 2, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

    def choose_file_from(self):
        file_path = fdg.askopenfilename(title="选择文件导入地址", filetypes=[("Py", ".py")])
        if file_path.strip() != "":
            self.file_from_path_var.set(file_path)
        else:
            msg.showinfo(title="PyToExe", message="已取消选择文件倒入地址。请注意选择文件导入地址，防止转换失败！")

    def choose_file_output(self):
        output_dir = fdg.askdirectory(title="选择文件导出地址(仅nuitka有效)")
        if output_dir.strip() != "":
            self.file_output_path_var.set(output_dir)
        else:
            msg.showinfo(title="PyToExe", message="已取消选择文件导出地址。请注意选择文件导出地址，防止转换失败！")

    def choose_file_icon(self):
        icon_path = fdg.askopenfilename(title="选择文件图标地址(可不选)", filetypes=[("ICO", ".ico")])
        if icon_path.strip() != "":
            self.file_icon_path_var.set(icon_path)
        else:
            msg.showinfo(title="PyToExe", message="已取消选择文件图标地址。建议选择文件图标，使软件更加个性化。")

    def console_order_entry(self):  # 查看当前代码
        label = tk.Label(self, text="当前代码：", anchor="w")
        label.place(x=OPTION_GAP * 2, y=BUTTON_HEIGHT * 7 + OPTION_GAP * 9, width=LABEL_WIDTH, height=LABEL_HEIGHT)

        entry = ttk.Entry(self, textvariable=self.console_order_var)
        entry.place(x=OPTION_GAP * 3 + LABEL_WIDTH, y=BUTTON_HEIGHT * 7 + OPTION_GAP * 9,
                    width=ENTRY_WIDTH * 3 + OPTION_GAP * 2, height=ENTRY_HEIGHT)

    def info(self):  # 左下角提示
        thread_change = Thread(target=self.change_info_label, args=())
        thread_change.start()

    def change_info_label(self):  # 改变左下角提示文字
        label = tk.Label(self, anchor="w")
        label.place(x=0, y=WINDOW_HEIGHT - LABEL_HEIGHT, width=WINDOW_WIDTH, height=LABEL_HEIGHT)
        n = 0
        while True:
            n_ = random.randint(0, len(INFO_LABEL_TEXTS)-1)
            if n_ == n:
                break
            else:
                n = n_
                label.config(text=INFO_LABEL_TEXTS[n])
                time.sleep(10)

    def make_exe(self):  # 生成
        file_from_path = self.file_from_path_var.get()
        file_output_path = self.file_output_path_var.get()
        file_icon_path = self.file_icon_path_var.get()
        tool = self.combobox2_var.get()
        module = self.combobox1_var.get()
        if_python = self.checkbutton1_1_var.get()
        one_file = [self.checkbutton1_2_var.get(), self.checkbutton2_1_var.get()]
        if_cmd = [self.checkbutton1_3_var.get(), self.checkbutton2_2_var.get()]
        if file_from_path == "":
            msg.showerror(title="提示", message="请先填好文件导入地址，否则软件将转换失败！")
        elif file_output_path == "" and tool == COMBOBOX_TEXT[1][0]:
            msg.showerror(title="提示", message="请先填好文件导出地址，否则软件将转换失败！")
        else:
            text = make_file(file_from_path, file_output_path, file_icon_path, tool, module, if_python, one_file,
                             if_cmd)
            # print(text)
            button_3.config(command=lambda: msg.showinfo(title="提示", message="当前转换中！请勿重复操作！"))
            self.console_order_var.set(text)
            self.master.update()
            time.sleep(0.5)
            os.system(self.console_order_var.get())
            button_3.config(command=lambda: self.make_exe())
            if tool == COMBOBOX_TEXT[1][1]:
                msg.showinfo(title="提示", message="已经成功保存到软件所在目录！请注意查看！文件夹名称与.py文件名称相同！")

    def open_output_dic(self):  # 打开文件夹
        file_output_path = self.file_output_path_var.get()
        if file_output_path == "":
            msg.showerror(title="提示", message="您还未选择文件导出地址！")
        else:
            os.system("explorer \"%s\"" % file_output_path.replace("/", "\\"))

    def install(self):  # 安装
        msg.showinfo(title="提示", message="接下来将安装pyinstaller和nuitka，如果你已安装可以忽略。")
        install_pyinstaller_and_nuitka()
        msg.showinfo(title="提示", message="程序运行完毕，请对照cmd窗口的消息来判断是否安装成功！")


class ToplevelAbout(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)

        # 变量
        self.master = master
        self.title_ = "关于软件"

        self.x = self.master.winfo_x()
        self.y = self.master.winfo_y()

        # 设置
        self.set()
        self.texts()

    def set(self):  # 设置窗口
        self.title(self.title_)
        self.geometry("%dx%d+%d+%d" % (TOPLEVEL_WIDTH, TOPLEVEL_HEIGHT, self.x, self.y))
        self.resizable(False, False)
        self.iconbitmap(WINDOW_ICON_PATH)

    def texts(self):  # 设置文字
        text = tk.Label(self, text=ABOUT_TEXT, justify="left")
        text.place(x=0, y=0, width=TOPLEVEL_WIDTH, height=TOPLEVEL_HEIGHT-BUTTON_HEIGHT*2)

        button = ttk.Button(self, text="确定", command=lambda: self.destroy())
        button.place(x=TOPLEVEL_WIDTH - BUTTON_WIDTH - OPTION_GAP, y=TOPLEVEL_HEIGHT - BUTTON_HEIGHT - OPTION_GAP,
                     width=BUTTON_WIDTH, height=BUTTON_HEIGHT)


class ToplevelInfo(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)

        # 变量
        self.master = master
        self.title_ = "帮助信息"

        self.x = self.master.winfo_x()
        self.y = self.master.winfo_y()

        # 设置
        self.set()
        self.texts()

    def set(self):  # 设置窗口
        self.title(self.title_)
        self.geometry("%dx%d+%d+%d" % (TOPLEVEL_WIDTH, TOPLEVEL_HEIGHT, self.x, self.y))
        self.resizable(False, False)
        self.iconbitmap(WINDOW_ICON_PATH)

    def texts(self):  # 设置文字
        text = tk.Label(self, text=INFO_TEXT, justify="left")
        text.place(x=0, y=0, width=TOPLEVEL_WIDTH, height=TOPLEVEL_HEIGHT - BUTTON_HEIGHT * 2)

        button = ttk.Button(self, text="确定", command=lambda: self.destroy())
        button.place(x=TOPLEVEL_WIDTH - BUTTON_WIDTH - OPTION_GAP, y=TOPLEVEL_HEIGHT - BUTTON_HEIGHT - OPTION_GAP,
                     width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
