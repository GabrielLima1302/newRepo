import requests
import lxml.html

html = requests.get('https://www.americanas.com.br/busca/halter')
doc = lxml.html.fromstring(html.content)

halteres = doc.xpath('//div[@class="grid__StyledGrid-sc-1man2hx-0 iFeuoP src__GridItem-sc-122lblh-0 gGJHBq"]')[0]

titles = halteres.xpath('.//h3[@class="styles__Name-sc-1e4r445-0 fYqJrQ product-name"]/text()')
print(titles)