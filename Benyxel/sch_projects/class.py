class dataInput:
    def __init__(self, user,email,password):
        self.usernames = user
        self.emails = email
        self.passwords = password
        
user1 = dataInput("Bernard", "benyxel@gmail.com", "1jjsd@jf")
print(f'''
      username is {user1.usernames}
      Email is {user1.emails}
      Password is {user1.passwords}
      ''')