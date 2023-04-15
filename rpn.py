from Token import Token

stack = []
tokens = []
f = open("Calc1.stk", "r")
for line in [l.rstrip() for l in f.readlines()]:    
    try:
        tokens.append(Token(line))
        index = len(tokens) - 1   
        print(tokens[index].toString())   
        #print(index)
        if(tokens[index].type == "NUM"):
            stack.append(int(tokens[index].lexeme))
        elif(len(stack)>=2):
            if(tokens[index].type == "STAR"):
                stack.append(stack.pop()*stack.pop())
            elif(tokens[index].type == "SLASH"):
                stack.append(int(1/stack.pop()*stack.pop()))
            elif(tokens[index].type == "MINUS"):
                stack.append((-stack.pop()) + stack.pop())
            elif(tokens[index].type == "PLUS"):
                stack.append(stack.pop()+stack.pop())
        else:
            print("Não há números o suficiente para executar as operações, o último valor calculado foi: "+str(stack.pop()))
            break
    except Exception as error:
        print(error)         
    

if(len(stack) == 1):
    print(stack.pop())
elif(len(stack) > 1):
    print("Sobraram estes números na pilha: "+str(stack))