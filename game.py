import random
import os

class NumberGuessingGame:
    """A fun number guessing game in Python"""
    
    def __init__(self, min_num=1, max_num=100):
        self.min_num = min_num
        self.max_num = max_num
        self.secret_number = random.randint(min_num, max_num)
        self.attempts = 0
        self.max_attempts = 10
        self.game_over = False
        self.player_won = False
        
    def display_welcome(self):
        """Display welcome message"""
        os.system('clear' if os.name == 'posix' else 'cls')
        print("=" * 50)
        print("🎮 WELCOME TO NUMBER GUESSING GAME 🎮")
        print("=" * 50)
        print(f"\nI'm thinking of a number between {self.min_num} and {self.max_num}")
        print(f"You have {self.max_attempts} attempts to guess it!")
        print("\n" + "=" * 50 + "\n")
    
    def get_player_guess(self):
        """Get and validate player's guess"""
        while True:
            try:
                guess = int(input(f"Attempt {self.attempts + 1}/{self.max_attempts} - Enter your guess: "))
                
                if guess < self.min_num or guess > self.max_num:
                    print(f"❌ Please enter a number between {self.min_num} and {self.max_num}!")
                    continue
                
                return guess
            except ValueError:
                print("❌ Invalid input! Please enter a valid number.")
    
    def check_guess(self, guess):
        """Check the guess and provide feedback"""
        self.attempts += 1
        
        if guess == self.secret_number:
            self.player_won = True
            self.game_over = True
            return "correct"
        elif guess < self.secret_number:
            return "too_low"
        else:
            return "too_high"
    
    def provide_feedback(self, result):
        """Provide feedback based on guess result"""
        if result == "correct":
            print(f"\n🎉 CONGRATULATIONS! You found it in {self.attempts} attempts!")
        elif result == "too_low":
            print(f"📈 The number is HIGHER than {guess}")
        elif result == "too_high":
            print(f"📉 The number is LOWER than {guess}")
    
    def check_game_over(self):
        """Check if game should end"""
        if self.attempts >= self.max_attempts and not self.player_won:
            self.game_over = True
            return True
        return False
    
    def display_game_over(self):
        """Display game over message"""
        print("\n" + "=" * 50)
        if self.player_won:
            print("🏆 YOU WIN! 🏆")
        else:
            print("💀 GAME OVER - YOU LOST! 💀")
            print(f"The number was: {self.secret_number}")
        print("=" * 50 + "\n")
    
    def play(self):
        """Main game loop"""
        self.display_welcome()
        
        while not self.game_over:
            guess = self.get_player_guess()
            result = self.check_guess(guess)
            self.provide_feedback(result)
            
            if result == "correct":
                self.game_over = True
            elif self.check_game_over():
                break
            else:
                remaining = self.max_attempts - self.attempts
                print(f"Remaining attempts: {remaining}\n")
        
        self.display_game_over()
    
    def play_again(self):
        """Ask player if they want to play again"""
        while True:
            choice = input("Do you want to play again? (yes/no): ").lower()
            if choice in ['yes', 'y']:
                return True
            elif choice in ['no', 'n']:
                return False
            else:
                print("❌ Invalid input! Please enter 'yes' or 'no'.")


def main():
    """Main function to run the game"""
    while True:
        game = NumberGuessingGame(1, 100)
        game.play()
        
        if not game.play_again():
            print("\n👋 Thanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()
