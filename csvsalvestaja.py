# suudab tegutsed järjendiga,kus sees on järjendid ja nendes järjendites veel järjendid [x,..,[y,..,[z,..],..],...]
def salvestaja(lõppandmed, lõpp_fail):
    saved_text = ''
    for grupp in lõppandmed:
        for osa in grupp:
            if isinstance(osa, list):
                for alamosa in osa:
                    if isinstance(alamosa, list):
                        for j in alamosa:
                            saved_text += str(j)+ ','
                    else:
                        saved_text += str(alamosa) + ','
            else:
                saved_text += str(osa) + ','
        saved_text += '\n' 
    print(saved_text)
    f = open(lõpp_fail, 'w')
    f.write(saved_text)
    f.close()
    
#tabelipealkirjad
lõpp_pealkirjad = ['Loomade arv kuu algul',\
                   ['sissetulek kokku', ['sünd', 'ostetud','teisest rühmast', 'muu']], \
                   ['väljaminek',['hukkumine', 'müük', 'teise rühma', 'lihaks']], \
                   'Loomade arv kuu lõpul']
#loomade arvu kuu algul küsib kasutajaliides
#loomade arvu kuu lõpus arvutab välja programm ja lisab järjendisse


#järgnev järjend on pärast kasutaja käest algandmete saamist ja andmetöötlejast läbikäimist
põhikarja_uted = [138,
                   [0,[0,0,0,0]],
                   [0,[0,19,0,0]],
                    0]
põhikarja_jäärad  = [6,[0,[0,0,0,0]],[0,[0,0,0,0]],0]
utikud = [80,[0,[0,0,0,0]],[0,[0,1,0,0]],0]
jäärikud = [1,[0,[0,0,0,0]],[0,[0,0,0,0]],0]
utt_talled = [83,[0,[0,0,0,0]],[0,[0,0,0,0]],0]
jäär_talled = [10,[0,[0,0,0,0]],[0,[0,0,0,0]],0]
kokku = [318,[0,[0,0,0,0]],[0,[20,0,0,0]],298]

lõppandmed = [lõpp_pealkirjad, põhikarja_uted, põhikarja_jäärad, utikud, jäärikud, utt_talled, jäär_talled, kokku]
    
    
salvestaja(lõppandmed, 'prrrroov.csv')