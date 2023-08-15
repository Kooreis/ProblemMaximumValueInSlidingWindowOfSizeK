```C#
using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    static void Main(string[] args)
    {
        int[] arr = { 1, 3, -1, -3, 5, 3, 6, 7 };
        int k = 3;
        int[] result = MaxSlidingWindow(arr, k);
        foreach (int num in result)
        {
            Console.Write(num + " ");
        }
    }

    public static int[] MaxSlidingWindow(int[] nums, int k)
    {
        if (nums == null || nums.Length == 0) return new int[0];
        int[] result = new int[nums.Length - k + 1];
        LinkedList<int> deque = new LinkedList<int>();
        for (int i = 0; i < nums.Length; i++)
        {
            if (deque.Any() && deque.First() == i - k) deque.RemoveFirst();
            while (deque.Any() && nums[deque.Last()] < nums[i]) deque.RemoveLast();
            deque.AddLast(i);
            if (i + 1 >= k) result[i + 1 - k] = nums[deque.First()];
        }
        return result;
    }
}
```