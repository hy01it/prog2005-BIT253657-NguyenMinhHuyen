numbers = list(map(int, input("Nhập các số: ").split()))
print("Các số lẻ:")
for num in numbers:
    if num % 2 != 0:
        print(num)
