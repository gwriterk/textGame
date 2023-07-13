from unittest import TestCase
from caseinsensitivedict import CaseInsensitiveDict


class TestCaseInsensitiveDict(TestCase):
    def test_getitem(self):
        myinstance = CaseInsensitiveDict()
        myinstance['jhin'] = 4
        self.assertEqual(myinstance['jhin'], 4)
        self.assertEqual(myinstance['JHIN'], 4)
        with self.assertRaises(KeyError):
            myinstance['Liam']

    def test_setitem(self):
        myinstance = CaseInsensitiveDict()
        myinstance['Kaisa'] = 5
        myinstance['KAISA'] = 'daughter of the void'
        self.assertEqual(myinstance['Kaisa'], 'daughter of the void')

    def test_list(self):
        myinstance = CaseInsensitiveDict()
        myinstance['jhin'] = 4
        myinstance['Kaisa'] = 5
        self.assertEqual(list(myinstance), ['jhin', 'Kaisa'])

    def test_len(self):
        myinstance = CaseInsensitiveDict()
        myinstance['jhin'] = 4
        myinstance['Kaisa'] = 5
        self.assertEqual(len(myinstance), 2)

    def test_del(self):
        myinstance = CaseInsensitiveDict()
        myinstance['Kaisa'] = 5
        self.assertEqual(myinstance['Kaisa'], 5)
        del myinstance['Kaisa']
        self.assertNotIn('Kaisa', myinstance)
        with self.assertRaises(KeyError):
            myinstance['Kaisa']

    def test_keyin(self):
        myinstance = CaseInsensitiveDict()
        myinstance['Kaisa'] = 5
        self.assertIn('Kaisa', myinstance)

    def test_keynotin(self):
        myinstance = CaseInsensitiveDict()
        self.assertNotIn('Jhin', myinstance)

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
    def test_get(self):
        myinstance = CaseInsensitiveDict()
        myinstance['Kaisa'] = 5
        self.assertIn('Kaisa', myinstance)
        self.assertNotIn('Jhin', myinstance)
        value = myinstance.get('Kaisa')
        nonvalue = myinstance.get('Jhin')
        self.assertEqual(value, 5)
        self.assertEqual(nonvalue, None)


        # items()
        #     Return a new view of the dictionary’s items ((key, value) pairs).
        #     See the documentation of view objects.

    def test_items(self):
        myinstance = CaseInsensitiveDict()
        myinstance['Kaisa'] = 5
        myinstance['Jhin'] = 4
        self.assertIn('Kaisa', myinstance)
        self.assertIn('Jhin', myinstance)
        items_list = []
        for i in myinstance:
            t = (i, myinstance[i])
            items_list.append(t)
        self.assertIn(('Kaisa', 5), items_list)
        self.assertIn(('Jhin', 4), items_list)

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
    def test_popitem(self):
        myinstance = CaseInsensitiveDict()
        myinstance['Kaisa'] = 5
        self.assertIn('Kaisa', myinstance)
        item = myinstance.popitem()
        self.assertIs(item, ('Kaisa', 5))
        self.assertNotIn(item, myinstance)

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

        # values()
        #     Return a new view of the dictionary’s values. See the documentation
        #     of view objects.

    def test_values(self):
        myinstance = CaseInsensitiveDict()
        myinstance['Kaisa'] = 5
        myinstance['Jhin'] = 4
        self.assertIn('Kaisa', myinstance)
        self.assertIn('Jhin', myinstance)
        values = myinstance.values()
        print(f'values is {values}')
        self.assertIn(5, values)
        self.assertEqual(2, len(values))