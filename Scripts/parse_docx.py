import zipfile
import xml.etree.ElementTree as ET

docx_path = r'c:\Users\ASUS\OneDrive\Desktop\BTP - Copy\Graphic Era_Confernece_Paper (1).docx'
try:
    with zipfile.ZipFile(docx_path) as docx:
        xml_content = docx.read('word/document.xml')
        
    tree = ET.fromstring(xml_content)
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    
    lines = []
    for p in tree.findall('.//w:p', ns):
        texts = []
        for r in p.findall('.//w:r', ns):
            # check color
            color = r.find('.//w:color', ns)
            color_val = color.attrib.get(f'{{{ns["w"]}}}val') if color is not None else None
            
            t = r.find('.//w:t', ns)
            if t is not None and t.text:
                if color_val == 'FF0000':
                    texts.append(f'[RED: {t.text}]')
                elif color_val:
                    texts.append(f'[COLOR {color_val}: {t.text}]')
                else:
                    texts.append(t.text)
        if texts:
            lines.append(''.join(texts))
            
    with open('parsed_docx.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
        
    print('Extraction done. Total lines:', len(lines))
except Exception as e:
    print('Error:', e)
