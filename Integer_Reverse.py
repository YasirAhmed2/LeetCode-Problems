def reverse(x: int) -> int:
    INT_MAX = 2**31 - 1   # 2147483647
    INT_MIN = -2**31      # -2147483648
    
    sign = -1 if x < 0 else 1
    x = abs(x)
    rev = 0
    
    while x != 0:
        digit = x % 10
        x //= 10
        
        # Check for overflow before actually adding the digit
        if rev > (INT_MAX - digit) // 10:
            return 0
        rev = rev * 10 + digit
        
    return sign * rev

# Example usage
print(reverse(123))   # Output: 321
print(reverse(-123))  # Output: -321
print(reverse(120))   # Output: 21
print(reverse(1534236469))  # Output: 0 (overflow case)
