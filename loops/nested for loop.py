# Nested loop example: printing a multiplication table
for i in range(1, 11):  # Outer loop
    for j in range(1, 11):  # Inner loop
        print(f"{i} x {j} = {i * j}")
    print("-----")  # Separator after each row
