class AdminUpdate():
    def __init__(self):
        
        self.tracking = []
        
    def add_tracking(self,track,name,status):
        name = name
        track = track
        status = status
        self.tracking.append({"TrackingNum":track,"Sender":name,"Status":status})
        print(f"Tracking number {track} has been added successfully")
        print(self.tracking)
        


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


adding.add_tracking("YT6734773403949","Appiah", "received")
adding.add_tracking("12645","Mensah", "Shipped")
user.userAdd("12645","Bernard",1,"Laptop")

user.userAdd("YT6734773403949","Bernard",92,"T-rolls")
user.userCheck("12645")
user.userCheck("YT6734773403949")
