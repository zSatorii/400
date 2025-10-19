Johan = [
    {"nombre": "Ana", "nota": 85},
    {"nombre": "Carlos", "nota": 92},
    {"nombre": "Berta", "nota": 78}
]

Sebastian = sorted(Johan, key=lambda Castro: Castro["nota"], reverse=True)
print(Sebastian)