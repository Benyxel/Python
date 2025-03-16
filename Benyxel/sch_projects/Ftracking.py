class AdminUpdate():
    def __init__(self):
        
        self.tracking = []
        
    def adminAdd(self,trackNum,name,status):
        name = name
        trackNum = trackNum
        status = status
        self.tracking.append({"TrackingNum":trackNum,"Sender":name,"Status":status})
        print(f"Tracking number {trackNum} has been added successfully")
        
        


class UserAdd(AdminUpdate):
    def __init__(self):
        AdminUpdate.__init__(self)
        
        
    def userAdd(self,trackNum,name,quantity,product):
        trackNum = trackNum
        name = name
        quantity = quantity
        product = product
        self.tracking.append({"TrackingNum":trackNum,"Sender":name,"Quantity":quantity,"Product":product})
        print(f"Tracking number {trackNum} has been added successfully with {quantity} quantity username {name} \n ")
      
        
        
    def userCheck(self,trackNum):
        trackNum = trackNum
        found = False
        for i in self.tracking:
            if i ["TrackingNum"] == trackNum:
                print(f"Tracking number: {i['TrackingNum']} name: {i['Sender']} quantity: {i['Quantity']} product: {i['Product']} \n")
                found = True
                break
        if not found:
            print(f"Tracking number {trackNum} is not found, 'this could be the package is not updated yet or still in transit' \n")
                
                
adding = AdminUpdate()
user = UserAdd()

trackNum = input("Enter tracking number: ")
name = input("Enter name: ")
status = input("Enter status: ")
adding.adminAdd(trackNum,name,status)

trackNum = input("Enter tracking number: ")
name = input("Enter name: ")
quantity = input("Enter quantity: ")
product = input("Enter product: ")
user.userAdd(trackNum,name,quantity,product)

