#encoding = utf-8
import requests
from urllib import parse
import tkinter

url = 'http://192.168.20.223:8080/'
decrypt_api = 'hydra-tool-aes/api/v1/decrypt/?'  #解密
encrypt_api = 'hydra-tool-aes/api/v1/encrypt/?' #加密

headers = {'Content-Type':'application/json;charset=UTF-8'}
'''c = str(input("请输入需要加密的文字："))
s = str(input("请输入密钥："))'''

#root=tkinter.Tk()


decrypt_json = {
     'ciphertext':'',
     'secret':'123456'
 }#ciphertext:密文 secret：密钥
encrypt_json = {
    'cleartext':'',
    'secret':'123456'
}#cleartext：明文 secret：密钥
'''encrypt_json['cleartext'] = c
encrypt_json['secret'] = s
'''
def request(json_in,url,api,headers):
    try:
        json_data=parse.urlencode(json_in)
        url_in = url + api + json_data
        r = requests.post(url_in,headers=headers,timeout=30)
        r.raise_for_status()
        end_json = r.json()
        return end_json
    except:
        print('接口请求失败')

'''end_json = request(encrypt_json,url,encrypt_api,headers)


decrypt_json['ciphertext'] = end_json['results']['ciphertext'] #密文
decrypt_json['secret'] = end_json['results']['secret'] #密钥
end_json1 = request(decrypt_json,url,decrypt_api,headers)'''

def show(decrypt_json,encrypt_json,url,decrypt_api,encrypt_api,headers):
    c = str(input("请输入明文："))
    s = str(input("请输入密钥："))

    encrypt_json['cleartext'] = c
    encrypt_json['secret'] = s
    end_json = request(encrypt_json, url, encrypt_api, headers)

    decrypt_json['ciphertext'] = end_json['results']['ciphertext']  # 密文
    decrypt_json['secret'] = end_json['results']['secret']  # 密钥
    end_json1 = request(decrypt_json, url, decrypt_api, headers)
    if end_json1['results']['cleartext'] == c:
        print('加密解密成功,密文为：{0} \n 明文为：{1} \n 密钥为：{2}'.format(decrypt_json['ciphertext'], encrypt_json['cleartext'],
                                                            decrypt_json['secret']))
    else:
        print('加解密操作失败')

#show(decrypt_json,encrypt_json,url,decrypt_api,encrypt_api,headers)


def open(decrypt_json,encrypt_json,url,decrypt_api,headers):
    s = str(input("请输入密钥："))
    m = str(input("请输入密文："))

    decrypt_json['ciphertext']= m
    decrypt_json['secret'] = s
    end_json = request(decrypt_json,url,decrypt_api,headers)

    encrypt_json['cleartext'] = end_json['results']['cleartext']
    encrypt_json['secret'] = end_json['results']['secret']
    print(encrypt_json['cleartext'])

open(decrypt_json,encrypt_json,url,decrypt_api,headers)

'''
label=tkinter.Label(root,text='名文:',anchor='c').grid(row=0)
en_text = tkinter.StringVar()
en1_text = tkinter.StringVar()
En=tkinter.Entry(root,textvariable=en_text).grid(row=0,column=1)

label1=tkinter.Label(root,text='密钥:',anchor='c').grid(row=1)
En1=tkinter.Entry(root,show='*',textvariable=en_text).grid(row=1,column=1)
En.focus_get()
En1.focus_get()
tkinter.Button(root,text='加密',anchor='c',width=6,height=1,command=show).grid(row=2,column=1)

root.mainloop()
'''
