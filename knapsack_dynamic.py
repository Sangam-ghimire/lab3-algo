def knapsack_01(num_items, weights, values, capacity):

    # Initialize a DP table to store maximum values for each capacity and item count
    dp_table = [[0 for current_capacity in range(capacity + 1)] for item_index in range(num_items + 1)]

    # Fill the DP table
    for i in range(1, num_items + 1):
        for current_capacity in range(1, capacity + 1):
            if weights[i - 1] > current_capacity:
                dp_table[i][current_capacity] = dp_table[i - 1][current_capacity]
            else:
                dp_table[i][current_capacity] = max(dp_table[i - 1][current_capacity], 
                                                    values[i - 1] + dp_table[i - 1][current_capacity - weights[i - 1]])

    # Maximum value that can be achieved
    max_value = dp_table[num_items][capacity]

    # Determine which items are included in the knapsack
    included_items = []
    remaining_capacity = capacity
    for i in range(num_items, 0, -1):
        if dp_table[i][remaining_capacity] != dp_table[i - 1][remaining_capacity]:
            included_items.append(i)
            remaining_capacity -= weights[i - 1]

    included_items.reverse()

    # Create binary sequence indicating which items are included
    binary_sequence = [0] * num_items
    for item_index in included_items:
        binary_sequence[item_index - 1] = 1

    # Collect weights of included items
    weight_sequence = [weights[item_index - 1] for item_index in included_items]

    # Print results
    print(f"Maximum value that can be achieved: {max_value}")
    print("Items to include in the knapsack:")
    for item_index in included_items:
        print(f"Item {item_index}: (Weight = {weights[item_index - 1]}, Value = {values[item_index - 1]})")

    return {
        "max_value": max_value,
        "weight_sequence": weight_sequence,
        "binary_sequence": binary_sequence
    }

def main():
    num_items = int(input("Enter number of items: "))
    weights = []
    values = []
    for i in range(num_items):
        weight, value = map(int, input(f"Enter the weight and value of item {i + 1} (separated by space): ").split())
        weights.append(weight)
        values.append(value)
    capacity = int(input("Enter the capacity of the knapsack: "))

    knapsack_01(num_items, weights, values, capacity)

if __name__ == "__main__":
    main()
