#! /usr/bin/python


import sys
import os
import commands


baseName = '../out/BOOSTER_BT3_BTP'

file_ref = open(baseName + '_updatedatMay2014.twiss')

list_alt_files = [baseName + '_updatedatMay2014_bsw14l4.twiss',
                  baseName + '_updatedatMay2014_bsw15l1.twiss',
                  baseName + '_updatedatMay2014_bsw14l4_bsw15l1.twiss',
                  baseName + '.twiss']

#                    0     1   2   3   4      5      6     7     8 9 10     11     12  13  14    15    16 17 18
# the column are 'name,angle,k1L,k2L,k3L,beta11,beta22,disp1,disp3,x, y,alfa11,alfa22,mu1,mu2,disp2,disp3,px,py;'

# find the reference
alfa11_ref = float(0)
alfa22_ref = float(0)
beta11_ref = float(0)
beta22_ref = float(0)

for line in file_ref:
    if 'BT3$START' not in line:
        continue

    twiss = line.split()
    #print twiss
    alfa11_ref = float(twiss[11])
    alfa22_ref = float(twiss[12])
    beta11_ref = float(twiss[ 5])
    beta22_ref = float(twiss[ 6])

file_ref.close()

print alfa11_ref
print alfa22_ref
print beta11_ref
print beta22_ref


for filename in list_alt_files:
    file_alt = open(filename)

    for line in file_alt:
        if 'BT3$START' not in line:
            continue

        twiss = line.split()

        alfa11 = float(twiss[11])
        alfa22 = float(twiss[12])
        beta11 = float(twiss[ 5])
        beta22 = float(twiss[ 6])

        print filename
        print ''
        print 'alfa11 variation = %10.10f' % float( (alfa11-alfa11_ref)/alfa11_ref )
        print 'alfa22 variation = %10.10f' % float( (alfa22-alfa22_ref)/alfa22_ref )
        print 'beta11 variation = %10.10f' % float( (beta11-beta11_ref)/beta11_ref )
        print 'beta22 variation = %10.10f' % float( (beta22-beta22_ref)/beta22_ref )


#
#  madx32 < PSB_BT3_BTP.madx                                    >& logs/PSB_BT3_BTP
#  madx32 < PSB_BT3_BTP_updatedatMay2014.madx                   >& logs/PSB_BT3_BTP_updatedatMay2014 
#  madx32 < PSB_BT3_BTP_updatedatMay2014_bsw14l4.madx           >& logs/PSB_BT3_BTP_updatedatMay2014_bsw14l4.madx          
#  madx32 < PSB_BT3_BTP_updatedatMay2014_bsw15l1.madx           >& logs/PSB_BT3_BTP_updatedatMay2014_bsw15l1.madx        
#  madx32 < PSB_BT3_BTP_updatedatMay2014_bsw14l4_bsw15l1.madx   >& logs/PSB_BT3_BTP_updatedatMay2014_bsw14l4_bsw15l1.madx 
