import random
from collections import namedtuple
from capability import Capability
from powertypes import PowerDict

Vector = namedtuple('Vector', 'positive arousal')
"""An emotional vector, which is a 2d vector on the axes of positve vs arousal

so any emotion can be represented as one of the vectors, although incompletely

angry: low positive, high arousal
sad: low positive, low arousal
happy: high positive, high arousal
"""

class Emotions(PowerDict, Capability):
    """A full array of emotions.

    each emotion has a name and an atom.

    you can combine the scaled vectors of all of the atoms to get. the persons
    current total emotional vector.

    Attributes:
        person (Person): The person that this capability is attached to.

    Args:
        gen (function, optional): The generator function that generates the
            values for each emotion. Defaults to lambda: 0.5
        person (Person, optional): The person this capability is attached to.
            Defaults to None.
    """
    def __init__(self, gen=lambda: 0.5, person=None):

        # init its two base classes
        PowerDict.__init__(self)
        Capability.__init__(self, person)

        self['joy'] =        gen()
        self['contempt'] =   gen()
        self['surprise'] =   gen()
        self['shame'] =      gen()
        self['sadness'] =    gen()
        self['fear'] =       gen()
        self['anger'] =      gen()
        self['guilt'] =      gen()
        self['disgust'] =    gen()
        self['interest'] =   gen()

    # TODO: second oppinion
    vectors = {
        'joy':       Vector(+1.0,+1.0),
        'contempt':  Vector(-1.0,+1.0),
        'surprise':  Vector(+1.0,+1.0),
        'shame':     Vector(-1.0,-1.0),
        'sadness':   Vector(-1.0,-1.0),
        'fear':      Vector(-1.0,+1.0),
        'anger':     Vector(-1.0,+1.0),
        'guilt':     Vector(-1.0,-1.0),
        'disgust':   Vector(-1.0,-1.0),
        'interest':  Vector(+1.0,+1.0)
    }

    @property
    def vector(self):
        """Calculates the vector value of this emotional state.

        Returns:
            Vector: an averaged sum of all of the emotions
        """
        positives = 0
        arousals = 0
        for vec, val in zip(Emotions.vectors, self.values()):
            positives += val * vec.positive
            arousals += val * vec.arousal
        size = float(len(self))
        positives /= size
        arousals /= size
        return Vector(positives, arousals)

    def __json__(self):
        return self

    @classmethod
    def from_json(cls, obj):
        em = cls()
        for k, v in obj.items():
            if isinstance(v, float):
                em[k] = v
            else: # DEPRICATED
                em[k] = v[1]
        return em

    @classmethod
    def random(cls):
        """Generates a random emotional state.

        Returns:
            Emotions: the random emotional state.
        """
        return cls(gen=random.random)

if __name__ == '__main__':
    spec = Emotions()

