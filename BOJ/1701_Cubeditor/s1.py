# 1701_Cubeditor 풀이
# 2022-02-18

def length(s):
    c = 0
    for _ in s:
        c += 1
    return c


text = input()
len_t = length(text)
stop = 0
l = len_t

while l > 0:
    i = 0
    while i < len_t - l + 1:
        part = text[i:i + l]

        if part in text[i+1:len_t]:
            stop = 1
            break
        elif part in text[0:i]:
            stop = 1
            break
        else:
            if i + l < len_t and (text[i + l] not in part):
                i += l
                continue
        i += 1

    if stop == 1:
        break
    l -= 1

print(l)