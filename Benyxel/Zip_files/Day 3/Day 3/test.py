num = list(map(int, input("Data: ").strip().split()))
print(num)
maximum = max(num)
minimum = min(num)

# # original
# print("Data: ", num)
# print("Maximum Number: ", maximum)
# print("Minimum Number: ",minimum)

# # casting to string 
# print("Data: ", str(num))
# print("Maximum Number: ", str(maximum))
# print("Minimum Number: ", str(minimum))

# string format
print(f"Data: {num}")
print(f"Maximum Number: {maximum}")
print(f"Minimum Number: {minimum}")
