import math
while True:
 print "pilih menu:"
 print ('1.tambah')
 print ('2.kurang')
 print ('3.kali')
 print ('4.bagi')
 print ('5.pangkat')
 print ('6.akar')
 print "7.kembali"
 a=int(raw_input('pilih:'))
 if a==1:
  x=float(raw_input('masukkan angka1:'))
  y=float(raw_input('masukkan angka2:'))
  print "hasil tambahnya adalah:",x+y
 elif a==2:
  x=float(raw_input('masukkan angka1:'))
  y=float(raw_input('masukkan angka2:'))
  print "hasil penguangannya adalah",x-y
 elif a==3:
  x=float(raw_input('masukkan angka1:'))
  y=float(raw_input('masukkan angka2:'))
  print "hasil kali tersebut adalah:",x*y
 elif a==4:
  x=float(raw_input('masukkan angka1:'))
  y=float(raw_input('masukkan angka2:'))
  print "hasil bagi :",x/y            
 elif a==5:
  x=float(raw_input('masukkan angka1:'))
  y=float(raw_input('masukkan angka2:'))
  print "hasil pangkatnya adalah:",x**y
 elif a==6:
  x=float(raw_input('masukkan angka1:'))
  y=float(raw_input('masukkan angka2:'))
  print "hasil akar tersebut yaitu:",math.pow(x,1/y)
 elif a==7:
  print "kembali"
  break
 else:
  print "pilihan salah..!!! coba lagi"
