from unittest import TestCase
from caseinsensitivedict import CaseInsensitiveDict


class TestCaseInsensitiveDict(TestCase):
    def test_getitem(self):
        myinstance = CaseInsensitiveDict()
        myinstance['jhin'] = 4
        myinstance[True] = 'yes'
        self.assertEqual(myinstance['jhin'], 4)
        self.assertEqual(myinstance['JHIN'], 4)
        self.assertEqual(myinstance[True], 'yes')
        with self.assertRaises(KeyError):
            myinstance['Liam']

    def test_setitem(self):
        myinstance = CaseInsensitiveDict()
        myinstance['Kaisa'] = 5
        self.assertEqual(myinstance['Kaisa'], 5)
        myinstance['KAISA'] = 'daughter of the void'
        self.assertEqual(myinstance['Kaisa'], 'daughter of the void')
        myinstance[True] = (0, 1)
        self.assertEqual(myinstance[True], (0, 1))

    def test_list(self):
        myinstance = CaseInsensitiveDict()
        myinstance['jhin'] = 4
        myinstance[True] = 5
        self.assertEqual(list(myinstance), ['jhin', True])

    def test_len(self):
        myinstance = CaseInsensitiveDict()
        self.assertEqual(len(myinstance), 0)
        myinstance['jhin'] = 4
        myinstance['Kaisa'] = 5
        self.assertEqual(len(myinstance), 2)
        del myinstance['jhin']
        self.assertEqual(len(myinstance), 1)

    def test_del(self):
        myinstance = CaseInsensitiveDict()
        myinstance['Kaisa'] = 5
        self.assertEqual(myinstance['Kaisa'], 5)
        del myinstance['KAISA']
        self.assertNotIn('Kaisa', myinstance)
        with self.assertRaises(KeyError):
            myinstance['Kaisa']
        with self.assertRaises(KeyError):
            del myinstance['Kaisa']

    def test_keyin(self):
        myinstance = CaseInsensitiveDict()
        myinstance['Kaisa'] = 5
        self.assertIn('KAISA', myinstance)
        myinstance[True] = 'yes'
        self.assertIn(True, myinstance)

    def test_keynotin(self):
        myinstance = CaseInsensitiveDict()
        self.assertNotIn('Jhin', myinstance)
        myinstance['Kaisa'] = 5
        self.assertIn('Kaisa', myinstance)
        self.assertNotIn('Jhin', myinstance)
        del myinstance['Kaisa']
        self.assertNotIn('Kaisa', myinstance)

    def test_clear(self):
        myinstance = CaseInsensitiveDict()
        myinstance['Kaisa'] = 5
        self.assertIn('Kaisa', myinstance)
        self.assertEqual(myinstance, {'Kaisa': 5})
        myinstance.clear()
        self.assertEqual(myinstance, {})

    def test_copy(self):
        myinstance = CaseInsensitiveDict()
        myinstance['Kaisa'] = 5
        self.assertIn('Kaisa', myinstance)
        mysecondinstance = myinstance.copy()
        self.assertEqual(myinstance, mysecondinstance)
        self.assertFalse(myinstance is mysecondinstance)

        # get(key[, default])
        #     Return the value for key if key is in the dictionary, else
        #     default.  If default is not given, it defaults to None, so that
        #     this method never raises a KeyError.

    def test_items(self):
        myinstance = CaseInsensitiveDict()
        myinstance['Kaisa'] = 5
        myinstance[True] = 'yes'
        self.assertIn('Kaisa', myinstance)
        self.assertIn(True, myinstance)
        items_list = []
        for i in myinstance:
            t = (i, myinstance[i])
            items_list.append(t)
        self.assertIn(('Kaisa', 5), items_list)
        self.assertIn((True, 'yes'), items_list)

    def test_keys(self):
        myinstance = CaseInsensitiveDict()
        myinstance['Kaisa'] = 5
        self.assertIn('Kaisa', myinstance)
        keys = myinstance.keys()
        self.assertIn('Kaisa', keys)

        # pop(key[, default])
        #     If key is in the dictionary, remove it and return its value, else
        #     return default. If default is not given and key is not in the
        #     dictionary, a KeyError is raised.

        # popitem()
        #     Remove and return a (key, value) pair from the dictionary.  Pairs
        #     are returned in LIFO order.

        # setdefault(key[, default])
        #     If key is in the dictionary, return its value. If not, insert key
        #     with a value of default and return default.  default defaults to
        #     None.

        # update([other])
        #     Update the dictionary with the key/value pairs from other,
        #     overwriting existing keys. Return None.
        #
        #     update() accepts either another dictionary object or an iterable
        #     of key/value pairs (as tuples or other iterables of length two).
        #     If keyword arguments are specified, the dictionary is then
        #     updated with those key/value pairs: d.update(red=1, blue=2).

    def test_values(self):
        myinstance = CaseInsensitiveDict()
        myinstance['Kaisa'] = 5
        self.assertIn('Kaisa', myinstance)
        values = myinstance.values()
        self.assertIn(5, values)

    def test_eq(self):
        myinstance = CaseInsensitiveDict()
        self.assertEqual(myinstance, myinstance)
        self.assertEqual(myinstance, {})
        myinstance['Kaisa'] = 5
        self.assertEqual(myinstance, myinstance)
        self.assertEqual(myinstance, {'Kaisa': 5})
        self.assertEqual(myinstance, {'KAISA': 5})
        self.assertNotEqual(myinstance, {'Kaisa': 4})
        self.assertNotEqual(myinstance, {'Kaisa': '5'})
        self.assertNotEqual(myinstance, {'Kaira': 5})
        self.assertNotEqual(myinstance, {(0, 1): 5})
        self.assertNotEqual(myinstance, {})
        self.assertNotEqual(myinstance, {'Kaisa': 5, 'Jhin': 4})
