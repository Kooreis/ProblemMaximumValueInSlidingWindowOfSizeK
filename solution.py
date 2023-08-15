Here is a Python console application that solves the problem:

```python
from collections import deque

def max_in_sliding_window(arr, k):
    n = len(arr)
    if n < k:
        return -1
    max_values = []
    dq = deque()
    for i in range(k):
        while dq and arr[i] >= arr[dq[-1]]:
            dq.pop()
        dq.append(i)
    for i in range(k, n):
        max_values.append(arr[dq[0]])
        while dq and dq[0] <= i-k:
            dq.popleft()
        while dq and arr[i] >= arr[dq[-1]]:
            dq.pop()
        dq.append(i)
    max_values.append(arr[dq[0]])
    return max_values

def main():
    arr = [int(x) for x in input("Enter numbers separated by space: ").split()]
    k = int(input("Enter window size: "))
    result = max_in_sliding_window(arr, k)
    print("Maximum values in each sliding window: ", result)

if __name__ == "__main__":
    main()
```

This console application first takes a list of numbers and a window size as input from the user. It then finds the maximum value in each sliding window of size k in the list of numbers and prints the maximum values.