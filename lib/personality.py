import random
from capability import Capability
from powertypes import PowerDict


# TODO: Add testing
# this would actually be a good case for unit testing
# TODO: Add docset
class Personality(PowerDict, Capability):
    def __init__(self, traits={}, person=None):
        """
        So this is a representation of a recursive tree shaped personality trait
        which is just a glorified dict.
        """
        PowerDict.__init__(self, traits)
        Capability.__init__(self, person)

    def __json__(self):
        return self

    @staticmethod
    def from_json(obj):
        return Personality(obj)

    @classmethod
    def random(cls, default=random.random):
        if callable(default):
            r = default
        else:
            r = lambda: default
        traits = {
            'bulk_apperception': r(),
            'candor': r(),
            'vivacity': r(),
            'coordination': r(),
            'meekness': r(),
            'humility': r(),
            'cruelty': r(),# dont forget this was made for wild west
            'self_preservation': r(),
            'patience': r(),
            'dicisiveness': r(),
            'imagination': r(),
            'curiosity': r(),
            'aggression': r(), # once again
            'loyalty': r(),
            'empathy': r(),
            'tenacity': r(),
            'courage': r(),
            'sensuality': r(),
            'charm': r(),
            'humor': r()
        }
        return cls(traits, r())






