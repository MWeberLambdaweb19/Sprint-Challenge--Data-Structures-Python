from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        self.storage.add_to_tail(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        # self.current = self.storage.head
        # while list_buffer_contents != self.capacity:
        #     print('current', self.current.value)
        #     if self.current.next and list_buffer_contents != self.capacity:
        #         list_buffer_contents.append(self.current.value)
        #         self.current = self.current.next
        #     elif not self.current.next and list_buffer_contents != self.capacity:
        #         list_buffer_contents.append(self.current.value)
        #         break
        #     else:
        #         list_buffer_contents.pop(0)
        #         list_buffer_contents.insert(0, self.current.value)
        #         break
        self.current = self.storage.head
        while self.current:
            if len(list_buffer_contents) == self.capacity:
                list_buffer_contents.pop(0)
                list_buffer_contents.insert(0, self.current.value)
                break
            if len(list_buffer_contents) != self.capacity:
                print(self.current.value)
                print(list_buffer_contents)
                list_buffer_contents.append(self.current.value)
                self.current = self.current.next

        return list_buffer_contents

cat = RingBuffer(5)
cat.append('a')
cat.append('b')
cat.append('c')
cat.append('d')
print(cat.get())

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
