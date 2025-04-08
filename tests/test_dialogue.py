import unittest
from ..modules.casual_dialogue import get_running_event

class TestDialogue(unittest.TestCase):
    '''test class of casual_dialogue.py
    '''
    def test_find_first_event(self):
        '''イベントidと合致した業を取ってこれてるか
        '''
        EVENT_ID = 0
        JUDGE_TEXT = 'OK'

        dialogue_flow = [
            [0, 'OK'],
            [1, 'NO_1'],
            [2, 'NO_2'],
            [75, 'NO_75']
        ]
        self.assertEqual(get_running_event(EVENT_ID, dialogue_flow), JUDGE_TEXT)
