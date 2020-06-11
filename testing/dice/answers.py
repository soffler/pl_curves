import pytest
from dice import Dice


def test_valid_roll():
    """ Test that a dice roll is valid. """

    # Intialise a standard, six-sided dice.
    dice = Dice()

    # Roll the dice.
    roll = dice.roll()

    # Check that the value is valid.
    assert roll > 0 and roll < 7


def test_always_valid_roll():
    """ Test that a dice roll is "always" valid. """

    # Intialise a standard, six-sided dice.
    dice = Dice()

    # Roll the dice lots of times.
    for i in range(0, 10000):
        roll = dice.roll()

        # Check that the value is valid.
        assert roll > 0 and roll < 7


def test_average():
    """ Test that the average dice roll is correct. """

    # Intialise a standard, six-sided dice.
    dice = Dice()

    # Work out the expected average roll.
    exp = sum(range(1, 7)) / 6

    # Calculate the sum of the dice rolls.
    total = 0
    rolls = 100000
    for i in range(0, rolls):
        total += dice.roll()

    # Check that the average matches the expected value.
    average = total / rolls
    assert average == pytest.approx(3.5, rel=1e-2)


def test_fair():
    """ Test that a dice is fair. """

    # Intialise a standard, six-sided dice.
    dice = Dice()

    # Set the number of rolls.
    rolls = 1000000

    # Create a dictionary to hold the tally for each outcome.
    tally = {}
    for i in range(1, 7):
        tally[i] = 0

    # Roll the dice 'rolls' times.
    for i in range(0, rolls):
        tally[dice.roll()] += 1

    # Assert that the probability is correct.
    for i in range(1, 7):
        assert tally[i] / rolls == pytest.approx(1 / 6, 1e-2)


@pytest.mark.slow
@pytest.mark.parametrize("sides, rolls", [(5, 5000000), (7, 5000000)])
def test_double_roll(sides, rolls):
    """ Check that the probability for the sum of two n-sided dice matches
        the expected distribution.
    """

    # Store the expected probabilities for the sum of two dice.
    exp = {}
    for x in range(2, 2*sides + 1):
        exp[x] = prob_double_roll(x, sides)

    # Create a dictionary to hold the tally for each outcome.
    tally = {}
    for key in exp:
        tally[key] = 0

    # Initialise the dice.
    dice = Dice(sides)

    # Roll two dice 'rolls' times.
    for i in range(0, rolls):

        # Sum the value of the two dice rolls.
        roll_sum = dice.roll() + dice.roll()

        # Increment the tally for the outcome.
        tally[roll_sum] += 1

    # Compute the probabilities and check with expected values.
    for key in tally:

        average = tally[key] / rolls
        assert average == pytest.approx(exp[key], rel=1e-2)


def prob_double_roll(x, n):
    """ Expected probabilities for the sum of two dice."""
    # For two n-sided dice, the probability of two rolls summing to x is
    # (n − |x−(n+1)|) / n^2, for x = 2 to 2n.

    return (n - abs(x - (n+1))) / n**2
