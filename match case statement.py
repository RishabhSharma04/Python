# x = int(input("Enter any number > "))
# match x :
#     case 0:
#         print ("x is zero")
#     case 5:
#         print ("x is five")
#     case _ if x != 10:
#             print ("x is not 10")
#     case _ :
#         print ("end")

print ("1.BJP\n2.AAP\n3.INC")
vote = input("Do you want to vote :\t");
match vote :
    # print("Whom you want to vote : ")
    # print ("1.BJP\n2.AAP\n3.INC")
    case 1:
        print ("Bharat Mahaan Banega")
    case 2: 
        print ("Bharat galat haato mein chala gaya hai")
    case 3:
        print ("Bharat ko inse koi toh bachao")
    case _ :
        print ("Thanks for not voting")