def es_perfecto(Johan):
    if Johan < 1:
        return False
    Sebastian = 0
    for Castro in range(1, Johan):
        if Johan % Castro == 0:
            Sebastian += Castro
    return Sebastian == Johan

print(f"6 es perfecto: {es_perfecto(6)}")
print(f"28 es perfecto: {es_perfecto(28)}")
print(f"10 es perfecto: {es_perfecto(10)}")