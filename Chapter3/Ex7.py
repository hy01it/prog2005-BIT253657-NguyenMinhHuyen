numbers = list(map(int, input("Nhập các số: ").split()))
target = int(input("Nhập số cần tìm: "))
found = -1
for i in range(len(numbers)):
    if numbers[i] == target:
        found = i
        break
if found != -1:
    print("Vị trí:", found)
else:
    print("Không tìm thấy")
