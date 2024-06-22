def fractional_knapsack(weights, values, capacity):
    n = len(weights)
    # Calculate value per unit weight for each item
    value_per_unit_weight = [(values[i] / weights[i], weights[i], values[i]) for i in range(n)]
    # Sort items based on value per unit weight in descending order
    value_per_unit_weight.sort(reverse=True, key=lambda x: x[0])

    total_value = 0.0
    remaining_capacity = capacity
    weight_sequence = []
    binary_sequence = []

    for value_per_unit, weight, value in value_per_unit_weight:
        if remaining_capacity <= 0:
            break
        if weight <= remaining_capacity:
            # Take the whole item
            total_value += value
            remaining_capacity -= weight
            weight_sequence.append(weight)
            binary_sequence.append(1)
        else:
            # Take a fraction of the item
            total_value += value_per_unit * remaining_capacity
            weight_sequence.append(remaining_capacity)
            binary_sequence.append(remaining_capacity / weight)
            remaining_capacity = 0

        # Print maximum value that can be achieved
    print(f"Maximum value that can be achieved: {total_value}")

    # Print items to include in the knapsack
    print("Items to include in the knapsack:")
    for i in range(len(weight_sequence)):
        if binary_sequence[i] > 0:
            print(f"Item {i + 1}: (Weight = {weight_sequence[i]}, Value = {values[i]})")
    
    return {
        "max_value": total_value,
        "weight_sequence": weight_sequence,
        "binary_sequence": binary_sequence
    }


def main():
    # Take input from user
    n = int(input("Enter number of items: "))
    weights = []
    values = []
    for i in range(n):
        weight, value = map(int, input(f"Enter weight and value for item {i+1}: ").split())
        weights.append(weight)
        values.append(value)
    capacity = int(input("Enter the capacity of the knapsack: "))

    # Call fractional_knapsack function and print the result
    max_value = fractional_knapsack(weights, values, capacity)
    print(f"Maximum value that can be achieved: {max_value}")


if __name__ == "__main__":
    main()
