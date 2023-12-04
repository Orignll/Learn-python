#sistem konversi berat

def weight_conv():
    weight =int(input("masukkan berat anda: "))
    type =input("masukkan k atau l: ")

    if type.lower() == 'k':
        hasil = round(weight / 0.45359237)
        print (f"berat badanmu {hasil} pounds")

    elif type.lower() == 'l':
        hasil = round(weight * 0.45359237)
        print (f"berat badanmu {hasil} kg")
