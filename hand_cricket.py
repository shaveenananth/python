import random
def hand_cricket(over):
    balls=over*6
    run = 0
    for i in range(balls):
        comp = [1,2,3,4,5,6]
        computer=random.choice(comp)
        
        cur = int(input("enter run"))
        print(f"your coice {cur}, computer choice is {computer}")
        if cur==computer:
            print("your score is:", run)
            break
        
        else:
            run= run+cur
            print("your score is:", run)   

hand_cricket(2) 
