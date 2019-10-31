"""põhikarja_uted = [[138,\
                   [0,[0,0,0,0]],\
                   [0,[0,19,0,0,]],\
                    0]]
põhikarja_jäärad  = [[6,[0,[0,0,0,0]],[0,[0,0,0,0,]],0],] 
utikud = [[80,[0,[0,0,0,0]],[0,[0,1,0,0,]],0],]
jäärikud = [[1,[0,[0,0,0,0]],[0,[0,0,0,0,]],0],] 
utt_talled = [[83,[0,[0,0,0,0]],[0,[0,0,0,0,]],0],]
jäär_talled = [[10,[0,[0,0,0,0]],[0,[0,0,0,0,]],0],]
sõnastik = {'jäär':{2:põhikarja_jäärad, 1:jäärikud, 0:jäär_talled},
            'utt':{2:põhikarja_uted, 1:utikud, 0:utt_talled}}
            """
pealkirjade_sõnastik = {'sünd':[1,1,0], 'ostetud':[1,1,1],'teisest rühmast':[1,1,2], 'muu':[1,1,3],
                        'hukkumine':[2,1,0], 'müük':[2,1,1], 'teise rühma':[2,1,2], 'lihaks':[2,1,3]}

#print(sõnastik['jäär'][2])