def eval(o,a,b) :
  if o == '+' :
    return str(float(a)+float(b))
  if o == '-' :
    return str(float(a)-float(b))
  if o == '*' :
    return str(float(a)*float(b))
  if o == '/' :
    return str(float(a)/float(b))
  if o == '**' :
    return str(float(a)**float(b))

def EvaluateExpression(exp) :
  op = ['+','-','*','/','**']
  stack = list()
  exp = exp + ' '
  i = 0
  while( i < len(exp)) :
    if exp[i] == ' ' :
      pass
    else :
      j = i
      while(exp[j] != ' ') :
        j += 1
      if exp[i:j] in op :
        b = stack.pop(0)
        a = stack.pop(0)
        c = eval(exp[i:j],a,b)
        stack.insert(0,c)
        i = j+1
      else:
        stack.insert(0,exp[i:j])
        i = j+1      
  return stack[0]
