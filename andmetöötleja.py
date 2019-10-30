def vanus(sünnikuupäev, toimumiskuupäev):
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
    
def vahemikku_sobiv(toimumiskuupäev, algus, lõpp):
    
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

        
    
    
algus = (input('Sisesta alguskuupäev(pp.kk.aaaa): ')).split('.')
lõpp = (input('Sisesta lõppkuupäev(pp.kk.aaaa): ')).split('.')

fail = 'reportmovement_rehekivio_2019_09_2019_10.csv'

lõpp_pealkirjad = ['Loomade arv kuu algul',\
                   ['sissetulek kokku', ['sünd', 'ostetud','teisest rühmast', 'muu']], \
                   ['väljaminek',['hukkumine', 'müük', 'teise rühma', 'lihaks']], \
                   'Loomade arv kuu lõpul']

põhikarja_uted = [[0,[0,[0,0,0,0]],[0,[0,0,0,0,]],0],['Utt', 2]]
põhikarja_jäärad  = [[0,[0,[0,0,0,0]],[0,[0,0,0,0,]],0], ['Jäär', 2]] 
utikud = [[0,[0,[0,0,0,0]],[0,[0,0,0,0,]],0], ['Utt', 1]]
jäärikud = [[0,[0,[0,0,0,0]],[0,[0,0,0,0,]],0], ['Jäär', 1]] 
utt_talled = [[0,[0,[0,0,0,0]],[0,[0,0,0,0,]],0], ['Utt', 0]]
jäär_talled = [[0,[0,[0,0,0,0]],[0,[0,0,0,0,]],0], ['Jäär', 0]]

lopp_andmed = [põhikarja_uted, põhikarja_jäärad, utikud, jäärikud, utt_talled, jäär_talled]

f = open(fail, encoding = 'utf-8')
pealkirjad = f.readline().strip().split(',')
print(pealkirjad)

for i, loomaandmed in enumerate(f):
    üksikandmed = loomaandmed.strip().split('.')
    if vahemikku_sobiv(üksikandmed[0], algus, lõpp):
        sugu = üksikandmed[0].lowercase()
        vanus = vanus(üksikandmed[2], üksikandmed[0])
        if 'müük' in üksikandmed[10].lowercase():
        elif 'müük' in üksikandmed[10].lowercase():
        
        if sugu == 'jäär':
            
        else:
        
        
        
    
f.close()