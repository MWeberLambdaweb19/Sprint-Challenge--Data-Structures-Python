import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

class BinarySearchTree:
    def __init__(self, value):
        self.value = []
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value is None:
            BinarySearchTree(value)
        if value >= self.value:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
    
    def contains(self, target):
        if target == self.value:
            duplicates.append(target)

# for i in names_1:
#     first = BinarySearchTree(i)
# for j in names_2:
#     second = BinarySearchTree(j)
       
# first.contains(second)

first = BinarySearchTree(names_1)
second = BinarySearchTree(names_2)
first.contains(second)

## binary search tree!
## build a bst names 1
## contains with names 2

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
