import subprocess

def install(package):
    subprocess.call(['pip', 'install', package])

install('SpeechRecognition')
install('openai')
install('gtts')
install('playsound')