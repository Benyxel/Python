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
    def __init__(self,status):
        AdminUpdate.__init__(self,status)
        
        
    def add_tracking(self,trackNum,name,quantity):
        trackNum = trackNum
        name = name
        quantity = quantity
        print(f"Tracking number {trackNum} has been added successfully")
        print(self.tracking)
                
                
                
'''adding = AdminUpdate("Kwabena","Laptop",)
adding.add_tracking("12645", "Shipped")
adding.add_tracking("35677" ,"AT the warehouse")'''
