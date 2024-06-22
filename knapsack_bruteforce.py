from itertools import combinations

def knapsack_brute_force(weights, values, capacity):
    num_items = len(weights)
    max_value = 0
    best_items_indices = []

    # Function to calculate total value and weight for a combination
    def calculate_value_and_weight(combination):
        total_weight = 0
        total_value = 0
        for index in combination:
            total_weight += weights[index]
            total_value += values[index]
        return total_value, total_weight

    # Loop through all possible subset sizes from 1 to num_items
    for subset_size in range(1, num_items + 1):
        # Generate all combinations of items of size subset_size
        for combo in combinations(range(num_items), subset_size):
            total_value, total_weight = calculate_value_and_weight(combo)
            
            # Check if this combination is feasible and gives a higher value
            if total_weight <= capacity and total_value > max_value:
                max_value = total_value
                best_items_indices = list(combo)  # Convert tuple to list

    # Prepare binary sequence indicating which items are included
    binary_sequence = [0] * num_items
    for idx in best_items_indices:
        binary_sequence[idx] = 1

    # Prepare weight sequence of included items
    weight_sequence = [weights[idx] for idx in best_items_indices]

    print_results(max_value, weight_sequence,binary_sequence,weights, values)

    return {
        "max_value": max_value,
        "weight_sequence": weight_sequence,
        "binary_sequence": binary_sequence
    }

# Function to print the knapsack results
def print_results(max_value, weight_sequence, binary_sequence, weights, values):
    print(f"Maximum value that can be achieved: {max_value}")
    print("Items to include in the knapsack:")
    for idx, is_included in enumerate(binary_sequence):
        if is_included == 1:
            print(f"Item {idx + 1}: (Weight = {weights[idx]}, Value = {values[idx]})")



# Function to get inputs from the user
def get_user_input():
    num_items = int(input("Enter the number of items: "))
    weights = []
    values = []
    
    for i in range(num_items):
        input_str = input(f"Enter the weight and value of item {i+1} (separated by space): ")
        weight, value = map(int, input_str.split())
        weights.append(weight)
        values.append(value)
        
    capacity = int(input("Enter the capacity of the knapsack: "))
    
    return weights, values, capacity

# Main function to execute the brute force knapsack solution
def main():
    weights, values, capacity = get_user_input()
    result = knapsack_brute_force(weights, values, capacity)
    
    max_value = result["max_value"]
    included_indices = [idx + 1 for idx, include in enumerate(result["binary_sequence"]) if include == 1]

    print_knapsack_results(max_value, weights, values, included_indices)

# Run the main function
if __name__ == "__main__":
    main()
