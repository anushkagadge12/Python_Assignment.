user_input = input("Enter integers separated by space: ")
numbers = tuple(int(x) for x in user_input.split())

print("Original Tuple:", numbers)
print("Total items:", len(numbers))

if numbers:
    print("Last item:", numbers[-1])
else:
    print("Tuple is empty")

print("Reversed tuple:", numbers[::-1])
print("Contains 5?:", "Yes" if 5 in numbers else "No")

if len(numbers) > 2:
    remaining = numbers[1:-1]
    print("After removing first and last, sorted:", tuple(sorted(remaining)))
else:
    print("Not enough elements")