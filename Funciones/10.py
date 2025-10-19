def calcular_precio(Johan, Sebastian=1, Castro=0, Gonzalez=0.21):
    precio_base = Johan * Sebastian
    precio_con_descuento = precio_base * (1 - Castro)
    precio_final = precio_con_descuento * (1 + Gonzalez)
    return precio_final

precio1 = calcular_precio(100)
precio2 = calcular_precio(100, 2)
precio3 = calcular_precio(100, descuento=0.1)
precio4 = calcular_precio(producto=100, impuesto=0.10)