# 10-likdan 2-lik sanoq tizimiga o'tkazish
def decimal_to_binary(decimal_number):
    return bin(decimal_number)[2:]

if __name__ == "__main__":
    number = int(input("10-lik sanoq tizimidagi sonni kiriting: "))
    print("2-lik sanoq tizimi:", decimal_to_binary(number))
