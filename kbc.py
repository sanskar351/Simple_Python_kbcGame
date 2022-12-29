from playsound import playsound
listq=["What is the capital of India ?","What is the capital of Uttarakhand?","What is the capital of Uttarapradesh ?","What is the capital of Mumbai ?","What is the capital of Goa ?","What is the capital of Bihar ?","What is the capital of Gujrat ?","What is the capital of Punjab ?","What is the capital of Rajasthan ?","What is the capital of West Bengal ?"]
lista=[['(a) Delhi','(b) Dehradun','(c) Lucknow','(d) Maharashtra'],['(a) Delhi','(b) Dehradun','(c) Lucknow','(d) Maharashtra'],['(a) Delhi','(b) Dehradun','(c) Lucknow','(d) Maharashtra'],['(a) Delhi','(b) Dehradun','(c) Lucknow','(d) Maharashtra'],['(a) Panaji','(b) Patna','(c) Gandhinagar','(d) Chandigarh'],['(a) Panaji','(b) Patna','(c) Gandhinagar','(d) Chandigarh'],['(a) Panaji','(b) Patna','(c) Gandhinagar','(d) Chandigarh'],
['(a) Panaji','(b) Patna','(c) Gandhinagar','(d) Chandigarh'],['(a) Jaipur','(b) Kolkata','(c) Delhi','(d) Dehradun'],['(a) Jaipur','(b) Kolkata','(c) Delhi','(d) Dehradun']]
answers=['(a) Delhi','(b) Dehradun','(c) Lucknow','(d) Maharashtra','(a) Panaji','(b) Patna','(c) Gandhinagar','(d) Chandigarh','(a) Jaipur','(b) Kolkata']
price=5000
num=0
print("--WELCOME TO THE KON BANEGA CROREPATI--")
print("--Lets Play The Game--")
playsound(r'C:\Users\Sanskar Kumar\Downloads\kbc-awesome-5410.mp3')
for i in range(0,10):
    playsound(r'C:\Users\Sanskar Kumar\Downloads\Kbc ! Question ! Sound Effect ! Notification.mp3')
    print("Your Question is on the screen")
    print(listq[i])
    print("Your Options are-")

    for j in range(0,4):
        print(lista[i][j]) 
    while True:
        a=input("Enter option :- ")
        if(a=='a'or a=="A"):
            
            num=0
            break
        elif(a=='b'or a=="B"):
            num=1
            break
        elif(a=='c'or a=="C"):
            num=2
            break
        elif(a=='d'or a=="D"):
            num=3
            break
    if(lista[i][num]==answers[i]):
        price=price*10
        print("You Won Rs ",price)

        playsound(r'C:\Users\Sanskar Kumar\Downloads\Kbc Correct Answer - Sound ! Notification.mp3')
    else:
        print(" You are Wrong ")
        playsound(r'C:\Users\Sanskar Kumar\Downloads\Kbc - Wrong Answer Sound.mp3')
       
        break
print("Your Total Winning Amount is Rs ",price,".")
playsound(r'C:\Users\Sanskar Kumar\Downloads\KBC - Audience Clapping.mp3')

