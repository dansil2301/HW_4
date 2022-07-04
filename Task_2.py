example = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print([example[i] for i in range(1, len(example)) if example[i - 1] < example[i]])
