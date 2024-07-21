# chinesePoker-best-hand
a cli-based program that will (maybe) output the best possible hand for a given user input of 13 cards, following chinese poker rules

### chinese poker

- only relevant details will be covered
- for a more comprehensive guide on the game, please refer to other resources
<br></br>
- a simple game that uses conventional poker hand rankings 
- players are dealt 13 cards and must create three poker hands, two of which are the 'back' and 'middle' hands consisting of 5 cards, and the final hand of 3 cards being the 'front'
- the 'back' hand must be the strongest hand, and the 'front' must be the weakest hand.

### strategy

- this program will make the best hand from a 'back'-heavy perspective
- more complicated strategies may be added in the future but for now this program will create the hands from back to front, maximising the hand ranking in each layer
- for example, it may be favourable to forgo a low flush in the back in order to have more power in the middle and front
- however this program will make the flush instead and then use the left over cards to make the next best hand for the middle, and then the left over cards from that to make the best hand for the front
  
### card representation

- cards are represented using the rank x and the suit y like so: xy
- the valid ranks are '2 3 4 5 6 7 8 9 10 j q k a' in order of power.
- the valid suits are 'c s h d' in no particular order.
<br></br>
- a valid input for a hand would be: jd, 9s, 5d, 2h, 5c, 3c, jc, 10c, 10h, 8c, 3s, as, 6c
  
