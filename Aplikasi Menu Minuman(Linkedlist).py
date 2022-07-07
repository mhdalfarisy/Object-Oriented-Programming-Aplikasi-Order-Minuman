import os
import sys

import sys #this allows you to use the sys.exit command to quit/logout of the application
def main():
    login()
    
def login():
    username="Admincode"
    password="Adminaccess"
    print("Enter username : ")
    answer1=input()
    print("Enter password : ")
    answer2=input()
    if answer1==username and answer2==password:
        print("Welcome")
        menu()
        
    else:
        print("Try again")
        login()

class Menu_minuman: #Class ibarat ruangan, dan Menu_minuman ibarat isi dari kelas
        Jenis_minuman=''
        Nama_minuman=''
        Harga_minuman=''

pilih = 0 #Dibuat 0 karena nanti kita akan mengisi angka nya melalui aplikasi
Daftarminuman = []

def menu():
	print("Menu Aplikasi Daftar Minuman LinkedList python"); 
	print("-------------------------------------------")
	print("1. Input Daftar Menu Minuman")
	print("2. Tampilkan Daftar Menu Minuman")
	print("3. Update Daftar Menu Minuman")
	print("4. Hapus Daftar Menu Minuman")
	print("5. Author")
	print("6. Keluar Aplikasi")
	pilih = int(input("Masukkan pilihan anda : "))
	if pilih == 1 :
		pilih1()
		menu()
	
	elif pilih == 2:
		tampil() #Menampilkan menu yang ada dengan memasukan funtion tampil
		input("kembali menu utama") #
		menu() 
  
	elif pilih == 3:
		index_update=-1 
		tampil()
		id_edit = input("Input Nama Minuman yang akan di update ")
		for a in range(0, len(Daftarminuman)):
			print(Daftarminuman)
			if id_edit == Daftarminuman[a].Jenis_minuman: 
					index_update = a
					break 
		if(index_update > -1): #Lebih besar dari min 1 , maka masuk ke bari 40. 0 setelah index_update awalnya -1, ini itu nilai bantu untuk 
			print("INPUT DATA YANG DI UPATE ") 
			pilihan_minuman = Menu_minuman()
			pilihan_minuman.Jenis_minuman = (input("masukkan jenis minuman : "))
			pilihan_minuman.Nama_minuman = (input("masukkan nama minuman : "))
			pilihan_minuman.Harga_minuman = (input("memasukan harga minuman : "))
			Daftarminuman[index_update] = pilihan_minuman 
			print("berhasil update daftar minuman") 
		else : print("data minuman tidak ditemukan") 
		input("kembali menu utama") 
		menu()
  
	elif pilih ==4:
		tampil()
		index_delete=-1
		id_hapus = int(input("Input nama minuman yang akan di hapus : ")) 
		for a in range(0, len(Daftarminuman)): 
			if id_edit == Daftarminuman[a].Nama_minuman:
						index_delete = a
						break
		if(index_delete > -1):
			del Daftarminuman[index_delete]
			print("Data Telah di hapus") 
		else : print("data minuman tidak ditemukan")
		input("kembali menu utama") 
		menu()
	elif pilih == 5 :
		author()
		input("\n\n kembali menu utama") 
		menu()
	elif pilih == 6 :
		sys.exit()
	
def tampil():
	print("DAFTAR MINUMAN")
	for data in Daftarminuman:
		print("Jenis Minuman : "+str(data.Jenis_minuman)) 
		print("Nama Minuman : "+str(data.Nama_minuman))
		print("Harga Minuman: " + "Rp " +str(data.Harga_minuman))
		print("----------------------")

def author():
	print("Muhammad Al-farisy")
	

def pilih1():
	ulang = 'Y'
	while ulang in('y', 'Y'):
		PilihanMinumanBaru = Menu_minuman()
		print("INPUT DAFTAR MINUMAN ") 
		PilihanMinumanBaru.Jenis_minuman = (str(input("masukkan jenis minuman : "))) 
		PilihanMinumanBaru.Nama_minuman = (str(input("masukkan nama minuman : ")))
		PilihanMinumanBaru.Harga_minuman = (str(input("masukan harga minuman : ")))
		Daftarminuman.append(PilihanMinumanBaru) 
		ulang = input("Apakah Anda Ingin Mengulang (Y/ T)? ")		

main()