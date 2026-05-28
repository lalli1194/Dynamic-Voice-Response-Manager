import threading
import time
from tts_enginne import TTSEngine

class VoiceController:
    def __init__(self):
        self.tts=TTSEngine()
        self.paused=False
        self.stopped=False
        self.thread=None
    
    def play(self,text):
        self.paused=False
        self.stopped=False

        def worker():
            words=text.split()
            for word in words:
                if self.stopped:
                    break
                while self.paused:
                    time.sleep(0.1)
                self.tts.speak(word)
            print("speech completed")
        self.thread=threading.Thread(target=worker)
        self.thread.start()
    def pause(self):
        self.paused=True
        print("paused")
    
    def resume(self):
        self.paused=False
        print("Resumed")
    
    def stop(self):
        self.stopped=True
        self.tts.stop()
        print("stopped")
    
    def set_speed(self,rate):
        self.tts.set_speed(rate)