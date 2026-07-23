def outer():
    print("Run outer...")


    def inner(num):
        print("Run inner...", num)

    return inner    


getInner=outer()    
getInner(33)