
class Capability(object):
    """Something that a person can do.

    Built as an abstract superclass for more usefull classes.

    Attributes:
        person (Person): The person that this Capability is attached to.

    Args:
        person (Person): See attribute.
    """
    def __init__(self, person):
        self.person = person


    def run(self, prompt):
        """Run the capability on an prompt.

        Args:
            prompt (???): The input prompt.

        Returns:
            ???: The optional output value.
        """
        pass


    def can_run(self, prompt):
        """Check if the prompt can be ran with this capability.

        Args:
            prompt (???): The input prompt.

        Returns:
            bool: True if this capability can run this prompt.
        """
        return False
