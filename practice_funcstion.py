from main import my_title
import re

def my_string_title(s):
    s1 = ""
    list_name = re.findall("[^-\s\$]+",s.lower()) #tim ra tat ca nhung chuoi con ma chuoi con do la nhung ky tu lien ke khong phai la - khoang trang
    print(list_name) # in de test
    for val in list_name:
        s1 = s1 + my_title(val) + " " #Cong don chuoi con thanh 1 chuoi lon da duoc in hoa chu cai dau tien

    return s1 #tra ve chuoi da duoc in hoa chu cai dau tien cua cac tu

z = my_string_title("toi join-smith la trAn")
print(z)
