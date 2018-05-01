
import time


if __name__ == "__main__":

    sequence = 'ATCGTGTGTCAGTCAGTGAATGACAATTGACATCGTGTGTCAGTCAGTGAATGACAATTGACATCGTGTGTCAGTCAGTGAATGACAATTGACATCGTGTGTCAGTCAGTGAATGACAATTGACATCGTGTGTCAGTCAGTGAATGACAATTGACATCGTGTGTCAGTCAGTGAATGACAATTGACATCGTGTGTCAGTCAGTGAATGACAATTGACATCGTGTGTCAGTCAGTGAATGACAATTGACATCGTGTGTCAGTCAGTGAATGACAATTGACATCGTGTGTCAGTCAGTGAATGACAATTGACATCGTGTGTCAGTCAGTGAATGACAATTGACATCGTGTGTCAGTCAGTGAATGACAATTGACATCGTGTGTCAGTCAGTGAATGACAATTGACATCGTGTGTCAGTCAGTGAATGACAATTGACATCGTGTGTCAGTCAGTGAATGACAATTGACATCGTGTGTCAGTCAGTGAATGACAATTGACATCGTGTGTCAGTCAGTGAATGACAATTGACATCGTGTGTCAGTCAGTGAATGACAATTGACATCGTGTGTCAGTCAGTGAATGACAATTGACATCGTGTGTCAGTCAGTGAATGACAATTGACATCGTGTGTCAGTCAGTGAATGACAATTGACATCGTGTGTCAGTCAGTGAATGACAATTGACATCGTGTGTCAGTCAGTGAATGACAATTGACATCGTGTGTCAGTCAGTGAATGACAATTGACATCGTGTGTCAGTCAGTGAATGACAATTGACATCGTGTGTCAGTCAGTGAATGACAATTGACATCGTGTGTCAGTCAGTGAATGACAATTGACATCGTGTGTCAGTCAGTGAATGACAATTGACATCGTGTGTCAGTCAGTGAATGACAATTGACATCGTGTGTCAGTCAGTGAATGACAATTGACATCGTGTGTCAGTCAGTGAATGACAATTGACATCGTGTGTCAGTCAGTGAATGACAATTGACATCGTGTGTCAGTCAGTGAATGACAATTGACATCGTGTGTCAGTCAGTGAATGACAATTGACATCGTGTGTCAGTCAGTGAATGACAATTGACATCGTGTGTCAGTCAGTGAATGACAATTGACATCGTGTGTCAGTCAGTGAATGACAATTGACATCGTGTGTCAGTCAGTGAATGACAATTGACATCGTGTGTCAGTCAGTGAATGACAATTGAC'

    # timer decorator
    def timeit(f):
        def wrap(*args):
            start_time = time.time()
            ret = f(*args)
            elapsed = time.time() - start_time
            print('{} function took {:.3f} ms'.format(f.__name__, (elapsed)*1000.0))
            return ret
        return wrap

    # reverse (does not need a method but for the example)
    @timeit
    def reverse(seq):
        return seq[::-1]

    # complement method 1
    @timeit
    def complement_one(seq):
        sequence_mapping = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        return ''.join([sequence_mapping[s] for s in seq])

    # complement method 2
    @timeit
    def complement_two(seq):
        return seq.translate(str.maketrans('ATCG','TAGC'))

    # reverse complement method 1
    @timeit
    def reverse_complement_one(seq):
        return ''.join([{'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}[s] for s in seq])[::-1]

    # reverse complement method 2
    @timeit
    def reverse_complement_two(seq):
        return seq.translate(str.maketrans('ATCG','TAGC'))[::-1]

    # --------------------------------------------

    print('sequence: {}'.format(sequence))

    # complement
    print('---')
    print('only complement')
    print('---')
    complement_one(sequence)
    complement_two(sequence)

    # reverse complement
    print('\n---')
    print('reverse complement')
    print('---')
    reverse(complement_one(sequence))
    reverse(complement_two(sequence))

    # reverse complement optimization
    print('\n---')
    print('reverse complement optimization')
    print('---')
    reverse_complement_one(sequence)
    reverse_complement_two(sequence)
