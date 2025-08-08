import time

def main():
    while True:
        request = input("(q for quit) Enter the time of countdown: ").strip().lower()
        
        if request == "q":
            print("Quitting")
            quit()
        
        try:
            request = int(request)
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        while request > 0:
            print(request)
            request -= 1
            time.sleep(1)
        
        print("Time's up.")

main()
