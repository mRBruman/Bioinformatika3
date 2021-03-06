from ete3 import Tree
from numpy import *
from lxml import *
from six import *

t = Tree('(((JX993988.1BatcoronavirusCp/Yunnan2011:0.012981016,'
         '(KF569996.1RhinolophusaffiniscoronavirusisolateLYRa11:0.041438321,'
         '((MT308984.1MutantSARScoronavirusUrbanicloneSARS-Urbani-MA_SHC014-spike:0.0,'
         'MK062183.1SARScoronavirusUrbaniisolateicSARS-C7:0.0):0.009581511,'
         'KP886808.1BatSARS-likecoronavirusYNLF_31C:0.024414014)0.391:0.002599861)0.928:0.005210785)0.992:0'
         '.010970686,((((GU190215.1BatcoronavirusBM48-31/BGR/2008:0.155729881,'
         'KY352407.1Severeacuterespiratorysyndrome-relatedcoronavirusstrainBtKY72:0.168578059)1.000:0.114432751,'
         '(MN514967.1DromedarycamelcoronavirusHKU23isolateDcCoV-HKU23/camel/Nigeria/NV1385/2016:2.268074743,'
         '(LC556375.1Severeacuterespiratorysyndrome-relatedcoronavirusRc-o319RNA:0.170796385,'
         '(MT040335.1PangolincoronavirusisolatePCoV_GX-P5L:0.089440177,'
         '(MT121216.1PangolincoronavirusisolateMP789:0.042569301,'
         '((MG772933.1BatSARS-likecoronavirusisolatebat-SL-CoVZC45:0.010367620,'
         'MG772934.1BatSARS-likecoronavirusisolatebat-SL-CoVZXC21:0.019180917)1.000:0.030928486,'
         '(NC_045512.2Severeacuterespiratorysyndromecoronavirus2isolateWuhan-Hu-1:0.014404740,'
         'MN996532.2BatcoronavirusRaTG13:0.023624656)0.998:0.017953519)0.992:0.019431069)1.000:0.078443246)1.000:0'
         '.074156307)0.992:0.094869217)0.365:0.008770971)1.000:0.105399737,'
         '(MK211374.1CoronavirusBtRl-BetaCoV/SC2018:0.061445532,((JX993987.1BatcoronavirusRp/Shaanxi2011:0.019698091,'
         '((DQ648856.1Batcoronavirus:0.001691650,DQ412042.1BatSARScoronavirusRf1:0.001949702)0.998:0.009854919,'
         '(KJ473813.1BtRf-BetaCoV/SX2013:0.007810181,'
         'KJ473811.1BtRf-BetaCoV/JL2012:0.026685009)0.936:0.004202253)1.000:0.028687848)0.690:0.003424203,'
         '((GQ153542.1BatSARScoronavirusHKU3-7:0.006085939,(GQ153547.1BatSARScoronavirusHKU3-12:0.000604590,'
         'MT782115.1MutantBatSARScoronavirusHKU3isolateicHKU3-SRBD-MA:0.000605056)0.994:0.006737155)1.000:0'
         '.040515748,(KJ473814.1BtRs-BetaCoV/HuB2013:0.016996041,'
         'DQ412043.1BatSARScoronavirusRm1:0.061498380)0.911:0.005413101)0.435:0.004365926)0.960:0.012299737)0.873:0'
         '.011780769)0.994:0.021027934,(DQ071615.1BatSARScoronavirusRp3:0.024253430,'
         'KJ473815.1BtRs-BetaCoV/GX2013:0.021549703)0.728:0.005045734)0.586:0.005109327)0.968:0.004886010,'
         '(FJ588686.1BatSARSCoVRs672/2006:0.012234242,((KJ473816.1BtRs-BetaCoV/YN2013:0.007181907,'
         'KC881005.1BatSARS-likecoronavirusRsSHC014:0.005475585)0.580:0.002998310,'
         '(MK211376.1CoronavirusBtRs-BetaCoV/YN2018B:0.000597184,'
         '(MK211378.1CoronavirusBtRs-BetaCoV/YN2018D:0.000597185,'
         'MK211377.1CoronavirusBtRs-BetaCoV/YN2018C:0.003585697)0.000:0.000000006)0.990:0.005464407)0.904:0.002429279'
         ')0.136:0.000739358,(MK211375.1CoronavirusBtRs-BetaCoV/YN2018A:0.006428507,'
         '((((KY417149.1BatSARS-likecoronavirusisolateRs4255:0.006641767,'
         '(KY417152.1BatSARS-likecoronavirusisolateRs9401:0.001761633,'
         '(KY417147.1BatSARS-likecoronavirusisolateRs4237:0.002394973,'
         'KF367457.1BatSARS-likecoronavirusWIV1:0.002990391)0.785:0.001232660)0.770:0.002996039)0.865:0.002357717,'
         '(KY417145.1BatSARS-likecoronavirusisolateRf4092:0.009000940,'
         '(KY417151.1BatSARS-likecoronavirusisolateRs7327:0.004036572,'
         '(KY417146.1BatSARS-likecoronavirusisolateRs4231:0.001354129,'
         'KY417142.1BatSARS-likecoronavirusisolateAs6526:0.002840909)0.614:0.002395218)0.443:0.000754925)0.890:0'
         '.000000006)0.401:0.001793846,(KY417150.1BatSARS-likecoronavirusisolateRs4874:0.002987944,'
         '(KY417143.1BatSARS-likecoronavirusisolateRs4081:0.000000006,'
         'BatSARS-likecoronavirusisolateRs4247:0.000596758)0.728:0.000000006)0.870:0.001794590)0.945:0.002594770,'
         'KY417144.1BatSARS-likecoronavirusisolateRs4084:0.006418727)0.394:0.000593441)0.757:0.000633613);')
print("Unrooted tree")
print(t)

t.set_outgroup(t & "MN514967.1DromedarycamelcoronavirusHKU23isolateDcCoV-HKU23/camel/Nigeria/NV1385/2016")
print(t)

f = open("rootedTree.txt", "w")
f.write(t.write())
f.close()
