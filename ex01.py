#KHAI BÁO BIẾN
print("------------------------------------------------------------------------------------------------")
m = int(10)
n = str("hello world")
p = float(8)
q = complex(20,5)
print("Hàm if")
name = "Sen"
age = 21
is_valid = True
if is_valid: {
    print(" Toi ten = ", name),
    print(" Tuoi = ", age)
}
print("------------------------------------------------------------------------------------------------")

print("Một vài ví dụ khai báo biến")
print("Kiểu int =  ",m)
print("Kiểu chuỗi = ",n)
print("Kiểu float = ",p)
print("Kiểu số phức = ",q)


#DANH SÁCH
print("Khai báo danh sách")
fruits = ["apple", "banana", "cherry"]
x1, y1, z1 = fruits
print(x1)
print(y1)
print(z1)

print("------------------------------------------------------------------------------------------------")

#TÍNH TOÁN
print("Một vài phép tính toán cơ bản")
x = 10
y = 15
a = x + y
b = x - y
c = x*y
d = x / y
e = x // y
print( "x + y = ",a)
print( "x - y = ",b)
print( "x * y = ",c)
print( "x / y = ",d)
print( "x // b = ",e)
print( "x % y = ",x%y)


print("------------------------------------------------------------------------------------------------")

#TOÁN TỬ LOGIC
#AND
a1 = True
b1 = False
print(a1 and b1)  # False
print(a1 and True)  # True
print(b1 and False)  # False

#OR

print(a1 or b1)  # True
print(b1 or b1)  # False

#NOT

print(not a1)  # False
print(not b1)  # True

# > < == !=
# x = 10, y = 15
print((x > y) and (y < 10))  # True
print((x < y) or (y == 5))  # True


print("------------------------------------------------------------------------------------------------")

#NHẬP, XUẤT DỮ LIỆU
# Nhập một số nguyên
so_nguyen = int(input("Nhap mot so nguyen: "))
print("Ban da nhap:", so_nguyen)

# Nhập một chuỗi
chuoi = input("Nhap mot chuoi: ")
print("Chuoi vua nhap la:", chuoi)

#XUẤT DỮ LIỆU
ten = "Huong Sen"
tuoi = 20
print("Ten  la:", ten)
print( tuoi, "tuoi")


# Sử dụng format()
print("Ten: {}, Tuoi: {}".format(ten, tuoi))

print("------------------------------------------------------------------------------------------------")

# CẤU TRÚC IF ELSE
print("CẤU TRÚC IF ELSE")
diem = float(input("Nhap diem cua ban: "))

if diem >= 8.5:
    print("Xep loai: Gioi")
elif diem >= 7:
    print("Xep loai: Kha")
elif diem >= 5:
    print("Xep loai: Trung binh")
else:
    print("Xep loai: Yeu")

print("------------------------------------------------------------------------------------------------")

#CẤU TRÚC VÒNG LẶP
# Duyệt qua danh sách
danh_sach = ["Huong", "Sen", "Nguyen"]
for ten in danh_sach:
    print("Xin chao,", ten)
print("---------------------------------------------")

# Duyệt qua khoảng số
for i in range(1, 6):
    print("So:", i)
print("---------------------------------------------")

#WHILE
n = 5
while n > 0:
    print("Gia tri n:", n)
    n -= 1
print("----------------------------------------------")


#BREAK, CONTINUE, PASS
for i in range(1, 10):
    if i == 5:
        break
    print(i)

for i in range(1, 10):
    if i % 2 == 0:
        continue
    print(i)

for i in range(1, 6):
    if i == 3:
        pass  
    print(i)

print("------------------------------------------------------------------------------------------------")

#CHUỖI
print("CHUỖI")
#KHAI BÁO CHUỖI
chuoi1 = 'Xin chao'
chuoi2 = "Hello World"
chuoi3 = '''Day la chuoi
nhieu dong'''
chuoi4 = """Hello
Python"""

print(chuoi1)
print(chuoi2)
print(chuoi3)
print(chuoi4)
print("----------------------------------------------")

#TRUY CẬP KÝ TỰ
print("TRUY CẬP KÝ TỰ CHUỖI")
chuoi = "HuongSen"

print(chuoi[0])    
print(chuoi[1:5]) 
print(chuoi[:4])   
print(chuoi[4:])   

print("----------------------------------------------")

#NỐI CHUỖI
ho = "Nguyen Thi Huong"
ten = "Sen"
ho_ten = ho + " " + ten
print(ho_ten)  
print("----------------------------------------------")