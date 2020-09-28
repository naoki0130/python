# coding: utf-8
import subprocess
from datetime import datetime


def jtalk(t):
    open_jtalk = ['open_jtalk']
    mech = ['-x', '/usr/local/Cellar/open-jtalk/1.11/dic']
    htsvoice = ['-m', '/usr/local/Cellar/open-jtalk/1.11/voice/mei/mei_normal.htsvoice']
    speed = ['-r', '1.0']
    outwav = ['-ow', 'out.wav']
    cmd = open_jtalk + mech + htsvoice + speed + outwav
    c = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    t = t.encode()
    c.stdin.write(t)
    c.stdin.close()
    c.wait()
    aplay = ['afplay', 'out.wav']
    wr = subprocess.Popen(aplay)


def say_datetime():
    d = datetime.now()
    text = '%s月%s日、%s時%s分%s秒' % (d.month, d.day, d.hour, d.minute, d.second)
    t = "こんにちは"
    jtalk(t)


if __name__ == '__main__':
    say_datetime()

"""
#coding: utf-8
import subprocess
import tempfile


def run(message, voice_path='voice.wav'):
    speed = 1.0
    dic_path = "/usr/local/Cellar/open-jtalk/1.11/dic"
    model_path = "/usr/local/Cellar/open-jtalk/1.11/voice/mei/mei_normal.htsvoice"

    with tempfile.NamedTemporaryFile(mode='w+') as tmp:
        tmp.write(message)
        tmp.seek(0)
        command = 'open_jtalk -x {} -m {} -r {} -ow {} {}'.format(
            dic_path, model_path, speed, voice_path, tmp.name)
        proc = subprocess.run(
            command,
            shell=True,
        )
"""
