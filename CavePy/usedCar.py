import random
import time

def displayIntro():
    print ('You decide you want a used car.')
    print ('You search online everywhere and find the perfect match.')
    print ('The car is a 1991 Volvo 740SE Wagon')
    print ('It is on Kijiji for 850 Dollars, You go for it!')
    print
    
def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print ('You meet with the owner and he tells you it is 850 dollars firm. Do you haggle the price down (1) or buy for the full price (2)')
        cave = raw_input()
    return cave

def checkCave(chosenCave):
#    print ('You approach the cave...')
#    time.sleep(2)
#    print ('It is dark and spooky...')
#    time.sleep(2)
#    print ('A large dragon jumps out in front of you! He opens his jaws and...')
#    print
#    time.sleep(2)
    
    #friendlyCave = random.randint(1, 2)
    
    if chosenCave == "1":#first 
        print ('You saved 500 dollars!')
        print ('You notice a crunching sound when turning left, do you repair it Y/N')
        nextCave = raw_input()
        if nextCave == "y": #paired with elif line 39 second
            print("It turns out the CV joints were going bad, good job on repairing the Volvo")
            print("During the repair you meet an older fella, do you give him the time of day? Y/N")
            nextCave = raw_input()
            if nextCave == "Y" or "y": #third level
                print("While sitting and having a soda with this strange chap, he decides to tell you about your old Volvo")
                print("Turns out your Volvo is a very rare car here in North America, a bit more than 1000 released in all of North America")
                print("They only came out in three colors, Red, Black and White.")
                print("You must be feeling pretty good about yourself huh? YOU SHOULD!")
            else: #third level
                print("You walk past the kind old chap as if you have an inflated sense of self")
                print("You get not even two blocks down the street as the old chap watches your car")
                print("The Volvo stalls, BUT WAIT!! You have an OBD1 in under your hood")
                print("But you don't know how to read it, the old chap giggles.")
                print("You should feel embarassed, the old man was a mechanic from Sweden.")
                    
        elif nextCave =="n": # pair with second
            print("You drive around for a couple days until eventually your CV joints give, ruining your entire car.")
            print("You just destoryed a cult classes, feel bad.")
            print("BUT WAIT YOU CAN STILL BE SAVED.. Did you get CAA? Y/N")
            nextCave = raw_input()
            
            if nextCave == "Y" or nextCave=="y":#3
                print("CAA towed your car to a nearby mechanic and because of the rarity of your Volvo")
                print ("an old man fixes it for little to no cost!")
                print ("What a great guy.")
            else:
                print("Why would you, right? It's a friggin 1991 VOLVO! Pour some gas on it and set it on fire")
                print("I don't blame you... But the Volvo guys will")
                print("And since the writer of this program is in several Volvo Clubs.. SHAME ON YOU!!")
            
            '''nextCave = raw_input()
            if nextCave == "y":
                print("yay you win")'''
        
    else:#1
        print ("By paying full price for the Volvo the previous owner felt bad")
        print ("He tells you all about a neat trick to replace a very noticable rust stain in your headliner")
        print ("Do you repair the headliner Y/N?")
        
        nextCave = raw_input()#2
        if nextCave == "y" or nextCave == "Y":
            print("So proud of your new headliner and all the work you put into it, you post a video on youTube")
            print("You get over 50,000 hits on your video and find out that your Volvo is actually very rare")
            print("Someone strange contacts you from youTube, do you check the message? Y/N")
            
            nextCave = raw_input()#3
            if nextCave == "Y" or nextCave == "y":
                print("Turns out a Volvo Rep saw over 1,000,000KM on your odometer")
                print("HE OFFERS YOU A BRAND NEW VOLVO!! of course it's not the real deal anymore")
                print("I mean lets face it, since ford bought them they've never been the same")
                print("BUT HEY NOT BAD FOR 850 Dollars EH?!")
            else:
                print("You choose to ignore all messages from your youTube account")
                print("You keep on keepin' on with your Volvo, but honestly?")
                print("You really should have checked that message, what's the harm?")
        else: #2
            print ("You hit a bump in the road and the entire headliner falls down!")
            print ("YOU CANT SEE!!! YOU DONT KNOW WHATS GOING ON!!" )
            print ("Do you turn left or right? L/R")
            nextCave = raw_input()
            
            if nextCave == "L" or nextCave == "l" or nextCave == "Left":#3
                print ("You hit an oncoming truck!")
                print ("Doesn't matter you're in a Volvo")
                print ("The truck bounces right off of you and blows up")
            else: #3
                print ("You turn into the ditch!! ")
                print ("Nothing can stop your Volvo!!")
                print ("You hit a bear!!! THE BEAR IS DEAD!! ")
                print ("YOU HIT AN ELEPHANT!! THE ELEPHANT IS DEAD!!! OH MY GOD!!!!!!!")
                print ("The Volvo eventually stops. YOU'RE ALIVE!!")
                print ("..and your Volvo starts right back up like nothing happened!")


def main():
    
    
    playAgain = 'yes'
    while playAgain == 'yes' or playAgain == 'y':
        displayIntro()
        caveNumber = chooseCave()
        checkCave(caveNumber)
    
        print ('Do you want to play again? (yes or no)')
        playAgain = raw_input()


if __name__ == "__main__": main()
