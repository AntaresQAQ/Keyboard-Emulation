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
python -m pip install pyHook-xxxx.whl pywin32‑xxxx.whl
python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
```

**MacOS**

需要安装Quartz, AppKit

```bash
python3 -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
```

##### 运行

复制`config_default.py`为`config.py`，按实际需要修改配置参数

在程序目录下新建`input.txt`文件，写入需要模拟输入的字符

在程序目录下执行：

```bash
python3 run.py
```

