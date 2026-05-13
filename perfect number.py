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
        print("\n Analyzing...\n")
        l = divisors(num)
        for i in l:
            s = i+s
        if num == s or num == s/2:
            print(f"  >  {num} is perfect")
        else :
            print(f"  >  {num} is not perfect")
            

    perfectnum(int(input('num:\n  >  ')))
    print()
