service=input("Jenis layanan yang digunkan? Internet, Game, Pengetikan? *Pisahkan dengan spasi* " ).lower().split()
b=len(service)
def bulat():
    for serva in serv:
        if serva<30:
            serva=30
            servs.append(serva)
        else:
            serva=serva
            servs.append(serva)    
if b==3:
    inet=float(input("Berapa lama waktu internet? "))
    game=float(input("Berapa lama waktu pengetikan? "))
    ketik=float(input("Berapa lama waktu game? "))
    serv=[inet,ketik,game]
    servs=[]
    bulat()
    biaya=(servs[0]*4000/60+servs[1]*2000/60+servs[2]*5000/60)
    print("Biaya rental anda adalah Rp", biaya)
elif b==1 and service[0]=="internet":
    inet=int(input("Berapa lama waktu internet?"))
    serv=[inet]
    servs=[]
    bulat()
    biaya=(servs[0]*4000/60)
    print(biaya)
elif b==1 and service[0]=="pengetikan":
    ketik=int(input("Berapa lama waktu pengetikan?"))
    serv=[ketik]
    servs=[]
    bulat()
    biaya=(servs[0]*2000/60)
    print("Biaya rental anda adalah Rp", biaya)
elif b==1 and service[0]=="game":
    game=int(input("Berapa lama waktu game?"))
    serv=[game]
    servs=[]
    bulat()
    biaya=(servs[0]*5000/60)
    print("Biaya rental anda adalah Rp", biaya)
elif service[0]=="internet" and service[1]== "game":
    inet=int(input("Berapa lama waktu internet? "))
    game=int(input("Berapa lama waktu game? "))
    serv=[inet,game]
    servs=[]
    bulat()
    biaya=(servs[0]*4000/60+servs[1]*5000/60)
    print("Biaya rental anda adalah Rp", biaya)
elif service[0]=="internet" and service[1]== "pengetikan":
    inet=int(input("Berapa lama waktu internet? "))
    ketik=int(input("Berapa lama waktu pengetikan? "))
    serv=[inet,ketik]
    servs=[]
    bulat()
    biaya=(servs[0]*4000/60+servs[1]*2000/60)
    print("Biaya rental anda adalah Rp", biaya)
elif service[0]=="game" and service[1]== "pengetikan":
    game=int(input("Berapa lama waktu Game? "))
    ketik=int(input("Berapa lama waktu pengetikan? "))
    serv=[ketik,game]
    servs=[]
    bulat()
    biaya=(servs[1]*2000/60+servs[1]*5000/60)
    print("Biaya rental anda adalah Rp", biaya)
else:
    print("input salah")    
scan=input("Apakah Anda melakukan scan ? Ya/Tidak ").lower()
if scan=="ya":
    jumlah_scan=int(input("Berapa lembar ?"))
else:
    jumlah_scan=int(0)
cetak=input("Apakah Anda melakukan print ? Ya/tidak ").lower()
if cetak=="ya":
    print_warna=int(input("Berapa lembar print warna ? "))
    print_bw=int(input("Berapa lembar print hitam-putih ? "))
else:
    print_warna=int(0)
    print_bw=int(0)
teh_botol=input("Apakah Anda ambil teh Botol ? Ya/Tidak ")
if teh_botol=="ya":
    jumlah_teh_botol=int(input("Berapa botol? "))
else:
    jumlah_teh_botol=int(0)
semua=biaya+(jumlah_scan*1000)+(print_bw*300)+(print_warna*500)+(jumlah_teh_botol*3000)
print("Total biaya adalah Rp",semua)
input()