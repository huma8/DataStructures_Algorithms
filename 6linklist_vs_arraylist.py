import time
import random
import ctypes
from collections import deque

# LinkedList implementation
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, val):
        """Append to the end of the list - O(n)"""
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def insert_at_index(self, index, val):
        """Insert at a specific index - O(n)"""
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        
        new_node = ListNode(val)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self.size += 1

    def delete_by_value(self, val):
        """Delete first occurrence of value - O(n)"""
        if not self.head:
            raise ValueError("List is empty")
        
        if self.head.val == val:
            self.head = self.head.next
            self.size -= 1
            return
        
        current = self.head
        while current.next and current.next.val != val:
            current = current.next
        
        if current.next:
            current.next = current.next.next
            self.size -= 1
        else:
            raise ValueError("Value not found")

    def get(self, index):
        """Get value at index - O(n)"""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        
        current = self.head
        for _ in range(index):
            current = current.next
        return current.val

    def __len__(self):
        return self.size

# Dynamic Array implementation (from 5dynamic_array.py, simplified)
class DynamicArray:
    def __init__(self):
        self.n = 0                      # Eleman sayısı
        self.capacity = 1               # Başlangıç kapasitesi
        self.array = self._make_array(self.capacity)

    def _make_array(self, capacity):
        return (capacity * ctypes.py_object)()

    def add(self, item):
        """Append to the end of the array - O(1) amortized"""
        if self.n == self.capacity:
            self._resize(2 * self.capacity)
        self.array[self.n] = item
        self.n += 1

    def insert(self, index, data):
        """Insert at a specific index - O(n) due to shifting"""
        if not 0 <= index <= self.n:
            raise IndexError("index out of bounds")
        if self.n == self.capacity:
            self._resize(2 * self.capacity)
        for i in range(self.n, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = data
        self.n += 1

    def delete(self, data=None):
        """Delete by value - O(n)"""
        if self.n == 0:
            raise IndexError("delete from empty array")
        if data is not None:
            for i in range(self.n):
                if self.array[i] == data:
                    for j in range(i, self.n - 1):
                        self.array[j] = self.array[j + 1]
                    self.array[self.n - 1] = None
                    self.n -= 1
                    if 0 < self.n < self.capacity // 4:
                        self._resize(self.capacity // 2)
                    return
            raise ValueError("value not found in array")
        else:
            self.array[self.n - 1] = None
        self.n -= 1
        if 0 < self.n < self.capacity // 4:
            self._resize(self.capacity // 2)

    def _resize(self, new_capacity):
        new_array = self._make_array(new_capacity)
        for i in range(self.n):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def get(self, index):
        """Get value at index - O(1)"""
        if not 0 <= index < self.n:
            raise IndexError("index out of bounds")
        return self.array[index]

    def __len__(self):
        return self.n

def measure_time(func, *args, **kwargs):
    """Helper function to measure execution time"""
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    return result, end_time - start_time

def compare_operations():
    print("Linked List vs Array List Performance Comparison")
    print("=" * 60)
    
    # Test sizes
    sizes = [100, 500, 1000]
    
    for size in sizes:
        print(f"\nTesting with {size} elements:")
        print("-" * 40)
        
        # Test Append operations
        # Linked List append
        ll = LinkedList()
        ll_append_times = []
        for i in range(size):
            _, append_time = measure_time(ll.append, f"item_{i}")
            ll_append_times.append(append_time)
        avg_ll_append = sum(ll_append_times) / len(ll_append_times)
        
        # Array List append
        da = DynamicArray()
        da_append_times = []
        for i in range(size):
            _, append_time = measure_time(da.add, f"item_{i}")
            da_append_times.append(append_time)
        avg_da_append = sum(da_append_times) / len(da_append_times)
        
        print(f"Append (average):")
        print(f"  Linked List:  {avg_ll_append*1000000:.2f} us")
        print(f"  Array List:   {avg_da_append*1000000:.2f} us")
        
        # Test Insert at beginning (this should show a big difference)
        # Linked List insert at beginning
        ll = LinkedList()
        start_time = time.time()
        for i in range(size):
            ll.insert_at_index(0, f"item_{i}")
        ll_insert_begin_time = time.time() - start_time

        # Array List insert at beginning
        da = DynamicArray()
        start_time = time.time()
        for i in range(size):
            da.insert(0, f"item_{i}")
        da_insert_begin_time = time.time() - start_time

        print(f"Insert at beginning (total for {size} ops):")
        print(f"  Linked List:  {ll_insert_begin_time*1000:.2f} ms")
        print(f"  Array List:   {da_insert_begin_time*1000:.2f} ms")
        
        # Test Random Access
        # Create structures with data for access testing
        ll = LinkedList()
        da = DynamicArray()
        for i in range(size):
            ll.append(f"item_{i}")
            da.add(f"item_{i}")
        
        # Random access middle element in Linked List
        mid_idx = size // 2
        _, ll_access_time = measure_time(ll.get, mid_idx)
        
        # Random access middle element in Array List
        _, da_access_time = measure_time(da.get, mid_idx)
        
        print(f"Random access (middle element):")
        print(f"  Linked List:  {ll_access_time*1000000:.2f} us")
        print(f"  Array List:   {da_access_time*1000000:.2f} us")
        
        # Test Delete from middle
        # Delete from middle in Linked List
        ll = LinkedList()
        for i in range(size):
            ll.append(f"item_{i}")
        _, ll_delete_time = measure_time(ll.delete_by_value, f"item_{size//2}")
        
        # Delete from middle in Array List
        da = DynamicArray()
        for i in range(size):
            da.add(f"item_{i}")
        _, da_delete_time = measure_time(da.delete, f"item_{size//2}")
        
        print(f"Delete from middle:")
        print(f"  Linked List:  {ll_delete_time*1000000:.2f} us")
        print(f"  Array List:   {da_delete_time*1000000:.2f} us")

def main():
    compare_operations()
    
    print("\nSummary of Linked List vs Array List:")
    print("-" * 40)
    print("Linked List:")
    print("  + Insertion/Deletion at beginning: O(1)")
    print("  + Memory efficient for insertions")
    print("  - Random access: O(n)")
    print("  - More memory overhead per element")
    print("\nArray List:")
    print("  + Random access: O(1)")
    print("  + Cache friendly")
    print("  - Insertion/Deletion at beginning: O(n)")
    print("  - May require resizing and copying")

if __name__ == "__main__":
    main()