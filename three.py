
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

class NodeStack:
    def __init__(self, value=None):
        self.value = value
        self.pre_min = None
        self.current_min = 0

class SimpleStack:
    def __init__(self):
        self.array = []
        self.min = None

    def push(self, value):
        if (value < 0):
            return
        node = NodeStack(value)
        self.array.append(node)
        if (self.min == None):
            self.min = value
            node.pre_min = None

        else:
            if (self.min >= value):
                node.pre_min = self.min
                node.current_min = 1
                self.min = value

    def pop(self):
        if len(self.array):
            node = self.array.pop()
            if (node.current_min == 1):
                self.min = node.pre_min
            if (len(self.array) == 0):
                self.min = None

            return node.value

        self.min = None
        return None

    def out(self):
        ar = []
        for node in self.array:
            ar.append(node.value)
        print ar

    def _min(self):
        return self.min

class MyQueue:
    def __init__(self):
        self.info = [SimpleStack(), SimpleStack()]

    def push(self, value):
        s = self.info[0]
        s.push(value)

    def pop(self):
        s = self.info[1]
        value = s.pop()
        if value is None:
            self.shift()
            value = s.pop()

        return value


    def shift(self):
        s0 = self.info[0]
        s1 = self.info[1]

        i = s0.pop()
        while (i is not None):
            s1.push(i)
            i = s0.pop()

        return


print '===========3.1.MultiStack========'
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
ms.out()


print '===========3.2.midle========'
s = SimpleStack()
s.push(1)
s.push(2)
s.push(3)
s.push(1)
s.push(2)
s.out()
print "min=", s._min()
s.pop()
s.out()
print "min=", s._min()
s.pop()
s.out()
print "min=", s._min()
s.pop()
s.out()
print "min=", s._min()
s.pop()
s.out()
print "min=", s._min()
s.pop()
s.out()
print "min=", s._min()
s.push(2)
s.out()
s.push(3)
s.push(0)
s.push(0)
s.push(0)
s.push(3)
s.push(4)
s.push(3)
s.out()
print "min=", s._min()


print '=======3.4 Queue using two stacks'
q = MyQueue()
q.push(1);
q.push(2);
q.push(3);
print q.pop();
print q.pop();
print q.pop();
print q.pop();
print q.pop();
q.push(1);
q.push(2);
q.push(3);
print q.pop();
print q.pop();
q.push(4);
q.push(5);
print q.pop();
print q.pop();
print q.pop();
