numbers = list(map(int, input("Nhập các số: ").split()))
total = 0
print("Các số chẵn:")
for num in numbers:
    if num % 2 == 0:
        print(num)
        total += num
print("Tổng số chẵn:", total)
