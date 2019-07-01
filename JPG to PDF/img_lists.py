import os

in_path=r"G:/JPG to PDF/inputs"
pdf_file=r"outputs/pdf_test.pdf"
file_list=os.listdir(path=in_path)
print(file_list)
file_list2=[]
for i in file_list:
    temp=i.split('.')
    if(temp[1] in ["jpg","png","jpeg","bmp"]):
        file_list2.append(i)
    else:
        pass

print(file_list2)