import asyncio


async def fetch_data(id, sleep_time):
    print(f"Coroutine {id} starting to fetch data.")
    await asyncio.sleep(sleep_time)  #simulate a network request or IO operation
    return {"id":id,"data":f"Sample data from the coroutine {id}"}


async def main():     
    #Create tasks for running coroutines concurrently

    # task1=asyncio.create_task(fetch_data(1,2))
    # task2=asyncio.create_task(fetch_data(2,3))
    # task3=asyncio.create_task(fetch_data(3,1))


    # result1=await task1
    # result2=await task2
    # result3=await task3

    # print(result1, result2, result3)


    # asyncio.gather: !not good in error handling 
    # Run coroutine concurrently and gather their return value 
    # results=await asyncio.gather(fetch_data(1,2), fetch_data(2,1), fetch_data(3,3))
    # Gather function is a quick way to concurrently run multiple coroutine


    # process the results 
    # for result in results:
    #     print(f"Received results: {result}")


    # taskGroup function: provides built in error handling
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for i, sleep_time in enumerate([2, 1, 3], start=1):
            task = tg.create_task(fetch_data(i, sleep_time))
            tasks.append(task)

    # After the Task Group block, all tasks have completed
    results = [task.result() for task in tasks]

    for result in results:
        print(f"Received result: {result}")    





asyncio.run(main())
