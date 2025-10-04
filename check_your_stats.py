import requests
import re
from collections import namedtuple
import time
import json
import argparse
import sys
from colorama import init, Fore, Back, Style
import os
from tabulate import tabulate

# Initialize colorama
init()

# Define a named tuple to store room information
Room = namedtuple('Room', ['name', 'url', 'points', 'difficulty'])

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    """Print an animated ASCII art banner."""
    banner = f"""
{Fore.RED}████████╗██╗  ██╗███╗   ███╗{Fore.WHITE} ███████╗ ██████╗██████╗  █████╗ ██████╗ ███████╗██████╗ 
{Fore.RED}╚══██╔══╝██║  ██║████╗ ████║{Fore.WHITE} ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
{Fore.RED}   ██║   ███████║██╔████╔██║{Fore.WHITE} ███████╗██║     ██████╔╝███████║██████╔╝█████╗  ██████╔╝
{Fore.RED}   ██║   ██╔══██║██║╚██╔╝██║{Fore.WHITE} ╚════██║██║     ██╔══██╗██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗
{Fore.RED}   ██║   ██║  ██║██║ ╚═╝ ██║{Fore.WHITE} ███████║╚██████╗██║  ██║██║  ██║██║     ███████╗██║  ██║
{Fore.RED}   ╚═╝   ╚═╝  ╚═╝╚═╝     ╚═╝{Fore.WHITE} ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝
    """
    
    loading_messages = [
        f"{Fore.CYAN}Initializing TryHackMe scraper...",
        f"{Fore.YELLOW}Preparing for room analysis...",
        f"{Fore.GREEN}Loading room database...",
        f"{Fore.MAGENTA}Starting up..."
    ]
    
    # Animated banner display
    clear_screen()
    for line in banner.split('\n'):
        print(line)
        time.sleep(0.1)
    
    # Loading animation
    for msg in loading_messages:
        print(f"\r{msg}", end='')
        time.sleep(0.5)
        sys.stdout.flush()
    
    print(f"\n\n{Fore.CYAN}Ready to analyze TryHackMe rooms!{Style.RESET_ALL}\n")
    time.sleep(0.5)

def fetch_raw_data(url):
    """Fetch raw data from a URL with error handling and retries."""
    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            if attempt == max_retries - 1:
                raise Exception(f"Failed to fetch data after {max_retries} attempts: {str(e)}")
            time.sleep(2 ** attempt)  # Exponential backoff

def parse_rooms(raw_data):
    """Parse room information from markdown table format."""
    rooms = []
    # Find the start of the room table
    table_start = raw_data.find("| Room Name | Room URL | Points | Difficulty |")
    if table_start == -1:
        raise Exception("Room table not found in the README")
    
    # Extract the table content
    table_content = raw_data[table_start:]
    
    # Parse the table with improved regex pattern
    pattern = r'\|\s*([^|]+?)\s*\|\s*(https://tryhackme\.com/room/[^|\s]+)\s*\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|'
    matches = re.findall(pattern, table_content)
    
    for match in matches:
        name, url, points, difficulty = match
        rooms.append(Room(
            name=name.strip(),
            url=url.strip(),
            points=int(points),
            difficulty=difficulty.strip()
        ))
    
    return rooms

def get_completed_rooms(user_id, limit=20):
    """Fetch completed rooms for a user with rate limiting and progress tracking."""
    rooms = []
    page = 1
    total_rooms = 0
    
    while True:
        url = f"https://tryhackme.com/api/v2/public-profile/completed-rooms?user={user_id}&limit={limit}&page={page}"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            current_rooms = data['data']['docs']
            if not current_rooms:
                break
            
            rooms.extend(current_rooms)
            total_rooms = len(rooms)
            print(f"{Fore.GREEN}Fetched page {page}, total rooms: {total_rooms}{Style.RESET_ALL}")
            
            page += 1
            time.sleep(2)  # Rate limiting
            
        except (requests.exceptions.RequestException, json.JSONDecodeError) as e:
            print(f"{Fore.RED}Error fetching page {page}: {str(e)}{Style.RESET_ALL}")
            time.sleep(5)  # Wait longer on error
            continue
    
    return rooms

def generate_table_data(rooms):
    """Convert room data to table format."""
    headers = ["Room Name", "URL", "Points", "Difficulty"]
    table_data = [[room.name, room.url, room.points, room.difficulty] for room in rooms]
    return headers, table_data

def save_results(completed_rooms, uncompleted_rooms, total_points_gained):
    """Save results to files in tabulated format."""
    # Prepare tables
    completed_headers, completed_data = generate_table_data(completed_rooms)
    uncompleted_headers, uncompleted_data = generate_table_data(uncompleted_rooms)
    
    # Calculate statistics
    potential_points = sum(room.points for room in uncompleted_rooms)
    stats_data = [
        ["Total Completed Rooms", len(completed_rooms)],
        ["Total Points Gained", total_points_gained],
        ["Remaining Rooms", len(uncompleted_rooms)],
        ["Potential Points Available", potential_points]
    ]
    
    # Top 5 rooms table
    top_5_rooms = sorted(uncompleted_rooms, key=lambda x: x.points, reverse=True)[:5]
    top_5_headers, top_5_data = generate_table_data(top_5_rooms)
    
    # Save completed rooms
    with open('completed_rooms.txt', 'w', encoding='utf-8') as f:
        f.write("Completed Rooms Summary\n")
        f.write("=" * 100 + "\n\n")
        
        # Write statistics
        f.write("Statistics\n")
        f.write("-" * 50 + "\n")
        f.write(tabulate(
            [["Total Rooms", len(completed_rooms)],
             ["Total Points", total_points_gained]],
            tablefmt="grid"
        ))
        f.write("\n\n")
        
        # Write completed rooms table
        f.write("Completed Rooms Detail\n")
        f.write("-" * 50 + "\n")
        f.write(tabulate(completed_data, 
                        headers=completed_headers,
                        tablefmt="grid"))
    
    # Save rooms to complete
    with open('rooms_to_complete.txt', 'w', encoding='utf-8') as f:
        f.write("Rooms To Complete Summary\n")
        f.write("=" * 100 + "\n\n")
        
        # Write statistics
        f.write("Current Progress\n")
        f.write("-" * 50 + "\n")
        f.write(tabulate(stats_data,
                        headers=["Metric", "Value"],
                        tablefmt="grid"))
        f.write("\n\n")
        
        # Write top 5 rooms table
        f.write("Top 5 High-Point Rooms to Complete\n")
        f.write("-" * 50 + "\n")
        f.write(tabulate(top_5_data,
                        headers=top_5_headers,
                        tablefmt="grid"))
        f.write("\n\n")
        
        # Write all uncompleted rooms table
        f.write("All Remaining Rooms\n")
        f.write("-" * 50 + "\n")
        f.write(tabulate(uncompleted_data,
                        headers=uncompleted_headers,
                        tablefmt="grid"))

def main(user_id):
    """Main function to process TryHackMe room data."""
    try:
        print_banner()
        
        # Fetch and parse room data from GitHub
        github_url = "https://raw.githubusercontent.com/pentestfunctions/thm-room-points/refs/heads/main/README.md"
        print(f"{Fore.CYAN}Fetching room data from GitHub...{Style.RESET_ALL}")
        raw_data = fetch_raw_data(github_url)
        all_rooms = parse_rooms(raw_data)
        print(f"{Fore.GREEN}Found {len(all_rooms)} total rooms{Style.RESET_ALL}")
        
        # Get user's completed rooms
        print(f"\n{Fore.CYAN}Fetching completed rooms for user {user_id}...{Style.RESET_ALL}")
        completed_rooms_data = get_completed_rooms(user_id)
        print(f"{Fore.GREEN}Total completed rooms: {len(completed_rooms_data)}{Style.RESET_ALL}")
        
        # Create a set of completed room codes
        completed_room_codes = set(room['code'] for room in completed_rooms_data)
        
        # Separate completed and uncompleted rooms
        completed = []
        uncompleted = []
        total_points_gained = 0
        
        for room in all_rooms:
            room_code = room.url.split('/')[-1]
            if room_code in completed_room_codes:
                completed.append(room)
                total_points_gained += room.points
            else:
                uncompleted.append(room)
        
        # Sort rooms by points
        uncompleted.sort(key=lambda x: x.points, reverse=True)
        completed.sort(key=lambda x: x.points, reverse=True)
        
        # Save results in tabulated format
        save_results(completed, uncompleted, total_points_gained)
        
        # Display summary in console
        print(f"\n{Fore.GREEN}Analysis complete!{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Results written to 'completed_rooms.txt' and 'rooms_to_complete.txt'{Style.RESET_ALL}")
        
        # Display quick summary
        print(f"\n{Fore.YELLOW}Quick Summary:{Style.RESET_ALL}")
        stats = [
            ["Total Completed Rooms", len(completed)],
            ["Total Points Gained", total_points_gained],
            ["Remaining Rooms", len(uncompleted)],
            ["Potential Points Available", sum(room.points for room in uncompleted)]
        ]
        print(tabulate(stats, headers=["Metric", "Value"], tablefmt="grid"))
        
    except Exception as e:
        print(f"{Fore.RED}An error occurred: {str(e)}{Style.RESET_ALL}")
        raise

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="TryHackMe Room Data Scraper and Analyzer")
    parser.add_argument("user_id", help="TryHackMe user ID hash")
    args = parser.parse_args()
    
    main(args.user_id)
