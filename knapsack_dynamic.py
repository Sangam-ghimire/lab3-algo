def knapsack_01(num_items, weights, values, capacity):

    dp = [[0 for i in range(capacity + 1)] for j in range(num_items + 1)]

    for i in range(1, num_items + 1):
        for w in range(1, capacity + 1):

            if weights[i - 1] > w:
                dp[i][w] = dp[i - 1][w]
            else:

                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])


    max_value = dp[num_items][capacity]


    included_items = []
    w = capacity
    for i in range(num_items, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            included_items.append(i)
            w -= weights[i - 1]


    included_items.reverse()


    binary_sequence = [0] * num_items
    for item in included_items:
        binary_sequence[item - 1] = 1


    weight_sequence = [weights[item - 1] for item in included_items]


    print(f"Maximum value that can be achieved: {max_value}")
    print("Items to include in the knapsack:")
    for item in included_items:
        print(f"Item {item}: (Weight = {weights[item - 1]}, Value = {values[item - 1]})")


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
