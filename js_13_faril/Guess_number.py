# game tebak angka

def guess_number():
    angka_rahasia = 9
    batas = 3
    penghitung = 0


    while penghitung < batas :
        user = int(input("Masukkan angka > "))
        if user == angka_rahasia:
            print("Selamat kamu benar")
            break
        else :
            print("Kamu salah")
            penghitung +=1
            print ("kesempatanmu tinggal", batas - penghitung )
    else:
        print("kamu salah, angka yang benar adalah 9")
