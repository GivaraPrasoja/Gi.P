print ("\n\n================ Welcome To MY Mart ================\n")

pembelian = int(input("\n### Harga barang = Rp. "))
bayar = pembelian
nama_member = ("Givara Prasoja")
no_member = ("G.231.19.0135")

#diskon
diskon = pembelian * 40/100 # diskon 40%
diskon_member = bayar * 10/100 # diskon member 10%
diskon40 = bayar - diskon # diskon 40% tapi bukan member
diskon10 = diskon40 * 10/100 # jumlah setelah diskon 40% lalu diskon lagi 10%
setelah_diskon = diskon40 - diskon10  # Harga yang harus di bayar setelah dapat 2 diskon

if (pembelian >= 500000):
    bayar = pembelian
    print ("\nSelamat Anda mendapatkan Diskon  : 40%" )
    print ("Anda mendapat Protongan harga    : Rp; %s" %diskon )
    print ("\n# Yang harus anda bayar          : Rp; %s \n\n" % diskon40)

    member = str(input("### Apakah anda memiliki kartu member? [ya / tidak] "))

    if member == "ya":
        print ("\n== Nama Member Anda  : ",nama_member)
        print ("== No. Member Anda   : ",no_member)
        print ("\nAnda mendapatkan potongan harga lagi   : 10%" )
        print ("potongan belanja anda adalah           : Rp; %s"% diskon10 )
        print ("\n# Total yang harus anda bayar adalah   : Rp; %s \n\n" % setelah_diskon )
        #Cetak Struk
        print ("================ NOTA PEMBAYARAN ================\n")
        print ("== Nama Member Anda     : ",nama_member)
        print ("== No. Member Anda      : ",no_member,"\n")
        cash = int(input("== Uang yang dibayar    : Rp; " ))
        uang = cash
    
        #Kembalian
        kembalian_member = uang - setelah_diskon 

        print ("== Total Belanja Anda   : Rp; %s"%setelah_diskon)
        print ("________________________________________--")
        print ("== Uang kembalian       : Rp; %s" %kembalian_member)
        

    
    elif member == 'tidak':
        print ("\n# Total yang harus anda bayar adalah : Rp; %s\n" %diskon40 )

        #Cetak Struk
        print ("================ NOTA PEMBAYARAN ================\n")
        cash = int(input("== Uang yang dibayar    : Rp; " ))
        uang = cash
    
        #kembalian
        uang_kembali = uang - diskon40
    
        print ("== Total Belanja Anda   : Rp; %s"%diskon40)
        print ("________________________________________--")
        print ("== Uang kembalian       : Rp; %s\n" % uang_kembali)

    

if(pembelian < 500000): #jika belanja kurang dari Rp,500.000
    print ("\nMaaf Anda tidak mendapat diskon\n")
    print ("Total yang harus anda bayar adalah  : Rp; %s " %bayar )
    
    member = str(input("\n### Apakah anda memiliki kartu member? [ya/tidak]"))

    if member == "ya": #Jika member akan mendapat diskon 10%
        
        hanya_member = bayar - diskon_member
        print ("\n== Nama Member Anda     : ",nama_member)
        print ("== No. Member Anda      : ",no_member,"\n")
        print ("\nSelamat Anda mendapatkan diskon        : 10%" )
        print ("potongan belanja anda adalah           : Rp; %s"% diskon_member )
        print ("\n# Total yang harus anda bayar adalah   : Rp; %s \n\n" %hanya_member )

        #Cetak Struk
        print ("================ NOTA PEMBAYARAN ================\n")
        cash = int(input("== Uang yang dibayar    : Rp; " ))
        uang = cash
        kembalian_member = uang - hanya_member
        print ("== Total Belanja Anda   : Rp; %s"%hanya_member)
        print ("________________________________________--")
        print ("== Uang kembalian       : Rp; %s" %kembalian_member)
        
    elif member == 'tidak':
        print ("\nTotal yang harus anda bayar adalah : Rp; %s\n" %bayar )
        #Cetak Struk
        print ("================ NOTA PEMBAYARAN ================\n")
        cash = int(input("== Uang yang dibayar      : Rp; " ))
        uang = cash
    
        #kembalian
        uang_kembali = uang - bayar
    
        print ("== Total Belanja Anda     : Rp; %s"%bayar)
        print ("________________________________________--")
        print ("== Uang kembalian         : Rp; %s\n" % uang_kembali)

print ("\n Terimakasih Telah belanja DiToko kami :)" ) 
print (" Hati hati di jalan meskipun hidup ini tidak selalu sejalan :')")
print (" Selalu jaga kesehatan, kebersihan, ,iman, dan jangan lupa pakai masker :)")