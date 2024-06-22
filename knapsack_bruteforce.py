from itertools import combinations

def knapsack_brute_force(weights, values, capacity):
    n = len(weights)
    max_value = 0
    best_combination = []

    # Function to calculate total value and weight for a combination
    def calculate_value_and_weight(combination):
        total_weight = 0
        total_value = 0
        for index in combination:
            total_weight += weights[index]
            total_value += values[index]
        return total_value, total_weight

    # Loop through all possible subset sizes from 1 to n
    for subset_size in range(1, n + 1):
        # Generate all combinations of items of size subset_size
        for combo in combinations(range(n), subset_size):
            total_value, total_weight = calculate_value_and_weight(combo)
            
            # Check if this combination is feasible and gives a higher value
            if total_weight <= capacity and total_value > max_value:
                max_value = total_value
                best_combination = list(combo)  # Convert tuple to list

    binary_sequence = [0] * n
    for idx in best_combination:
        binary_sequence[idx] = 1

    
    weight_sequence = [weights[idx] for idx in best_combination]

        # Print results
    print(f"Maximum value that can be achieved: {max_value}")
    print("Items to include in the knapsack:")
    for idx in best_combination:
        print(f"Item {idx + 1}: (Weight = {weights[idx]}, Value = {values[idx]})")
    
    return {
        "max_value": max_value,
        "weight_sequence": weight_sequence,
        "binary_sequence": binary_sequence
    }

# Function to get inputs from the user
def get_user_input():
    n = int(input("Enter the number of items: "))
    weights = []
    values = []
    
    for i in range(n):
        input_str = input(f"Enter the weight and value of item {i+1} (separated by space): ")
        weight, value = map(int, input_str.split())
        weights.append(weight)
        values.append(value)
        
    capacity = int(input("Enter the capacity of the knapsack: "))
    
    return weights, values, capacity

# Main function to execute the brute force knapsack solution
def main():
    weights, values, capacity = get_user_input()
    max_value, best_combination = knapsack_brute_force(weights, values, capacity)
    
    print(f"Maximum value: {max_value}")
    if best_combination:
        print("Items to include in the knapsack:")
        for idx in best_combination:
            print(f"  - Item {idx+1}: (Weight = {weights[idx]}, Value = {values[idx]})")
    else:
        print("No items can be included in the knapsack.")

# Run the main function
if __name__ == "__main__":
    main()
