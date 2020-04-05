# Keyboard Emulation

#### 介绍
把文本文件字符模拟为键盘按键输入

#### 使用说明

##### 安装依赖

**Ubuntu/Debian**

```bash
apt install python3-xlib
python3 -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
```

**CentOS**

```bash
yum install python3-xlib
python3 -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
```

**Windowns**

下载[PyWin32](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pywin32) 和 [PyHook](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyhook)

```bash
python3 -m pip install pyHook-xxxx.whl pywin32‑xxxx.whl
python3 -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
```