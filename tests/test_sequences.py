from examples import sequences

def test_golomb_seq():
    assert sequences.golomb_seq(1) == [1]


def test_golomb_seq_lst():
    assert sequences.golomb_seq_lst(1) == [1]
    assert sequences.golomb_seq_lst(2) == [1, 2]
    assert sequences.golomb_seq_lst(3) == [1, 2, 2]

def test_golomb():
    n = 10**3
    lst = sequences.golomb_seq_lst(n)
    for i, item in enumerate(lst):
        assert item == sequences.golomb_seq(i)
