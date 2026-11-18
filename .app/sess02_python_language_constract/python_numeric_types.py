# Python script to demonstrate the various number/numeric types supported by Python.

# Get the code to make Decimal numbers work.
from decimal import Decimal, getcontext, ROUND_DOWN

# Get the code to make fraction numbers work.
from fractions import Fraction

# --------------------------------------------------
# 1. INTEGERS - whole numbers, both +ve and -ve
# --------------------------------------------------
int_value = 8
print(("INTEGER DEMONSTRATION").center(38, " "))
print('-' * 38) # Console.WriteLine(new string('-', 38));
print(f"The value in the variable 'int_value' is {int_value}")
print(f"The type of the variable 'int_value' is {type(int_value)}\n")

# ----------------------------------------------------------------------
# 2. FLOATS - Numbers with decimal places, both +ve and -ve
# ----------------------------------------------------------------------
float_value = 3.141592653
print(("FLOAT DEMONSTRATION").center(38, " "))
print('-' * 38)  
print(f"The value in the variable 'float_value' is {float_value}")
print(f"The type of the variable 'float_value' is {type(float_value)}\n")

# ---------------------------------------------------------------
# 3. DECIMALS - Numbers with decimal places, both +ve and -ve
# ---------------------------------------------------------------
# Set the precision for decimal operations
getcontext().prec = 7 # Set the required precision. You can set this to a higher value to maintain higher precisions
# for rounding numbers with lots of decimal places eg. Decimal(345.234578912345789)
decimal_value = Decimal(8.14592654)
print(("DECIMAL DEMONSTRATION").center(38, ""))
print('-' * 38) 
print(f"The original value in the variable 'decimal_value' is {decimal_value}")
# Use ROUND_DOWN to ensure no rounding up takes place.
decimal_value = Decimal(1.234578901234589).quantize(Decimal("0.0000001"), rounding=ROUND_DOWN)
print(f"The value in the variable 'decimal_value' is {decimal_value}")
print(f"The type of the variable 'decimal_value' is {type(decimal_value)}\n")

# ------------------------------------------------------------
# 4. COMPLEX NUMBERS - numbers with real and imaginary parts
# ------------------------------------------------------------
complex_value = 3 + 4j
print(("COMPLEX NUMBERS DEMONSTRATION").center(38, ""))
print('-' * 38) # Console.WriteLine(new string('-', 38));
print(f"The value in the variable 'complex_value' is {complex_value}")
print(f"The type of the variable 'complex_value' is {type(complex_value)}\n")
print(f"Real part: {complex_value.real}")
print(f"Imaginary part: {complex_value.imag}")

# ------------------------------------------------------------
# 5. FRACTIONAL NUMBERS - ration al numbers
# ------------------------------------------------------------
fraction_value = Fraction(7, 3)
print(("FRACTIONAL NUMBERS DEMONSTRATION").center(38, ""))
print('-' * 38) # Console.WriteLine(new string('-', 38));
print(f"The value in the variable 'fraction_value' is {fraction_value}")
print(f"The type of the variable 'fraction_value' is {type(fraction_value)}\n")

# ------------------------------------------------------------
# 6. Boolean (True or False)
# ------------------------------------------------------------
true_value = True
false_value = False; n = 5; a = 8 # Declare multiple variable in a single line
print(f"DEMONSTRATING BOOLEAN VALUES".center(38, " "))
print('-' * 38)
print(f"The value in the boolean variable 'true_value' is {true_value}")
print(f"The value in the boolean variable 'false_value' is {false_value}")
print(f"The type of the boolean variable 'true_value' is {type(true_value)}")
print('-' * 38)
print(f"Using booleans in arithmetic operations")
print(f"True + True = {true_value + true_value}")
print(f"True + False = {true_value + false_value}")
print(f"False + False = {false_value + false_value}")
print(f"False + n(5) is: {false_value + n}")
print(f"True + a(8) is: {true_value + a}")
print(f"True x a(8) is: {true_value * a}")
print(f"(n < a) x 10 + (n == a) x 20 is: {(n < a) * 10 + (n == a) * 20}")

# Demonstrate various numbering systems

# Binary values base2

print('Binary value(s) demonstration')

# Binary values or literals are represented using the prefix 0b or 0B (zero & letter b)

binary_value = 0b1011  # Binary for 11 in decimal

print(f"Value of 'binary_value' is:{bin(binary_value)}"

      f"\nIn Octal {oct(binary_value)}\nIn decimal: {binary_value}"

      f"\nIn Hexadecimal {hex(binary_value)}\n\n")

# Octal values base8

print('Octal value(s) demonstration')

# Octal values or literals are represented using the prefix 0o or 0O (zero & letter o)

octal_value = 0o20  # Binary for 16 in decimal

print(f"Value of 'octal_value' is:{oct(octal_value)}"

      f"\nIn binary {bin(octal_value)}\nIn decimal: {octal_value}"

      f"\nIn Hexadecimal {hex(octal_value)}\n\n")

# Hexadecimal values base16

print('Hexadecimal value(s) demonstration')

# Hexadecimal values or literals are represented using the prefix 0x or 0X (zero & letter x)

hex_value = 0x18  # Hexadecimal for 24 in decimal

print(f"Value of 'hex_value' is:{hex(hex_value)}"

      f"\nIn binary {bin(hex_value)}"

      f"\nIn octal {oct(hex_value)}"

      f"\nIn decimal: {hex_value}\n\n")
