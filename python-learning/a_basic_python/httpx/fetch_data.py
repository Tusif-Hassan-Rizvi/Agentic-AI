import asyncio
import httpx

# BASE URL for testing API calls
BASE_URL = "https://jsonplaceholder.typicode.com/posts"


# 1. GET Request (with Query Parameters)
async def get_example(client):
    print("--- 1. GET Request ---")
    response = await client.get(BASE_URL, params={"userId": 1})
    print("Status Code:", response.status_code)
    print("First Post Title:", response.json()[0]["title"])
    print()


# 2. POST Request (Sending JSON Body)
async def post_example(client):
    print("--- 2. POST Request ---")
    payload = {
        "title": "Agentic AI Engineering",
        "body": "Building multi-agent systems with FastAPI and LangGraph",
        "userId": 1
    }
    response = await client.post(BASE_URL, json=payload)
    print("Status Code:", response.status_code)
    print("Created Object ID:", response.json()["id"])
    print()


# 3. PUT Request (Complete Resource Update)
async def put_example(client):
    print("--- 3. PUT Request ---")
    updated_payload = {
        "id": 1,
        "title": "Updated Title via PUT",
        "body": "Replaced entire post content",
        "userId": 1
    }
    response = await client.put(f"{BASE_URL}/1", json=updated_payload)
    print("Status Code:", response.status_code)
    print("Updated Title:", response.json()["title"])
    print()


# 4. PATCH Request (Partial Resource Update)
async def patch_example(client):
    print("--- 4. PATCH Request ---")
    patch_payload = {"title": "Only Updated Title via PATCH"}
    response = await client.patch(f"{BASE_URL}/1", json=patch_payload)
    print("Status Code:", response.status_code)
    print("Patched Title:", response.json()["title"])
    print()


# 5. DELETE Request (Remove Resource)
async def delete_example(client):
    print("--- 5. DELETE Request ---")
    response = await client.delete(f"{BASE_URL}/1")
    print("Status Code:", response.status_code)
    print("Delete Finished!")
    print()


# 6. Error Handling & Timeouts
async def error_handling_example(client):
    print("--- 6. Error Handling & Timeouts ---")
    try:
        response = await client.get(f"{BASE_URL}/999999")
        response.raise_for_status()  # Raises exception if status is 4xx or 5xx
    except httpx.HTTPStatusError as exc:
        print(f"Caught HTTP Error! Status Code: {exc.response.status_code}")
    print()


# 7. Concurrent Requests (Fetching Multiple URLs simultaneously)
async def concurrent_fetch_example(client):
    print("--- 7. Concurrent Requests (asyncio.gather) ---")
    urls = [f"{BASE_URL}/{i}" for i in range(1, 4)]  # Posts 1, 2, and 3
    
    # Create 3 async fetch tasks
    tasks = [client.get(url) for url in urls]
    
    # Fire all 3 requests concurrently
    responses = await asyncio.gather(*tasks)
    
    for idx, resp in enumerate(responses, start=1):
        print(f"Post #{idx} Title: {resp.json()['title']}")
    print()


# Main Entry Point reusing a single AsyncClient session
async def main():
    # Recommended: Re-use 1 AsyncClient session for all requests
    async with httpx.AsyncClient(timeout=10.0) as client:
        await get_example(client)
        await post_example(client)
        await put_example(client)
        await patch_example(client)
        await delete_example(client)
        await error_handling_example(client)
        await concurrent_fetch_example(client)


if __name__ == "__main__":
    asyncio.run(main())