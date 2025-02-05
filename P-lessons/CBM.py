
def calculate_cmb(length, width, height):
    return length * width * height / 1000000

length = float(input("Enter the length here in CM: "))
width = float(input("Enter the width here in CM: "))
height = float(input("Enter the height here in CM: "))

cbm = calculate_cmb(length, width, height)

shipping_fee = cbm * 250 * 16.1
print(f"The CBM is {cbm}")
print(f"The shipping fee is {shipping_fee}")

