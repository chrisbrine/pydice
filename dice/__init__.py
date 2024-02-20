from dice.nums import number_array, divider

def showDiceText(roll: int = 6) -> str:
    index = 0
    current_numbers = ['' for _ in range(7)]
    while roll > 0:
      if index > 0:
        for i, line in enumerate(divider):
          current_numbers[i] = line + current_numbers[i]
      for i, line in enumerate(number_array[roll % 10]):
        current_numbers[i] = line + current_numbers[i]
      index += 1
      roll = roll // 10
    return '\n'.join(current_numbers)


def rollDice(sides: int = 6) -> int:
    from random import randint
    roll = randint(1, sides)
    print(f'\nYou rolled a {roll}!')
    print(showDiceText(roll))
    return roll

def dice(sides: int = 6, rolls: int = 1):
    # rolls a dice and shows the result
    print(f'Rolling a {sides} sided dice {rolls} times:')
    result = [rollDice(sides) for _ in range(rolls)]
    print(f'You rolled: {result}')