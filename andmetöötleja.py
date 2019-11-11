from datetime import date
# mis vanuses loom on
###vajab tuunida kui aasta vahetub, siis kõik loomad lähevad vanemasse gruppi ehkki ei peaks
def vanuse_arvutaja(sünnikuupäev, toimumiskuupäev):
    """
from datetime import date

d0 = date(2008, 8, 18)
d1 = date(2008, 9, 26)
delta = d1 - d0
print(delta.days
talled muutuvad noorteks kevadel kui uued talled peale tulevad  ehk märsikuus ca 9-12 kuud
noored muutuvad vanadeks sügisel paaritusse minnes ca +-1,5 aastaselt

"""
    toimumiskuupäev = toimumiskuupäev.split('.')
    t_aasta = int(toimumiskuupäev[2])
    t_kuu = int(toimumiskuupäev[1])
    t_päev = int(toimumiskuupäev[0])
    
    sünnikuupäev = sünnikuupäev.split('.')
    sünni_päev = int(sünnikuupäev[0])
    sünni_kuu = int(sünnikuupäev[1])
    sünni_aasta = int(sünnikuupäev[2])
    
    toimumiskuupäev = date(t_aasta, t_kuu, t_päev)
    sünnikuupäev = date(sünni_aasta, sünni_kuu, sünni_päev)
    päevades_vanus = toimumiskuupäev - sünnikuupäev
    
    aasta = t_aasta
    
    sünniaeg =(aasta,3,1)
    paarituskuupäev =(aasta,9,1)
    
    if päevades_vanus <= 365*(10/12):
        return 0
    elif päevades_vanus <= 365*(1+7/12):
        return 1
    else:
        return 2

#kas liikumis kuupäev sobib etteantud vahemikku
def vahemikku_sobiv(toimumiskuupäev, algus, lõpp):
    algus = algus.split('.')
    lõpp = lõpp.split('.')
    toimumiskuupäev = toimumiskuupäev.strip().split('.')
    aasta = int(toimumiskuupäev[2])
    kuu = int(toimumiskuupäev[1])
    päev = int(toimumiskuupäev[0])
    algus_aasta = int(algus[2])
    lõpp_aasta = int(lõpp[2])
    algus_kuu = int(algus[1])
    lõpp_kuu = int(lõpp[1])
    algus_päev = int(algus[0])
    lõpp_päev = int(lõpp[0])
    if aasta > algus_aasta and aasta < lõpp_aasta:# lõpp ja algus aasta
        return True
    
    elif aasta == algus_aasta:#sama algus aasta
        if kuu > algus_kuu:#kuu
            return True
        elif kuu == algus_kuu:#kuu
            if päev >= algus_päev:#päeva võrdlus
                return True
            
    elif aasta == lõpp_aasta:#sama lõpp aasta
        if kuu < lõpp_kuu:#kuu
            return True
        elif kuu == lõpp_kuu:#kuu
            if päev <= lõpp_päev:#päeva võrdlus
                return True
    else:
        return False

# lisab +1 õigesse loomarühma ja liikumispõhjusesse
def andmete_lisaja(liikumis_põhjus, sugu, vanus, loomagruppide_sõnastik, pealkirjade_sõnastik):
    if 'sünd' in liikumis_põhjus:
        liikumis_põhjus = 'sünd'
    elif 'ost' in liikumis_põhjus:
        liikumis_põhjus = 'ostetud'
    elif 'st rühm' in liikumis_põhjus:
        liikumis_põhjus = 'teisest rühmast'
    elif 'hukku' in liikumis_põhjus:
        liikumis_põhjus = 'hukkumine'
    elif 'kadunud' in liikumis_põhjus:
        liikumis_põhjus = 'hukkumine'
    elif 'müük' in liikumis_põhjus:
        liikumis_põhjus = 'müük'
    elif 'se rühma' in liikumis_põhjus:
        liikumis_põhjus = 'teise'
    elif 'liha' in liikumis_põhjus:
        liikumis_põhjus = 'lihaks'
    
    a = pealkirjade_sõnastik[liikumis_põhjus][0]#kas on sissetulek või välja minek
    b = pealkirjade_sõnastik[liikumis_põhjus][2]#liikumis_põhjuse asukoht sissetuleku ja väljamineku järjendis
    
    loomagruppide_sõnastik[sugu][vanus][a][1][b] += 1# nr 1 asukoht tuleneb looma gruooide järjendite ehitusest [siss/väljaminek,[liikumispõhjus]]
    loomagruppide_sõnastik['kokku'][a][1][b] += 1
    
    loomagruppide_sõnastik[sugu][vanus][a][0] += 1
    loomagruppide_sõnastik['kokku'][a][0] += 1
    if a == 1:#loomi tuli juurde muudame loomade arvu perioodi lõpus
        loomagruppide_sõnastik[sugu][vanus][3] += 1
        loomagruppide_sõnastik['kokku'][3] += 1
    if a == 2:#loomi läks ära muudame loomade arvu perioodi lõpus
        loomagruppide_sõnastik[sugu][vanus][3] -= 1
        loomagruppide_sõnastik['kokku'][3] -= 1
        
def andmetöötleja(algus, lõpp, fail, loomade_algne_hulk):
    """
    loomade_algne_hulk = {'põhikarja uted': arv, 'põhikarja jäärad': arv, 'utikud': arv, 'jäärikud': arv, 'utt_talled': arv, 'jäär_talled': arv }
    algus = (input('Sisesta alguskuupäev(pp.kk.aaaa): '))
    lõpp = (input('Sisesta lõppkuupäev(pp.kk.aaaa): '))
    ###ajutine algus ja lõpp, hiljem info GUI-st
    fail = 'algfaili näidis.csv'
    ###ajutine fail, hiljem info GUI-st
    """

    lõpp_pealkirjad = ['Loomade arv kuu algul',\
                       ['sissetulek kokku', ['sünd', 'ostetud','teisest rühmast', 'muu']], \
                       ['väljaminek',['hukkumine', 'müük', 'teise rühma', 'lihaks']], \
                       'Loomade arv kuu lõpul']

    """
    lihtsustab loomagruppide järjendite lugemist

    põhikarja_uted = [138,\#['Loomade arv kuu algul',\
                       [0,[0,0,0,0]],\#['sissetulek kokku', ['sünd', 'ostetud','teisest rühmast', 'muu']], \
                       [0,[0,19,0,0,]],\#['väljaminek',['hukkumine', 'müük', 'teise rühma', 'lihaks']], \
                        0],\#'Loomade arv kuu lõpul']
    """
    #loomagruppide järjendid
    põhikarja_uted = [loomade_algne_hulk['põhikarja uted'],[0,[0,0,0,0]],[0,[0,0,0,0,]],loomade_algne_hulk['põhikarja uted']]
    põhikarja_jäärad  = [loomade_algne_hulk['põhikarja jäärad'],[0,[0,0,0,0]],[0,[0,0,0,0,]],loomade_algne_hulk['põhikarja jäärad']]
    utikud = [loomade_algne_hulk['utikud'],[0,[0,0,0,0]],[0,[0,0,0,0,]],loomade_algne_hulk['utikud']]
    jäärikud = [loomade_algne_hulk['jäärikud'],[0,[0,0,0,0]],[0,[0,0,0,0,]],loomade_algne_hulk['jäärikud']]
    utt_talled = [loomade_algne_hulk['utt_talled'],[0,[0,0,0,0]],[0,[0,0,0,0,]],loomade_algne_hulk['utt_talled']]
    jäär_talled = [loomade_algne_hulk['jäär_talled'],[0,[0,0,0,0]],[0,[0,0,0,0,]],loomade_algne_hulk['jäär_talled']]
    #loomagruppide järjendid kokkuvõte
    
    loomade_algne_hulk_kokku = 0
    for grupp in loomade_algne_hulk:
        loomade_algne_hulk_kokku += loomade_algne_hulk[grupp]
    kokku = [loomade_algne_hulk_kokku,[0,[0,0,0,0]],[0,[0,0,0,0,]],loomade_algne_hulk_kokku]

    #loomagruppide_sõnastik lihtsustab leida looma vastavalt soole('jäär', 'utt') ja vanusele(2=vana(põhikari),1=noor,0=tall
    loomagruppide_sõnastik = {'jäär':{2:põhikarja_jäärad, 1:jäärikud, 0:jäär_talled},
                              'utt':{2:põhikarja_uted, 1:utikud, 0:utt_talled},
                              'kokku': kokku}

    #pealkirjade_sõnastik lihtsustab leida loomagruppide järjendist liikumis põhjuse asukohta
    pealkirjade_sõnastik = {'sünd':[1,1,0], 'ostetud':[1,1,1],'teisest rühmast':[1,1,2], 'muu':[1,1,3],
                            'hukkumine':[2,1,0], 'müük':[2,1,1], 'teise rühma':[2,1,2], 'lihaks':[2,1,3]}

    #lõplikud andmed mis lähevad faili salvestamiseks
    lõpp_andmed = [lõpp_pealkirjad,\
                   põhikarja_uted, põhikarja_jäärad,\
                   utikud, jäärikud,\
                   utt_talled, jäär_talled,\
                   kokku]

    f = open(fail, encoding = 'utf-8')
    pealkirjad = f.readline().strip().split(',')

    for loomaandmed in f:#otsib välja looma liikumise põhjuse
        üksikandmed = loomaandmed.strip().split(',')#järjend algfailist
        toimumiskuupäev = üksikandmed[0]
        if vahemikku_sobiv(toimumiskuupäev, algus, lõpp):#kui sobib vahemikku hakkab otsima liikumise põhjust
            
            liikumis_põhjus = üksikandmed[10].lower()# mis põhjusel loom liigub müük, ostedud, hukkund jne
            sugu = üksikandmed[2].lower()# jäär(M) või utt(N)
            vanus = vanuse_arvutaja(üksikandmed[3], üksikandmed[0])# kas tall(0)/noorloom(1)/põhikarjaloom(2)
            
            andmete_lisaja(liikumis_põhjus, sugu, vanus, loomagruppide_sõnastik, pealkirjade_sõnastik)#muudab vastava loomagrupi ja kokkuvõtte andmeid(lisab õiges kohas +1)
            
    f.close()
    return lõpp_andmed

#loomade_algne_hulk = {'põhikarja uted': 314, 'põhikarja jäärad': 10, 'utikud': 100, 'jäärikud': 20, 'utt_talled': 215, 'jäär_talled': 210 }
#algus = '01.09.2019'#(input('Sisesta alguskuupäev(pp.kk.aaaa): '))
#lõpp = '04.10.2019'#(input('Sisesta lõppkuupäev(pp.kk.aaaa): '))
###ajutine algus ja lõpp, hiljem info GUI-st
#fail = 'algfaili näidis.csv'
###ajutine fail, hiljem info GUI-st

#print (andmetöötleja(algus, lõpp, fail, loomade_algne_hulk))

"""
print(lõpp_pealkirjad)
print(põhikarja_uted)
print(põhikarja_jäärad)
print(utikud)
print(jäärikud)
print(utt_talled)
print(jäär_talled)
print(kokku)
"""