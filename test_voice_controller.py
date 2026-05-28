import unittest
from speech_queue import SpeechQueue

class TestSpeechQueue(unittest.TestCase):
    def test_add_text(self):
        queue=SpeechQueue()
        queue.add_text("hello")
        self.assertEqual(queue.size(),1)

    def test_clear_queue(self):
        queue=SpeechQueue()
        queue.add_text("one")
        queue.add_text("two")

        queue.clear()

        self.assertEqual(queue.size(), 0)
    
if __name__ == "__main__":
    unittest.main()