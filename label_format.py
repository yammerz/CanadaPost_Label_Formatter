import os
from pypdf import PdfWriter, PdfReader
from datetime import datetime

file_name = "Labels/label.pdf"

with open(file_name, "rb") as in_f:
    input1 = PdfReader(in_f)
    output = PdfWriter()
    original = PdfWriter()


    numPages = len(input1.pages)
    print("document has %s pages." % numPages)

    for i in range(numPages):
        page = input1.pages[i]
        original.add_page(page)
       
        print(
            page.mediabox.left,
            page.mediabox.bottom,
            page.mediabox.right, 
            page.mediabox.top)

        page.trimbox.lower_left = (460, 75)
        page.trimbox.upper_right = (765, 540)
        page.cropbox.lower_left = (460, 75)
        page.cropbox.upper_right = (765, 540)
        output.add_page(page)



    with open("Labels/print/{}.pdf".format(datetime.isoformat(datetime.now()).split("T")[0]), "wb") as out_f:
        output.write(out_f)
        cwd = os.getcwd()
     
        os.startfile("{}/{}".format(cwd.replace('\\', '/'), out_f.name))

    with open("Labels/archive/{}-original.pdf".format(datetime.isoformat(datetime.now()).split("T")[0]), "wb") as original_f:
        original.write(original_f)




