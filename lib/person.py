
from util import json_load, json_dump
from personality import Personality
from emotion import Emotions
from memories import Memories
from definitions import PEOPLE_DIR
from capability import Capability
from weather import Weather
from listen import Listen
from powertypes import PowerDict
import os


class Person(PowerDict, Capability):
    def __init__(self, capabilities={}):
        for v in capabilities.values():
            v.parent = self
        Capability.__init__(self, self)
        PowerDict.__init__(self, capabilities)


    def save(self):
        unique_name = self['unique_id']
        folder = os.path.join(PEOPLE_DIR, unique_name)

        # create the file if it doesnt exist
        if not os.path.exists(folder):
            os.mkdir(folder)

        # save all of the pieces to individual files
        for k, cap in self.items():
            filepath = os.path.join(folder, k + '.json')
            json_dump(cap, filepath)

    cap_classes = {
        'memories': Memories,
        'personality': Personality,
        'emotions': Emotions,
        'listen': Listen,
        'weather': Weather
    }

    @classmethod
    def load(cls, unique_id):
        folder = os.path.join(PEOPLE_DIR, unique_id)

        # check if they exist
        if not os.path.exists(folder):
            return None

        caps = {}
        for k, v in Person.cap_classes.iteritems():
            filepath = os.path.join(folder, k + '.json')
            if os.path.exists(filepath):
                caps[k] = json_load(filepath, cls=v)
            else:
                caps[k] = v()
        return cls(caps)

    @classmethod
    def list(cls, parse=False):
        ids = os.listdir(PEOPLE_DIR)
        if parse:
            return [Person.load(x) for x in ids]
        else:
            return ids

    @classmethod
    def random(cls):
        cap = {}
        for k, v in Person.cap_classes.items():
            cap[k] = v.random()
        return cls(cap)





if __name__ == '__main__':
    for person in Person.list(True):
        print(person['full_name'], 'loaded successfully')
        person.save()
        print(person['full_name'], 'saved successfully')




