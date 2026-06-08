# Create a class and function, and a list out the items in the list
class SubFieldInAI():
    def SubFields():
        subFieldList=["Machine Learning","Neural Networks","Vison","Robotics","Speech Processing","Natural Language Processing"]
        print("Sub-Field in AI are:")
        [print(aiName) for aiName in subFieldList] #List comprehensive loop 

# Create a class and function that check whether the given number is odd or even
class OddEven():
    def oddEvenCheck():
        print("I tell you whether the given number is Odd or Even.")
        num=int(input("Enter your Number here:"))
        if(num%2==0):
            print(f"The given number {num} is Even")
        else:
            print(f"The given number {num} is Odd")

# Create a class and function that check based on your gender whether the given age is eligible for marriage or not
class EligibilityForMarriage():
    def checkMarriageEligibility():
        gender=input("Enter your gender Male/Female :")
        age=int(input("Enter your age: "))
        if((gender=="Male")&(age>=21)):
            print(f"Your age is {age}, so you're eligible for marriage")
        elif((gender=="Female")&(age>=18)):
            print(f"Your age is {age}, so you're eligible for marriage")
        else:
            print(f"Your age is {age}, so you're note eligible for marriage")
            
#Calculate the percentage of 10th Marks
class FindPercent():
    def percentange():
        tamil=int(input("Enter your Tamil marks : "))
        english=int(input("Enter your English marks : "))
        maths=int(input("Enter your Maths marks : "))
        socialScience=int(input("Enter your Social Science marks : "))
        science=int(input("Enter your Science marks : "))
        total=(tamil+english+maths+socialScience+science)
        avg=float(total/5)
        print(f"Total marks obtained out of 500 is : {total}")
        print(f"Percentage obtained out of 100 is: {avg:.2f}")

#print area and perimeter of triangle using class and function
class Triangle():
    def triangle():
        height=int(input("Enter the Area of Height value : "))
        breadth=int(input("Enter the Area of Breadth value : "))
        triangle=float((height*breadth)/2)
        print(f"The area of Triangle is {triangle}")
        height1=int(input("Enter the Area of Height1 value : "));
        height2=int(input("Enter the Area of Height2 value : "));
        p_breadth=int(input("Enter the Perimeter of Breadth value : "));
        perimeter=height1+height2+p_breadth;
        print(f"The area of perimeter value is {perimeter}")
        