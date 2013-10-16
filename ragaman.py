
def strip_boring(x):
    """Remove any characters which have no meaning for the purposes of
        an anagram"""
    import string
    # XXX specious subsumption: is str
    x = x.lower()
    return [y for y in x if y in string.ascii_lowercase]

# TODO s->seq
def make_converter(s):
    """Returns a callable to convert each element of a permuted
        sequence back to its original type"""
    # TODO probably wrong
    if type(s) is str:  # TODO unicode?
        return lambda x: ''.join(x)
    else:
        return type(s)

# TODO s->seq
def perm(s, r=None):
    """Permute a sequence and recombine in a sane way (convert back
        to initial type)"""
    from itertools import permutations
    passed_type = make_converter(s)
    more_interesting = strip_boring(s)
    # XXX this exposes some underlying properties of permutations() -
    # when does this matter?
    return [passed_type(x) for x in permutations(more_interesting, r)]

# Don't create a function to generate "clean" permutations - just
# sort and uniq yourself. Better to keep composability

for x in sorted(set(perm('anagram'))):
    if 'aa' in x \
    or 'mnr' in x \
    or 'rng' in x \
    or 'nrg' in x:
        continue
    print x

# TODO # assign probability of being English word
# -> this is domain dependent. in the extreme case, mandarin and english
# will be completely different, so it makes no sense to assign a probability for
# english based on a mandarin model

# TODO # filter out results <> some statistical threshold
