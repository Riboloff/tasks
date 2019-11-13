import copy
#4.1 minimal binary search tree from order array

class TreeNode:
    value = None
    left = None
    right = None

    def __init__(self, v):
        self.value = v



def createMinimalBST(array, start, end):
    if (end < start):
        return None

    mid = (end + start) / 2
    
    node = TreeNode(array[mid])
    node.left = createMinimalBST(array, start, mid - 1)
    node.right = createMinimalBST(array, mid + 1, end)

    return node

def out(node):
    if node == None:
        return

    out_ar = [node.value]

    if (node.left):
        out_ar.append(node.left.value)
    if (node.right):
        out_ar.append(node.right.value)
    print out_ar
    out(node.left)
    out(node.right)

    return

#4.3 List of depths 
def createList(node, linkedList):
    linkedList.append(node.value)
    linkedListRight = copy.copy(linkedList)

    if (node.left == None and node.right == None):
        print linkedList
        return

    if (node.left != None):
        createList(node.left, linkedList)
    else:
        print linkedList

    if (node.right != None):
        createList(node.right, linkedListRight)
    else:
        print linkedListRight

    return

array = [1,2,3,4,5,7,10,11]

node = createMinimalBST(array, 0, len(array) - 1)
out(node)

createList(node, [])


