from util import json_load
from random import sample
from definitions import REFERENCE_DIR
from capability import Capability
from powertypes import PowerDict
import os

first_sample = lambda x: sample(x, 1)[0]

class Memories(PowerDict, Capability):
    personal = json_load(os.path.join(REFERENCE_DIR, 'personal.json'))
    def __init__(self, info={}, person=None):
        PowerDict.__init__(self, info)
        self.update(Memories.calculated(self))
        Capability.__init__(self, person)

    @classmethod
    def calculated(cls, self):
        return {
            'full_name': self['first_name'] + " " + self['last_name'],
            'unique_id': self['first_name'] + "_" + self['last_name']
            }

    def run_phrase(self):
        return "" # TODO: Alex

    def __json__(self):
        return self

    @classmethod
    def from_json(cls, obj):
        return cls(obj)

    @classmethod
    def random_gender(cls):
        return first_sample(cls.personal['gender']).lower()

    @classmethod
    def names(cls):
        return cls.personal['names']

    @classmethod
    def random_first_name(cls, gender):
        names = cls.names()
        if gender in names:
            pool = names[gender]
        else:
            pool = names['male'] + names['female']
        return first_sample(pool)

    @classmethod
    def random_last_name(cls):
        return first_sample(cls.personal['surnames'])

    @classmethod
    def random(cls):
        mem = cls()
        mem.gender = cls.random_gender()
        mem.first_name = cls.random_first_name(mem.gender)
        mem.last_name = cls.random_last_name()
        return mem

if __name__ == '__main__':
    mem = Memories.random()



