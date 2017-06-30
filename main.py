#adding various libraries
from spy_details import Spy,spy, friends, chatmessage
from steganography.steganography import Steganography
from datetime import datetime
from termcolor import colored, cprint
#defining a function to add a friend
def add_friend():
    new_friend = Spy('', '', 0, 0.0)
    new_friend.name = raw_input("please add your friends name : ")
    new_friend.salutation = raw_input("are they mr or miss : ")
    new_friend.age = int(raw_input("age: "))
    new_friend.rating = float(raw_input("rating: "))
    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        friends.append(new_friend)
    else:
        print("sorry! invalid entry. we can't add a spy with the details you provided. please try again later. ")
    return len(friends)

#defining the function from where you can select the friend to chat
def select_a_friend():
    number = 0
    for friend in friends:
        print('%s aged %d with rating %.2f is online') % (friend.name, int(friend.age), float(friend.rating))
        number = number + 1
    select_friend = raw_input("choose from your friendlist. ")
    select_friend_postion = int(select_friend) - 1
    if select_friend_postion > number:
        print("invalid index entered")
        start_chat(spy.name,spy.age,spy.rating)
    else:
        return select_friend_postion

#defining the function so that you can send a message in encrypted form.
def send_a_message():
    select_friend = select_a_friend()
    original_image = raw_input("what is the name ofthe image")
    output_path = original_image
    text = raw_input("what message do u want to send ? ")
    if len(text) <= 0:
        print("u cannot send empty message!!!!")
    elif len(text) > 100:
        print("you exceed the message limit .. please try again later!!!!")
        del friends[select_friend]
    else:
        Steganography.encode(original_image, output_path, text)
        chats = chatmessage(text, True)
        friends[select_friend].chat.append(chats)
        print("your secret message is ready.")

#defining a function to decrypt and then read a message.
def read_a_message():
    sender = select_a_friend()
    output_path = raw_input("what is the name of the image.")
    secret_text = Steganography.decode(output_path)
    chat = chatmessage(secret_text, False)
    friends[sender].chat.append(chat)
    if secret_text.upper() == "SOS" or secret_text.upper() == "SAVE ME" or secret_text.upper() == "HELP":
        print("you will receive help soon...")
    print("your secret message is saved.")

#defining a function to read your previous chat.
def read_chat():
    read_for = select_a_friend()
    for chats in friends[read_for].chat:
        if chats.sent_by_me:
            text1 = colored(chats.time.strftime("%a, %d %b %Y %H:%M:%S +0000"), 'blue', attrs=['reverse', 'blink'])
            print(text1)
            print colored(' you said : ', 'green', 'on_red'), chats.message
        else:
            text1 = colored(chats.time.strftime("%a, %d %b %Y %H:%M:%S +0000"), 'blue', attrs=['reverse', 'blink'])
            print(text1)
            print colored(friends[read_for].name, 'green', 'on_red'), chats.message


print("welcome to spy chat application.")
question = "continue as " + spy.salutation + " " + spy.name + "(Y/N)?"
existing = raw_input(question)
status_messages = ['my name is bond,james bond', 'shaken! not stirred', 'die another day']

#defining a function to add the status .
def add_status_message(current_status_message):
    if current_status_message != None:
        print("your current status message is : ") + current_status_message + '\n'
    else:
        print("you don't have any status message currently \n")
        default = raw_input("do you want to select from your older status (Y/N)?")
        if default.upper() == "N":
            new_status_message = raw_input("what status you want to set?")
            if len(new_status_message) > 0:
                update_status_message = new_status_message
                status_messages.append(update_status_message)
        elif default.upper() == "Y":
            item_position = 1
            for message in status_messages:
                print(str(item_position) + "." + message)
                item_position = int(item_position) + 1
            message_selection = raw_input("choose from above messages : ")
            message_selection = int(message_selection)
            if len(status_messages) >= message_selection:
                updated_message = status_messages[message_selection - 1]
                return updated_message

#defining a function which gives the spy various choices and them what to do.
def start_chat(spy_name, spy_age, spy_rating):
    current_status_message = None
    show_menu = True
    while show_menu:
        menu_choices = "what do u want to do \n1. add a status \n2. add a friend \n3. send a message \n4. read the secret message \n5.chat history \n6. close application "
        menu_choice = raw_input(menu_choices)
        if len(menu_choice) > 0:
            menu_choice = int(menu_choice)

            if menu_choice == 1:
                print("you choose to update status.")
                current_status_message = add_status_message(current_status_message)
            elif menu_choice == 2:
                print("you choose to add a friend. please provide us your friends details. ")
                number_of_friends = add_friend()
                print 'You have %d friends' % (number_of_friends)
            elif menu_choice == 3:
                print("you choose to send a message.")
                send_a_message()
            elif menu_choice == 4:
                print("you choose to read a message. ")
                read_a_message()
            elif menu_choice == 5:
                read_chat()
            elif menu_choice == 6:
                show_menu = False
                exit(0)
            else:
                print("you choose an invalid entry. please try again later.")
        else:
            print("please choose an option.")

#function for asking the spy name
def ask_name():
    spy_name = raw_input("please enter your name: ")
    if len(spy_name) == 0:
        while len(spy_name) == 0:
            print("error! please enter your name.")
            spy_name = raw_input("please enter your name")
            return spy_name

    else:
        return spy_name

#function for asking the spy salutation and returning the fullname of spy
def ask_salutation(name):
    fullname = None
    result = True
    while result:
        spy_salutation = raw_input("should i call you miss or mr. : ")
        if len(spy_salutation) > 0 and spy_salutation.upper() == "MR" or spy_salutation.upper() == "MISS":
            fullname = spy_salutation + " " + name
            result = False
        else:
            print("invalid details .. try again later")
    return fullname

#function for asking the age and checking whether user's age is valid to spy or not
def ask_age():
    spy_age = raw_input("what is your age :")
    if len(spy_age) == 0:
        print("please enter your age")
        spy_age = raw_input("what is your age :")
    elif int(spy_age) < 12 or int(spy_age) > 50:
        print("your age is not valid to become a spy.")
        exit(0)
    else:
        return int(spy_age)

#function for asking the rating and telling the spy in which category the spy lies.
def ask_rating():
    spy_rating = float(raw_input("you are rated as : "))
    if spy_rating > 4.0:
        return "%.1f you are one of the best spy." % (spy_rating)
    elif spy_rating <= 4.0 and spy_rating >= 3.0:
        return "%.1f you are one of the good ones." % (spy_rating)
    elif spy_rating <= 2.0 and spy_rating > 3.0:
        return "%.1f you can always work hard." % (spy_rating)
    else:
        return "%.1f we can always need someone in office." % (spy_rating)

#function for returning the final welcome message.
def display(name, age, rating):
    return ("Welcome %s. Your age is %s. And You are rated as : %s ") % (name, str(age), str(rating))

#if user choose to enter as default user then welcome message is printed.
if (existing.upper() == "Y"):
    print("authentication complete. welcome %s %s .") % (spy.salutation, spy.name)
    start_chat(spy.name, spy.age, spy.rating)
#if user doesn't want to move further as default user then the user as to enter his/her details.
else:
    def start():
        ask_salutation(ask_name())
        ask_age()
        ask_rating()


    output = display(ask_salutation(ask_name()), ask_age(), ask_rating())
    print(output)
    start_chat(spy.name, spy.age, spy.rating)
