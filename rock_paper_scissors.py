from random import choice


class RockPaperScissor:
    """ Overall class to manage Rock, Paper, scissors game"""

    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
        self.game_active = True

    def run_game(self):
        """ Starts the main loop for the game. """
        while self.game_active:
            print("This is ROCK, PAPER, SCISSORS.")
            print("\nEnter 'q' to quit anytime. ")
            self.player_decision = input("\nwhat do you choose? ")

            if self.player_decision == "q":
                sure = input("Are you sure you want to Quit?. y/n  ")
                if sure.lower() == "y":
                    self.game_active = False
                elif sure.lower() == "n":
                    print("\n")
                    rps.run_game()
                else:
                    print("\nChoose y/n")

            else:
                self.computer_plays()
                self.check_result()

    def computer_plays(self):
        """ This simulates computer's play """
        self.com_play = choice(self.choices)

    def check_result(self):
        player_dec = self.player_decision.lower()
        choices = self.choices
        com_play = self.com_play
        if player_dec in choices:

            self._player_rock()
            self._player_paper()
            self._player_scissors()
            self._game_tie()

        else:
            print("Wrong keyword entered!")
            print("\nEnter the correct word.")
            self.run_game()

    def _player_rock(self):
        """ Players chooses rock """
        player_dec = self.player_decision.lower()
        choices = self.choices
        com_play = self.com_play
        # player choses rock, COM paper
        if player_dec == choices[0] and com_play == choices[1]:
            print(f"COM chose {com_play}.")
            print("You lost")

        # player choses rock, COM scissors
        if player_dec == choices[0] and com_play == choices[2]:
            print(f"COM chose {com_play}.")
            print("You Win!")

    def _player_paper(self):
        player_dec = self.player_decision.lower()
        choices = self.choices
        com_play = self.com_play
        """ Players chooses paper """
        # player choses paper, COM rock
        if player_dec == choices[1] and com_play == choices[0]:
            print(f"COM chose {com_play}.")
            print("You Win!")

        # player choses paper, COM scissors
        if player_dec == choices[1] and com_play == choices[2]:
            print(f"COM chose {com_play}.")
            print("You lost!")

    def _player_scissors(self):
        """ Players chooses scissors """
        player_dec = self.player_decision.lower()
        choices = self.choices
        com_play = self.com_play
        # player choses scissors, COM rock
        if player_dec == choices[2] and com_play == choices[0]:
            print(f"COM chose {com_play}.")
            print("You lost!")

        # player choses scissors, COM paper
        if player_dec == choices[2] and com_play == choices[1]:
            print(f"COM chose {com_play}.")
            print("You Win!")

    def _game_tie(self):
        """ If player and COM choices match. """
        player_dec = self.player_decision.lower()
        choices = self.choices
        com_play = self.com_play
        if player_dec == com_play:
            print("It's a tie!")
            print(f"You both chose {com_play}")
            self.run_game()


if __name__ == "__main__":
    # Make a game instance, and run the game.
    rps = RockPaperScissor()
    rps.run_game()
