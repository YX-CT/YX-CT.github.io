import time, sys, os

version_code = str(input('Please input version_code(e.g. 10):'))
version_name = str(input('Please input version_name(e.g. 4.2):'))
update_log = str(input('Please input update_log:'))
nowtime = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

a = '{"code":200,"msg":"查询成功","version_code":'
b = ',"version_name":"'
c = '","apk_url":"https:\/\/xiyangyu.github.io\/xiaopijiaowu\/小皮教务_'
d = '.apk","update_log":"'
e = '","update_time":"'
f = '"}'

output = a + version_code + b + version_name + c + version_name + d + update_log + e + nowtime + f

f = open('version.html', 'r+')

flist = f.readlines()

flist[0] = output

f = open('version.html', 'w+')

f.writelines(flist)
