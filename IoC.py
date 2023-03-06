text = "andi Idna"

# for c in text:
#     histogram[c - 65] += 1

histogram = [0] * 26
for c in text.lower().replace(' ', ''):
    histogram[ord(c) - ord('a')] += 1

n = len(text)


print(histogram)

# ioc = 