file = open("sample.txt", "r")
text = file.read()
file.close()

words = text.split()
print("Word count:", len(words))

freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1

print("Word frequency:", freq)
