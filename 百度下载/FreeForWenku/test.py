import docx

doc = docx.Document('094421.docx')

print(doc)
if len(doc.paragraphs)==0:
    print("666")