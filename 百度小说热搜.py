import re
import requests

# 百度小说热搜网址
url = "https://top.baidu.com/board?tab=novel"

# 伪装头
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:145.0) Gecko/20100101 Firefox/145.0"
}

# 发送请求、获得响应
response = requests.get(url, headers=headers)
response.encoding = 'utf-8-sig'

soup = response.text

# 构造正则表达式（小说名、作者、类型、简介）
pattern = re.compile(
    r'<div class="c-single-text-ellipsis">(?P<novels_name>.*?)</div>.*?'
    r'<div class="intro_1l0wp">(?P<writers>.*?)</div>.*?'
    r'<div class="intro_1l0wp">(?P<types>.*?)</div>.*?'
    r'<div class="hot-index_1Bl1a">(?P<hots>.*?)</div>',
    re.S
)

# 匹配每个小说
novels = pattern.findall(soup)# 生成的时一个列表，如果有捕获组，就是列表中包含元组

# 匹配每个小说
for item in novels:
    name = item[0]
    writer = item[1]
    type_ = item[2]
    hot = item[3]
    print(f"{name}  {writer}  {type_}  {hot}")



"""# 匹配每个小说
novels = pattern.finditer(soup)# 生成一个迭代器，每一个迭代对象都是match属性

# 匹配每个小说
for item in novels:
    name = item.group("novels_name")
    writer = item.group("writers")
    type_ = item.group("types")
    hot = item.group("hots")
    # 清理文本中的HTML标签
    name = re.sub(r'<.*?>', '', name).strip()
    writer = re.sub(r'<.*?>', '', writer).strip()
    type_ = re.sub(r'<.*?>', '', type_).strip()
    hot = re.sub(r'<.*?>', '', hot).strip()
    # 格式化输出
    print(f"{name}  {writer}  {type_}  {hot}")"""