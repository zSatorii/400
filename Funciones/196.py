Johan = [10, 15, 12, 20, 18]
Sebastian = []
for Castro in range(1, len(Johan)):
    Sebastian.append(Johan[Castro] - Johan[Castro - 1])
print(Sebastian)