#!/usr/bin/env python3

#Which car should you actually drive?

#Dictionary of responses
responses = {
        "y/y": "I'd say a rocket car, but those aren't legal in drive thrus.",
        "y/n": "Probably should just drive a Ferrari or something.",
        "n/n": "Just drive a Prius since they are practical.",
        "n/y": "See if you can get an Oscar Mayer Weinermobile."
        }

#Print description of what is going to happen
print("Lets see what car you should drive!")

#while loop to repeat until proper input is submitted
while True:
    #Checks if the user likes to drive fast or not and stores the response
    fast = input("Do you like to drive fast? y/n: ").lower()
    if fast  == "y":
        print("So you're a daredevil.")
        break
    elif fast == "n":
        print("So you're safe.")
        break
    else:
        print("Please input a proper respone.")

#while loop to repeat until proper input is submitted
while True:
    #Checks if the user is always hungry or not and stores the response
    hungry = input("Are you always hungry? y/n: ").lower()
    if hungry == "y":
        print("Don't worry, me too.")
        break
    elif hungry == "n":
        print("Must be nice.")
        break
    else:
        print("Please input a proper response.")

#Prints the output based on the responses and the dictionary of responses
print(responses.get(f"{fast}/{hungry}"))
