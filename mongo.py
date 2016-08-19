import json
import requests
headers = {
    'Content-Type': 'application/json',
}
number=open('no_of_reviews.txt','w')
for i in range(130):
    payload = '{"sno":'+str(i)+'}'
    r=requests.post('http://justin10.com/srinu/review', headers=headers, data=payload)
    data=r.content
    if(data):idle
        data=(json.loads(data))
        model=data['phone']
        all_results=data['review']
        number.write(model)
        number.write(' ')
        number.write(str(len(all_results)))
        number.write('\n')
        total=''
        for j in all_results:
            total+=j['review']
        f=open('Cell_Phones/'+model+'.txt','w')
        f.write(total.encode('ascii','ignore'))
        f.close()
    else:
        print r
number.close()