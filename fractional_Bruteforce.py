from itertools import combinations

def fractional_knapsack_bruteforce(weights, values, capacity):
    num_items = len(weights)
    max_value = 0.0
    best_items = []

    # Iterate over all possible combinations of items
    for subset_size in range(1, num_items + 1):
        for indices in combinations(range(num_items), subset_size):
            total_weight = sum(weights[idx] for idx in indices)
            total_value = sum(values[idx] for idx in indices)

            if total_weight <= capacity:
                if total_value > max_value:
                    max_value = total_value
                    best_items = [(idx, 1.0) for idx in indices]
            else:
                remaining_capacity = capacity
                current_value = 0.0
                included_items = []

                for idx in indices:
                    if weights[idx] <= remaining_capacity:
                        included_items.append((idx, 1.0))
                        remaining_capacity -= weights[idx]
                        current_value += values[idx]
                    else:
                        fraction = remaining_capacity / weights[idx]
                        included_items.append((idx, fraction))
                        current_value += values[idx] * fraction
                        remaining_capacity = 0
                        break

                if current_value > max_value:
                    max_value = current_value
                    best_items = included_items

    # Prepare binary sequence and weight sequence
    binary_sequence = [0] * num_items
    weight_sequence = []

    for idx in range(num_items):
        if idx in [item_idx for item_idx, _ in best_items]:
            item_idx = [item_idx for item_idx, _ in best_items].index(idx)
            fraction = best_items[item_idx][1]

            binary_sequence[idx] = fraction
            weight_sequence.append(weights[idx] * fraction)
        else:
            binary_sequence[idx] = 0
    
    print_results(max_value, weight_sequence, binary_sequence, weights, values)

    return {
        "max_value": max_value,
        "weight_sequence": weight_sequence,
        "binary_sequence": binary_sequence
    }

def print_results(max_value, weight_sequence, binary_sequence, weights, values):
    print(f"Maximum value that can be achieved: {max_value}")
    print("Items to include in the knapsack:")
    for idx, fraction in enumerate(binary_sequence):
        if fraction > 0:
            print(f"Item {idx + 1}: (Weight = {weights[idx]}, Value = {values[idx]}, Fraction = {fraction})")

def main():
    num_items = int(input("Enter number of items: "))
    weights = []
    values = []
    for i in range(num_items):
        weight, value = map(int, input(f"Enter the weight and value of item {i + 1} (separated by space): ").split())
        weights.append(weight)
        values.append(value)
    capacity = int(input("Enter the capacity of the knapsack: "))

    result = fractional_knapsack_bruteforce(weights, values, capacity)

    # Printing results again here is redundant, as it's already done in the function
    # print_results(result["max_value"], result["weight_sequence"], result["binary_sequence"], weights, values)

if __name__ == "__main__":
    main()
