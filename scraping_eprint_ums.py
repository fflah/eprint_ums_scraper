from selenium import webdriver   
import time                      
from bs4 import BeautifulSoup
import csv


'''
::Kode jurusan UMS::
Fakultas Agama Islam: FAK=5FG/
Ekonomi Islam: I100/
Ushuluddin: H000/
Hukum Ekonomi Syariah (HES): I000/
Ilmu Alquran dan Tafsir: G100/
Pendidikan Agama Islam (PAI): G000/
Fakultas Ekonomi dan Bisnis: FAK=5FB/
Akuntansi: B200/
Ilmu Ekonomi dan Studi Pembangunan: B300/
Manajemen: B100/
Fakultas Farmasi: FAK=5FK/
Farmasi: K100/
Fakultas Geografi: FAK=5FE/
Geografi: E100/
Fakultas Hukum: FAK=5FC/
Hukum: C100/
Fakultas Ilmu Kesehatan: FAK=5FJ/
Fisioterapi: J120/
Fisioterapi D3: J100/
Fisioterapi D4: J110/
Gizi: J310/
Gizi D3: J300/
Keperawatan: J210/
Keperawatan D3: J200/
Kesehatan Masyarakat: J410/
Profesi Ners: J230/
Fakultas Ilmu Komunikasi dan Informatika: FAK=5FL/
Ilmu Komunikasi: L100/
Teknik Informatika: L200/
Fakultas Kedokteran: KED/
Kedokteran: J500/
Fakultas Kedokteran Gigi: KEDG/
Kedokteran Gigi: j520/
Fakultas Psikologi: FAK=5FF/
Psikologi: F100/
Magister Profesi Psikologi: T100/
Fakultas Teknik: FAK=5FD/
Teknik Arsitektur: D300/
Teknik Elektro: D400/
Teknik Industri: D600/
Teknik Kimia: D500/
Teknik Mesin: D200/
Teknik Otomotif: D700/
Teknik Sipil: D100/
Fakultas Keguruan dan Ilmu Pendidikan: FAK=5FA/
Pendidikan Akuntansi: A210/
Pendidikan Anak Usia Dini: A430/
Pendidikan Bahasa Inggris: A320/
Pendidikan Bahasa, Sastra Indonesia dan Daerah: A310/
Pendidikan Biologi: A420/
Pendidikan Geografi: A610/
Pendidikan Guru Sekolah Dasar: A510/
Pendidikan Kewarganegaraan: A220/
Pendidikan Matematika: A410/
Pendidikan Olahraga: A810/
Pendidikan Teknik Informatika: A620/
Fakultas Pasca Sarjana: FAK=5FO/
Magister Administrasi Pendidikan: Q100/
Magister Akuntansi: W100/
Magister Farmasi: V100/
Magister Hukum: R100/
Magister Hukum Ekonomi Syariah: O200/
Magister Manajemen: P100/
Magister Pemikiran Islam: O000/
Magister Pendidikan Bahasa Inggris: S400/
Magister Pendidikan Dasar: Q200/
Magister Pendidikan Islam: O100/
Magister Pengkajian Bahasa: S200/
Magister Sains Psikologi: S300/
Magister Teknik Kimia: U200/
Magister Teknik Mesin: U100/
Magister Teknik Sipil: S100/
Program Doktor (S3) Ilmu Hukum: R200/
Unit: UNIT/
Humas: U=5FHum/
Kemahasiswaan: U=5FMhs/
Fakultas Agama Islam: FAK=5FG/
Ekonomi Islam: I100/
Ushuluddin: H000/
Hukum Ekonomi Syariah (HES): I000/
Ilmu Alquran dan Tafsir: G100/
Pendidikan Agama Islam (PAI): G000/
Ekonomi Islam: I100/
Ushuluddin: H000/
Hukum Ekonomi Syariah (HES): I000/
Ilmu Alquran dan Tafsir: G100/
Pendidikan Agama Islam (PAI): G000/
Fakultas Ekonomi dan Bisnis: FAK=5FB/
Akuntansi: B200/
Ilmu Ekonomi dan Studi Pembangunan: B300/
Manajemen: B100/
Akuntansi: B200/
Ilmu Ekonomi dan Studi Pembangunan: B300/
Manajemen: B100/
Fakultas Farmasi: FAK=5FK/
Farmasi: K100/
Farmasi: K100/
Fakultas Geografi: FAK=5FE/
Geografi: E100/
Geografi: E100/
Fakultas Hukum: FAK=5FC/
Hukum: C100/
Hukum: C100/
Fakultas Ilmu Kesehatan: FAK=5FJ/
Fisioterapi: J120/
Fisioterapi D3: J100/
Fisioterapi D4: J110/
Gizi: J310/
Gizi D3: J300/
Keperawatan: J210/
Keperawatan D3: J200/
Kesehatan Masyarakat: J410/
Profesi Ners: J230/
Fisioterapi: J120/
Fisioterapi D3: J100/
Fisioterapi D4: J110/
Gizi: J310/
Gizi D3: J300/
Keperawatan: J210/
Keperawatan D3: J200/
Kesehatan Masyarakat: J410/
Profesi Ners: J230/
Fakultas Ilmu Komunikasi dan Informatika: FAK=5FL/
Ilmu Komunikasi: L100/
Teknik Informatika: L200/
Ilmu Komunikasi: L100/
Teknik Informatika: L200/
Fakultas Kedokteran: KED/
Kedokteran: J500/
Kedokteran: J500/
Fakultas Kedokteran Gigi: KEDG/
Kedokteran Gigi: j520/
Kedokteran Gigi: j520/
Fakultas Psikologi: FAK=5FF/
Psikologi: F100/
Magister Profesi Psikologi: T100/
Psikologi: F100/
Magister Profesi Psikologi: T100/
Fakultas Teknik: FAK=5FD/
Teknik Arsitektur: D300/
Teknik Elektro: D400/
Teknik Industri: D600/
Teknik Kimia: D500/
Teknik Mesin: D200/
Teknik Otomotif: D700/
Teknik Sipil: D100/
Teknik Arsitektur: D300/
Teknik Elektro: D400/
Teknik Industri: D600/
Teknik Kimia: D500/
Teknik Mesin: D200/
Teknik Otomotif: D700/
Teknik Sipil: D100/
Fakultas Keguruan dan Ilmu Pendidikan: FAK=5FA/
Pendidikan Akuntansi: A210/
Pendidikan Anak Usia Dini: A430/
Pendidikan Bahasa Inggris: A320/
Pendidikan Bahasa, Sastra Indonesia dan Daerah: A310/
Pendidikan Biologi: A420/
Pendidikan Geografi: A610/
Pendidikan Guru Sekolah Dasar: A510/
Pendidikan Kewarganegaraan: A220/
Pendidikan Matematika: A410/
Pendidikan Olahraga: A810/
Pendidikan Teknik Informatika: A620/
Pendidikan Akuntansi: A210/
Pendidikan Anak Usia Dini: A430/
Pendidikan Bahasa Inggris: A320/
Pendidikan Bahasa, Sastra Indonesia dan Daerah: A310/
Pendidikan Biologi: A420/
Pendidikan Geografi: A610/
Pendidikan Guru Sekolah Dasar: A510/
Pendidikan Kewarganegaraan: A220/
Pendidikan Matematika: A410/
Pendidikan Olahraga: A810/
Pendidikan Teknik Informatika: A620/
Fakultas Pasca Sarjana: FAK=5FO/
Magister Administrasi Pendidikan: Q100/
Magister Akuntansi: W100/
Magister Farmasi: V100/
Magister Hukum: R100/
Magister Hukum Ekonomi Syariah: O200/
Magister Manajemen: P100/
Magister Pemikiran Islam: O000/
Magister Pendidikan Bahasa Inggris: S400/
Magister Pendidikan Dasar: Q200/
Magister Pendidikan Islam: O100/
Magister Pengkajian Bahasa: S200/
Magister Sains Psikologi: S300/
Magister Teknik Kimia: U200/
Magister Teknik Mesin: U100/
Magister Teknik Sipil: S100/
Program Doktor (S3) Ilmu Hukum: R200/
Magister Administrasi Pendidikan: Q100/
Magister Akuntansi: W100/
Magister Farmasi: V100/
Magister Hukum: R100/
Magister Hukum Ekonomi Syariah: O200/
Magister Manajemen: P100/
Magister Pemikiran Islam: O000/
Magister Pendidikan Bahasa Inggris: S400/
Magister Pendidikan Dasar: Q200/
Magister Pendidikan Islam: O100/
Magister Pengkajian Bahasa: S200/
Magister Sains Psikologi: S300/
Magister Teknik Kimia: U200/
Magister Teknik Mesin: U100/
Magister Teknik Sipil: S100/
Program Doktor (S3) Ilmu Hukum: R200/

'''
def eprint_ums():
    driver = webdriver.Chrome(executable_path='env/chromedriver')
    alamatURL = 'http://eprints.ums.ac.id/view/divisions/L200/'   #L200, kode jurusan    
    driver.get(alamatURL)   
    data_eprints = []
    dosen_ = []
    # range tahun angkatan 2020-2021
    for i in list(range(2020, 2022)):
        driver.find_element_by_link_text(str(i)).click()
        time.sleep(1)
        page_source = driver.page_source

        soup = BeautifulSoup(page_source, 'lxml')
        p = soup.find_all('p')    
        for i in p:
            for a in i.find_all('a', href=True):
                xpath = "//a[@href='{}']".format(a['href'])    
                time.sleep(0.05)
                driver.find_element_by_xpath(xpath).click()
                page_skripsi = driver.page_source
                
                soup_ = BeautifulSoup(page_skripsi, 'lxml')
                dosen = soup_.find_all('span', {'class' : 'person_name'})
                dosen = [span.get_text() for span in dosen]
                
                abstrak = soup_.find('meta', attrs={'name': 'DC.description'})
                keyword = soup_.find('meta', attrs={'name': 'eprints.keywords'})
                abstrak = (abstrak['content'])
                judul = soup_.find('meta', attrs={'name': 'eprints.title'})
                judul = (judul['content'])
                if keyword != None:
                    print(keyword['content'])
                    if len(dosen) >= 2:
                        data = {
                            'dosen':dosen[1],
                            'judul':judul,
                            'abstrak':abstrak,
                            'keyword': keyword['content']

                        }
                        print('data ===> ' + judul)
                        dosen_.append(dosen[1])
                
            data_eprints.append(data)
            print('total data = ' + str(len(data_eprints)))

            driver.execute_script("window.history.go(-1)")
        driver.execute_script("window.history.go(-1)")  

    # sort by nama dosen
    Dosen = list(dict.fromkeys(dosen_))    
    Ember = []
    for i in Dosen:        
        for x in data_eprints:
            if i == x['dosen']:
                Ember.append(x)
            else:
                pass     

    keys = Ember[0].keys()
    with open('data_eprints.csv', 'w', newline='')  as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(Ember)
    
    driver.close()

eprint_ums()

