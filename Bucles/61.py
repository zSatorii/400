def signo_zodiacal(Johan, Sebastian):
    if (Johan == 3 and Sebastian >= 21) or (Johan == 4 and Sebastian <= 19):
        return "Aries"
    elif (Johan == 4 and Sebastian >= 20) or (Johan == 5 and Sebastian <= 20):
        return "Tauro"
    elif (Johan == 5 and Sebastian >= 21) or (Johan == 6 and Sebastian <= 20):
        return "Géminis"
    else:
        return "Otro signo"

print(f"Nacido el 25 de marzo: {signo_zodiacal(3, 25)}")
print(f"Nacido el 5 de mayo: {signo_zodiacal(5, 5)}")
print(f"Nacido el 15 de junio: {signo_zodiacal(6, 15)}")