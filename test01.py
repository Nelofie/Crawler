from urllib import request
from urllib import parse

# 网址
url = "http://www.douban.com/"

# 爬取结果
response = request.urlopen(url)

data = response.read()

data = data.decode('utf-8')

print(data)

# 打印爬取网页的各类信息

print(type(response))
print(response.geturl())
print(response.info())
print(response.getcode())

http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom=

i:ありがとう
from:AUTO
to:AUTO
smartresult:dict
client:fanyideskweb
salt:1511752619120
sign:2610cd9a7b625b5407fa2769344a5435
doctype:json
version:2.1
keyfrom:fanyi.web
action:FY_BY_ENTER
typoResult:false

i:ありがとう
from:ja
to:zh-CHS
smartresult:dict
client:fanyideskweb
salt:1511752663332
sign:ff071d566c175d44fb5090c1587ce154
doctype:json
version:2.1
keyfrom:fanyi.web
action:FY_BY_CLICKBUTTION
typoResult:false