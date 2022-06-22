# Author: Paola Cernada
# GitHub username: paolacernada
# Date: 6/3/2022
# Description: Create a RealEstateGame class that
#              allows two or more individuals to
#              play a simplified version of the
#              game Monopoly.


class Player:
    """
    Player is a class that generates a player and
    stores information about the player in order
    for the player to participate in a RealEstateGame.
    """

    def __init__(self, name, account_balance):
        self._name = name
        self._account_balance = account_balance
        self._is_active = True
        self._location = 0

    def get_name(self):
        """
        A method to get the name of the player.

        :return: the player's name.
        """
        return self._name

    def get_account_balance(self):
        """
        A method to check the player's account balance.

        :return: the player's account balance.
        """
        return self._account_balance

    def get_is_active(self):
        """
        A method to check whether the player is active.

        :return: the status of the player
                 is_active = True or False
        """
        return self._is_active

    def get_location(self):
        """
        A method to get the location of the player.

        :return: the player's location.
        """
        return self._location

    def set_name(self, name):
        """
        A method to set the name of the player.

        :param name: the name of the player.
        :return: the player's name.
        """
        self._name = name

    def set_account_balance(self, account_balance):
        """
        A method to set the account balance of the player.

        :param account_balance: the account balance of the player.
        :return: the player's account balance.
        """
        self._account_balance = account_balance

    def set_is_active(self, is_active):
        """
        A method to set the status of the player.

        :param is_active: the status of the player.
        :return: True if the player is active, otherwise False.
        """
        self._is_active = is_active

    def set_location(self, location):
        """
        A method to set the location of the player.

        :param location: the location of the player.
        :return: the player's location.
        """
        self._location = location


class Space:
    """
    Space is a class that generates spaces and saves
    information about them, so they may be used in a
    RealEstateGame.
    """

    def __init__(self, name, rent_amount, can_be_purchased):
        self._name = name
        self._rent_amount = rent_amount
        self._can_be_purchased = can_be_purchased
        self._owner = ""

    def get_name(self):
        """
        A method to retrieve the name of the space.

        :return: the name of the space.
        """
        return self._name

    def get_rent_amount(self):
        """
        A method to get the rent for the space.

        :return: the rent amount for the space.
        """
        return self._rent_amount

    def get_can_be_purchased(self):
        """
        A method for determining the state of the
        space and whether it may be purchased.

        :return: True or False.
        """
        return self._can_be_purchased

    def get_purchase_price(self):
        """
        A method for determining the purchasing price
        of a particular place.

        :return: the cost of buying the given space.
        """
        return self._rent_amount * 5

    def get_owner(self):
        """
        A method to get the owner of a space.

        :return: the owner of the space.
        """
        return self._owner

    def set_name(self, name):
        """
        A method to set the name of the space.

        :param name: the name of the space.
        :return: the name of the space.
        """
        self._name = name

    def set_rent_amount(self, rent_amount):
        """
        A method to set the rent amount of the space.

        :param rent_amount: the rent amount for the space.
        :return: the rent for the space.
        """
        self._rent_amount = rent_amount

    def set_can_be_purchased(self, can_be_purchased):
        """
        A method to set the status of the
        space and whether it may be purchased.

        :param can_be_purchased: the status of the space.
        :return: True or False.
        """
        self._can_be_purchased = can_be_purchased

    def set_owner(self, owner):
        """
        A method to set the owner of a space.

        :param owner: the name of the new owner of the space.
        :return: the name of the owner.
        """
        self._owner = owner


class RealEstateGame:
    """
    RealEstateGame is a class that lets two or more players
    play a simplified version of the game Monopoly.
    """

    def __init__(self):
        self._player_dict = {}
        self._space_list = []
        self._is_end_game = True
        self._money_on_GO = 0

    def create_spaces(self, money_on_GO, rent_amounts):
        """
        Accepts two parameters: the amount of money supplied
        to players when they land on or pass through the "GO"
        space, and a 24-int list which are rent amounts.

        :param money_on_GO: money Player receives when they land/pass GO.
        :param rent_amounts: list of ints, represents rent amount for 24 spaces.
        :return: n/a.
        """

        MONOPOLY_BOARD = ["Amsterdam", "Athens",
                          "Barcelona", "Berlin",
                          "Budapest", "Copenhagen",
                          "Dublin", "Edinburgh",
                          "Florence", "Helsinki",
                          "Lisbon", "London",
                          "Majorca", "Munich",
                          "Paris", "Porto",
                          "Prague", "Reykjavik",
                          "Rome", "Salamanca",
                          "Stockholm", "Tallinn",
                          "Venice", "Zagreb"]

        self._money_on_GO = money_on_GO

        assert (len(rent_amounts) == len(MONOPOLY_BOARD))

        for index in range(len(MONOPOLY_BOARD)):
            self._space_list.append(Space(MONOPOLY_BOARD[index], rent_amounts[index], True))

        self._space_list.insert(0, Space("GO", 0, False))

    def create_player(self, player_name, initial_balance):
        """
        Uses two parameters: a distinct name and a starting
        account balance.

        :param player_name: the name of the player.
        :param initial_balance: amount of $ player starts with.
        :return: n/a.
        """
        self._player_dict[player_name] = Player(player_name, initial_balance)

    def get_player_account_balance(self, player_name):
        """
        Takes the player's name as an argument and returns
        the player's account balance.

        :param player_name: the name of the player.
        :return: the player's account balance.
        """
        return self._player_dict[player_name].get_account_balance()

    def get_player_current_position(self, player_name):
        """
        Accepts the player's name as an input and returns
        the player's current location on the board as an
        integer (where the "GO" space is position zero).

        :param player_name: the name of the player.
        :return: the player's current position on the
         board as an integer.
        """
        return self._player_dict[player_name].get_location()

    def buy_space(self, player_name):
        """
        If the player's account balance is larger than the
        purchase amount and the slot is not already occupied,
        the player buys the space.

        :param player_name: the name of the player.
        :return: True or False.
        """
        player = self._player_dict[player_name]
        space = self._space_list[player.get_location()]

        # If the player has enough money to buy the space and the space is available, the player buys -
        # the space and is set as the owner of the space.
        if player.get_account_balance() > space.get_purchase_price() and space.get_can_be_purchased():
            player.set_account_balance(player.get_account_balance() - space.get_purchase_price())
            space.set_owner(player.get_name())
            space.set_can_be_purchased(False)

            return True

        return False

    def move_player(self, player_name, spaces_to_move):
        """
        Moves the player from the current location.

        :param player_name: the name of the player.
        :param spaces_to_move: the number of spaces to move.
        :return: n/a.
        """
        assert (type(spaces_to_move) is int)
        assert (0 < spaces_to_move < 7)

        # To prevent a key error when accessing the dictionary.
        assert (player_name in self._player_dict)

        player = self._player_dict[player_name]

        if player.get_account_balance() <= 0:
            return

        # If player's current location greater than the location to be set.
        if player.get_location() > (player.get_location() + spaces_to_move) % 25:
            player.set_account_balance(player.get_account_balance() + self._money_on_GO)

        # % len(self._space_list) To move from end point to start point.
        player.set_location((player.get_location() + spaces_to_move) % len(self._space_list))

        # The player location is an int that represents the index on the space_list.
        space = self._space_list[player.get_location()]

        # If the space cannot be purchased and the owner is not the player and space is not GO.
        if not space.get_can_be_purchased() and space.get_owner() != player.get_name() and space.get_name() != "GO":

            # Get the space's current owner.
            space_owner = self._player_dict[space.get_owner()]

            # If the player has enough money to pay the rent due.
            if player.get_account_balance() > space.get_rent_amount():

                # The current owner receives the rent money from the player.
                space_owner.set_account_balance(space_owner.get_account_balance() + space.get_rent_amount())
                # The rent owed is deducted from the player's account.
                player.set_account_balance(player.get_account_balance() - space.get_rent_amount())

            elif player.get_account_balance() < space.get_rent_amount():
                # The current owner receives the player's balance (to cover rent), and the player is eliminated.
                space_owner.set_account_balance(space_owner.get_account_balance() + player.get_account_balance())
                self._player_game_over(player_name)

    def check_game_over(self):
        """
        If all players except one have a 0 account balance,
        the game is ended.

        :return: the name of the winner if the game is over
                 otherwise, returns an empty string.
        """

        counter = 0
        winner = ""

        for player in self._player_dict:
            if self._player_dict[player].get_account_balance() <= 0:
                counter += 1
            else:
                winner = self._player_dict[player].get_name()

        if len(self._player_dict) == counter + 1:
            return winner

        return ""

    def _player_game_over(self, player_name):
        """
        If the player's balance is 0, the player loses the game,
        and must be removed as the owner of any spaces.

        :param player_name: the name of the player.
        :return: n/a.
        """

        player = self._player_dict[player_name]

        for space in self._space_list:
            if space.get_owner() == player_name:
                space.set_owner("")
                space.set_can_be_purchased(True)

        player.set_account_balance(0)
        player.set_is_active(False)


def main():
    """
    A main function to interactively test/play the RealEstateGame :-)
    """

    game = RealEstateGame()

    rents = [50, 50, 50, 75, 75, 75, 100, 100, 100, 150, 150, 150, 200, 200, 200, 250, 250, 250, 300, 300, 300, 350,
             350, 350]

    game.create_spaces(50, rents)

    player_list = ["PowerGirl", "AstroBoy", "BlueLagoon"]

    game.create_player("PowerGirl", 290)
    game.create_player("AstroBoy", 290)
    game.create_player("BlueLagoon", 290)

    turn = 0

    winner = ""
    while winner == "":

        for player in player_list:

            if game.get_player_account_balance(player) != 0:
                turn += 1

                print("Active Player: ", player, "  Turn #", turn)

                number_of_moves = 0
                while number_of_moves < 1 or number_of_moves > 6:
                    number_of_moves = int(input("How many spaces will you move 1-6? \n"))

                    if number_of_moves < 1 or number_of_moves > 6:
                        print("Invalid input. Please, try again.")

                game.move_player(player, number_of_moves)

                if game.get_player_current_position(player) != 0:
                    buy_property = "invalid"
                    while buy_property.lower() != "y" and buy_property.lower() != "n":
                        buy_property = input("Would you like to buy this space? [Y / N] \n")

                        if buy_property.lower() != "y" and buy_property.lower() != "n":
                            print("Invalid answer. Please, try again.")

                    if buy_property.lower() == "y":
                        is_purchased = game.buy_space(player)

                        if is_purchased:
                            print("Congratulations on your new purchase!\n")

                        else:
                            print("Sorry, invalid action!\n")

                            if game.get_player_account_balance(player) == 0:
                                print("In-Game Update:")
                                print(player, "is out of the game!\n")

                print(player, ": Current position: ", game.get_player_current_position(player))
                print(player, ":  Account balance: ", game.get_player_account_balance(player), "\n")

            winner = game.check_game_over()

    print(winner, ", you win!")


if __name__ == "__main__":
    main()
