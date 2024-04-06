import requests
 
while(True): 
    name=input("Enter your name : ")
    print("\nHello",name,
'''\b, welcome to 'Crush Chronicles: A Journey to Girlfriend Status', a game designed to help you in your 
love life by converting your crush into your girlfriend \nSorry girls, you are ineligible for the game but 
if you have different preferences then you may continue :)\n''')

    age=int(input("Enter your age : "))

    if age<18:
        print("Sorry but you can't play this game as you are a minor")
        print("1.Restart     2.Exit")
        option=int(input("Enter your choice (1 or 2) : "))
        if(option==1):
            continue
        else:
            break

    print("\nThe game believes in you that you have entered your true age your current relationship status is single ;) ") 
    print("So let us start the game with her name\n")

    her_name=input("Enter her name : ")
    her_age=input("Enter her age (Don't worry, I am not going to check if she's minor or not) : ")

    print("\nHmm, pretty good name, by the way it's meaning is -")

    url = "http://ping.skarj.pl/adjective"
    payload = {"string": her_name}

    response = requests.get(url, params=payload)

    if response.status_code == 200:
        adjective = response.json()["output"]
        print(adjective)
    else:
        print(" ")

    print("\nwow, that's an intersting meaning :) ")


    print("\nWhat is the first thing about her that comes to your mind when you think about her? (for ex. beautiful)\n")   
    quality=input("Enter : ") 
    print("\nGreat, now to show her that you have a good vocabulary, for mentioning her qualities you can use words like -")

    url = "http://ping.skarj.pl/synonym"
    payload = {"string": quality}

    for i in range(3):
        response = requests.get(url, params=payload)

        if response.status_code == 200:
            synonym = response.json()["output"]
            print(synonym)
    
        else:
            print("Leave it, I can't think of some synonym LOL")        


    animal=input("\nEnter her favourite animal : ")
    print("\nWhat a coincidence, I also love",animal,"\bs and now you should too :) \n")    

    qna=input("Do she have a pet? (Y or N) : ")

    if qna=="Y" or qna=="y":
        pet_name=input("Enter it's name (don't say you don't know) : ")
        print('''\nYou can come close to her by showing her that you likes her pet and can also keep an 
owo name of''',pet_name,"like -")
        
        url = "http://ping.skarj.pl/owo"
        payload = {"string": pet_name}

        response = requests.get(url, params=payload)

        if response.status_code == 200:
            owo_text = response.json()["output"]
            print(owo_text)
        else:
            print("O",pet_name,"o")
        print("\nYou have to accept, that's a unique name")    

    else:
        print("Great, you can gift her",animal,"on next valentines day or on her birthday")    


    print('''\nYou know what, girls like humorous boys, so you should tell her jokes in between the 
conversations and if you are not good in it then why am I sitting here? I am here to help you -\n''')  

    jokes=int(input("Enter the no. of jokes you want : "))  
    
    url = "http://ping.skarj.pl/joke"
    payload = {"string": " "}

    for i in range(jokes):
        response = requests.get(url, params=payload)

        if response.status_code == 200:
            joke = response.json()["output"]
            print(joke)
        else:
            print("Do you know why are you listening to me attentively? because you love me")

    response = requests.get(url, params=payload)        


    print('''\nDo you know, I am very good in predicting future. Are you thinking that why did'nt I 
predicted yours? Thats because your future is bright as you are going to get your crush as your girlfriend soon\n
What I was saying is that you can impress her by predicting her future by just asking her zodiac sign\n''')
    
    zodiac=input("Enter her zodiac sign : ")

    print("\nOk, tell her that -")

    url = "http://ping.skarj.pl/astrologer"
    payload = {"string": her_name+" "+her_age+" "+zodiac}

    response = requests.get(url, params=payload)

    if response.status_code == 200:
        prediction = response.json()["output"]
        print(prediction)
    else:
        print("She's going to get a boyfriend who will love her very much")


    print('''\nYou know, the more common things you have with her, the better your relationship would be, you
can ask her her favourite celebrity and can tell her that your favourite is also the same and to show that
you genuinely have the same choice you can tell her information about the celebrity which will show that 
you actually follows him/her. I'll help you with information\n''')
    
    celebrity=input("Enter the celebrity's name : ")

    url = "http://ping.skarj.pl/celebrity"
    payload = {"string": celebrity}

    response = requests.get(url, params=payload)

    if response.status_code == 200:
        celebrity_info = response.json()["output"]
        print(celebrity_info)
    else:
        print("Never heard of that :( What does she watches?")


    print('''\nGood friendship and relationship forms with consuming content together, how about Animes?
If she already loves watching Animes, you can join her or other way round, if you watches and she doesn't
watches then you can encourage her to watch them with you. watching Animes together will make both of you
aware of each others thinking and emotions which will make your relationship stonger
What if both of you don't watches Animes? No worries, just tell me the genre and I'll suggest you a few
Animes\n''')
    
    genres = input("Enter the genres : ")
    url = "http://ping.skarj.pl/anime_suggestion"
    payload = {"string": genres}

    for i in range(3):
        response = requests.get(url, params=payload)

        if response.status_code == 200:
            anime_suggestion = response.json()["output"]
            print(anime_suggestion)
        else:
            print("Never heard of that genre")

    print("\nIf I have repeated the name of an Anime, that means it's a must watch :)\n")


    print('''After all these things sometimes flirting or presenting your emotions with Pick up lines can 
can ignite the spark or can act as the last nail in the coffin. Tell me how many pick up lines do you want?\n''')
   
    pick=int(input("Enter the no. of Pick up lines you want : "))

    for i in range(pick):
        url = "http://ping.skarj.pl/pickupLine"
        payload = {"string": " "}

        response = requests.get(url, params=payload)

        if response.status_code == 200:
            pickup_line = response.json()["output"]
            print(pickup_line)
        else:
            print("Are you a global variable? because no matter where I am, you are always in my mind")    

    
    print('''\nWell, all the best to you, I have helped you as much as I can, now if the girl is not taken
or insane, she would accept you as her boyfriend :)\n''')
    
    print("By the way I must say that",name,her_name,"sounds very good together")

    print("What comes to my mind after hearing your names together is - \n")

    url = "http://ping.skarj.pl/rhyme"
    payload = {"string": name+" "+her_name}

    response = requests.get(url, params=payload)

    if response.status_code == 200:
        rhyming_line = response.json()["output"]
        print(rhyming_line)
    else:
        print("Nothing")

    print('''\nIf you didn't liked it then you must know, it was deep :) 
I loved this journey, not hoping to see you again as now onwards you would'nt be single anymore''') 

    print("\n1.Satisfied    2.I can do this all day\n")   

    option=int(input("Enter your choice (1 or 2): "))

    if(option==2):
        pass
    else:
        break

print("The End")    










