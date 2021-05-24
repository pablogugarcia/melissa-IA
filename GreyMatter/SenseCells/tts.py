import os
import sys
import subprocess


def tts(message):
    """
    This function takes a message as an argument and converts it to spech depending on the 
    OS.
    """
    if sys.platform == 'darwin':
        tts_engine = 'say'
        return os.system(tts_engine + ' ' + message)
    elif sys.platform == 'linux2' or sys.platform == 'linux':
        tts_engine = 'espeak'
        language = '-ven+f3'
        speed = '-s170'
        return subprocess.call([tts_engine, language, speed, message])
