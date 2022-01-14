def isThuanNghich(n):
    str1 = str(n);     
    str2 = str1[::-1]; 
    if (str1 == str2):
        return True;
    else:
        return False;
 
n = int(input("Nhập số nguyên dương n = "));
print("Tổng các chữ số của", n , "là", isThuanNghich(n));
m = int(input("Nhập số nguyên dương m = "));
print("Tổng các chữ số của", m , "là", isThuanNghich(m));
print("Tổng các chữ số của", n , "là", isThuanNghich(n));
#Vũ Thanh Hùng 1451020117
ho = input("Nhập họ: ")
tendem = input("Nhập tên đệm: ")
ten = input("Nhập tên: ")
print("Tên của bạn là : " ,ho+tendem+ten)
print(len(ho),len(tendem),len(ten))
