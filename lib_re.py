import re

p = re.compile("[a-z]+")
m = p.match("python")  # 첫 문자
print(m.group())  # python
print(m.start())  # 0
print(m.span())  # (0, 6)

m = p.search("3 python")
print(m.group())  # python
print(m.start())  # 3
print(m.end())  # 8
print(m.span())  # (2, 8)

# 축약
m = re.match('[a-z]+', 'python')
print(m)

p = re.compile("a.b")
print(20, p.match("acbcab"))  # <re.Match object; span=(0, 3), match='acb'>
print(21, p.match("ab"))  # None

####################################################
# 컴파일 옵션
p = re.compile("a.b")
m = p.match('a\nb')  # None
print(m)

# DOTALL
p = re.compile('a.b', re.DOTALL)
m = p.match('a\nb')
print(m)  # <re.Match object; span=(0, 3), match='a\nb'>

# IGNORECASE
p = re.compile('[a-z]+')
print(p.match("Python"))  # None

p = re.compile('[a-z]+', re.I)
print(p.match("Python"))  # <re.Match object; span=(0, 6), match='Python'>

# MULTILINE

# VERBOSE

####################################################
# 백슬래시 문제
p = re.compile('\section')  # 의도: "\section" 문자열 찾기, 실제: \s로 인식
p = re.compile('\\section')  # escape 쓰려는데 파이썬이 특이해서 \\ -> \로 바꿔버림
p = re.compile('\\\\section')  # 이러면 되는데, 별로임
p = re.compile(r'\\section')  # r이나 R 붙여주면 raw string으로 쓰겠다는 의미
####################################################
# |
p = re.compile('Crow|Servo')
print(p.match('CrowHi'))  # <re.Match object; span=(0, 4), match='Crow'>
print(p.match('ServoHi'))  # <re.Match object; span=(0, 5), match='Servo'>

# ^ (\A는 MULTILINE에서도 항상 전체의 처음)
p = re.compile('^Life')
print(p.search('Life is too short'))  # <re.Match object; span=(0, 4), match='Life'>
print(p.search('My Life is too short'))  # None
##
p = re.compile("Life")
print(60, p.match("aLife"))  # None
print(61, p.match("Life"))  # <re.Match object; span=(0, 4), match='Life'>
##

# $ (\Z는 MULTILINE에서도 항상 전체의 마지막)
p = re.compile('short$')
print(p.search('Life is too short'))  # <re.Match object; span=(12, 17), match='short'>
print(p.search('Life is too short, you need python'))  # None
# ^, $ 를 문자열로는 \^ \$

# \b: 단어 구분자
p = re.compile(r'\bclass\b')  # 파이썬은 \b를 백스페이스라고 인지해서
print(p.search('no class at all'))  # <re.Match object; span=(3, 8), match='class'>
print(p.search('class at all'))  # <re.Match object; span=(0, 5), match='class'>
print(p.search('no classroom at all'))  # None

p = re.compile(r'\bclass')
print(p.search('no subclass at all'))  # None
print(p.search('no classroom at all'))  # <re.Match object; span=(3, 8), match='class'>

# \B
p = re.compile(r'\Bclass\B')
print(p.search('no class at all'))  # None
print(p.search('no AclassB at all'))  # <re.Match object; span=(4, 9), match='class'>
print(p.search('no classroom at all'))  # None

####################################################
p = re.compile('(ABC)+')
m = p.search('ABCABC OK?')
print(m)  # <re.Match object; span=(0, 6), match='ABCABC'>
print(m.group())  # ABCABC

p = re.compile(r"\w+\s+\d+[-]\d+[-]\d+")  # abc  1212-23-343
m = p.search("park    010-1234-1234")
print(m)  # <re.Match object; span=(0, 18), match='park 010-1234-1234'>

# 그루핑은 반복되는 문자열을 찾을 때 사용되는데, 더 중요하게는 특정 문자열만 뽑아내기 위해서
p = re.compile(r'(\w+)\s+\d+[-]\d+[-]\d+')
m = p.search("park    010-1234-1234")
print(m.group())  # park    010-1234-1234
print(m.group(1))  # park
# print(m.group(2))  # error
# print(m.group(0))  # park    010-1234-1234

p = re.compile(r'(\w+)\s+(\d+[-]\d+[-]\d+)')
m = p.search("park    010-1234-1234")
print(m.group(1))  # park
print(m.group(2))  # 010-1234-1234

p = re.compile(r'(\w+)\s+((\d+)[-]\d+[-](\d+))')
m = p.search("park    010-1234-5678")
print(m.group(1))  # park
print(m.group(2))  # 010-1234-1234
print(m.group(3))  # 010
print(m.group(4))  # 5678

p = re.compile(r'(\b\w+)\s+\1')  # (그룹) + " " + n번째 그룹과 동일한 단어
m = p.search('Paris in the the spring')
print(m.group())  # the the

# [] 안에 .은 문자 .
# [] 안에 ^은 반전을 의미

# file1.bar file2.bat file3.cf
# bat 확장자는 제외해라 ->
p = re.compile(".*[.]([^b].?.?|.[^a]?.?|..?[^t]?)$")
# 안 그래도 복잡한데 여기ㅔㅇ 조건이 하나 더 추가된다면? 노답. 그래서,
# (?!...) : Matches if ... doesn’t match next.
p = re.compile('.*[.](?!bat$).*$')  # = 뒤에 bat로 끝나는 애를 제외해라.
p = re.compile('.*[.](?!bat$|exe$).*$')

####################################################
# 문자열 바꾸기 https://wikidocs.net/4309

