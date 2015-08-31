
from willie.module import commands, example
import random
import sys


@commands('rand', 'alea')
@example('.rand 2', re=r'random\(0, 2\) = (0|1|2)', repeat=10)
@example('.rand -1 -1', 'random(-1, -1) = -1')
@example('.rand', re=r'random\(0, \d+\) = \d+')
@example('.rand 99 10', re=r'random\(10, 99\) = \d\d', repeat=10)
@example('.rand 10 99', re=r'random\(10, 99\) = \d\d', repeat=10)
def rand(bot, trigger):
    """Replies with a random number between first and second argument."""
    arg1 = trigger.group(3)
    arg2 = trigger.group(4)

    if arg2 is not None:
        low = int(arg1)
        high = int(arg2)
    elif arg1 is not None:
        low = 0
        high = int(arg1)
    else:
        low = 0
        high = sys.maxsize

    if low > high:
        low, high = high, low

    number = random.randint(low, high)
    if bot.config.lang == 'ca':
        bot.reply("aleatori(%d, %d) = %d" % (low, high, number))
    elif bot.config.lang == 'es':
        bot.reply("aleatorio(%d, %d) = %d" % (low, high, number))
    else:
        bot.reply("random(%d, %d) = %d" % (low, high, number))


if __name__ == "__main__":
    from willie.test_tools import run_example_tests
    run_example_tests(__file__)
