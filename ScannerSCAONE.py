# ! / usr / bin / env python2
# - * - coding: utf-8 - * -
#
#


"" " 
Cyber ​​Maros Ar-Ge Training adına geliştirmiş hedef 
situs ve sunucudaki sitelerde SQL Injection açığı
arama aracı.
"" "

__author__   =  " DimasAriadi "
__date__     =  " 2018/06/20 "
__mail__     =  " dimasariadi787@yahoo.com "

coba :
	__version__  =  terbuka ( " versi " , " r " ) .read (). strip ()
kecuali :
	__version__  =  " 0.0.1 "

impor os
impor sys
waktu impor

dari src import crawler
dari src import sqliScan
dari src import reverseIp

dari colorama import init, Fore, Style

warna = {
	" " :         " " ,
	" red " : Fore. MERAH ,
	" cyan " : Kedepan. CYAN ,
	" blue " : Fore. BIRU ,
	" hijau " : Depan. HIJAU ,
	" white " : Fore. PUTIH ,
	" yellow " : Fore. KUNING ,
	" magenta " : Kedepan. MAGENTA ,
	" bright " : Gaya. TERANG
}

textTypes = { " info " : " [INFO] " , " err " : " [ERROR] " , " " : " " }}

sitesFromReverse   = []
sitesFromCrawler   = []
sitesFromSqliScan = []

 logo def ():
	warna cetak [ " cerah " ] + warna [ " biru " ] +  "" "
        _ _____ ____ __ ______ __
 _ __ (_) ___ // __ \ / / / _ __ / ___ ____ / /
| | / / / \ __ \ / / / / / / / __ \ / __ \ / /
| | / / / ___ / / / _ / / / /___ / / / / _ / / / _ / / /  
| ___ / _ // ____ / \ ___ \ _ \ / _____ / / _ / \ ____ / \ ____ / _ /                                                  
\ t \ t \ t Versi: % s
\ t \ t \ t http://github.com/DimasAriadi
\ t \ t \ t dimasariadi112.blogspot.com
"" " % ( __version__ )
def  vprint ( teks , warna = " " , ketik = " " ):
	'' ' Fungsi untuk menggunakan cetak lebih mengesankan ' ''

	text =   colors [ ' yellow ' ] + textTypes [ type ] + colors [ ' magenta ' ] +  " [ "   + time.strftime ( " % H:% M:% S " ) +  " ] "  + warna [color] + teks
	cetak teks

 penggunaan def ():
	warna cetak [ ' cerah ' ] + warna [ ' biru ' ] +  "" "
Penggunaan: viSQL
-----------------
	$ python2 viSQL.py -t http://www.bible-history.com
	$ python2 viSQL.py --target 54.201.8.54
	$ python2 viSQL.py -h / - bantuan
"" "

def  rIp ( url ):
	'' ' Suatu fungsi untuk menggunakan src / reverseIp.py ' ''
	
	vprint ( " Reverse IP lookup dimulai " , " hijau " , " info " )

	untuk situs di reverseIp.run (url):
		vprint ( "   "  + situs, " cyan " , " info " )
		sitesFromReverse.append ( ' http: // '  + situs)

def  crawl ():
	'' ' Suatu fungsi untuk menggunakan src / crawler.py ' ''

	vprint ( " Perayap dimulai " , " hijau " , " info " )

	untuk situs di sitesFromReverse:
		vprint ( " Merangkak -> "  + situs, " yellow " , " info " )

		sites = crawler.run (situs)

		if  type (situs) ! =  daftar :
			vprint (situs, " red " , " err " )
			terus
		lain :
			lulus

		vprint ( "   Ditemukan % s url. " % ( len (situs)), " cyan " , " info " )
		sitesFromCrawler.append ((situs, situs))

def  sC ():
	'' ' Suatu fungsi untuk pengguna src / sqliScan.py ' ''

	vprint ( " Pemindaian SQLi dimulai " , " hijau " , " info " )

	untuk tup di sitesFromCrawler:

		if  len (tup [ 1 ]) ==  0 :
			terus
		lain :
			lulus

		vprint ( " Situs: "  + tup [ 0 ], " yellow " , " info " )

		untuk url dalam tup [ 1 ]:
			test = sqliScan.run (url)

			jika test ==  Benar :
				vprint ( " SQLi vuln! -> "  + url, " cyan " , " info " )
			uji elif ==  " keluar " :
				istirahat
			lain :
				lulus

		cetak  " - "  *  20

def  main ():
	'' ' Fungsi utama ' ''

	if  len (sys.argv) ==  3  dan sys.argv [ 1 ] di [ ' -t ' , ' --target ' ]:
		url = sys.argv [ - 1 ]

		vprint ( " Situs web Target: "  +   url, " yellow " , " info " )
		
		rIp (url)
		merangkak()
		sC ()

	lain :
		pemakaian()

if  __name__  ==  " __main__ " :
	init ( autoreset = True )
	logo()
	vprint ( " Program dimulai " , " hijau " , " info " )
	utama()
	vprint ( " Program mematikan " , " kuning " , " info " )