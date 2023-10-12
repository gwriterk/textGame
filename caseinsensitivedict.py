class CaseInsensitiveDict:
    def __init__(self, mapping={}, **kwargs):
        self.dict = {}
        for key in kwargs:
            self.dict[key] = kwargs[key]
        if isinstance(mapping, dict) or isinstance(mapping, CaseInsensitiveDict):
            for key in mapping:
                self.dict[key] = mapping[key]
        else:
            for key, value in mapping:
                self.dict[key] = value


    def __getitem__(self, key):
        for i in self.dict:
            if isinstance(i, str) and isinstance(key, str):
                if i.lower() == key.lower():
                    return self.dict[i]
            elif i == key:
                return self.dict[i]
        raise KeyError('That is not correct.')

    def __setitem__(self, key, value):
        # key = 'Snake' value = 5
        existing = None
        for i in self.dict:
            if isinstance(i, str) and isinstance(key, str):
                if i.lower() == key.lower():
                    existing = i
                    break
            elif i == key:
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
        if len(self) == 0:
            if len(other) == 0:
                return True
            else:
                return False
        if not (isinstance(other, dict) or isinstance(other, CaseInsensitiveDict)):
            return False
        if len(self) != len(other):
            return False
        for i in self:
            i_found_in_j = False
            for j in other:
                if i == j:
                    if self[i] == other[j]:
                        i_found_in_j = True
                        break
                elif isinstance(i, str) and isinstance(j, str):
                    if i.lower() == j.lower():
                        if self[i] == other[j]:
                            i_found_in_j = True
                            break
                else:
                    i_found_in_j = False
        return i_found_in_j

        # must return a Bool, works to compare self with other dictionary objects
        # *** valid to pass in other types to comparison op (won't raise exception); returns False
        # must also account for case insensitivity in keys
        # iterating is necessary, but simply checking if each key of one exists in the other is...
        # ...not sufficient; one cannot have more keys than the other, values must also be the same
        # as soon as your check returns False at any point, you can stop the method!
        # if the two dict objects pass all the checks, the method should return True

    def __repr__(self):
        return repr(self.dict)

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
        return self.dict.popitem()


    def get(self, key, default=None):
        for item in self.dict:
            if isinstance(item, str) and isinstance(key, str):
                if item.lower() == key.lower():
                    return self.dict[item]
            elif item == key:
                return self.dict[item]
        return default


    def setdefault(self, key, default=None):
        if key in self.dict:
            value = self.dict[key]
            return value
        else:
            self.dict[key] = default
            return default

    def update(self, other=(), **kwargs): # kwargs is a dictionary
        if isinstance(other, dict):
            for key in other:
                self.dict[key] = other[key]
        # if other is a list of tuples or a tuple
        elif isinstance(other, tuple) or isinstance(other,list):
            for key, value in other:
                # other = (('red', 1),)
                self.dict[key] = value
        for key in kwargs:
            self.dict[key] = kwargs[key]
        return None



if __name__ == '__main__':
    myinstance = CaseInsensitiveDict()
    myinstance['Kaisa'] = 5
    myinstance['Jhin'] = 4
    mysecondinstance = CaseInsensitiveDict()
    mysecondinstance['Kaisa'] = 5
    mysecondinstance['Jhin'] = 4
    print(myinstance == mysecondinstance)