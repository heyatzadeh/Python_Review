class CustomContainer:
    def __init__(self):
        self.__bookmarks = {}

    @classmethod
    def factoryMethod(cls):
        return cls()

    def __str__(self):
        return self.__bookmarks

    def add(self, bookmark):
        self.__bookmarks[bookmark.lower()] = self.__bookmarks.get(bookmark.lower(), 0) + 1

    def __add__(self, other):
        self.add(other)

    def __getitem__(self, bookmark):
        return self.__bookmarks.get(bookmark.lower(), 0)

    def __setitem__(self, bookmark, count):
        self.__bookmarks[bookmark.lower()] = count

    def __len__(self):
        return len(self.__bookmarks.keys())

    def __iter__(self):
        return iter(self.__bookmarks.keys())

    @property
    def bookmarks(self):
        return self.__bookmarks

    @bookmarks.setter
    def bookmarks(self, bookmarks):
        self.__bookmarks = bookmarks

    # bookmarks = property(bookmarks, bookmarks)


container = CustomContainer()
container.add('python')
container.add('python')
container.add('Python')
container.add('python')
container.add('python')
container.add('Python')
container + 'python'
container + 'c++'
container + 'c++'
container + 'c++'
container + 'java'
container['python'] = 1000
print(container.__str__())
print(len(container))
for item in container:
    print(item)

print(container.bookmarks)
