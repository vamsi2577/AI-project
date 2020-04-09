seats = []
for n in range(6):
    seats.append([0,0,0])

def displayBookings():
    print("all bookings")
    print("NOTE: '1' Indicates the seat is booked and '0' Indicates seat is empty")
    for row in seats:
        print(row)

def bookSeat():
    booked = False
    a= int(input("Enter your age:"))
    p=""
    while(p!="YES" and p!="NO"):
        p= input("are you physically-callenged(yes/no):").upper()
    
    if p == "YES":
        booked=str(bookSeatAtFront())
        if booked == "False":
            booked=str(bookSeatAtMiddle())
            if booked =="False":
                booked=str(bookSeatAtBack())
            elif booked =="True":
                bookagain()
        elif booked =="True":
            bookagain()
    elif p == "NO":
        if a>=50:
            booked=str(bookSeatAtFront())
            if booked == "False":
                booked=str(bookSeatAtMiddle())
                if booked =="False":
                    booked=str(bookSeatAtBack())
                elif booked =="True":
                    bookagain()
            elif booked =="True":
                bookagain()
        elif a<=49:
            booked=str(bookSeatAtMiddle())
            if booked == "False":
                booked=str(bookSeatAtFront())
                if booked == "False":
                    booked=str(bookSeatAtBack())
                elif booked =="True":
                    bookagain()
            elif booked =="True":
                bookagain()
    
    

def bookSeatAtFront():
    print("Booking seat at the front")
    for row in range(0,2):
        for column in range(0,3):
          if seats[row][column]==0:
            print("Booking seat...")
            print("Row: " + str(row) +" Column: "+ str(column))
            seats[row][column]=1
            print("We have now booked this seat for you.")
            #Stop Searching
            return True
        
    #We scanned the front seats without finding an empty seat:
    print("Sorry front seats are full")
    return False

def bookSeatAtMiddle():
    print("Booking seat at the middle")
    for row in range(2,4):
        for column in range(0,3):
            if seats[row][column]==0:
                print("Booking seat...")
                print("Row: " + str(row) +" Column: "+ str(column))
                seats[row][column]=1
                print("We have now booked this seat for you.")
                #Stop Searching
                return True
    #We scanned the front seats without finding an empty seat:
    print("Sorry middle seats are full")
    return False

def bookSeatAtBack():
    print("Booking seat at the back")
    for row in range(4,6):
        for column in range(0,3):
            if seats[row][column]==0:
                print("Booking seat...")
                print("Row: " + str(row) +" Column: "+ str(column))
                seats[row][column]=1
                print("We have now booked this seat for you.")
                #Stop Searching
                return True

    #We scanned the whole bus without finding an empty seat:
    print("Sorry the bus is full - Cannot make a booking")
    return False

def bookagain():
    r=""
    while(r!="YES" and r!="NO"):
        r= input("do you want to book another seat(yes/no):").upper()
    
    if r =="YES":
        bookSeat()
    else:
        displayBookings()
#the seats array is initialised by reading the content of the CSV file.
def loadBookings():
    file = open("seats.csv","r")
    row = 0
    for line in file:
        data = line.split(",")
        if len(data)==3:
            for column in range(0,3):
                seats[row][column] = int(data[column])
            row =row +1
    file.close()

#When the user exit the program , the content of the CSV file is replaced with the content of the seats array.
def saveBookings():
    file = open("seats.csv","w")
    r=""
    while(r!="YES" and r!="NO"):
        print("NOTE: Reset function deallocates all seats")
        r= input("do you want to reset the program data(yes/no):").upper()
        if r =="YES":
            reset()
        elif r =="NO":
            for row in range(0,6):
                line=""
                for column in range(0,3):
                    line = line + str(seats[row][column]) + ","
                line = line[:-1] + ("\n") #Remove last comma and add a new line
                file.write(line)    
            file.close()

#To reset the program overwrite all the bookings to 0
def reset():
    file = open("seats.csv","w")
    for row in range(0,6):
        line=""
        for column in range(0,3):
            seats[row][column]=0
            line = line + str(seats[row][column]) +","
        line = line[:-1]+("\n")
        file.write(line)
    file.close()
    displayBookings()
    
    
    
loadBookings()
bookSeat()
saveBookings()


