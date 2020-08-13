import xml.etree.ElementTree as eltree

tree = eltree.parse('data.xml')
root = tree.getroot()
for child in root:
    print(child.tag.upper())
    for pro in child:
        print(f"\t{pro.tag.capitalize()} {pro.text}")
