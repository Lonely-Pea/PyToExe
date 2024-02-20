# PyToExe

> <a herf="./README_CN.md">����˵��</a> || <a herf="/README.md">English</a>
> ���ߣ�@BiliBiliSmallball

## �������

PyToExe �ǻ��� Python �������<br>
�����԰������� python �ļ�����ɿ�ִ�г���<br>
���ṩ��һ�� GUI ���棬�����Զ���������ֻ�赥�����ɴ�� python �ļ���<br>
��������� pyinstaller �� nuitka ����������ļ���<br>
���ڸ��������;�����ĵģ���Ϊ���ߺ����������й�������������ļ������кܶ��﷨����<br>
���ڣ�����Ȼ�޷�������ʾ���ԣ���Ϊ��û�н������Ե����á�<br>
��ȴ����ǵĸ���<br>

## ����ԭ�������

��������� Python ģ�� tkinter ���й�����<br>
Ҫ�� python �ļ�����ɿ�ִ�г���������� pyinstaller �� nuitka��<br>

## ����˵��

### ��Ҫ��ģ��

�����Ǹó������������ģ�鼰����;��<br>  
|��|��;|
|:---|:---|
|tkinter|interface based|
|tkinter.messagebox|message popup|
|tkinter.ttk|interface based|
|os|system orders called|
|time|animation needed|
|threading|more threads builded|
|random|random number made|

### self_builede ģ��

�����������Խ�ģ�鼰����;��<br>

| ģ��     | ��;              |
| :------- | :---------------- |
| constant | constant saved    |
| option   | interface builded |
| function | packaging         |

### ���ʹ�øó���

��� `main.py`ʹ��<div style="font-size:10px">Ϊɶ�����Ŀ�����һ�£�</div>

### File main.py

��ģ�� `main.py`��,����ʹ����Щ�����������ӿںͺ���:<br>

```python
if __name__ == "__main__":
  window = Window()  # ����������
  desktop = Desktop(master=window)  #�����ӿ�

  window.mainloop()  #��ʾ������
```

���� _window_ �����й���ʵ�ֵĻ���������������Ĺ������ڶ��� window �и��Ļ�����������

### File constant.py

����Ŀ`constant.py`��,��д��һЩ���ò���������.<br>
����:<br>

```python
INSTALL_TEXT = [
  "pip install pyinstaller",
  "pip install nuitka"
]
```

��Щ�ַ������ڰ�װ pyinstaller �� nuitka ���д����<br>

### function.py

���ļ� function.py �У����ǹ���һ������<br>

> make_file��file_from_path�� file_output_path=������ file_icon_path=������ tool=��pyinstaller���� module=��Basic���� if_python=False�� one_file=��False�� True����
> if_cmd=��False��False����

�Թ�����ִ�г���<br>
����ֻ�ǽ�����ת��Ϊ���벢�鿴���ս��*test*<br>
���磺

```python
text = ""
if tool == COMBOBOX_TEXT[1][1]:  # pyinstaller called
  text += COMBOBOX_TEXT[1][1]  # write "pyinstaller" at the front
  if one_file[1]:  # one_file setted
    text += " %s" % PYINSTALLER_TEXTS[1]  # write "-w" behind "pyinstaller"
```

### File option.py

���ļ� option.py �У����ǹ�������Ľӿڡ��������ĵط��������<br>

�������ļ��е������༰����;��<br>

| class                      | purposes               |
| :------------------------- | :--------------------- |
| Window(tk.Tk)              | root window builded    |
| Desktop(tk.Frame)          | main interface builded |
| ToplevelAbout(tk.Toplevel) | build About window     |
| ToplevelInfo(tk.Toplevel)  | build help window      |

#### Window(tk.Tk)

��������У���һ����Ϊ set��self�� �ĺ����������ø����ڡ�

�����Ǵ���Ľ��ͣ�<br>

```python
self.screenwidth = self.winfo_screenwidth()
self.screenheight = self.winfo_screenheight()
self.x = (self.screenwidth - WINDOW_WIDTH) / 2
self.y = (self.screenheight - WINDOW_HEIGHT) / 2
self.size = "%dx%d+%d+%d" % (WINDOW_WIDTH, WINDOW_HEIGHT, self.x, self.y)
```

ͨ����������ȷ�����򴰿�λ�ã�

> self.screenwidth = self.winfo_screenwidth()
>
> self.screenheight = self.winfo_screenheight()

ͨ����������ȷ�����򴰿ڵĴ�С��

> self.x = (self.screenwidth - WINDOW_WIDTH) / 2
>
> self.y = (self.screenheight - WINDOW_HEIGHT) / 2

#### Desktop(tk.Frame)

��������У�Ҳ�Ǵ����д���ĵط������ǹ����������档<br>

�������� **init**��self�� master�� �е��õ����к�������Щ�����ڴ����е��õĺ��������� globalized in there �����ͱ��� there ������Ҫ��<br>

| function                       | function called                                                                             | variable globalized | variable needed                                                                 |
| :----------------------------- | :------------------------------------------------------------------------------------------ | :------------------ | :------------------------------------------------------------------------------ |
| set_place()                    | /                                                                                           | /                   | /                                                                               |
| set_combobox()                 | self.change_checkbutton_frame(tool)                                                         | /                   | self.combobox1_var<br>self.combobox2_var                                        |
| checkbutton()                  | /                                                                                           | frame1<br>frame2    | self.checkbutton1_1_var<br>self.checkbutton1_2_var<br>self.checkbutton1_3_var   |
| change_checkbutton_frame(tool) | /                                                                                           | /                   | /                                                                               |
| sidebar()                      | self.make_toplevel_about()<br>self.make_code()<br>self.make_exe()<br>self.open_output_dic() | button_3            | /                                                                               |
| entry_file                     | self.choose_file_from()<br>self.choose_file_output()<br>self.choose_file_icon()             | /                   | self.file_from_path_var<br>self.file_output_path_var<br>self.file_icon_path_var |
| console_order_entry()          | /                                                                                           | /                   | self.console_order_var                                                          |
| install()                      | /                                                                                           | /                   | /                                                                               |
| info()                         | self.change_info_label()                                                                    | /                   | /                                                                               |

There are a bit too much.It doesn't matter.Just let me introduce some of them.

##### info()

������֪������� tkinter �����ӿڣ������ҾͲ����ܴ tkinter �ӿڵĹ����ˡ���������ԭ�������е�����<h5>����ע����������</h5><br>

������ֻ���ܺ��� info�������ȿ�һ�´��룺<br>

> thread_change = Thread(target=self.change_info_label, args=())
>
> thread_change.start()

��Щ������Ϊ�˹���һ�� now �̣߳�ʹ�����򲻻�ͣ�ͣ�������

���ǵõ������������һ����Ϊ self.change_info_label���� ���º�����<br>
Ȼ�������ǿ������������<br>

###### self.change_info_label()

```python
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
```

��������Ĵ��롣<br>
������������һ����Ϊ _n_ ����ʱ������<br>
Ȼ�����ǽ���һ�� _while_ ѭ����<br>
�����ѭ���У���������ѡȡһ���������Ϊ�б��������<br>
�������� _n\_\_ �� \_n_ ��ͬ�������ٴΡ�while����<br>
Ȼ������ʹ��������ѡ���б��е�Ԫ�أ���������Ϊ���� self.entry_var ��Ԫ�ء�<br>
Ȼ������ʹ��ģ�� time ���亯�� sleep���� ���߳���ͣ 10 �롣<br>
Ȼ����һ����while���ٴγ��֡�<br>
����������л����� python �﷨���Ⲣ���ѡ�<br>

#### ToplevelAbout(tk.Toplevel) and ToplevelInfo(tk.Toplevel)

������֪��+4�������Ǽ�����һ���ġ����Դ˴���ֻѡ������֮һ��Ϊ���ܡ�<br>

�������������� Window��tk.Tk��<br>
���� Lable �ؼ�����ʾ��Ϣ���Ը�������

���ǿ��Ը���` tk ��`��Ԫ�ص�`justify`���Ե�ֵ���ı��ǩ���ݡ�<br>
����:<br>

> text = tk.Label(self, text=ABOUT_TEXT, justify="left")
>
> text.place(x=0, y=0, width=TOPLEVEL_WIDTH \* 3)

������ _justify_ �� _anchor_ ������<br>

| Ԫ��    | Ԥ��ֵ                                             | ���         |
| :------ | :------------------------------------------------- | :----------- |
| justify | left<br>right<br>center<br>                        | For lines    |
| anchor  | e<br>w<br>n<br>s<br>ne<br>se<br>nw<br>sw<br>center | for one line |

�����б�ָ���˿ؼ��� `_anchor_` ħ����������ӵ�е�λ�� if **name** == "**main**":
import sys
my*app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(my_app.exec*())����:<br>
|������|ָ����|
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

## ����

### ��������

1. Github:
1. [Codes on Github(the lastest)](https://github.com/Lonely-Pea/PyToExe.git "Click to download")
1. Lanzouy:
1. [PyToExe Build 230804 v1.0.0](https://wwcs.lanzouy.com/ifvRo14rzrlg "Click to download")
1. [PyToExe Build 230813 v1.1.0](https://wwcs.lanzouy.com/iAy9f15ajtsd "Click to download")

### �汾���ص�ַ

1. Lanzouy:
1. [PyToExe Build 230804 v1.0.0](https://wwcs.lanzouy.com/ib5RM14rzs9a "Click to download")
1. [PyToExe Build 230813 v1.1.0](https://wwcs.lanzouy.com/iInhb15ajusj "Click to download")

## PyToExe ��Ŀ��ҳ

[PyToExe Official Website](https://lonely-pea.github.io/PyToExeWeb "Click to go to")

## Bug ����

�� <lonely-pea@qq.com> ���͵����ʼ����ṩ�����������Ľ��顣
�����û�еõ�ʲô����Ҳ����ͨ����������䷢�͵����ʼ������ҡ�

## ��Ŀ��ͼ

H �����Ǹ��������Ļ��ͼ�����԰汾��Build 230813 v1.1.0��:<br>
![Screenshot_1](Screenshot/screenshot_1.png "Main interface")

![Screenshot_2](Screenshot/screenshot_2.png "About interface")

![Screenshot_3](Screenshot/screenshot_3.png "Help interface")

## �ر���л

��л Lonely-Pea �ı�̣��Լ�@BiliBiliSmallball �ķ���<br>
��л����֧�ָüƻ����ˡ�<br>
�������Ϊ����һ������Ľ�Ŀ�����ܸ������Ͻǵ����Ǳ���<br>
