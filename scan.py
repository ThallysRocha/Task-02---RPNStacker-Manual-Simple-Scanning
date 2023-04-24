from Token import Token

def scan(source):
    tokens = []
    f = open(source, "r")
    for line in [l.rstrip() for l in f.readlines()]:    
            tokens.append(Token(line))
    return tokens
               
    