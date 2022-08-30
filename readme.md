# 字幕转语音工具

## 简介

通过输入srt文件，获取合成的音频文件，支持中英混合输入

srt文件需要放在 `srt\` 目录下 重命名为 `1.srt`

单句文件会生成在 `wav\` 目录下

最终音频文件 `out.mp3` 会生成在项目根目录下

合成语音直接用的paddlespeech接口

（每次照搬paddlespeech的代码总让我有一种丰收的喜悦

## 安装

python3.6+

首先安装宇宙第一机器学习框架（误）paddlepaddle，此处给出的是CPU版，如果你有n卡，请前往

[这里](https://www.paddlepaddle.org.cn/)安装cuda版本。

安装

```
pip install paddlepaddle -i https://mirror.baidu.com/pypi/simple
```

然后安装paddlespeech和其他依赖

```
pip install paddlespeech -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install pysrt pydub -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 运行

srt文件放好之后运行 `main.py` 

注意

首次运行的时候会下载模型，下次就不会那么慢了

模型存在 `~\paddlespeech\` 路径下

要么自己造轮子，要么pip install一个停车场，import一辆车，然后用一个轮子
