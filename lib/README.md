# README

How can I make this seem more human?

This project is mostly meant for me so this file holds notes.

## Things I should be googling:

- grice's maxim I think this will be a good set of rules to follow.


## Things I should be thinking about:

- speakers meaning vs audience meaning (as a measure of accuracy for the ais)

## Philosophy of this application:

I am going to try to study as much psychology as possible and try to mimic all of the
ideas in psychology using analogous datatypes.

When people write code they think 'how can I make this as simple as possible'
so that in the future they can understand and manipulate the code.  Their goal
is to avoid 'spaghetti code'.  the issue however is that brains are structured
a lot like spaghetti and so I dont think clean simple code will be able to
create the structure and malliability of the human brain.  So i am purposefully
not trying to avoid spaghetti code.  If we have succeeded we will not be able to
easily understand what went wrong and why.  We will need a new field of research
into robo psychology in order to fix issues within one of these persons brains.

### Personality Traits

So one psychological idea, which comes from sci fi not necessarily actual psychology
is the personality trait chart from westworld, where each character had a list of some
personality traits with a score or a scale associated with each, and sub personality
traits contained within each.  Each of these traits will define how a character will
act in certain situations.

The highest level traits in the show are:

- Bulk Apperception
- Candor
- Vivacity
- Coordination
- Meekness
- Humility
- Cruelty
- Self Preservation
- Patience
- Dicisiveness
- Imagination
- Curiosity
- Aggression
- Loyalty
- Empathy
- Tenacity
- Courage
- Sensuality
- Charm
- Humor

How each of these are used to define the action a character takes is not delved apon
in the show.  I intend to supply these as global values that the code can referenc
in order to pick an action.  At the moment I plan on hard-coding these
reactions and their necessary personality traits but in the future I plan on
allowing the traits to be modified my the character or internal forces within the
character.

### Emotions

another idea from a video i watched recently was about emotions. it was a theory
on which emotions exist, our basic emotions that all other emotions are a combination
of. one person believed that there were 10 basic emotions:

- joy
- contempt
- surprise
- shame
- sadness
- fear
- anger
- guilt
- disgust
- excitement

another theory put all emotions on two axes:
    pleasant <-> unpleasant
             and
high arousal <-> low arousal

neither of these feel satisfying as a powerful analogy for emotion.  However I
feel it would be good to combine them.  Use a 0-1 scale on each emotion so that
they can feel complicated combinations of emotions and create a representation
of each of the possible emotions by multiplying the arousal level of each
emotional atom by a vector in the emotional space and adding them up and
using the resulting vector as a way to represent in a simpler sense how they
feel.

We will call each of the above items (joy, contempt, surprise, etc)
Emotional Atoms.  And the second idea will be called the Arousal Space.
The set of emotional atoms and their states will define the persons position in
arousal space.


### Combinations

I realized that a lot of these modules will be combined using neural nets.
Which means that hopefully most of the modules created will have [-1 1] or
[0 1] interface for each value within them that each module can be represented
as a black box with a possible input vector and a possible output vector.

I should think about making an interface for them all to implement.

I do need to think about how to define what the imputs are.  What does emotion
take? What is outputs seems obvious, it should output the emotional states.

### Cognitive biases

- Hindsight bias
- Confirmation bias

### Neural hormones

- GABA
- Endorphins
- Excitatory
- Norepinepherin
- glutimate
- inhibitory
- seratonin
- acetylcholine
- dopamine
- endochrine hormones (slow, lingering)
- adrenaline
- sex hormones?

### Parts of the brain

// TODO: Fill in

### Disorders?

- face blindness

### Sensation vs Perception

// TODO
Logarithmic scale (webers law)
// There are so many things here!
four touch senses
- pressure
- warmth
- cold
- pain

# Alex

- Learn Structure
    + Functions
    + Classes
- Learn documentation
    + Comments
    + Docstrings
- Make Jordan document his code
- Fill in TODO: Alex
- Help Jordan figure out how to generate and interpret speech
    + TODO: Alex is to generate text based on "Intent"
    + Generate Intents from text
    + Figure out how to generate more and more complex Intents from text

# Jordan

- Generate smart objects (minds are fluid and complex, programming is hard and simple)
    + identifier type
    + sentence type
    + dict type (figure out a more representive type)
    + list type (figure out a more representive type)
    + num type
    + value type
    + thunk


