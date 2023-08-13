"""
常量

"""

WINDOW_TITLE = "PyToExe"
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300
WINDOW_ICON_PATH = "ico//icon.ico"

TOPLEVEL_WIDTH = 200
TOPLEVEL_HEIGHT = 150

OPTION_GAP = 5

LABEL_WIDTH = 145
LABEL_HEIGHT = 25

BUTTON_WIDTH = 75
BUTTON_HEIGHT = 25

ENTRY_WIDTH = 75
ENTRY_HEIGHT = 25

COMBOBOX_WIDTH = 100
COMBOBOX_HEIGHT = 25

CHECKBUTTON_WIDTH = 125
CHECKBUTTON_HEIGHT = 25

COMBOBOX_TEXT = [
    ["基本", "tkinter", "pyqt5"],
    ["nuitka", "pyinstaller"]
]

CHECKBUTTON_TEXT = [
    ["脱离python环境", "打包为单个文件", "不显示cmd窗口"],  # nuitka
    ["打包为单个文件", "不显示cmd窗口"]  # pyinstaller
]

NUITKA_TEXTS = ["--standalone", "--windows-disable-console", "--output-dir=", "--plugin-enable=",
                "--windows-icon-from-ico=", "--onefile"]

PYINSTALLER_TEXTS = ["-D", "-F", "-i", "-n", "-w"]

INSTALL_TEXT = [
    "pip install pyinstaller",
    "pip install nuitka"
]

INFO_LABEL_TEXTS = [
    "第一次运行软件时会自动安装pyinstaller和nuitka",
    "在安装nuitka的时候需要你在弹出的窗口内输入文字，请全部输入yes",
    "在安装nuitka的时候请准备好加速器，用来加速访问github",
    "如果提示安装失败，请手动安装",
    "如果安装nuitka时反复失败，请检查所需的程序是否准备好",
    "你的电脑操作系统上最好安装好python3",
    "转换的时候可能会卡，这些是正常的",
    "文件导出地址一栏为nuitka专用",
    "用pyinstaller转换成功后程序保存在软件安装目录内",
    "用pyinstaller转换成功后程序保存的目录名称为程序名称+.dist",
    "转换时请确保电脑上已经安装了文件所需的库",
    "转换过程可能失败，如果失败请检查程序是否有错误",
    "如果用pyinstaller转换过程中提示icon错误，请检查引入的icon文件",
    "转换完成后请将所有文件复制到程序目录",
    "如果你不想点来点去，你可以直接填写\"当前代码栏\"生成",
    "软件官网:https://lonely-pea.github.io/PyToExeWeb",
    "软件版本:Build 230804 v1.0.0",
    "软件制作:Lonely-Pea",
    "如有更好的意见或bug，请往邮箱:lonely-pea@qq.com发送邮件",
    "感谢你使用该软件"
]

ABOUT_TEXT = """
制作人：Lonely-Pea
版本：Build 230813 v1.1.0

相较于v1.0.0新增：
1.增加了生成代码功能并且可以通过修改代码来修改生成方式，也可以直接修改代码框的区域来生成。
2.增加了左下角帮助信息一键全部查看。
3.更改了左下角提示生成方式。
4.修改了文件或文件夹目录内有空格不能打包成功的bug
（小版本更新）

详见左下角！
感谢你对本软件的使用！

"""
