# Poker Game

## Contents
- [Objective](#objective)
- [Module Proposal](#module-proposal)
- [Helpers Module](#helpers-module)
- [Verification](#verification)

## Objective

Simulate the behavior of a **poker card game** in **Texas Holdem** mode using object-oriented programming techniques.

## Module Proposal

Proposed modules and classes by module:

```
├── test_poker.py
├── game.py
│   └── Game
├── cards.py
│   ├── Card
│   ├── Deck
│   └── Hand
└── roles.py
    ├── Dealer
    └── Player
```

### Game 🎲

Should have the following function:

```python
def get_winner(
    players: list[Player],
    common_cards: list[Card],
    private_cards: list[list[Card]],
) -> tuple[Player | None, Hand]:
```

> 💡 This function should return the winning player and the winning hand. In the case of a tie, the player will be `None`, but the winning hand will still have a value.

### Dealer 🎩

| Data     | Responsibilities                  |
| --------- | ---------------------------------- |
| Deck      | Reveal community cards             |
| Players   | Deal cards to players              |
|           | Ask each player for their best hand|
|           | Determine the best hand           |

### Player 🙅‍♀️

| Data    | Responsibilities                          |
| ------- | ------------------------------------------ |
| Name    | Receive 2 private cards                   |
|         | Receive 5 community cards                 |
|         | Find the best combination of cards        |

A `Player` object should be created by passing the player's name. **Examples**: `Player('Player 1'), Player('Player 2')`

### Card 🃏

| Data               | Responsibilities                      |
| ------------------- | ------------------------------------- |
| Card number        | Know if one card is less than another |
| Card suit          | Represent a card                      |

A `Card` object should be created from a string. **Examples**: `Card('Q♠'), Card('7♣'), Card('A♠')`

### Hand 🤙

| Data            | Responsibilities                     |
| ---------------- | ------------------------------------- |
| 5 cards         | Discover the category of the hand     |
| Card suit       | Know if one hand is greater than another |

- The method `__contains__()` should be implemented to determine if a `Card` belongs to a `Hand`.
- The `Hand` object should contain an attribute `cat` that identifies the category of the hand, as well as an attribute `cat_rank` that stores the "ranking" of its category. In most cases, this is the highest card, but not always. **Examples**:

| `hand.cat`             | `hand.cat_rank` | Explanation                                   |
| ---------------------- | --------------- | --------------------------------------------- |
| `Hand.HIGH_CARD`       | `'J'`           | Highest card                                 |
| `Hand.ONE_PAIR`        | `'5'`           | Highest card                                 |
| `Hand.TWO_PAIR`        | `('10', '7')`   | Tuple with highest cards (from highest to lowest) |
| `Hand.THREE_OF_A_KIND` | `'K'`           | Highest card                                 |
| `Hand.STRAIGHT`        | `'9'`           | Highest card                                 |
| `Hand.FLUSH`           | `'Q'`           | Highest card                                 |
| `Hand.FULL_HOUSE`      | `('3', 'J')`    | Tuple with the trio card and the pair card   |
| `Hand.FOUR_OF_A_KIND`  | `'Q'`           | Highest card                                 |
| `Hand.STRAIGHT_FLUSH`  | `'7'`           | Highest card                                 |

### Deck 🗃️

| Data     | Responsibilities     |
| --------- | --------------------- |
| 52 cards | Deal random cards     |

> 💡 OPTIONAL

## Helpers Module

The [helpers](./helpers.py) file contains support functions for the project.

The most important is: `combinations(values, n)` which generates all possible combinations of `values` of size `n`:

```python
>>> list(helpers.combinations((1, 2, 3, 4, 5), n=3))
[(1, 2, 3),
 (1, 2, 4),
 (1, 2, 5),
 (1, 3, 4),
 (1, 3, 5),
 (1, 4, 5),
 (2, 3, 4),
 (2, 3, 5),
 (2, 4, 5),
 (3, 4, 5)]
```

Two important notes:

- What we pass is an **iterable**, so a list of `Card` objects could be used.
- The parameter `n` must be passed by name.

## Verification

- You can download the [test file](./test_poker.py) for pytest here.
