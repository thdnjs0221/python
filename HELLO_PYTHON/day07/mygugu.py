#9 2 
#


#
# for i in range(9,2,-1):
#     if i%2==0:
#         for j in range(1,9+1):
#             print(i,"*",j,"=",i*j )
#
def showdan(dan):
    print("{}*{}={}".format(dan,1,1*dan))
    print("{}*{}={}".format(dan,2,2*dan))
    print("{}*{}={}".format(dan,3,3*dan))
    print("{}*{}={}".format(dan,5,5*dan))
    print("{}*{}={}".format(dan,6,6*dan))
    print("{}*{}={}".format(dan,7,7*dan))
    print("{}*{}={}".format(dan,8,8*dan))
    print("{}*{}={}".format(dan,9,9*dan))
    
showdan(2)
showdan(3)
showdan(4)
showdan(5)
showdan(6)
showdan(7)
showdan(8)
showdan(9)

