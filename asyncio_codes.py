import asyncio

async def greet(name):
    print(f"Hello, {name}!")
    await asyncio.sleep(1)
    print(f"Goodbye, {name}!")
#asyncio.run(greet("Alice"))

async def main():
    await asyncio.gather(
        greet("Alice"),
        greet("Bob"),
        greet("Charlie")
    )

if __name__ == "__main__":
    asyncio.run(main())

#outputs:
#Hello, Alice!
#Hello, Bob!        
#Hello, Charlie!
#Goodbye, Alice!        
#Goodbye, Bob!
#Goodbye, Charlie!
