def money(bill,tip_perc):
    tip=(tip_perc/100)*bill
    total=bill+tip
    print("total bill is",total)
money(200,20)
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
n=int(input("please enter any number"))
print("the factorial of your number is",factorial(n))