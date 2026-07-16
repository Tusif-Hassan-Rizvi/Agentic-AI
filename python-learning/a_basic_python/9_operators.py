# ==========================================
# 1. ARITHMETIC OPERATORS
# ==========================================
a = 10
b = 3
print('Addition (+):', a + b)           # Output: 13
print('Subtraction (-):', a - b)        # Output: 7
print('Multiplication (*):', a * b)     # Output: 30
print('Division (/):', a / b)           # Output: 3.3333333333333335
print('Floor Division (//):', a // b)   # Output: 3
print('Modulus/Remainder (%):', a % b)  # Output: 1
print('Exponent/Power (**):', a ** b)   # Output: 1000


# ==========================================
# 2. ASSIGNMENT OPERATORS
# ==========================================
x = 5                                   # Simple Assignment
x += 3                                  # Add and Assign (Same as: x = x + 3) -> x is now 8
x -= 2                                  # Subtract and Assign -> x is now 6
y, z = 10, 20                           # Multiple Assignment


# ==========================================
# 3. COMPARISON (RELATIONAL) OPERATORS
# (Always return True or False)
# ==========================================
m = 10
n = 20
print('Equal (==):', m == n)            # Output: False
print('Not Equal (!=):', m != n)        # Output: True
print('Greater Than (>):', m > n)       # Output: False
print('Less Than (<):', m < n)          # Output: True
print('Greater or Equal (>=):', m >= n) # Output: False
print('Less or Equal (<=):', m <= n)    # Output: True


# ==========================================
# 4. LOGICAL OPERATORS
# (Used to combine conditional statements)
# ==========================================
p = True
q = False
print('Logical AND:', p and q)          # Output: False (Both must be True)
print('Logical OR:', p or q)            # Output: True (At least one must be True)
print('Logical NOT:', not p)            # Output: False (Inverts the boolean)


# ==========================================
# 5. IDENTITY OPERATORS
# (Compare if objects point to the same memory location)
# ==========================================
list_one = [1, 2, 3]
list_two = [1, 2, 3]
list_three = list_one

print('Is (same object):', list_one is list_two)     # Output: False (Same values, different memory addresses)
print('Is (same object):', list_one is list_three)   # Output: True (Points to the exact same address)
print('Is Not:', list_one is not list_two)           # Output: True


# ==========================================
# 6. MEMBERSHIP OPERATORS
# (Check if a sequence is present in an object)
# ==========================================
name_list = ['Tausif', 'Tanzil', 'Tanwir']
print('In:', 'Tausif' in name_list)                  # Output: True
print('Not In:', 'Rahul' not in name_list)           # Output: True


# ==========================================
# 7. BITWISE OPERATORS
# (Operate on binary representations of numbers)
# ==========================================
num1 = 6  # Binary: 0110
num2 = 3  # Binary: 0011
print('Bitwise AND (&):', num1 & num2)  # Binary: 0010 -> Output: 2
print('Bitwise OR (|):', num1 | num2)   # Binary: 0111 -> Output: 7