


"""
Phrase object represents something that the user will say to the person.

It mosly will be used to get information about the phrase like, verb, subject,
object, type.  I really dont understand how to get those things from the phrase
but I feel like they are necessary.
"""
class Phrase(object):
    def __init__(self, text):
        self.text = text

    """
    Im not sure about this one but im thinking that it will respond: question,
    statement, command
    """
    def get_type(self):
        pass

    """
    Gets the verb in the phrase. I understand that its more complicated than that
    but we need to start somewhere
    """
    def get_verb(self):
        pass

    """
    Gets the subject of the phrase. Once again...
    """
    def get_subject(self):
        pass

    """
    gets the object...
    """
    def get_object(self):
        pass

    """
    gets the modifier...
    """
    def get_modifier(self):
        pass