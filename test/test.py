import re
import requests

# te = '<a data-param="?_f=index_businessnews_0_0" href="/a/723735181_120381931?scm=1103.plate:542:0.0.1_1.0" target=_blank title="下调26%！房地产“中间商”，终于降价了"> '
pattern = re.compile(r'<a.+?href="(.*?)".+?title="(.*?)".*?>')

# print(te)
# all_matches  = pattern.findall(te)
# print(all_matches)
# for href, data, title in all_matches:
#     print(f'href = " {href} "')
#     print(f'data {data}')
#     print(f'title = " {title}"')
#     print('--------')
# exit()
resp = requests.get('https://www.sohu.com/')
if resp.status_code == 200:
    print(resp.text)
    
    all_matches = pattern.findall(resp.text)
    # print(resp.text)
    # print(all_matches)
    for href, title in all_matches:
        print(f'href = " {href} "')
        #print(f'target = " {tar} "')
        print(f'title = " {title}"')
        print('--------')

'''
        <a href="/a/723840012_100140727?scm=1103.plate:219:0.0.1_3_1029123902632169472.0" 
        target=_blank 
        title="中秋节传统民俗：“男不拜月”你知道吗？"> 
        '''