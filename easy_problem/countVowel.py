text = input()
vowel = "AEIOUaeiou"
cnt = 0
for i in text:
    if i in vowel:
        cnt += 1
print(cnt)
