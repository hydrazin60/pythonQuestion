### Python Programs for List and Tuple Operations

#### 1. Find the Common Elements Between Two Lists
```python
def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

# Example usage:
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
print(find_common_elements(list1, list2))  # Output: [3, 4, 5]
```

#### 2. Split a List into Chunks of Size `n`
```python
def split_into_chunks(input_list, n):
    return [input_list[i:i + n] for i in range(0, len(input_list), n)]

# Example usage:
input_list = [1, 2, 3, 4, 5, 6]
n = 2
print(split_into_chunks(input_list, n))  # Output: [[1, 2], [3, 4], [5, 6]]
```

#### 3. Find the Maximum Difference Between Any Two Elements in a List
```python
def max_difference(input_list):
    if len(input_list) < 2:
        return 0
    return max(input_list) - min(input_list)

# Example usage:
input_list = [10, 3, 5, 9, 20]
print(max_difference(input_list))  # Output: 17
```

#### 4. Reverse a Tuple Without Using Slicing
```python
def reverse_tuple(input_tuple):
    reversed_tuple = tuple(reversed(input_tuple))
    return reversed_tuple

# Example usage:
input_tuple = (1, 2, 3, 4, 5)
print(reverse_tuple(input_tuple))  # Output: (5, 4, 3, 2, 1)
```

#### 5. Check if Two Tuples Are the Same When Sorted
```python
def are_tuples_same(tuple1, tuple2):
    return sorted(tuple1) == sorted(tuple2)

# Example usage:
tuple1 = (3, 1, 2)
tuple2 = (2, 1, 3)
print(are_tuples_same(tuple1, tuple2))  # Output: True
