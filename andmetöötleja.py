def vanus(sünnikuupäev, toimumiskuupäev): # mis vanuses loom on
    toimumiskuupäev = toimumiskuupäev.split('.')
    aasta = int(toimumiskuupäev[2])
    sünnikuupäev = sünnikuupäev.split('.')
    sünni_kuu = int(sünnikuupäev[1])
    sünni_aasta = int(sünnikuupäev[2])
    aastates_vanus = sünni_aasta - aasta
    if aastates_vanus < 1:
        return 0
    elif aastates_vanus < 2:
        return 1
    else:
        return 2
    
def vahemikku_sobiv(toimumiskuupäev, algus, lõpp):#kas liikumis kuupäev sobib etteantud vahemikku
    
    toimumiskuupäev = toimumiskuupäev.split('.')
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
"""
lõpp_pealkirjad = ['Loomade arv kuu algul',\
                   ['sissetulek kokku', ['sünd', 'ostetud','teisest rühmast', 'muu']], \
                   ['väljaminek',['hukkumine', 'müük', 'teise rühma', 'lihaks']], \
                   'Loomade arv kuu lõpul']
"""
###???   
def andmete_lisaja(liikumis_põhjus, sugu, vanus, liikumis_põhjus, loomagruppide_sõnastik, ):# lisab +1 õigesse loomarühma ja liikumispõhjusesse
    if 'sünd' in liikumis_põhjus:
        liikumis_põhjus = 'sünd'
    elif 'ost' in liikumis_põhjus:
        liikumis_põhjus = 'ostetud'
    elif 'st rühm' in liikumis_põhjus:
        liikumis_põhjus = 'teisest rühmast'
    elif 'hukku' in liikumis_põhjus:
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
    kokku[a][1][b] += 1
    
    loomagruppide_sõnastik[sugu][vanus][a][0] += 1
    kokku[a][0] += 1
    if a == 1:#loomi tuli juurde muudame loomade arvu perioodi lõpus
        loomagruppide_sõnastik[sugu][vanus][3] += 1
        kokku[3] += 1
    if a == 1:#loomi läks ära muudame loomade arvu perioodi lõpus
        loomagruppide_sõnastik[sugu][vanus][3] -= 1
        kokku[3] -= 1
        
        
algus = (input('Sisesta alguskuupäev(pp.kk.aaaa): ')).split('.')
lõpp = (input('Sisesta lõppkuupäev(pp.kk.aaaa): ')).split('.')
###ajutine algus ja lõpp, hiljem info GUI-st
fail = 'algfaili näidis.csv'
###ajutine fail, hiljem info GUI-st

lõpp_pealkirjad = ['Loomade arv kuu algul',\
                   ['sissetulek kokku', ['sünd', 'ostetud','teisest rühmast', 'muu']], \
                   ['väljaminek',['hukkumine', 'müük', 'teise rühma', 'lihaks']], \
                   'Loomade arv kuu lõpul']

"""
lihtsustab loomagruppide järjendite lugemist

põhikarja_uted = [[138,\#['Loomade arv kuu algul',\
                   [0,[0,0,0,0]],\#['sissetulek kokku', ['sünd', 'ostetud','teisest rühmast', 'muu']], \
                   [0,[0,19,0,0,]],\#['väljaminek',['hukkumine', 'müük', 'teise rühma', 'lihaks']], \
                    0],\#'Loomade arv kuu lõpul']
                   ['Utt', 2]]#sugu ja vanus(2=vana(põhikari),1=noor,0=tall)
"""
#loomagruppide järjendid
põhikarja_uted = [0,[0,[0,0,0,0]],[0,[0,0,0,0,]],0]
põhikarja_jäärad  = [0,[0,[0,0,0,0]],[0,[0,0,0,0,]],0]
utikud = [0,[0,[0,0,0,0]],[0,[0,0,0,0,]],0]
jäärikud = [0,[0,[0,0,0,0]],[0,[0,0,0,0,]],0]
utt_talled = [0,[0,[0,0,0,0]],[0,[0,0,0,0,]],0]
jäär_talled = [0,[0,[0,0,0,0]],[0,[0,0,0,0,]],0]
#loomagruppide järjendid kokkuvõte
kokku = [0,[0,[0,0,0,0]],[0,[0,0,0,0,]],0]

loomagruppide_sõnastik = {'jäär':{2:põhikarja_jäärad, 1:jäärikud, 0:jäär_talled},
                          'utt':{2:põhikarja_uted, 1:utikud, 0:utt_talled}}
#loomagruppide_sõnastik lihtsustab leida looma vastavalt soole('jäär', 'utt') ja vanusele(2=vana(põhikari),1=noor,0=tall

pealkirjade_sõnastik = {'sünd':[1,1,0], 'ostetud':[1,1,1],'teisest rühmast':[1,1,2], 'muu':[1,1,3]
                        'hukkumine':[2,1,0], 'müük':[2,1,1], 'teise rühma':[2,1,2], 'lihaks':[2,1,3]}
#pealkirjade_sõnastik lihtsustab leida loomagruppide järjendist liikumis põhjuse asukohta

lopp_andmed = [lõpp_pealkirjad,\
               põhikarja_uted, põhikarja_jäärad,\
               utikud, jäärikud,\
               utt_talled, jäär_talled,\
               kokku]#lõplikud andmed mis lähevad faili salvestamiseks

f = open(fail, encoding = 'utf-8')
pealkirjad = f.readline().strip().split(',')
print(pealkirjad)

for i, loomaandmed in enumerate(f):#otsib välja looma liikumise põhjuse
    üksikandmed = loomaandmed.strip().split('.')#järjend algfailist
    
    if vahemikku_sobiv(üksikandmed[0], algus, lõpp):#kui sobib vahemikku hakkab otsima liikumise põhjust
        
        liikumis_põhjus = üksikandmed[10].lowercase()# mis põhjusel loom liigub müük, ostedud, hukkund jne
        sugu = üksikandmed[0].lowercase()# jäär(M) või utt(N)
        vanus = vanus(üksikandmed[2], üksikandmed[0])# kas tall(0)/noorloom(1)/põhikarjaloom(2)
        
        andmete_lisaja(vajab uuendamist):#muudab vastava loomagrupi andmeid(lisab õiges kohas +1)
        
f.close()
print(lõpp_pealkirjad)
print(põhikarja_uted)
print(põhikarja_jäärad)
print(utikud)
print(jäärikud)
print(utt_talled)
print(jäär_talled)
print(kokku)