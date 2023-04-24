from scan import scan

stack = []
tokens = scan("Calc1.stk")
for token in tokens:
    if(token.type == "NUM"):
        stack.append(int(token.lexeme))
    elif(len(stack)>=2):
        if(token.type == "STAR"):
            stack.append(stack.pop()*stack.pop())
        elif(token.type == "SLASH"):
            stack.append(int(1/stack.pop()*stack.pop()))
        elif(token.type == "MINUS"):
            stack.append((-stack.pop()) + stack.pop())
        elif(token.type == "PLUS"):
            stack.append(stack.pop()+stack.pop())
    else:
        print("Não há números o suficiente para executar as operações, o último valor calculado foi: "+str(stack.pop()))
        break
    

if(len(stack) == 1):
    print(stack.pop())
elif(len(stack) > 1):
    print("Sobraram estes números na pilha: "+str(stack))