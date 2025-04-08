from main import *

def test_MED():
    for S, T in test_cases:
        assert fast_MED(S, T) == MED(S, T)

def test_align():
    for i in range(len(test_cases)):
        S, T = test_cases[i]
        align_S, align_T = fast_align_MED(S, T)
        print(f"\nAligning {S} and {T}:\n{align_S}\n{align_T}\nExpected:\n{alignments[i][0]}\n{alignments[i][1]}")
        assert (align_S == alignments[i][0] and align_T == alignments[i][1])

