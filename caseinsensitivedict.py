class CaseInsensitiveDict:
    def __init__(self):
        self.dict = {}

    def __getitem__(self, key):
        print('I was called.')
        for i in self.dict:
            if i.lower() == key.lower():
                return self.dict[i]
        raise KeyError('That is not correct.')

    def __setitem__(self, key, value):
        # key = 'Snake' value = 5
        existing = None
        for i in self.dict:
            if i.lower() == key.lower():
                existing = i
                break
        if existing:
            del self.dict[existing]
        self.dict[key] = value

    def __iter__(self):
        return iter(self.dict)

    def __len__(self):
        return len(self.dict)

    def __delitem__(self, key):
        existing = None
        for i in self.dict:
            if i.lower() == key.lower():
                existing = i
                break
        if existing:
            del self.dict[existing]
        else:
            raise KeyError

    def __eq__(self, other):
        for i in self:
            self_value = self[i]
            if i in other:
                other_value = other[i]
            else:
                return False
            if self_value != other_value:
                return False
        return True

    def clear(self):
        self.dict = {}

    def copy(self):
        myinstance = CaseInsensitiveDict()
        for key in self:
            myinstance[key] = self[key]
        return myinstance

    def keys(self):
        key_list = []
        for key in self:
            key_list.append(key)
            return key_list

    def values(self):
        value_list = []
        for i in self.dict:
            t = self.dict[i]
            value_list.append(t)
            return value_list

    def items(self):
        items_list = []
        for i in self.dict:
            t = (i, self.dict[i])
            items_list.append(t)
        return items_list

    def popitem(self):
        myinstance = CaseInsensitiveDict()
        for key in myinstance:
            value = myinstance[key]
            item = (key, value)
            myinstance.popitem(item)
            return item

    def get(self, key, default=None):
        if key in self.dict:
            return self.dict[key]
        else:
            return default



if __name__ == '__main__':
    myinstance = CaseInsensitiveDict()
    myvariable = myinstance['jhin']
    # myvariable = myinstance.__getitem__('jhin')
    # myvariable = myinstance.__getitem__(myinstance, 'jhin')
    print(f'myvariable is {myvariable}')
    myinstance['Kaisa'] = 5
    print(f'Kaisa is', myinstance['Kaisa'])
    myinstance['KAISA'] = 'daughter of the void'
    print(f'Kaisa is now', myinstance['Kaisa'])
    # 1. Get a value by key
    # 2. Set a value by key
    # 3. Delete a value by key
    # j['Jhin'] = 4
    # j = {'Key': (value1, value2), 'Jhin': 4}
    # j['jhin'] = 5
    # j = {'Key': (value1, value2), 'Jhin': 4, 'jhin': 5}
    # j = {'Key': (value1, value2), 'jhin': 5}
    # del j['jhin']
    # j = {'Key': (value1, value2)}