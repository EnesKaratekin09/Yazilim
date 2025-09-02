def main():
    while True:
        f_numb=input("Enter first number: ").strip()
        try:
            numb=float(f_numb)
            break
        except ValueError:
            print("Please enter a valid number!")
            continue
    while True:
        op=input("Choose an operator(+,-,/,x): ").strip()
        if op=="+" or op=="-" or op=="/" or op=="x":
            break
        else:
            print("Please choose an valid operator!")
            continue
    while True:
        s_numb=input("Enter second number: ").strip()
        try:
            numb=float(s_numb)
            break
        except ValueError:
            print("Please enter a valid number!")
            continue
    def print_result(x,o,y):
        if o=="+":
            print(f"{x} + {y} = ",float(x)+float(y))
        elif o=="-":
            print(f"{x} - {y} = ",float(x)-float(y))
        elif o=="/":
            print(f"{x} / {y} = ",float(x)/float(y))
        elif o=="x":
            print(f"{x} x {y} = ",float(x)*float(y))
    print_result(f_numb,op,s_numb)
    main()
main()
