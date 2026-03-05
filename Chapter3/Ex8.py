numbers = list(map(int, input("Nhập các số: ").split()))
for num in numbers:
    if num > 10:
        print("Số đầu tiên > 10:", num)
        break
else:
    print("Không có số nào > 10")
