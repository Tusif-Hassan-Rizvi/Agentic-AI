import asyncio

# A shared variable
shared_resource = 0

# An asyncio Lock
lock = asyncio.Lock()


async def modify_shared_resource():
    global shared_resource
    async with lock:
        # Critical section starts
        print(f"Resource before modification: {shared_resource}")
        shared_resource += 1  # Modify the shared resource
        await asyncio.sleep(1)  # Simulate an IO operation
        print(f"Resource after modification: {shared_resource}")
        # Critical section ends


async def access_resource(semaphore, resource_id):
    async with semaphore:
        # Simulate accessing a limited resource
        print(f"Accessing resource {resource_id}")
        await asyncio.sleep(1)  # Simulate work with the resource
        print(f"Releasing resource {resource_id}")


# events         

async def waiter(event):
    print("waiting for the event to be set")
    await event.wait()
    print("event has been set, continuing execution")

async def setter(event):
    await asyncio.sleep(2)  # Simulate doing some work
    event.set()
    print("event has been set!")

     

async def main():
    # await asyncio.gather(*(modify_shared_resource() for _ in range(5)))

    # semaphore 
    # semaphore = asyncio.Semaphore(2)  # Allow 2 concurrent accesses
    # await asyncio.gather(*(access_resource(semaphore, i) for i in range(5)))   

    # event 
    event = asyncio.Event()
    await asyncio.gather(waiter(event), setter(event))



asyncio.run(main())