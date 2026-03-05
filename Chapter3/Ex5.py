numbers = list(map(float, input("Nhập các số cách nhau bởi dấu cách: ").split()))
for i in range(1, len(numbers)):
    key = numbers[i]
    j = i - 1
    while j >= 0 and numbers[j] < key:
        numbers[j + 1] = numbers[j]
        j -= 1
    numbers[j + 1] = key
print("Danh sách giảm dần:", numbers)
