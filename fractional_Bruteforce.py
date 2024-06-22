from itertools import combinations

def fractional_knapsack_bruteforce(weights, values, capacity):
    n = len(weights)
    max_value = 0.0
    best_combination = []

    # Generate all combinations of items
    for i in range(1, n + 1):
        for combo in combinations(range(n), i):
            total_weight = sum(weights[j] for j in combo)
            total_value = sum(values[j] for j in combo)

            # Check if the total weight exceeds the capacity
            if total_weight <= capacity:
                if total_value > max_value:
                    max_value = total_value
                    best_combination = [(j, 1.0) for j in combo]

            # If total weight exceeds capacity, try taking fractional parts
            else:
                remaining_capacity = capacity
                current_value = 0.0
                included_items = []

                for j in combo:
                    if weights[j] <= remaining_capacity:
                        included_items.append((j, 1.0))  # Fully include item j
                        remaining_capacity -= weights[j]
                        current_value += values[j]
                    else:
                        fraction = remaining_capacity / weights[j]
                        included_items.append((j, fraction))  # Include fraction of item j
                        current_value += values[j] * fraction
                        remaining_capacity = 0  # No more capacity left

                        # Since capacity is fully used, break the loop
                        break

                if current_value > max_value:
                    max_value = current_value
                    best_combination = included_items

    # Prepare binary sequence and weight sequence
    binary_sequence = [0] * n
    weight_sequence = []

    for idx in range(n):
        if idx in [j for j, _ in best_combination]:
            item_idx = [j for j, _ in best_combination].index(idx)
            fraction = best_combination[item_idx][1]

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

    max_value, weight_sequence, binary_sequence = fractional_knapsack_bruteforce(weights, values, capacity)

    print_results(max_value, weight_sequence, binary_sequence, weights, values)

if __name__ == "__main__":
    main()
