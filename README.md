# Euro-poloy

This project is a personal implementation of a simplified version of the game Monopoly. The main objective is to create a class called RealEstateGame that allows multiple players to play the game.

# Game Rules

* Players start at the "GO" space on the board and take turns rolling a single die (values 1-6) to move around the board spaces.
The spaces are arranged in a circular manner, and players pass each space repeatedly.
* Each player receives a certain amount of money at the start and every time they land on or pass the "GO" space.
* Each space on the board, except for "GO," can be purchased. Once purchased, the player becomes the owner and can charge rent to other players who land on that space.
* If a player runs out of money, they become inactive and cannot move or own spaces.
* The game continues until all players but one have run out of money. The last player with money is declared the winner.

# RealEstateGame Class

The RealEstateGame class represents the game being played. It provides the following methods (and may have additional ones) to facilitate the gameplay:

* create_spaces(money_on_go, rent_amounts): Creates the game spaces.
  * Takes two parameters: the amount of money given to players when they land on or pass the "GO" space, and an array of 24 integers representing rent amounts for each space.
* The method creates a space named "GO" that cannot be purchased by any player.
* It creates 24 additional game spaces, totaling 25 spaces:
  * Spaces have unique names and rent amounts initialized from the provided array.
  * Each space has a purchase price equal to 5 times the rent amount.
* create_player(name, initial_balance): Creates a player.
  * Takes two parameters: a unique name and an initial account balance.
* get_player_account_balance(name): Retrieves a player's account balance.
  * Takes the name of the player as a parameter and returns their account balance.
* get_player_current_position(name): Retrieves a player's current position on the board.
  * Takes the name of the player as a parameter and returns their current position as an integer, with the "GO" space being position zero.
* buy_space(name): Allows a player to purchase the current space.
  * Takes the name of the player as a parameter.
* If the player has an account balance greater than the purchase price and the space doesn't already have an owner:
  * Deducts the purchase price of the space from the player's account.
  * Sets the player as the owner of the current space.
  * Returns True.
* Otherwise, returns False.
* move_player(name, spaces_to_move): Moves a player a certain number of spaces.
  * Takes the name of the player and the number of spaces to move as parameters.
  * If the player's account balance is 0, the method returns immediately without performing any action.
  * The number of spaces to move is an integer between 1 and 6.
  * The method advances the player around the circular board by the specified number of spaces.
  * If the player lands on or passes the "GO" space while moving, the player receives the "GO" amount of money.
  * After the move is complete, the player pays rent for the new space occupied, if necessary:
    * No rent is paid if the player is occupying the "GO" space, or if the space has no owner.
