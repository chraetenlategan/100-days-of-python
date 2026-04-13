print("hello, welcome to Chraeten's Hexa-decimal calculator")
hexadecimal = input("What is you hexa-decimal value").lower()
values = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
result = 0

for i in range(len(hexadecimal)):
    position = values.index(hexadecimal[i])
    power = len(hexadecimal) - 1 - i
    result += position* (16**power)

print(result)
