z=raw_input("Masukan Karakter : ")
y=input("Masukan Jumlah Baris : ")
x=y-1
for a in range(x):
    for b in range(x):
        if (a>=b):
            print z,
    print ""
for c in range (y):
    print z,
print ""
for d in range(x):
    for e in range(x):
        if (d<=e):
            print z,
    print ""
print "\n"
