import json
import asyncio

async def read_file(file_path,order):
    try:
        with open(file_path) as fs:
            file_content = json.load(fs)
        
            suffix = {1: "st", 2: "nd", 3: "rd"}.get(order, "th")
            print(f"{order}{suffix} file")

            for item in file_content:
                user_id = item.get("user_id","N/A")
                username = item.get("name","N/A")
                user_age = item.get("age","N/A")
                user_email = item.get("email","N/A")
                user_purcases = item.get("purchases","N/A")

                
                print(f"\nuser's id is {user_id}")
                print(f"username is {username}")
                print(f"user's age is {user_age}") 
                print(f"user's email is {user_email}")
                print(f"user's purchase(s) is/are {user_purcases}")
                print("-"*30)

    except FileNotFoundError:
        print(f"Error: {file_path} not found")
    
    except json.JSONDecodeError:
        print(f"Error: {file_path} is invalid json file")
    

async def main():
    await asyncio.gather(
        
        read_file("user_data1.json",1),
        read_file("user_data2.json",2),
        read_file("user_data3.json",3)
        
        )

if __name__ == "__main__":
    asyncio.run(main())