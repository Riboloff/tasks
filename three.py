
#Three in One
class InfoStack:
    def __init__(self, start, step):
        self.start = start
        self.step = step
        self.size = 0

    def getLastIndex(self):
        return (self.size - 1) * self.step + self.start

    def getNextIndex(self):
        return self.getLastIndex() + self.step


class MultiStack:
    def __init__(self, count):
        self.array = []
        self.info = []

        for i in range(0, count):
            self.info.insert(i, InfoStack(i, count))
        
    def add(self, number, value):
        stack = self.info[number]
        index = stack.getNextIndex()
        if (index > len(self.array) - 1):
            self.array.extend([None, None]);
        self.array[index] = value
        stack.size = stack.size + 1

    def out(self):
        print self.array

    def pop(self, number):
        stack = self.info[number]
        index = stack.getLastIndex()
        if index < 0:
            return None
        stack.size = stack.size - 1
        element = self.array[index]
        print index
        self.array[index] = None
        self._clean()
        return element

    def _clean(self):
        if self.array[-1] == self.array[-2] == None:
            self.array.pop()
            self.array.pop()


ms = MultiStack(2)
ms.add(0, 'iddqd')
ms.add(1, 'idkfa')
ms.add(0, 'idclip')
ms.add(0, 'iddt')
ms.add(1, 'iddt')
ms.out()
print ms.pop(0)
print ms.pop(0)
print ms.pop(0)
print ms.pop(0)
print ms.pop(0)
ms.out()
print ms.pop(1)
ms.out()
print ms.pop(1)
ms.out()
ms.add(0, 'iddqd')
ms.add(1, 'idkfa')
ms.add(0, 'idclip')
ms.add(0, 'iddt')
ms.add(1, 'iddt')
ms.out()

