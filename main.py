import os

import pysrt
from paddlespeech.cli.tts.infer import TTSExecutor
from pydub import AudioSegment


def main():
    srtpath = "srt/"
    wavpath = "wav/"

    check_mkdir(srtpath)
    check_mkdir(wavpath)

    mysrt = pysrt.open("srt/1.srt")

    outwav = AudioSegment.empty()
    outwav += AudioSegment.silent(duration=mysrt[0].start.ordinal)

    i = 1
    for part in mysrt:
        file_name = str(i) + "-" + part.text + ".wav"
        tospeech(part.text, file_name)
        yuyin = AudioSegment.from_file("wav/" + file_name)
        outwav += yuyin
        try:
            silent_time = mysrt[i].start.ordinal-int(outwav.duration_seconds*1000)
            outwav += AudioSegment.silent(duration=silent_time)
        except:
            continue
        i += 1

    outwav.export("out.mp3", format="mp3")


def tospeech(text, name="name"):
    tts = TTSExecutor()
    outputpath = "wav/" + name
    tts(text=text, output=outputpath, am="fastspeech2_mix", lang="mix", spk_id=174)

def check_mkdir(path):
    """ 检查一个目录是否存在，不存在则新建 """
    if not os.path.exists(path):
        os.makedirs(path)


if __name__ == "__main__":
    main()
