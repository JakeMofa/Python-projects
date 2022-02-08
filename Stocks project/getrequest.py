import requests
import lxml
from lxml import html
 
r = requests.get('http://gun.io')
tree = lxml.html.fromstring(r.content)
elements = tree.get_element_by_id('frontsubtext')
for el in elements:
print(el.text_content())