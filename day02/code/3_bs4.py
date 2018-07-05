from bs4 import BeautifulSoup

soup = BeautifulSoup(open('test.html'), 'lxml')
#
# print(soup.a)
# print(soup.a.attrs)
# print(soup.a.attrs.get('href'))
#
# obj  = soup.p
# print('string%s'%soup.p.string)
# print('get_text()%s'%soup.p.get_text())
#
# print(soup.find('div',id='a'))
# print(soup.find('div',id='a').contents)
# print(soup.find('div',id='a').descendants)

print(soup.select('#a .b'))