def start_game():
    playing = True

    while playing:
        fuel = 100
        lives = 3

        print("\nWelcome to the Jungle Adventure!")
        print("You are an explorer in search of a lost treasure hidden deep inside the ancient jungle.")
        print("Be careful! You have limited fuel and only 3 lives.")
        
        while lives > 0:
            print(f"\nFuel remaining: {fuel}")
            print(f"Lives remaining: {lives}\n")

            print("You arrive at the edge of the jungle with your jeep.")
            print("You can either go 'left' into the dense forest trail or 'right' onto the rocky hill path.")
            choice1 = input("Which direction do you want to go? (left/right): ").lower()
            fuel -= 10

            if choice1 == "left":
                print("\nYou take the narrow trail into the forest. It's quiet and a bit creepy.")
                print("Soon, you come to a fork in the trail.")
                print("Option 1: Climb an ancient tree to get a better view. (-20 fuel)")
                print("Option 2: Cross an old bridge over a river. (-30 fuel)")
                choice2 = input("What will you do? (1/2): ")

                if choice2 == "1":
                    fuel -= 20
                    lives -= 1
                    print("\nYou try to climb the tree, but the branch breaks.")
                    print("You fall into a hidden pothole.")
                    print("You lost a life!")
                elif choice2 == "2":
                    fuel -= 30
                    lives -= 1
                    print("\nYou attempt to cross the old bridge.")
                    print("It collapses, and you fall into a hidden well.")
                    print("You lost a life!")
                else:
                    lives -= 1
                    print("\nInvalid choice. You wander in the jungle and get nowhere.")
                    print("You lost a life!")

            elif choice1 == "right":
                print("\nYou take the rocky hill path. It's steep but manageable.")
                print("After a while, you find two more paths ahead.")
                print("Option 1: Enter a dark cave. (-25 fuel)")
                print("Option 2: Follow a glowing trail that seems promising. (-10 fuel)")
                choice3 = input("What will you do? (1/2): ")

                if choice3 == "1":
                    fuel -= 25
                    lives -= 1
                    print("\nYou step into the cave, but the entrance collapses behind you.")
                    print("You are trapped and can't get out.")
                    print("You lost a life!")
                elif choice3 == "2":
                    fuel -= 10
                    print("\nYou follow the glowing trail, and it leads you to a hidden temple.")
                    print("Inside, you find the legendary treasure chest.")
                    print("Congratulations! You found the treasure and won the game!")
                    print(f"You finished with {fuel} fuel remaining and {lives} lives.")
                    break
                else:
                    lives -= 1
                    print("\nInvalid choice. You get lost and eventually run out of time.")
                    print("You lost a life!")

            else:
                lives -= 1
                print("\nInvalid direction. You drive off the path and waste fuel.")
                print("You lost a life!")

            if fuel <= 0:
                print("\nYou've run out of fuel. You're stranded in the jungle.")
                print("Game Over.")
                break

            if lives == 0:
                print("\nYou've run out of lives. The jungle adventure ends here.")
                print("Game Over.")

        # restart
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            playing = False
            print("\nThanks for playing Jungle Adventure. Goodbye!")

# Start the game
start_game()
