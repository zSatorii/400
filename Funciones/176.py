Johan = [1, 2, 3, 4, 5, 6]
for Sebastian in range(0, len(Johan), 2):
    if Sebastian + 1 < len(Johan):
        Castro = Johan[Sebastian] + Johan[Sebastian + 1]
        print(f"{Johan[Sebastian]} + {Johan[Sebastian + 1]} = {Castro}")