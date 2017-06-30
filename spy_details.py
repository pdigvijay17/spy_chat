from datetime import datetime
#class of spy is made
class Spy :
    def __init__(self,name,salutation,age,rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.online = True
        self.chat = []
        self.current_status_message = None
#object of class is made
spy = Spy('bond','mr','40',4.7)
#various other object of class is made.
friend_1 = Spy('rambo','mr','25','4.39')
friend_2 = Spy('misha','miss','28','4.98')
friend_3 = Spy('jack sparrow','mr','32','5')
#list which store the details of class object is made.
friends = [friend_1,friend_2,friend_3]


#another class for  chat history
class chatmessage:
    def __init__(self, message, sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me