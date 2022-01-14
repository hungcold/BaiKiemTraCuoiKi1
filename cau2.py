def totalDigitsOfNumber(n):
    total = 0;
    while (n > 0):
        total = total + n % 10;
        n = int(n / 10);
    return total;
n = int(input("Nhập số nguyên dương n = "));
print("Tổng các chữ số của", n , "là", totalDigitsOfNumber(n));
#Vũ Thanh Hùng 1451020117
name = input(" Nhập tên đệm :  ")
print(name)
n = len(name)
def totalDigitsOfNumber(n):
    total = 0;
    while (n > 0):
        total = total + n % 10;
        n = int(n / 10);
    return total;
n = int(input("Nhập số kí tự tên đệm + tên = "));
print("Tổng các kí tự của", n , "là", totalDigitsOfNumber(n));
##
tendem=str(input("Nhập tên đệm: "));
print(tendem);
ten=(str(input("Nhập tên của bạn: ")));
print("N = ",len(tendem),"+",len(ten),"=",len(tendem)+len(ten));

