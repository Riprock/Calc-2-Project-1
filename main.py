
def main():
    p0 = .5


def formula(pn, k, i,start_i):# start_i will just be called a formula (pn, k ,i 0) as starting index will always be 0
    calculated_terms = []
    if(i == 30):
        print("A")
    else:
        print("p(n+1) = kp(n)(1-p(n)")
        print(4)
        nextp = (k*pn)(1-pn)
        i += 1
        calculated_terms.append(nextp)
        formula(nextp,k,i)