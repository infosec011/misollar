# hexadecimal_conversion_method3.py

def decimal_to_hexadecimal_using_math(decimal_number):
    import math
    hex_map = "0123456789ABCDEF"
    result = ""
    while decimal_number > 0:
        remainder = decimal_number % 16
        result = hex_map[remainder] + result
        decimal_number = math.floor(decimal_number / 16)
    return result

if __name__ == "__main__":
    number = int(input("10-lik sanoq tizimidagi sonni kiriting: "))
    print("16-lik sanoq tizimi (Math kutubxonasi bilan):", decimal_to_hexadecimal_using_math(number))
