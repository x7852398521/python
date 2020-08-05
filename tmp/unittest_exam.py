# -*- coding: utf-8 -*-
import python_exam
import unittest

input_value = {'hired': {'be': {'to': {'deserve': 'I'}}}}
output_value = {'I': {'deserve': {'to': {'be': 'hired'}}}}

class TestMethods(unittest.TestCase):
    def test_dict_reverse(self):
        self.assertEqual(python_exam.dict_reverse(input_value), output_value)

if __name__ == '__main__':
    unittest.main()