from tkinter import END


print("Welcome to the COVID 19 support service. Please select an option below")
print("1. Statistics\n2. Prevention\n3. Symptoms\n4. Treatment\n5. Report case\n6. Exit")
message=("Enter choice(1/2/3/4/5/6):")
print=(message)

statistics=input("Currently in SA there are 27403 confirmed cases\n Currently in USA there are 1700000 confirmed cases\n Currently in China there are 82995 confirmed cases\n Would you like to see the confirmed cases for a random country? y/n:")

x=str(input("Enter:"))
if x=="y":
    print("To select a random country, type a number from 0 to 9:")
elif x=="n":
    pass

x=0
while x != 9:
    x=int(input("Option:"))
    if x==0:
        print("Currently in Namibia there are 3467 confirmed cases")
    elif x==1:
        print("Currently in Mexico there are 451952 confirmed cases")
    elif x==2:
        print("Currently in Brazil there are 463218 confirmed cases")
    elif x==3:
        print("Currently in Peru there are 98097 confirmed cases")
    elif x==4:
        print("Currently in Argentina there are 126170 confirmed cases")
    elif x==5:
        print("Currently in Nigeria there are 3228 confirmed cases")
    elif x==6:
        print("Currently in Congo(Democratic Republic of the) there are 92 457 confirmed cases")
    elif x==7:
        print("Currently in Australia there are 7155 confirmed cases")
    elif x==8:
        print("Currently in Botswana there are 95 confirmed cases")
    elif x==9:
        print("Currently in Zimbabwe there are 258 confirmed cases")
    else:
        pass

prevention=input("To prevent the spread of COVID-19\n Clean your hands often. Use soap and water, or an alcohol-based hand rub.\n Maintain a safe distance from anyone who is coughing or sneezing\n Don't touch your eyes, nose or mouth\n Cover your nose or mouth with your bent elbow or a tissue when you cough or sneeze.\n Stay home if you feel unwell.\n If you have a fever, cough, and difficulty breathing, seek medical attention. Call in advance.\n Follow the directions of your local health authority.")

symptoms=input("Most common symptoms:\n Fever\n Dry cough\n Tiredness\n Less common symptoms:\n Aches and pains\n Sore throat\n Diarrhoea\n Conjuctivitis\n Headache\n Loss of taste or smell\n A rash on skin, or discolouration of fingers or toes\n Serious Symptoms:\n Difficulty breathing or shortness of breath\n Chest pain or pressure\n loss of speech or movement")

treatment=input("If you feel sick, you should rest, drink plenty of fluid, and eat nutritious food. Stay in a seperate room from other family members, and use a dedicated bathroom if possible. Clean and disinfect frequently touched surfaces.")

report_case=input("Do have any of the symptoms?y/n:")

x=0
while x != 0:
    x=int(input())
    if x==1:
        print(statistics)
    elif x==2:
        print(prevention)
    elif x==3:
        print(symptoms)
    elif x==4:
        print(treatment)
    elif x==5:
        print(report_case)
    else:
        END

