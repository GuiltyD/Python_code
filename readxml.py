from xml.etree.ElementTree import parse

doc = parse('node.xml')
print(doc.getroot())
for item in doc.iterfind(r'people/item'):
    print(item.findtext('name'))
    print(item.findtext('gender'))
    print(item.findtext('age'))
