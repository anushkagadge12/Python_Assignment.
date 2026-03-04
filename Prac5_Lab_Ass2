user_input = input("Enter item prices separated by space: ")
prices = tuple(float(x) for x in user_input.split())

print("Prices:", prices)

if prices:
    print("Total items sold:", len(prices))
    print("Cheapest price:", min(prices))
    print("Costliest price:", max(prices))
    print("Ascending order:", tuple(sorted(prices)))
    print("Number of costliest items sold:", prices.count(max(prices)))
else:
    print("No items sold")