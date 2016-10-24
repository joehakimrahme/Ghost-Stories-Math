# -*- coding: utf-8 -*-
from __future__ import division
import itertools
import random


colors = ('red', 'blue', 'yellow', 'black', 'green', 'white')


class Exorcism(object):
    def __init__(self, dice, special_powers=None):
        if special_powers is None:
            special_powers = {'Wild White'}
        self.special_powers = special_powers
        self.dice = dice

    def _success(self, roll, resistance):
        """Return True if a roll has at least an amount of 'black' equal to
        resistance.
        'black' was chosen arbitrarily.
        """
        hits = roll.count('black')
        if 'Wild White' in self.special_powers:
            hits += roll.count('white')
        return hits >= resistance

    def probability(self, resistance):
        all_combinations = list(itertools.product(colors, repeat=self.dice))
        success = []
        # Blue has the special power of rerolling if the exorcisms fails
        if 'Second Wind' in self.special_powers:
            n = 2
            for i in all_combinations:
                for j in all_combinations:
                    if any(self._success(roll, resistance)
                           for roll in (i, j)):
                        success.append((i, j))
        else:
            n = 1
            for i in all_combinations:
                if self._success(i, resistance):
                    success.append(i)

        return len(success) / (len(all_combinations) ** n)

    def scenario(self, resistance, sample_size=100000):
        """Simulate `sample_size` rolls and return the ratio of successes.
        """
        success = []
        for _ in range(sample_size):
            roll = [random.choice(colors) for _ in range(self.dice)]
            if self._success(roll, resistance):
                success.append(roll)
            else:
                if 'Second Wind' in self.special_powers:
                    roll = [random.choice(colors) for _ in range(self.dice)]
                    if self._success(roll, resistance):
                        success.append(roll)
        return len(success) / sample_size
