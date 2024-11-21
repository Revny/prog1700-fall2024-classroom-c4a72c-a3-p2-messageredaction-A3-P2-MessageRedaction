#Program 2 – Message Redaction
#Description:   Design and write a program that counts and removes all desired letters from 
#               any user-entered sentence or phrase.

#Student #:     
#Student Name: Lucas 

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    while True: #while loop that will keep runing untill exit is typed
        phrase=input("type a phrase or type quit to exit the program" )
        if phrase.lower=="quit":
            print("exiting")
            break
    
    redacted_letters=input("enter a comma-separated phrase that you want redacted") 
    redacted_letters=[letter for letter in redacted_letters.split ]
        #letters and words that will be redacted
    redacted_words=""
    redactedcount=1

    for char in phrase: 
        if char.lower() in redacted_letters:
            redacted_words='-'
            redactedcount +1

    print(f"the number of redacted letters is: {redacted_letters}")
    print(f"the number of redacted words is: {redacted_words}")






    # YOUR CODE ENDS HERE
    main()