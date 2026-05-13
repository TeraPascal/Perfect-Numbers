import datetime
while True:
    def divisors(num):
        l=[]
        for i in range(num):
            i = i+1
            r = num%i
            if r == 0 :
                l.append(i)
        return(l)

    def perfectnum(num):
        s = 0
        #print("\n Analyzing...\n")
        l = divisors(num)
        #print(l)
        for i in l:
            s = i+s
        #print(s)
        if num == s or num == s/2:
            print(datetime.datetime.now(),f"\n  {num} is perfect\n")
            
    limit = int(input("maximum num ..\n"))

    for n in range(limit):
        n = n+1
        perfectnum(n)
    print("done.")
