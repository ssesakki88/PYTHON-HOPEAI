class CallMultipleFunctions():
    def Subfields():
        fields=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Netural Language Processing"]
        print("Sub-fields in AI are:")
        for x in fields:
            print(x)
    def OddEven():
        num=int(input("Enter a number:"))
        if((num%2==1)):
            print(num,"is Odd Number")
        else:
            print(num,"is Even Number")
    def Elegible():
        Gender=input("Your Gender:")
        Age=int(input("Your Age:"))
        ELG='ELIGIBLE'
        NELG='NOT ELIGIBLE'

        if(Gender=="Male"):
            if(Age>=21):
                print(ELG)
            else:
                print(NELG)
        elif(Gender=="Female"):
            if(Age>=18):
                print(ELG)
            else:
                print(NELG)
        else:
            print('INVALID INPUT')
    def percentage():
        Sub1=int(input("Subject1="))
        Sub2=int(input("Subject2="))
        Sub3=int(input("Subject3="))
        Sub4=int(input("Subject4="))
        Sub5=int(input("Subject5="))
        Tot=Sub1+Sub2+Sub3+Sub4+Sub5
        print("Total:",Tot)
        Per=100*Tot/500
        print("Percentage :", Per)
    def triangle():
        h=int(input("Height:"))
        b=int(input("Breath:"))
        AOT=(h*b)/2
        print("Area of Triangle:",AOT)
        h1=int(input("Height1:"))
        h2=int(input("Height2:"))
        b1=int(input("Breath:"))
        perimeter=h1+h2+b1
        print("Perimeter of Triangle: ",perimeter)