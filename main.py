# CAPSTONE PROJECT MODULE 1
# Siamdhani Nurcahyo
# Yellow Pages (Data Kontak Telepon)
import re

data_kontak_customer = {'contact_id' : ['ID1','ID2'],
              'contact_name' : ['Siamdhani','Nurcahyo'],
              'contact_phone' : ['08584423523','0819726789'],
              'contact_email' : ['siamdhani@gmail.com','nurcahyo@yahoo.com'],
              'contact_address' : ['Jakarta','Bandung']
            }

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.com\b'

def print_menu():
    response_menu = input("""\n################# Data Kontak Pelanggan #################

                1. Tampilkan Kontak Pelanggan
                2. Menambahkan Kontak Pelanggan
                3. Mengubah Kontak Pelanggan
                4. Menghapus Kontak Pelanggan
                5. Keluar
                Silahkan Pilih [1-5] : """)

    return response_menu

def display_kontak_pelanggan(response_report,CONTACT_ID_FOR_DISPLAY):
    if response_report == '1':
        for value in data_kontak_customer.values():
            if not value:
                print("\n\t\t***!!! Tidak Ada Data Kontak Pelanggan !!!***")
                break
            else:
                print("\n\t\tDaftar Kontak Pelanggan : ")
                for i in range(len(data_kontak_customer['contact_id'])):
                    print(f"\t\t{i+1}. Kontak ID : {data_kontak_customer['contact_id'][i]}, Nama : {data_kontak_customer['contact_name'][i]}, No. Telp : {data_kontak_customer['contact_phone'][i]}, Email : {data_kontak_customer['contact_email'][i]}, Alamat : {data_kontak_customer['contact_address'][i]}")
                break
    else:
        for value in data_kontak_customer.values():
            if not value:
                print("\n\t\t***!!! Tidak Ada Data Kontak Pelanggan !!!***")
                break
            else:
                if CONTACT_ID_FOR_DISPLAY in data_kontak_customer['contact_id']:
                    index = data_kontak_customer['contact_id'].index(CONTACT_ID_FOR_DISPLAY)
                    print("\n\t\tData Kontak Pelanggan dengan Kontak ID : ", CONTACT_ID_FOR_DISPLAY)
                    print(f"\t\t{index+1}. Kontak ID : {data_kontak_customer['contact_id'][index]}, Nama : {data_kontak_customer['contact_name'][index]}, No. Telp : {data_kontak_customer['contact_phone'][index]}, Email : {data_kontak_customer['contact_email'][index]}, Alamat : {data_kontak_customer['contact_address'][index]}")
                    break
                else:
                    print("\n\t\t***!!! Tidak Ada Data Kontak Pelanggan !!!***")
                    break

def add_kontak_pelanggan(CONTACT_ID):
    checkpoint = 0
    if CONTACT_ID in data_kontak_customer['contact_id']:
        print("\n\t\t***!!! Data Kontak Pelanggan Sudah Ada !!!***")
        return
    while True:
        if checkpoint == 0:
            CONTACT_NAME = input("\t\tMasukkan Nama Pelanggan [Maks 20 Karakter] : ") #use for add
            if len(CONTACT_NAME) > 20:
                print("\n\t\t***!!! Nama Pelanggan Tidak Boleh Lebih Dari 20 Karakter !!!***")
            else:
                checkpoint += 1
        if checkpoint == 1:
            CONTACT_PHONE = input("\t\tMasukkan No. Telp Pelanggan [Wajib Angka] : ") #use for add
            if not CONTACT_PHONE.isnumeric():
                print("\n\t\t***!!! No. Telp Wajib Angka Semua !!!***")
            else:
                checkpoint += 1
        if checkpoint == 2:
            CONTACT_EMAIL = input("\t\tMasukkan Email Pelanggan [Format Email -> ___@___.com] : ") #use for add
            if  not (re.fullmatch(regex, CONTACT_EMAIL)):
                print("\n\t\t***!!! Email Tidak Sesuai Format || Contoh : snpz1@pwdk.com !!!***")
            else:
                checkpoint += 1
        if checkpoint == 3:
            CONTACT_ADDRESS = input("\t\tMasukkan Alamat Pelanggan [Maks 30 Karakter]: ") #use for add
            if len(CONTACT_ADDRESS) > 30:
                print("\n\t\t***!!! Alamat Tidak Boleh Lebih Dari 30 Karakter !!!***")
            else:
                checkpoint += 1
        if checkpoint == 4:
            break
    
    while True:
        confirm_add_data = input("\n\t\tApakah Data akan disimpan ? (Y/N)(y/n) : ").lower().strip()
        if confirm_add_data == 'y':
            for key in data_kontak_customer.keys():
                data_kontak_customer[key].append(locals()[key.upper()])
            print("\n\t\t***!!! Data Kontak Pelanggan Tersimpan !!!***")
            break
        elif confirm_add_data == 'n':
            print("\n\t\t***!!! Data Kontak Pelanggan Tidak Tersimpan !!!***")
            break

def update_kontak_pelanggan(CONTACT_ID_FOR_UPDATE):
    checkpoint = 0
    if CONTACT_ID_FOR_UPDATE in data_kontak_customer['contact_id']:
        index = data_kontak_customer['contact_id'].index(CONTACT_ID_FOR_UPDATE)
        print("\t\tData Kontak Pelanggan dengan Kontak ID : ", CONTACT_ID_FOR_UPDATE)
        print(f"\t\t{index+1}. Kontak ID : {data_kontak_customer['contact_id'][index]}, Nama : {data_kontak_customer['contact_name'][index]}, No. Telp : {data_kontak_customer['contact_phone'][index]}, Email : {data_kontak_customer['contact_email'][index]}, Alamat : {data_kontak_customer['contact_address'][index]}")
    else:
        print("\n\t\t***!!! Tidak Ada Data Kontak Pelanggan !!!***")
        return

    while True:
        proceed_update_data = input("\n\t\tTekan Y/y jika ingin lanjut Update data atau N/n jika ingin batal Update : ").lower().strip()
        if proceed_update_data == 'y':
            while True:
                response_update_key = input("""\n\t\tPilih Data Yang Ingin Diupdate :

                1. Nama Pelanggan
                2. No. Telp Pelanggan
                3. Email Pelanggan
                4. Alamat Pelanggan
                5. Kembali
                Silahkan Pilih [1-5] : """)
                
                if response_update_key == '5':
                    break
                else:
                    if response_update_key == '1':
                        while True:
                            while True:
                                CONTACT_NAME_FOR_UPDATE = input("\n\t\tMasukkan Nama Baru [Maks 20 Karakter] : ")
                                if len(CONTACT_NAME_FOR_UPDATE) > 20:
                                    print("\n\t\t***!!! Nama Pelanggan Tidak Boleh Lebih Dari 20 Karakter !!!***")
                                else:
                                    break
                            confirm_update_data= input("\n\t\tApakah Data Akan Diupdate ? (Y/N)(y/n) : ").lower().strip()
                            if confirm_update_data == 'y':
                                data_kontak_customer['contact_name'][index] = CONTACT_NAME_FOR_UPDATE
                                print("\n\t\t***!!! Nama Kontak Pelanggan Terupdate !!!***")
                                break
                            elif confirm_update_data == 'n':
                                print("\n\t\t***!!! Nama Kontak Pelanggan Tidak Terupdate !!!***")
                                break
                    elif response_update_key == '2':
                        while True:
                            while True:
                                CONTACT_PHONE_FOR_UPDATE = input("\n\t\tMasukkan No.Telp Baru [Wajib Angka] : ")
                                if not CONTACT_PHONE_FOR_UPDATE.isnumeric():
                                    print("\n\t\t***!!! No. Telp Wajib Angka Semua !!!***")
                                else:
                                    break
                            confirm_update_data= input("\n\t\tApakah Data Akan Diupdate ? (Y/N)(y/n) : ").lower().strip()
                            if confirm_update_data == 'y':
                                data_kontak_customer['contact_phone'][index] = CONTACT_PHONE_FOR_UPDATE
                                print("\n\t\t***!!! No.Telp Kontak Pelanggan Terupdate !!!***")
                                break
                            elif confirm_update_data == 'n':
                                print("\n\t\t***!!! No.Telp Kontak Pelanggan Tidak Terupdate !!!***")
                                break
                    elif response_update_key == '3':
                        while True:
                            while True:
                                CONTACT_EMAIL_FOR_UPDATE = input("\n\t\tMasukkan Email Baru [Format Email -> ___@___.com] : ")
                                if  not (re.fullmatch(regex, CONTACT_EMAIL_FOR_UPDATE)):
                                    print("\n\t\t***!!! Email Tidak Sesuai Format || Contoh : snpz1@pwdk.com !!!***")
                                else:
                                    break
                            confirm_update_data= input("\n\t\tApakah Data Akan Diupdate ? (Y/N)(y/n) : ").lower().strip()
                            if confirm_update_data == 'y':
                                data_kontak_customer['contact_email'][index] = CONTACT_EMAIL_FOR_UPDATE
                                print("\n\t\t***!!! Email Kontak Pelanggan Terupdate !!!***")
                                break
                            elif confirm_update_data == 'n':
                                print("\n\t\t***!!! Email Kontak Pelanggan Tidak Terupdate !!!***")
                                break
                    elif response_update_key == '4':
                        while True:
                            while True:
                                CONTACT_ADDRESS_FOR_UPDATE = input("\n\t\tMasukkan Alamat Baru [Maks 30 Karakter] : ")
                                if len(CONTACT_ADDRESS_FOR_UPDATE) > 30:
                                    print("\n\t\t***!!! Alamat Tidak Boleh Lebih Dari 30 Karakter !!!***")
                                else:
                                    break
                            confirm_update_data= input("\n\t\tApakah Data Akan Diupdate ? (Y/N)(y/n) : ").lower().strip()
                            if confirm_update_data == 'y':
                                data_kontak_customer['contact_address'][index] = CONTACT_ADDRESS_FOR_UPDATE
                                print("\n\t\t***!!! Alamat Kontak Pelanggan Terupdate !!!***")
                                break
                            elif confirm_update_data == 'n':
                                print("\n\t\t***!!! Alamat Kontak Pelanggan Tidak Terupdate !!!***")
                                break
        elif proceed_update_data == 'n':
            break
    
def delete_kontak_pelanggan(CONTACT_ID_FOR_DELETE):
    if CONTACT_ID_FOR_DELETE in data_kontak_customer['contact_id']:
        index = data_kontak_customer['contact_id'].index(CONTACT_ID_FOR_DELETE)
        print("\t\tData Kontak Pelanggan dengan Kontak ID : ", CONTACT_ID_FOR_DELETE)
        print(f"\t\t{index+1}. Kontak ID : {data_kontak_customer['contact_id'][index]}, Nama : {data_kontak_customer['contact_name'][index]}, No. Telp : {data_kontak_customer['contact_phone'][index]}, Email : {data_kontak_customer['contact_email'][index]}, Alamat : {data_kontak_customer['contact_address'][index]}")
    else:
        print("\n\t\t***!!! Tidak Ada Data Kontak Pelanggan !!!***")
        return
    while True:
        confirm_delete_data= input("\n\t\tApakah Data Akan Dihapus ? (Y/N)(y/n) : ").lower().strip()
        if confirm_delete_data == 'y':
            for key in data_kontak_customer.keys():
                data_kontak_customer[key].pop(index)
            print("\n\t\t***!!! Data Kontak Pelanggan Terhapus! !!!***")
            break
        elif confirm_delete_data == 'n':
            print("\n\t\t***!!! Data Kontak Pelanggan Tidak Terhapus !!!***")
            break

while True:
    response_menu = print_menu()
    if response_menu == '1':
        while True:
            response_display = input("""\n################# Daftar Kontak Pelanggan #################

                1. Tampilkan Seluruh Data Kontak Pelanggan
                2. Tampilkan Data Kontak Pelanggan Tertentu
                3. Kembali Ke Menu Utama
                Silahkan Pilih [1-3] : """)
            if response_display == '3':
                    break
            else:
                while True:
                    if response_display == '1':
                        display_kontak_pelanggan(response_display,None)
                        break
                    elif response_display == '2':
                        CONTACT_ID_FOR_DISPLAY = input("\n\t\tMasukkan Kontak ID : ")
                        display_kontak_pelanggan(response_display,CONTACT_ID_FOR_DISPLAY)
                        break
                    else:
                        break
                
    elif response_menu == '2':
        while True:
            response_add = input("""\n################# Menambah Data Kontak Pelanggan #################

                1. Tambah Data Kontak Pelanggan
                2. Kembali Ke Menu Utama
                Silahkan Pilih [1-2] : """)
            if response_add == '2':
                    break
            else:
                while True:
                    if response_add == '1':
                        CONTACT_ID_FOR_ADD = input("\n\t\tMasukkan Kontak ID : ")
                        add_kontak_pelanggan(CONTACT_ID_FOR_ADD)
                        break
                    else:
                        break
    elif response_menu == '3':
        while True:
            response_update = input("""\n################# Mengubah Data Kontak Pelanggan #################

                1. Ubah Data Kontak Pelanggan
                2. Kembali Ke Menu Utama
                Silahkan Pilih [1-2] : """)
            if response_update == '2':
                    break
            else:
                while True:
                    if response_update == '1':
                        CONTACT_ID_FOR_UPDATE = input("\n\t\tMasukkan Kontak ID : ")
                        update_kontak_pelanggan(CONTACT_ID_FOR_UPDATE)
                        break
                    else:
                        break
    elif response_menu == '4':
        while True:
            response_delete= input("""\n################# Menghapus Data Kontak Pelanggan #################

                1. Hapus Data Kontak Pelanggan
                2. Kembali Ke Menu Utama
                Silahkan Pilih [1-2] : """)
            if response_delete == '2':
                    break
            else:
                while True:
                    if response_delete == '1':
                        CONTACT_ID_FOR_DELETE = input("\n\t\tMasukkan Kontak ID : ")
                        delete_kontak_pelanggan(CONTACT_ID_FOR_DELETE)
                        break
                    else:
                        break
    elif response_menu == '5':
        print("\n\t\t***!!! Sampai Jumpa !!!***\n")
        exit(0)