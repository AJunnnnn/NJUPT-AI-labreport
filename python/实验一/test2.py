s = [9, 7, 8, 3, 2, 1, 5, 6]
print(f"变化前的数组为{s}")
for i in range(0, len(s)):
    if s[i] % 2 == 0:
        s[i] = s[i] * s[i]
print(f"变化后的数组为{s}")
