import requests
import pandas as pd
import time
from tqdm import tqdm
from statistics import mode, StatisticsError

cookies = {
    'connect.sid': 'COOKIE_GOES_HERE_FOR_PREMIUM_ROOMS',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.7',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
}

def get_completed_rooms(user_id, limit=20):
    rooms = []
    page = 1
    while True:
        url = f"https://tryhackme.com/api/v2/public-profile/completed-rooms?user={user_id}&limit={limit}&page={page}"
        response = requests.get(url, cookies=cookies, headers=headers)
        data = response.json()
        
        if not data['data']['docs']:
            break
        
        rooms.extend(data['data']['docs'])
        page += 1
        
        print(f"Fetched page {page-1}, total rooms so far: {len(rooms)}")
        time.sleep(2)
    
    return rooms

def get_room_points(room_code):
    url = f"https://tryhackme.com/api/v2/rooms/scoreboard?roomCode={room_code}&limit=100"
    response = requests.get(url, cookies=cookies, headers=headers)
    data = response.json()
    
    if data['status'] == 'success' and len(data['data']) > 1:
        scores = [user['score'] for user in data['data'] if user['score'] > 0]
        if scores:
            try:
                return mode(scores)  # Return the most common score
            except StatisticsError:
                # If there's no unique mode, return the maximum score
                return max(scores)
    return 0

def get_room_difficulty(room_code):
    url = f"https://tryhackme.com/api/v2/rooms/details?roomCode={room_code}"
    response = requests.get(url, cookies=cookies, headers=headers)
    data = response.json()
    
    if data['status'] == 'success':
        return data['data']['difficulty']
    return "Unknown"

def difficulty_color(difficulty):
    colors = {
        "info": "blue",
        "easy": "green",
        "medium": "orange",
        "hard": "red",
        "insane": "purple"
    }
    return colors.get(difficulty.lower(), "")

def main():
    user_id = "5e3595f110c4674ba9f80e7a"
    print("Fetching completed rooms...")
    rooms = get_completed_rooms(user_id)
    total_rooms = len(rooms)
    print(f"Total rooms found: {total_rooms}")
    
    results = []
    print("\nProcessing rooms and fetching points and difficulty...")
    for room in tqdm(rooms, total=total_rooms, desc="Progress"):
        room_code = room['code']
        room_name = room['title']
        room_url = f"https://tryhackme.com/room/{room_code}"
        points = get_room_points(room_code)
        difficulty = get_room_difficulty(room_code)
        
        results.append({
            "Room Name": room_name,
            "Room URL": room_url,
            "Points": points,
            "Difficulty": difficulty
        })
        
        tqdm.write(f"Processed {room_name} - Points: {points}, Difficulty: {difficulty}")
        time.sleep(2)  # Be nice to the API
    
    print("\nSorting results by points (highest to lowest)...")
    df = pd.DataFrame(results)
    df = df.sort_values(by='Points', ascending=False).reset_index(drop=True)
    
    print("Creating markdown table...")
    markdown_table = "| Room Name | Room URL | Points | Difficulty |\n"
    markdown_table += "|-----------|----------|--------|------------|\n"
    
    for _, row in df.iterrows():
        difficulty_formatted = f'<span style="color: {difficulty_color(row["Difficulty"])}">{row["Difficulty"]}</span>'
        markdown_table += f"| {row['Room Name']} | {row['Room URL']} | {row['Points']} | {difficulty_formatted} |\n"
    
    print("Saving results to file...")
    with open("room_points.md", "w") as f:
        f.write(markdown_table)
    
    print("Results saved to room_points.md")
    print(f"Total rooms processed: {total_rooms}")
    print(f"Total points: {sum(df['Points'])}")

if __name__ == "__main__":
    main()
