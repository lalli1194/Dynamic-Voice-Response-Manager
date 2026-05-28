from queue import Queue
class SpeechQueue:
    def __init__(self):
        self.queue=Queue()

    def add_text(self,text):
        self.queue.put(text)
    
    def get_next(self):
        if not self.queue.empty():
            return self.queue.get()
        return None
    
    def clear(self):
        while not self.queue.empty():
            self.queue.get()
        
    def size(self):
        return self.queue.qsize()