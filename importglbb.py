import GLBB

def main():
    #kecepatan akhir jika yang diketahui adalah tinggi
    va = 25
    a = 10
    t = 10

    kecepatanAkhirT = GLBB.kecepatanAkhirTinggi(va, a, t)

    print("KECEPATAN AKHIR JIKA YANG DIKETAHUI ADALAH TINGGI (Vt)")
    print("kecepatan awal\t: ", va)
    print("percepatan\t: ", a)
    print("tinggi\t: ", t)
    print("kecepatan akhir\t: ", kecepatanAkhirT)

    #kecepatan akhir jika yang diketahui adalah jarak
    va = 25
    a = 10
    s = 5

    kecepatanAkhirS = GLBB.kecepatanAkhirJarak(va, a, s)

    print("\nKECEPATAN AKHIR JIKA YANG DIKETAHUI ADALAH JARAK (Vt)")
    print("kecepatan awal\t: ", va)
    print("percepatan\t: ", a)
    print("jarak\t: ", s)
    print("kecepatan akhir\t: ", kecepatanAkhirS)

    # Jarak
    va = 25
    a = 10
    t = 15

    jarak = GLBB.jarak(va, t, a)

    print("\nJARAK (S)")
    print("kecepatan awal\t: ", va)
    print("percepatan\t: ", a)
    print("tinggi\t: ", t)
    print("Jarak\t: ", jarak)

    # percepatan
    va = 20
    vt = 40
    ta = 10
    tt = 20

    percepatan = GLBB.percepatan(va, vt, ta, tt)

    print("\nPERCEPATAN (a)")
    print("kecepatan awal\t: ", va)
    print("kecepatan akhir\t: ", vt)
    print("tinggi mulamula\t: ", ta)
    print("tinggi akhir\t: ", tt)
    print("percepatan\t: ", percepatan)

if __name__ == "__main__":
    main()