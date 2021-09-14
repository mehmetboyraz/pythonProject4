import datacustomes as dc
import random


def log_in():
    print("Kartlı işlemer için 1'e basın")
    print("Kartsız işlemler için 2 ' ye basın")
    print("**************************")
    secim = input("seçim = ")
    hak = 3
    if secim == "1":
        loop = True
        while loop:
            if hak == 0:
                break

            kartnumarası = input("Kart  numaranızı giriniz")
            karsıfresı = input("kart sıfrenızı gırınız")

            for x in dc.datacustomer:
                if kartnumarası == x[7] and karsıfresı == x[6]:

                    global info
                    info = list(x)
                    print("***********")
                    print("hoşgeldiniz = ", info[1], info[2])
                    print("**************************")
                    loop = False

                    break
            while loop:
                print("***********************")
                print("kart ŞİFRESİ ve ya NUMARASI yanlış")
                hak -= 1
                print("***********************")
                print("kalan giriş hakkınız : {}".format(hak))
                break

    if secim == "2":
        loop = True
        while loop:
            if hak == 0:
                break

            tcNo = input("tc no giriniz : ")
            sms = random.randint(1000, 9999)
            print(sms)
            smsgir = int(input("sms kodunu giriniz"))
            for x in dc.datacustomer:
                if sms == smsgir and tcNo == x[9]:
                    info = list(x)
                    print("hoş geldiniz : ", info[1], info[2])
                    print("**************************")
                    loop = False
                    break
            while loop:
                print("tc veya sms no yanlış girdiniz")
                hak -= 1
                print("*************")
                print("kalan hakkınız", hak)
                break

    if secim != "1" and secim != "2":
        print("lütfen menüden bir sayı seçiniz")
        log_in()


def bakıyeSorgulama():
    loop = True
    while loop:

        print("bakiye sorgulama : 1")
        print("para yatırma : 2")
        print("para çekme : 3 ")
        print("havale gerçekleştirme : 4")
        print("Anlık kredi başvurursu : 5")
        print("**************************")
        ıslemsecım = input("Yapmak istediğiniz işlemi tuşlayınız: ")
        if ıslemsecım == "1":
            print("BAKİYENİZ : ", info[8])
            oncekimenu = input("bır önceki menü için 0'a çıkmak için 1'e basın = ")
            if oncekimenu == "0":
                loop = True
            elif oncekimenu == "1":
                loop = False

        if ıslemsecım == "2":
            yatırılacaktutar = int(input("yatırmak istediğiniz tutarı giriniz: "))
            info[8] += yatırılacaktutar
            dc.update("bakıye", info[8], info[0])
            print("yeni bakiyeniz = ", info[8])
            loop = False
            oncekimenu = input("bır önceki menü için 0'a çıkmak için 1'e basın = ")
            if oncekimenu == "0":
                loop = True
            elif oncekimenu == "1":
                loop = False

        if ıslemsecım == "3":
            cekılecektutar = int(input("cekmek istediğiniz  tutarı giriniz: "))
            info[8] -= cekılecektutar
            dc.update("bakıye", info[8], info[0])
            print("yeni bakiyeniz = ", info[8])
            loop = False
            oncekimenu = input("bır önceki menü için 0'a çıkmak için 1'e basın = ")
            if oncekimenu == "0":
                loop = True
            elif oncekimenu == "1":
                loop = False

        if ıslemsecım == "4":
            yatırılacakhesap = input("yatırmak istediğiniz hesabın kart numarasını giriniz: ")
            for x in dc.datacustomer:
                # x=list(x)
                if yatırılacakhesap == x[7]:
                    print(x[1], x[2], "kişisine para aktarım gercekleşecek onaylıyormusunuz: ")
                    onay = input("onay için 1 e basın: ")
                    if onay == "1":

                        tutar = int(input("gönderim yapılacak tutarı giriniz: "))

                        x[8] += tutar
                        dc.update("bakıye", x[8], x[0])

                        info[8] -= tutar
                        dc.update("bakıye", info[8], info[0])

                        loop = False
                        oncekimenu = input("bır önceki menü için 0'a çıkmak için 1'e basın = ")
                        if oncekimenu == "0":
                            loop = True
                        elif oncekimenu == "1":
                            loop = False

        if ıslemsecım == "5":
            for x in dc.datacustomer:
                print(x[5] * 24, "tl krediniz için subemize başvurabilirsiniz.")
                loop = False
                oncekimenu = input("bır önceki menü için 0'a çıkmak için 1' e basın =")
                if oncekimenu == "0":
                    loop = True
                elif oncekimenu == "1":
                    loop = False

        elif ıslemsecim != "1" and ıslemsecim != "2" and ıslemsecim != "3" and ıslemsecim != "4" and ıslemsecim != "5":
            print("lütfen menüden bir sayı seçiniz")
            bakıyeSorgulama()