import asyncio


# Define a coroutine that simulates a time-consuming task 
async def fetch_data(delay):
    print("Fetching data...")
    await asyncio.sleep(delay)  #simulate and I/O operation with sleep
    print("Data fetched")
    return {"data":"Some Data"}  #Return Some data


# coroutine function
# Define another coroutine that calls the first coroutine
async def main():
    print("Start of main coroutine")
    task=fetch_data(2)
    # Await the fetch_data coroutine, pausing execution of main until fetch_data completes
    result=await task
    print(f"Received result: {result}")
    print("End of the main coroutine")

# main() -> coroutine object. that coruoutine object needs to be awaited in order to executed

# ***********************************************************************************************

# another example 
# Define a coroutine that simulates a time-consuming task
async def fetch_data(delay, id):
    print("Fetching data... id:", id)
    await asyncio.sleep(delay)  # Simulate an I/O operation with a sleep
    print("Data fetched, id:", id)
    return {"data": "Some data", "id": id}  # Return some data


# Define another coroutine that calls the first coroutine
async def main():
    task1 = fetch_data(2, 1)
    task2 = fetch_data(2, 2)

    result1 = await task1  #await wait for the tast1 to be execute then it's go the next
    print(f"Received result: {result1}")

    result2 = await task2
    print(f"Received result: {result2}")

# Run the coroutine     
asyncio.run(main())