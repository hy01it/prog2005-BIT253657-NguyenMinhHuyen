numbers = list(map(int, input("Nhập các số: ").split()))
swap_count = 0
for i in range(len(numbers)):
    for j in range(0, len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            swap_count += 1
print("Danh sách tăng dần:", numbers)
print("Số lần hoán đổi:", swap_count)
