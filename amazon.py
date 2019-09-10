def test(A):
    import itertools
    a=list(itertools.permutations(A,2))
    re=0
    for i in a:
        r=i[0]%i[1]
    re=re+r
    return (re%(10**9+7))