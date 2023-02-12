import unittest

def short_strings(strings):
    short_strings = []
    for string in strings:
        if len(string) <= 3:
            short_strings.append(string)
    return short_strings

class TestShortStrings(unittest.TestCase):
    def test_short_strings(self):
        initial_array = ['душ', 'кот', 'огурец', 'дом', 'игла']
        result = short_strings(initial_array)
        self.assertEqual(result, ['душ','кот', 'дом'])

if __name__ == '__main__':
    unittest.main()