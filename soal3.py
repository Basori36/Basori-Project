kiri = ['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v', 'b']
kanan = ['y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'n', 'm']
status = True
k = input ('masukka kata: ')
for i in range(len(k)-1):
    if (k[i] in kiri and k[i+1] in kiri or k[i] in kanan and k[i+1] in kanan):
        status = False
        print (status)
        print('setiap karakter tidak bergantian')

if status == True:
    print(status)
    print('setiap karakter selalu bergantian')


        