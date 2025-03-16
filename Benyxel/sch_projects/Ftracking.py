class AdminUpdate():
    def __init__(self,Sender,Item):
        self.Sender = Sender
        self.Item = Item
        self.tracking = []
        
    def add_tracking(self,track,status):
        track = track
        status = status
        self.tracking.append({"TrackingNum":track,"Sender":self.Sender,"Item":self.Item,"Status":status})
        print(f"Tracking number {track} has been added successfully")
        print(self.tracking)
        


class UserAdd(AdminUpdate):
    def __init__(self,Sender,Item):
        AdminUpdate.__init__(self,Sender,Item)
        
        
    def addAdd(self,trackNum,name,quantity,product):
        trackNum = trackNum
        name = name
        quantity = quantity
        product = product
        self.tracking.append({"TrackingNum":trackNum,"Sender":name,"Quantity":quantity,"Product":product})
        print(f"Tracking number {trackNum} has been added successfully with {quantity} quantity username {name} ")
        print(self.tracking)
        
        
        
    def userCheck(self,trackNum):
        trackNum = trackNum
        for i in self.tracking:
            if i["TrackingNum"] == trackNum:
                print(f"Tracking number {trackNum} is available")
            else:
                print(f"Tracking number {trackNum} is not available")
                
                
                
adding = AdminUpdate("Kwabena","Laptop",)
adding = UserAdd("kwabena","car")
adding.add_tracking("12645", "Shipped")


adding.addAdd("12645","Bernard",1,"Laptop")
