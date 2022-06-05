import random
def computer():#generates 4 random colors
    color=["b","r","g","y"]
    color_1=random.choice(color)
    color_2=random.choice(color)
    color_3=random.choice(color)
    color_4=random.choice(color)
    data=(color_1,color_2,color_3,color_4)
    return data#returns the number of correct colors in the correct place
    
    
    
def try_it(color_1,color_2,color_3,color_4):#asks the user to enter the colors
    print("colors are (b)lue,(r)ed,(g)reen,(y)ellow")
    choice=True
    while choice==True:
        colors1=input("enter your choice from the list for position one")
        colors1=colors1.lower()
        if colors1 !='b' and colors1 !='r' and colors1 !='g' and colors1 !='y':
            print("its not in the list")
        else:
            choice=False
    choice=True
    while choice==True:
        colors2=input("enter your choice from the list for position two")
        colors2=colors2.lower()
        if colors2 !='b' and colors2 !='r' and colors2 !='g' and colors2 !='y':
            print("its not in the list")
        else:
            choice=False
    choice=True
    while choice==True:
        colors3=input("enter your choice from the list for position three")
        colors3=colors3.lower()
        if colors3 !='b' and colors3 !='r' and colors3 !='g' and colors3 !='y':
            print("its not in the list")
        else:
            choice=False
    choice=True
    while choice==True:
        colors4=input("enter your choice from the list for position four")
        colors4=colors4.lower()
        if colors4 !='b' and colors1 !='r' and colors4 !='g' and colors4 !='y':
            print("its not in the list")
        else:
            choice=False
    choice=True
    correct=0
    wrong=0
    if color_1==colors1:#checks if the user has the correct colors in the correct place
        correct+=1
    elif color_1==colors2 or color_1==colors3 or color_1==colors4:
        wrong+=1
    if color_2==colors2:
        correct+=1
    elif color_2==colors1 or color_2==colors3 or color_2==colors4:
        wrong+=1
    if color_3==colors3:
        correct+=1
    elif color_3==colors2 or color_3==colors1 or color_3==colors4:
        wrong+=1
    if color_4==colors4:
        correct+=1
    elif color_4==colors2 or color_4==colors3 or color_4==colors1:
        wrong+=1
    print("correct color in the correct place:",correct)#prints the number of correct colors in the correct place
    print("correct color in the wrong place:",wrong)#prints the number of correct colors in the wrong place
    print()
    data2=[correct,wrong]
    return data2
def main():
    (color_1,color_2,color_3,color_4)=computer()
    score=0
    play=True
    while play==True:
        (correct)=try_it(color_1,color_2,color_3,color_4)
        score+=1
        if correct==4:
            play=False
    print("you win !")#tells the user if they won or not
    print("you took ",score,"gueses")
    
main()

