import pyttsx3

class TTSEngine:
    def __init__(self):
        self.engine=pyttsx3.init()

    def set_speed(self,rate):
        self.engine.setProperty("rate",rate)
    
    def speak(self,text):
        self.engine.say(text)
        self.engine.runAndWait()

    def stop(self):
        self.engine.stop()