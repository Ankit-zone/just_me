class User:
     def __init__(self,username):
          self.username=username
     def send_message(self,chatroom,content):
          message=Message(self,content)
          chatroom.add_message(message)

     
class Message:
     def __init__(self,sender,content):
          self.sender=sender
          self.content=content
     def Display_message(self):
          print(f"{self.sender} - {self.content}")
     
class Chatroom:
     def __init__(self):
          self.users=[]
          self.message=[]
     def add_user(self,user):
          self.users.append(user)
     def add_message(self,message):
          self.message.append(message)
     def view_history(self):
          for i in self.message:
               i.Display_message()

user1=User("Ankit")
user2=User("Riya")
chatroom=Chatroom()
user1.send_message("Ankit","Hello Everyone!")
user2.send_message("Ankit","Hello Ankit ")
chatroom.view_history()


