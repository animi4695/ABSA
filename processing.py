from collections import OrderedDict
def curate(asin):
    fi=open('FeatureList/'+asin+'_feature_list','r')
    features=fi.readlines()
    feat=[]
    for i in features:
        i=i.strip()
        i=i.strip("(' ')")
        i=' '.join([i])
        i=i.replace('\'','')
        i=i.replace(',','')
        feat.append(i)
    return feat
def grouping(asin):
    features=curate(asin)
    extra=['RAM','sensor','Dual SIM','Water resistant','screen protection','price','money','internal memory','external memory','processor','screen size','flash','slim']
    lis=['mobile','camera','front camera','display','battery','performance','sound','speaker','quality','charging','heating','hanging']
    pre={'mobile':['phone','product','handset','device','mobile'],'camera':['camera'],'front camera':['front camera'],'display':['display'],'battery':['battery','backup'],'performance':['performance'],'sound':['sound'],'speaker':['speaker'],'quality':['quality'],'charging':['charging'],'heating':['heat'],'hanging':['hang']}
    final={};misc={}
    lis.extend(extra)
    for key in lis:
        synonyms=[]
        for i in features:
            if(pre.has_key(key)):
                value=[(i) for term in pre[key] if term.lower() in i.lower()]
            else:
                if term.lower() in i.lower():value=[i]
            if len(value):features.remove(value[0])
            synonyms.extend(value)
        if(pre.has_key(key)):
            final[key]=synonyms
        else:
            misc[key]=synonyms
    final=remove_empty(final)
    misc=remove_empty(misc)
    return final,misc
def remove_empty(final):
    final={key:final[key] for key in final if len(final[key])!=0}
    return final
def number(asin):
    reviews=open('no_of_reviews.txt','r')
    reviews.readlines()
