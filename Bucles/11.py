def funcion_completa(
    Johan,             
    Sebastian="valor", 
    *Castro,           
    **Gonzalez         
):
    print("Obligatorio:", Johan)
    print("Opcional:", Sebastian)
    print("args:", Castro)
    print("kwargs:", Gonzalez)
funcion_completa(
    1,         
    2,         
    3, 4, 5,   
    x=10, y=20 
)