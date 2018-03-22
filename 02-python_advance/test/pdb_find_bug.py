import pdb
# python3 -m pdb myscripts.py

def add3Nums(a1, a2, a3):
    result = a1 + a2 + a3
    return result

def get3NumsAverage(s1, s2):
    s3 = s1 + s2 + s1
    result = 0 
    result = add3Nums(s1, s2, s3)/3
    return result

if __name__ == "__main__":

    a = 11
    pdb.set_trace()
    b = 12

    final = get3NumsAverage(a,b)
    print(final)
