import requests
import pandas as pd
import time
from tqdm import tqdm

def get_completed_rooms(user_id, limit=20):
    rooms = []
    page = 1
    while True:
        url = f"https://tryhackme.com/api/v2/public-profile/completed-rooms?user={user_id}&limit={limit}&page={page}"
        response = requests.get(url)
        data = response.json()
        
        if not data['data']['docs']:
            break
        
        rooms.extend(data['data']['docs'])
        page += 1
        
        print(f"Fetched page {page-1}, total rooms so far: {len(rooms)}")
        time.sleep(2)
    
    return rooms

def get_room_points(room_code):
    url = f"https://tryhackme.com/api/v2/rooms/scoreboard?roomCode={room_code}&limit=10"
    response = requests.get(url)
    data = response.json()
    
    if data['status'] == 'success' and len(data['data']) > 1:
        return data['data'][1]['score']  # Use the second user's score
    return 0

def main():
    user_id = "5e3595f110c4674ba9f80e7a"
    print("Fetching completed rooms...")
    rooms = get_completed_rooms(user_id)
    total_rooms = len(rooms)
    print(f"Total rooms found: {total_rooms}")
    
    results = []
    print("\nProcessing rooms and fetching points...")
    for room in tqdm(rooms, total=total_rooms, desc="Progress"):
        room_code = room['code']
        room_name = room['title']
        room_url = f"https://tryhackme.com/room/{room_code}"
        points = get_room_points(room_code)
        
        results.append({
            "Room Name": room_name,
            "Room URL": room_url,
            "Points": points
        })
        
        tqdm.write(f"Processed {room_name} - Points: {points}")
        time.sleep(2)  # Be nice to the API
    
    print("\nSorting results by points (highest to lowest)...")
    df = pd.DataFrame(results)
    df = df.sort_values(by='Points', ascending=False).reset_index(drop=True)
    
    print("Creating markdown table...")
    markdown_table = df.to_markdown(index=False)
    
    print("Saving results to file...")
    with open("room_points.md", "w") as f:
        f.write(markdown_table)
    
    print("Results saved to room_points.md")
    print(f"Total rooms processed: {total_rooms}")
    print(f"Total points: {sum(df['Points'])}")

if __name__ == "__main__":
    main()
