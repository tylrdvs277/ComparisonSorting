# Name:        Tyler Davis
# Course:      CPE 202
# Instructor:  Dave Parkinson
# Assignment:  Lab 6
# Term:        Fall 2017

def insert_sort(alist):
    count = 0
    for idx in range(1, len(alist)):
        count += 1
        while idx > 0 and alist[idx] < alist[idx - 1]:
            count += 1
            (alist[idx], alist[idx - 1]) = (alist[idx - 1], alist[idx])
            idx -= 1
        if idx == 0:
            count -= 1
    return count

def merge_sort(alist):
    if len(alist) <= 1:
        return (alist, 0)
    else:
        middle = len(alist) // 2
        (left, count_l) = merge_sort(alist[ : middle])
        (right, count_r) = merge_sort(alist[middle : ])
        count = count_l + count_r
        merge = []
        idx_l = idx_r = 0
        while idx_l < len(left) and idx_r < len(right):
            count += 1
            if left[idx_l] <= right[idx_r]:
                merge.append(left[idx_l])
                idx_l += 1
            else:
                merge.append(right[idx_r])
                idx_r += 1
        if idx_l < len(left):
            merge += left[idx_l : ]
        else:
            merge += right[idx_r : ]
        return (merge, count)

def select_sort(alist):
    count = 0
    for i in range(len(alist) - 1):
        big = alist[0]
        big_idx = 0
        last_idx = len(alist) - i - 1
        for idx in range(1, last_idx + 1):
            count += 1
            if alist[idx] > big:
                big_idx = idx
                big = alist[idx]
        (alist[big_idx], alist[last_idx]) = (alist[last_idx], alist[big_idx])
    return count

import random
import unittest

class TestLab6(unittest.TestCase):

    def epsilon_equal(self, x1, x2, epsilon = 0.01):
        return abs(x1 - x2) < epsilon
    
    def test_order_select_sort_1(self):
        """This test illustrates that selection sort is O(n^2) by comparing
        the number of comparisons from a list and a list of twice the size.
        If this sorting is O(n^2), it should take 4x the comparisons for a 
        list of double the size."""
        test_1n = select_sort(list(range(1000))[ : : -1])
        test_2n = select_sort(list(range(2000))[ : : -1])
        self.assertTrue(self.epsilon_equal((test_2n / test_1n), 4))

    def test_order_select_sort_2(self):
        test_1n = select_sort(list(range(2000))[ : : -1])
        test_2n = select_sort(list(range(4000))[ : : -1])
        self.assertTrue(self.epsilon_equal((test_2n / test_1n), 4))

    def test_worst_case_select_sort(self):
        """All cases of selection sort are O(n^2) because the algorithm 
        searches for the biggest element in the list and moves it to the end. 
        This algorithm has no specific worst case in terms of comparisons."""
        random.seed(10)
        worst_case = list(range(1000))
        random_case = [random.randint(0, 1000) for _ in range(1000)]
        self.assertEqual(select_sort(worst_case), select_sort(random_case))

    def test_order_insert_sort_1(self):
        """This test illustrates that insertion sort is O(n^2) by comparing
        the number of comparisons from a list and a list of twice the size.
        If this sorting is O(n^2), it should take 4x the comparisons for a 
        list of double the size."""
        test_1n = insert_sort(list(range(1000))[ : : -1])
        test_2n = insert_sort(list(range(2000))[ : : -1])
        self.assertTrue(self.epsilon_equal((test_2n / test_1n), 4))

    def test_order_insert_sort_2(self):
        test_1n = insert_sort(list(range(2000))[ : : -1])
        test_2n = insert_sort(list(range(4000))[ : : -1])
        self.assertTrue(self.epsilon_equal((test_2n / test_1n), 4))

    def test_worst_case_insert_sort(self):
        """Unlike selection sort, the comparisons for insertion sorts vary 
        based on the type of list. In the case of a list in reverse order, every 
        element must be moved to the beginning of the sorted portion. This 
        requires by far the most comparsions to see if the element is sorted."""
        random.seed(10)
        worst_case = list(range(1000))[ : : -1]
        random_case = [random.randint(0, 1000) for _ in range(1000)]
        best_case = list(range(1000))
        self.assertTrue(insert_sort(worst_case) > insert_sort(random_case) 
                        > insert_sort(best_case))

if __name__ == "__main__":
    unittest.main()
