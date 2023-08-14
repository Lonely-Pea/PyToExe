# PyToExe
## Introduction
PyToExe is software based on Python.<br>
It can help you package python files into executable programs.<br>
And it provides a interface that you can just click to package python files.<br>
It calls pyinstaller and nuitka to help packaging your files.<br>
Now the lauguage of the software is Chinese 'cause the maker is from China.(So this file may have a lot of grammar mistakes.)<br>
Now you still cannot change the display lauguage 'cuase I'v not set a lauguage file.<br>
Just Wait.<br>
## Principle
The interface of the software is based on Python module tkinter.<br>
To package python files into executable programs, it calls pyinstaller or nuitka.<br>
## Code Explanation
### Modules Needed
Here is all the modules this program need and their purposes:<br>

|modules|purposes|
|:---|:---|
|tkinter|interface based|
|tkinter.messagebox|message popup|
|tkinter.ttk|interface based|
|os|system orders called|
|time|animation needed|
|threading|more threads builded|
|random|random number made|

### self_builede Modules
Here is all the self-builded modules and their purposes:<br>

|modules|purposes|
|:---|:---|
|constant|constant saved|
|option|interface builded|
|function|packaging|

### How To Run the Program
To run this program,you need to run file main.py

### File main.py
In file main.py,we use these codes to build the interface and functions:<br>

~~~python
if __name__ == "__main__":
  window = Window()  # build root window
  desktop = Desktop(master=window)  # build interface

  window.mainloop()  # display the root window
~~~

Variable *window* is the earth for all the things work on.

### File constant.py
In file constant.py,I write some variables into it.<br>
Like this:<br>

~~~python
INSTALL_TEXT = [
  "pip install pyinstaller",
  "pip install nuitka"
]
~~~

These strings are to install pyinstaller and nuitka for packaging.<br>

### File function.py
In file function.py,we build a function:<br>
> make_file(file_from_path, file_output_path="", file_icon_path="", tool="pyinstaller", module="Basic", if_python=False, one_file=(False, True),
if_cmd=(False, False))

to build executable programs.<br>
We just convert parameters into codes and rutuen final result *test*<br>
Like this:<br>

~~~python
text = ""
if tool == COMBOBOX_TEXT[1][1]:  # pyinstaller called
  text += COMBOBOX_TEXT[1][1]  # write "pyinstaller" at the front
  if one_file[1]:  # one_file setted
    text += " %s" % PYINSTALLER_TEXTS[1]  # write "-w" behind "pyinstaller"
~~~

### File option.py
In file option.py,we build the interface of the program.The place with the most codes is just here.<br>

Here is all the class and their purposes in the file:<br>

|class|purposes|
|:---|:---|
|Window(tk.Tk)|root window builded|
|Desktop(tk.Frame)|main interface builded|
|ToplevelAbout(tk.Toplevel)|build About window|
|ToplevelInfo(tk.Toplevel)|build help window|

#### Window(tk.Tk)
In this class, there is a function called set(self) that can set the root window.

Here are the explanations of the codes:<br>

~~~python
self.screenwidth = self.winfo_screenwidth()
self.screenheight = self.winfo_screenheight()
self.x = (self.screenwidth - WINDOW_WIDTH) / 2
self.y = (self.screenheight - WINDOW_HEIGHT) / 2
self.size = "%dx%d+%d+%d" % (WINDOW_WIDTH, WINDOW_HEIGHT, self.x, self.y)
~~~

Get the width and the height of the screen:
> self.screenwidth = self.winfo_screenwidth()
>
> self.screenheight = self.winfo_screenheight()

Get the x coordinate and y coordinate:
> self.x = (self.screenwidth - WINDOW_WIDTH) / 2
>
> self.y = (self.screenheight - WINDOW_HEIGHT) / 2

#### Desktop(tk.Frame)
In this class, also the-most-code-written place, we build the main interface.<br>

Here is all the functions that are called in \_\_init\_\_(self, master) ,the functions these functions called in this class,  the variable globalized in there functions and the variable there functions needed:<br>

|function|function called|variable globalized|variable needed|
|:---|:---|:---|:---|
|set_place()|/|/|/|
|set_combobox()|self.change_checkbutton_frame(tool)|/|self.combobox1_var<br>self.combobox2_var|
|checkbutton()|/|frame1<br>frame2|self.checkbutton1_1_var<br>self.checkbutton1_2_var<br>self.checkbutton1_3_var|
|change_checkbutton_frame(tool)|/|/|/|
|sidebar()|self.make_toplevel_about()<br>self.make_code()<br>self.make_exe()<br>self.open_output_dic()|button_3|/|
|entry_file|self.choose_file_from()<br>self.choose_file_output()<br>self.choose_file_icon()|/|self.file_from_path_var<br>self.file_output_path_var<br>self.file_icon_path_var|
|console_order_entry()|/|/|self.console_order_var|
|install()|/|/|/|
|info()|self.change_info_label()|/|/|

There are a bit too much.It doesn't matter.Just let me introduce some of them.

##### info()
I think you know how to make interface by tkinter, so I won't introduce the functions of building tkinter interface.(The true reason is that I'm a bit lazy.)<br>

Now I only introduce the Function info().Look at the codes first:<br>
> thread_change = Thread(target=self.change_info_label, args=())
>
> thread_change.start()

These codes are to build a now thread to make the main program not getting caton.

We know this function called a new function called self.change_info_label().<br>
Then let we just check out this function.<br>

###### self.change_info_label()
~~~python
n = 0
while True:
  n_ = random.randint(0, len(INFO_LABEL_TEXTS)-1)
  if n_ == n:
    continue
  else:
    n = n_
    self.entry_var.set(INFO_LABEL_TEXTS[n])
    self.master.update()
    time.sleep(10)
~~~
Look at the codes above.<br>
We first make a temporary variable called *n*.<br>
Then, we build a *while* circulate.<br>
In this circulate, we first make a random number as the index of the list.<br>
If the random number *n_* is as same as *n*, we just "while" again.<br>
Then we use the index to choose the element in the list and take it as the element of the variable self.entry_var.<br>
Then, we use the module time and its function sleep() to pause the thread for 10 seconds.<br>
Then, the next "while" again.<br>
It is not difficult if you now a little of python grammar.<br>

#### ToplevelAbout(tk.Toplevel) and ToplevelInfo(tk.Toplevel)
As you know, they are seem to be same.So I just choose one of them for the introduction.<br>

Building window is like the steps in class Window(tk.Tk)<br>
building label to show the about information is a bit easy.

Something we need to know is that we can change the value of the element justify in the class tk.Label().<br>
Like this:<br>

> text = tk.Label(self, text=ABOUT_TEXT, justify="left")
>
> text.place(x=0, y=0, width=TOPLEVEL_WIDTH * 3)

Here are the differences of *justify* and *anchor*:<br>

|element|value|purpose|
|:---|:---|:---|
|justify|left<br>right<br>center<br>|For lines|
|anchor|e<br>w<br>n<br>s<br>ne<br>se<br>nw<br>sw<br>center|for one line|

Here are the means of the possible values of the element *anchor*:<br>
|value|mean|
|:---|:---|
|e|East|
|w|West|
|n|north|
|s|south|
|ne|northeast|
|se|southeast|
|nw|northwest|
|sw|southwest|
|center|center|

## Download
### Codes Downloaded
1. Github:
  1. [Codes on Github(the lastest)](https://github.com/Lonely-Pea/PyToExe.git "Click to download")
2. Lanzouy:
  1. [PyToExe Build 230804 v1.0.0](https://wwcs.lanzouy.com/ifvRo14rzrlg "Click to download")
  2. [PyToExe Build 230813 v1.1.0](https://wwcs.lanzouy.com/iAy9f15ajtsd "Click to download")

### Executable Porgrams Downloaded
1. Lanzouy:
  1. [PyToExe Build 230804 v1.0.0](https://wwcs.lanzouy.com/ib5RM14rzs9a "Click to download")
  2. [PyToExe Build 230813 v1.1.0](https://wwcs.lanzouy.com/iInhb15ajusj "Click to download")

## PyToExe Official Website
[PyToExe Official Website](https://lonely-pea.github.io/PyToExeWeb "Click to go to")

## Bug Feedback
Send email to <lonely-pea@qq.com> to give bug feedback or your suggestions.
If you don't get something well, you can also ask me by sending email to this mainbox.

## Software Screenshot
Here are the screenshots of this software(version: Build 230813 v1.1.0):<br>
![Screenshot_1](Screenshot/screenshot_1.png "Main interface")

![Screenshot_2](Screenshot/screenshot_2.png "About interface")

![Screenshot_3](Screenshot/screenshot_3.png "Help interface")

## thanks
Thank Lonely-Pea for programming.<br>
Thank Everybody who give supports for this program.<br>
Could you star it if you think it is a excellent program?<br>
