y=raw_input("masukkan karakter:")
x=input("masukkan jumlah baris:")
for a in range(x):
    for b in range(x):
        print " ",
        if a<=b:
            print y,
    print""
