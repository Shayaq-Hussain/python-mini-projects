print("=== MINI CALCULATOR ===")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("\nResults:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

if b != 0:
    print("Division:", a / b)
else:
    print("Cannot divide by zero!")