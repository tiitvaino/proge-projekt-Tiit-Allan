#tabelipealkirjad
lõpp_pealkirjad = ['Loomade arv kuu algul',\
                   ['sissetulek kokku', ['sünd', 'ostetud','teisest rühmast', 'muu']], \
                   ['väljaminek',['hukkumine', 'müük', 'teise rühma', 'lihaks']], \
                   'Loomade arv kuu lõpul']
#loomade arvu kuu algul küsib kasutajaliides
#loomade arvu kuu lõpus arvutab välja programm ja lisab järjendisse


#järgnev järjend on pärast kasutaja käest algandmete saamist ja andmetöötlejast läbikäimist
põhikarja_uted = [[138,\#['Loomade arv kuu algul',\
                   [0,[0,0,0,0]],\#['sissetulek kokku', ['sünd', 'ostetud','teisest rühmast', 'muu']], \
                   [0,[0,19,0,0,]],\#['väljaminek',['hukkumine', 'müük', 'teise rühma', 'lihaks']], \
                    0],\#'Loomade arv kuu lõpul']
                   ['Utt', 2]]#sugu ja vanus(2=vana(pähikari),1=noor,0=tall)
põhikarja_jäärad  = [[6,[0,[0,0,0,0]],[0,[0,0,0,0,]],0], ['Jäär', 2]] 
utikud = [[80,[0,[0,0,0,0]],[0,[0,1,0,0,]],0], ['Utt', 1]]
jäärikud = [[1,[0,[0,0,0,0]],[0,[0,0,0,0,]],0], ['Jäär', 1]] 
utt_talled = [[83,[0,[0,0,0,0]],[0,[0,0,0,0,]],0], ['Utt', 0]]
jäär_talled = [[10,[0,[0,0,0,0]],[0,[0,0,0,0,]],0], ['Jäär', 0]]
kokku = [[318,[0,[0,0,0,0]],[0,[20,0,0,0,]],298]]

lopp_andmed = [lõpp_pealkirjad, põhikarja_uted, põhikarja_jäärad, utikud, jäärikud, utt_talled, jäär_talled, kokku]