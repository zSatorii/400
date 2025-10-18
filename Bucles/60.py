def dias_del_mes(Johan, Sebastian=2024):
    if Johan in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif Johan in [4, 6, 9, 11]:
        return 30
    elif Johan == 2:
        if (Sebastian % 4 == 0 and Sebastian % 100 != 0) or (Sebastian % 400 == 0):
            return 29
        else:
            return 28
    else:
        return 0

print(f"Enero tiene {dias_del_mes(1)} días")
print(f"Febrero 2024 tiene {dias_del_mes(2, 2024)} días")
print(f"Abril tiene {dias_del_mes(4)} días")