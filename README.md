Hash Table Implementation Overview

This project features a hash table implemented in Python, designed to meet specific requirements:

Hash Function: Utilizes both multiplication and division methods for hashing integer keys.
Generic Functionality: Allows for any custom hash function to be set, providing flexibility in how keys are hashed.
Key-Value Storage: Supports storing integer keys and integer values.
Collision Resolution: Implements collision resolution through chaining using a doubly linked list.
Dynamic Resizing: The hash table automatically grows when it becomes full (doubles the size) and shrinks when it is 1/4 empty (halves the size).
C-Style Array Simulation: Uses Python lists to simulate C-style arrays for bucket storage.
Basic Operations: Includes methods for adding, finding, and deleting elements, as well as retrieving the current count of elements and buckets.