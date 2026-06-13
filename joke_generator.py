import requests
import json
from typing import Dict, Optional

class JokeGenerator:
    """A class to fetch and display random jokes from an external API"""
    
    # Using the official Joke API - no authentication required
    BASE_URL = "https://official-joke-api.appspot.com"
    
    @staticmethod
    def get_random_joke() -> Optional[Dict]:
        """
        Fetch a random joke from the Joke API
        
        Returns:
            dict: Contains joke type, setup, and punchline
            None: If the request fails
        """
        try:
            endpoint = f"{JokeGenerator.BASE_URL}/random_joke"
            response = requests.get(endpoint, timeout=5)
            
            # Check if request was successful
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Error: API returned status code {response.status_code}")
                return None
                
        except requests.exceptions.Timeout:
            print("Error: Request timed out. Please try again.")
            return None
        except requests.exceptions.ConnectionError:
            print("Error: Failed to connect to the API. Check your internet connection.")
            return None
        except requests.exceptions.RequestException as e:
            print(f"Error: An error occurred while fetching the joke: {e}")
            return None
    
    @staticmethod
    def get_joke_by_type(joke_type: str = "general") -> Optional[Dict]:
        """
        Fetch a random joke of a specific type
        
        Args:
            joke_type (str): Type of joke - 'general' or 'knock-knock'
        
        Returns:
            dict: Contains joke details
            None: If the request fails
        """
        try:
            endpoint = f"{JokeGenerator.BASE_URL}/jokes/{joke_type}/random"
            response = requests.get(endpoint, timeout=5)
            
            if response.status_code == 200:
                joke_data = response.json()
                # Handle case where response is a list
                if isinstance(joke_data, list):
                    return joke_data[0] if joke_data else None
                return joke_data
            else:
                print(f"Error: API returned status code {response.status_code}")
                return None
                
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None
    
    @staticmethod
    def display_joke(joke_data: Dict) -> None:
        """
        Display a joke in a formatted way
        
        Args:
            joke_data (dict): Joke data from the API
        """
        if not joke_data:
            return
        
        print("\n" + "="*60)
        print("😂 HERE'S YOUR JOKE:")
        print("="*60)
        
        if "setup" in joke_data and "punchline" in joke_data:
            print(f"\n{joke_data['setup']}")
            print(f"\n{joke_data['punchline']}")
        elif "joke" in joke_data:
            print(f"\n{joke_data['joke']}")
        
        if "type" in joke_data:
            print(f"\n[Type: {joke_data['type'].title()}]")
        
        print("\n" + "="*60 + "\n")
    
    @staticmethod
    def get_multiple_jokes(count: int = 5) -> list:
        """
        Fetch multiple random jokes
        
        Args:
            count (int): Number of jokes to fetch
        
        Returns:
            list: List of joke dictionaries
        """
        try:
            endpoint = f"{JokeGenerator.BASE_URL}/jokes/random/{count}"
            response = requests.get(endpoint, timeout=10)
            
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Error: API returned status code {response.status_code}")
                return []
                
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return []


def main():
    """Main function to run the joke generator"""
    print("\n" + "="*60)
    print("🎭 WELCOME TO THE RANDOM JOKE GENERATOR! 🎭")
    print("="*60)
    
    while True:
        print("\nOptions:")
        print("1. Get a random joke")
        print("2. Get a specific type of joke (general or knock-knock)")
        print("3. Get multiple jokes")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            print("\nFetching a random joke...")
            joke = JokeGenerator.get_random_joke()
            JokeGenerator.display_joke(joke)
        
        elif choice == "2":
            print("\nAvailable types: 'general', 'knock-knock'")
            joke_type = input("Enter joke type: ").strip().lower()
            
            if joke_type not in ["general", "knock-knock"]:
                print("Invalid type! Please choose 'general' or 'knock-knock'")
                continue
            
            print(f"\nFetching a {joke_type} joke...")
            joke = JokeGenerator.get_joke_by_type(joke_type)
            JokeGenerator.display_joke(joke)
        
        elif choice == "3":
            try:
                count = int(input("How many jokes do you want? (1-10): ").strip())
                if count < 1 or count > 10:
                    print("Please enter a number between 1 and 10")
                    continue
                
                print(f"\nFetching {count} jokes...")
                jokes = JokeGenerator.get_multiple_jokes(count)
                
                for i, joke in enumerate(jokes, 1):
                    print(f"\n--- Joke {i} ---")
                    JokeGenerator.display_joke(joke)
            
            except ValueError:
                print("Invalid input! Please enter a number.")
        
        elif choice == "4":
            print("\n🎭 Thanks for using the Joke Generator! Have a great day! 🎭\n")
            break
        
        else:
            print("Invalid choice! Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    # Check if requests library is installed
    try:
        import requests
    except ImportError:
        print("Error: The 'requests' library is not installed.")
        print("Please install it using: pip install requests")
        exit(1)
    
    main()
