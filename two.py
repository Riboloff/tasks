#! /usr/bin/python

class Node:
    def __init__(self, data=None):
        self.data=data
        self.next=None

class LinledList:
    def __init__(self):
        self.head = None

    def output(self):
        n = self.head
        while (n is not None):
            print n.data
            n = n.next

    def addNode(self, data=None):
        n = self.head
        while (n.next is not None):
            n=n.next
        n.next = Node(data)


    #2.1 Remove Dups: Write code to remove duplicates from an unsorted linked list.
    #without temp buffer 
    def removeDups(self):
        current = self.head
        while (current is not None):
            runner = current

            while (runner.next is not None):
                print current.data, runner.next.data
                if (current.data == runner.next.data):
                    if (runner.next.next is None):
                        runner.next = None
                        break
                    else:
                        runner.next = runner.next.next
                        continue

                runner = runner.next

            current=current.next

    def removeDumpBuffer(self):
        current = self.head
        dict = {};
        while (current is not None):
            if dict[current.data] is not None:
                current.next = current.next.next
            else:
                dict[current.data] = 1

            current=current.next

    def kToLast(self, k):
        if (k <= 0):
            return None
        current = self.head
        i = 1

        #find kth element from begin
        while (current.next is not None):
            if (i == k):
                break
            current=current.next
            i = i + 1

        if (i < k):
            print "count of elements less K"
            return None

        out = self.head
        while (current.next is not None):
            out=out.next
            current=current.next

        return out.data

        

list1 = LinledList()
list1.head = Node('one')

list1.addNode('one')
list1.addNode('one')
list1.addNode('two')
list1.addNode('three')
list1.addNode('three')
list1.addNode('three')
list1.addNode('three')
list1.addNode('three')
list1.addNode('four')
list1.addNode('five')
list1.addNode('five')
list1.addNode('two')
list1.addNode('four')
list1.addNode('four')


list1.output()
#list1.removeDups()
list1.removeDups()
print '----------'
list1.output()

print "=========K to Last:"
print '2 ', list1.kToLast(2)
print '5 ', list1.kToLast(5)
print '1 ', list1.kToLast(1)
print '0 ', list1.kToLast(0)
print '6 ', list1.kToLast(6)
print '-1 ', list1.kToLast(-1)
#print list1.kToLast(0)





