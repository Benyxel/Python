shippingAddress = ["M856+FOFOOFO+IMPORT 15015586074广东省佛山市南海区里水镇旗峰大道2号全顺祥物流基地18栋2号兴航仓（导航：兴航仓）M856"]

class SAddressR():
    def __init__(self):
        pass
    
    
    def address(self,name):  
        name = name 
        if name == "":
            print("Name is required")
        else:
            combined_address = f"{shippingAddress[0]}{name} "
            shippingAddress.append(combined_address)
            print(f"Dear {name}! Your Shipping Address is:\n({combined_address})")
            print(f"Your shipping mark is M856{name}")
            print(f"NOTE: please add all your tracking numbers at the add a tracking number section")
            


Requset = SAddressR()

name = input("Enter your name: ")

Requset.address(name)