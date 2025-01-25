def add_points(P, Q, a, p):
    if P == None:
        return Q
    
    if Q == None:
        return P
    
    if 
    
    xp, yp = P
    xq, yq = Q
    
    s = (yq - yp) * pow((xq - xp), -1, p) % p
    
    x = (pow(s, 2) - xp - xq) % p
    y = (s * (xp - x) - yp) % p
    return x, y
    