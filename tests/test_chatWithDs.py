import unittest
from chatWithDs import ConversationManager

class TestConversationManager(unittest.TestCase):
    def setUp(self):
        self.manager = ConversationManager()

    def test_add_message(self):
        self.manager.add_message('user', 'Hello')
        self.assertEqual(len(self.manager.history), 1)
        self.assertEqual(self.manager.history[0]['role'], 'user')
        self.assertEqual(self.manager.history[0]['content'], 'Hello')

    def test_max_length(self):
        for i in range(15):
            self.manager.add_message('user', f'Message {i}')
        self.assertEqual(len(self.manager.history), 15)  # 15 pairs, so 15 total

if __name__ == '__main__':
    unittest.main()
