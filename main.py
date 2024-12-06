# octal_conversion_method2.py

def decimal_to_octal_manual(decimal_number):
    result = ""
    while decimal_number > 0:
        result = str(decimal_number % 8) + result
        decimal_number //= 8
    return result

if __name__ == "__main__":
    number = int(input("10-lik sanoq tizimidagi sonni kiriting: "))
    print("8-lik sanoq tizimi (Qo'lda hisoblangan):", decimal_to_octal_manual(number))
