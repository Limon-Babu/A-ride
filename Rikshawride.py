name=input("What is your name, sir?")
place=input("Where to you wanna go, sir?")
mymoney=input("How much Taka do you have, sir?")
mymoney=int(mymoney)
rikshawfare=50
if mymoney>=rikshawfare:
    print("Hello,", name, ",sir! You are wellcome."
    "Get on the rikshaw, sir."
    "It will take a little bit to go there!"
    "There's a magazine, sir. You can read that if you want!")
else:
    print("Sorry, sir!", mymoney ,"Taka is not worth of it."
    "You should have at least ", rikshawfare, "Taka to go to", place, ", sir.")