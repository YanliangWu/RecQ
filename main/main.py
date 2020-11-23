import sys
sys.path.append("..")
from RecQ import RecQ
from tool.config import Config
#from visual.display import Display



if __name__ == '__main__':

    print '='*80
    print '   RecQ: An effective python-based recommender algorithm library.   '
    print '='*80
    print '0. Analyze the input data.(Configure the visual.conf in config/visual first.)'
    print '-' * 80
    print 'Generic Recommenders:'
    print '1. UserKNN        2. ItemKNN        3. BasicMF        4. SlopeOne        5. SVD'
    print '6. PMF            7. SVD++          8. EE             9. BPR             10. WRMF'
    print '11. ExpoMF'
    print '-' * 80

    print '***(CSIT5210 Project) Optimized Generic Recommenders:***'
    print '12. BPR-Optimizer'
    print '-' * 80

    print 'Social Recommenders:'
    print 's1. RSTE          s2. SoRec         s3. SoReg         s4. SocialMF       s5. SBPR'
    print 's6. SREE          s7. LOCABAL       s8. SocialFD      s9. TBPR           s10. SERec'
    print '-' * 80

    print 'Network Embedding based Recommenders:'
    print 'a1. CoFactor      a2. CUNE-MF       a3. CUNE-BPR      a4. IF-BPR'
    print '-' * 80

    print '***(CSIT5210 Project) Optimized Network Embedding based Recommenders:***'
    print 'a5. IF-BPR-Optimizer'
    print '-' * 80

    print 'Deep Recommenders:'
    print 'd1. APR           d2. CDAE          d3. DMF           d4. NeuMF           d5. CFGAN'
    print 'd6. IRGAN         d7. RSGAN         d8. NGCF          d9. LightGCN        d10. ESRF'
    print 'd11. DHCF         d12. DiffNet'
    print '-' * 80

    print '***(CSIT5210 Project) Optimized Deep Recommenders:***'
    print 'd13. RSGAN Softmax 0.1              d14. RSGAN Minibatch'
    print '-' * 80

    print 'Baselines:'
    print 'b1. UserMean      b2. ItemMean      b3. MostPopular   b4. Rand'


    print '='*80
    algor = -1
    conf = -1
    order = raw_input('please enter the num of the algorithm to run it:')
    import time
    s = time.time()
    # if order == '0':
    #     try:
    #         import seaborn as sns
    #     except ImportError:
    #         print '!!!To obtain nice data charts, ' \
    #               'we strongly recommend you to install the third-party package <seaborn>!!!'
    #     conf = Config('../config/visual/visual.conf')
    #     Display(conf).render()
    #     exit(0)

    algorthms = {'1':'UserKNN','2':'ItemKNN','3':'BasicMF','4':'SlopeOne','5':'SVD','6':'PMF',
                 '7':'SVD++','8':'EE','9':'BPR','10':'WRMF','11':'ExpoMF', '12':'BPR_Optimizer',
                 's1':'RSTE','s2':'SoRec','s3':'SoReg','s4':'SocialMF','s5':'SBPR','s6':'SREE',
                 's7':'LOCABAL','s8':'SocialFD','s9':'TBPR','s10':'SEREC','a1':'CoFactor',
                 'a2':'CUNE_MF','a3':'CUNE_BPR','a4':'IF_BPR', 'a5':'IF_BPR_Optimizer',
                 'd1':'APR','d2':'CDAE','d3':'DMF','d4':'NeuMF','d5':'CFGAN','d6':'IRGAN','d7':'RSGAN','d8':'NGCF',
                 'd9':'LightGCN', 'd10':'ESRF', 'd11':'DHCF', 'd12':'DiffNet', 'd13': 'RSGAN_Softmax0.1', 'd14': 'RSGAN_Minibatch',
                 'b1':'UserMean','b2':'ItemMean','b3':'MostPopular','b4':'Rand'}

    try:
        conf = Config('../config/'+algorthms[order]+'.conf')
    except KeyError:
        print 'Error num!'
        exit(-1)
    recSys = RecQ(conf)
    recSys.execute()
    e = time.time()
    print "Run time: %f s" % (e - s)
