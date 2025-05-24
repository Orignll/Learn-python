
suhu =int(input("masukkan suhu: "))
type =input("konversi ke c atau f: ")

if type.lower() == 'c':
    hasil = round (suhu * 9/5) + 32
    print (f"suhumu {hasil} celcius")

elif type.lower() == 'f':
    hasil = round (suhu - 32) * 5/9
    print (f"suhumu {hasil} fahrenheit")
