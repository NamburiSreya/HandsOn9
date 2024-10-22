import math

class ListNode:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.next = None
        self.prev = None

class HashContainer:
    def __init__(self, initial_capacity=8, hash_function=None):
        self.bucket_count = initial_capacity
        self.element_count = 0
        self.buckets = [None] * self.bucket_count
        self.hash_function = hash_function or self.default_hash

    def default_hash(self, key):
        # Multiplication method
        golden_ratio = 0.6180339887
        product = key * golden_ratio
        fractional_part = product - math.floor(product)
        
        # Division method
        hash_value = int(self.bucket_count * fractional_part)
        return hash_value // (self.bucket_count // self.bucket_count)  # Division by 1

    def compute_hash(self, key):
        return self.hash_function(key) % self.bucket_count

    def set_hash_function(self, hash_function):
        self.hash_function = hash_function

    def get_hash_function(self):
        return self.hash_function

    def adjust_capacity(self, new_bucket_count):
        old_buckets = self.buckets
        self.bucket_count = new_bucket_count
        self.buckets = [None] * self.bucket_count
        self.element_count = 0

        for bucket in old_buckets:
            current = bucket
            while current:
                self.add_element(current.key, current.data)
                current = current.next

    def add_element(self, key, value):
        if self.element_count >= self.bucket_count:
            self.adjust_capacity(self.bucket_count * 2)

        index = self.compute_hash(key)
        new_node = ListNode(key, value)

        if not self.buckets[index]:
            self.buckets[index] = new_node
        else:
            new_node.next = self.buckets[index]
            self.buckets[index].prev = new_node
            self.buckets[index] = new_node

        self.element_count += 1

    def delete_element(self, key):
        index = self.compute_hash(key)
        current = self.buckets[index]

        while current:
            if current.key == key:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.buckets[index] = current.next

                if current.next:
                    current.next.prev = current.prev

                self.element_count -= 1

                if self.element_count < self.bucket_count // 4 and self.bucket_count > 8:
                    self.adjust_capacity(self.bucket_count // 2)

                return True

            current = current.next

        return False

    def find_element(self, key):
        index = self.compute_hash(key)
        current = self.buckets[index]

        while current:
            if current.key == key:
                return current.data
            current = current.next

        return None

    def get_element_count(self):
        return self.element_count

    def get_bucket_count(self):
        return self.bucket_count

# Test the HashContainer
if __name__ == "__main__":
    hash_container = HashContainer()

    # Add some key-value pairs
    hash_container.add_element(5, 50)
    hash_container.add_element(15, 150)
    hash_container.add_element(25, 250)

    # Find and print values
    print(f"Value for key 5: {hash_container.find_element(5)}")
    print(f"Value for key 15: {hash_container.find_element(15)}")
    print(f"Value for key 25: {hash_container.find_element(25)}")

    # Remove a key
    hash_container.delete_element(15)

    # Try to find the removed key
    print(f"Value for key 15 after removal: {hash_container.find_element(15)}")

    # Add many elements to test resizing
    for i in range(100):
        hash_container.add_element(i, i * 10)

    print(f"Final element count: {hash_container.get_element_count()}")
    print(f"Final bucket count: {hash_container.get_bucket_count()}")

    # Test custom hash function
    def custom_hash(key):
        return key % 10

    hash_container.set_hash_function(custom_hash)
    hash_container.add_element(42, 420)
    print(f"Value for key 42 with custom hash: {hash_container.find_element(42)}")

    
## output
Value for key 5: 50
Value for key 15: 150
Value for key 25: 250
Value for key 15 after removal: None
Final element count: 102
Final bucket count: 128
Value for key 42 with custom hash: 420
