# Outer while loop
i = 1
while i <= 3:
    j = 1  # Reset j for each iteration of the outer loop
    # Inner while loop
    while j <= 3:
        print(f"i = {i}, j = {j}")
        j += 1
    print("-----")
    i += 1
