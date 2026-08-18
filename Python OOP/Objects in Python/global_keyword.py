# Try changing the module-vide variable without using 'global' keyword
counter = 10

def try_changing_without_global():
    counter = 50
    print(f"Value of counter inside function: {counter}")

try_changing_without_global()
print(f"Value of counter outside function: {counter}")

def try_changing_with_global():
    global counter
    counter = 50
    print(f"Value of counter inside function: {counter}")

try_changing_with_global()
print(f"Value of counter outside function: {counter}")
