from knapsack_dynamic import knapsack_01
import unittest


class TestKnapsackDynamic(unittest.TestCase):

    def test_one(self):
        num_items = 3
        weights = [10, 20, 30]
        values = [60, 100, 120]
        capacity = 50
        result = knapsack_01(num_items, weights, values, capacity)
        self.assertEqual(result["max_value"], 220)
        self.assertEqual(result["weight_sequence"], [20, 30])
        self.assertEqual(result["binary_sequence"], [0, 1, 1])

    def test_two(self):
        num_items = 3
        weights = [1, 2, 3]
        values = [10, 15, 40]
        capacity = 6
        result = knapsack_01(num_items, weights, values, capacity)
        self.assertEqual(result["max_value"], 65)
        self.assertEqual(result["weight_sequence"], [1, 2, 3])
        self.assertEqual(result["binary_sequence"], [1, 1, 1])

    def test_zero_capacity(self):
        num_items = 3
        weights = [10, 20, 30]
        values = [60, 100, 120]
        capacity = 0
        result = knapsack_01(num_items, weights, values, capacity)
        self.assertEqual(result["max_value"], 0)
        self.assertEqual(result["weight_sequence"], [])
        self.assertEqual(result["binary_sequence"], [0, 0, 0])

    def test_empty_weights_and_values(self):
        num_items = 0
        weights = []
        values = []
        capacity = 50
        result = knapsack_01(num_items, weights, values, capacity)
        self.assertEqual(result["max_value"], 0)
        self.assertEqual(result["weight_sequence"], [])
        self.assertEqual(result["binary_sequence"], [])

    def test_single_item_fits(self):
        num_items = 1
        weights = [10]
        values = [60]
        capacity = 15
        result = knapsack_01(num_items,weights, values, capacity)
        self.assertEqual(result["max_value"], 60)
        self.assertEqual(result["weight_sequence"], [10])
        self.assertEqual(result["binary_sequence"], [1])

    def test_single_item_does_not_fit(self):
        num_items = 1
        weights = [10]
        values = [60]
        capacity = 5
        result = knapsack_01(num_items, weights, values, capacity)
        self.assertEqual(result["max_value"], 0)
        self.assertEqual(result["weight_sequence"], [])
        self.assertEqual(result["binary_sequence"], [0])

    def test_items_with_same_value(self):
        num_items = 3 
        weights = [10, 20, 30]
        values = [100, 100, 100]
        capacity = 50
        result = knapsack_01(num_items, weights, values, capacity)
        self.assertEqual(result["max_value"], 200)
        self.assertEqual(result["weight_sequence"], [10, 20])
        self.assertEqual(result["binary_sequence"], [1, 1, 0])


if __name__ == '__main__':
    unittest.main()
