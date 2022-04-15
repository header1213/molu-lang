stack = []
storage = []

sourceCode = open('gugudan.molu', 'r', encoding='utf-8').read()

class MOLUERROR(Exception):
  def __init__(self):
    self.message = "몰?루 오류: 알 수 없는 오류."
  def __str__(self):
    return self.message
class NoLuError(MOLUERROR):
  def __init__(self):
    self.message = "몰? 오류: 닫는 '루'가 존재하지 않음."
class UnknownCommandError(MOLUERROR):
  def __init__(self, cmd):
    self.message = f"몰?루겠는 명령 오류: '{cmd}' 명령은 정의되지 않음."
class UnknownParameterError(UnknownCommandError):
  def __init__(self, p, l):
    self.message = f"몰?루겠는 매개변수 오류: 매개변수 '{p}'에서 '{l}'은 정의되지 않음."
class TooManyParametersError(MOLUERROR):
  def __init__(self, cmd, plen):
    self.message = f"너?무 많은 매개변수 오류: '{cmd}' 명령에는 최대 {plen}개의 매개변수가 허용됨."
class StackIndexError(MOLUERROR):
  def __init__(self, l):
    self.message = f"스?택 길이 오류: 스택에 {l}번째 값이 없음."
class NumberExecuteError(MOLUERROR):
  def __init__(self):
    self.message = "실?행 불가 오류: 수는 실행할 수 없음."
class OperateBunchError(MOLUERROR):
  def __init__(self):
    self.message = "연?산 불가 오류: 명령 덩어리는 연산할 수 없음."

def parameters(src):
  each = src.split(' ')
  res = []
  for p in each:
    if not p: continue
    i = 0
    for l in p:
      if l=='.': i+=1
      elif l==',': i-=1
      elif l=='?': i*=10
      else: raise UnknownParameterError(p, l)
    res.append(i)
  return res

def execute(cmd, params):
  plen = len(params)
  def checkLen(max):
    if plen > max: raise TooManyParametersError(max)
  
  if cmd=='?':
    if plen:
      for p in params: stack.append(p)
    else: stack.append(0)

  elif cmd=='!':
    checkLen(1)
    if plen == 1: print(stack.pop(-params[0]))
    else: print(stack.pop())
  
  elif cmd==':':
    checkLen(1)
    if plen == 1: print(chr(stack.pop(-params[0])))
    else: print(chr(stack.pop()))
  
  elif cmd=='.':
    checkLen(1)
    if plen == 1: stack.append(stack[-params[0]])
    else: stack.append(stack[-1])
  
  elif cmd==',':
    checkLen(2)
    if plen == 2: stack[-params[0]], stack[-params[1]] = stack[-params[1]], stack[-params[0]]
    elif plen == 1: stack[-1], stack[-params[0]] = stack[-params[0]], stack[-1]
    else: stack[-1], stack[-2] = stack[-2], stack[-1]
  
  elif cmd==';':
    checkLen(1)
    if plen == 1: stack.pop(-params[0])
    else: stack.pop()
  
  elif cmd in '+-*/':
    checkLen(1)
    if len(stack) < 1: raise StackIndexError(1)
    if type(stack[-1]) == str: raise OperateBunchError()
    if plen == 0 and len(stack) < 2: raise StackIndexError(2)
    if plen == 0 and type(stack[-2]) == str: raise OperateBunchError()
    
    if cmd=='+':
      if plen == 1: stack[-1] += params[0]
      else: stack[-2] += stack[-1]; stack.pop()
    elif cmd=='-':
      if plen == 1: stack[-1] -= params[0]
      else: stack[-2] -= stack[-1]; stack.pop()
    elif cmd=='*':
      if plen == 1: stack[-1] *= params[0]
      else: stack[-2] *= stack[-1]; stack.pop()
    elif cmd=='/':
      if plen == 1: stack[-1] /= params[0]
      else: stack[-2] /= stack[-1]; stack.pop()
  
  elif cmd=='~':
    checkLen(2)
    if plen:
      bunch = stack.pop(-params[0])
    else:
      bunch = stack.pop(-1)
    
    if type(bunch) != str:
      raise NumberExecuteError()

    if plen == 2:
      for p in range(params[1]):
        run(bunch)
    else:
      run(bunch)
  
  # print('stack:', stack)

def run(code):
  mol = lu = 0
  try:
    while code.find('몰', lu) != -1:
      mol = code.find('몰', lu)
      cmd = code[mol+1]

      if cmd in '?!.,;+-*/~':
        lu = code.find('루', mol)
        if lu == -1: raise NoLuError(cmd)
        execute(cmd, parameters(code[mol+2:lu]))
      elif cmd in '{}':
        findfrom = mol + 1
        while True:
          innermol = code.find('몰{', findfrom)
          innerlu = code.find('}루', findfrom)
          if innermol == -1 or innermol > innerlu: break
          else: findfrom = innerlu + 1
        lu = code.find('}루', findfrom)
        if lu == 0: raise NoLuError()
        stack.append(code[mol+2:lu])

        # print('stack:', stack)
      else:
        raise UnknownCommandError(cmd)
  except MOLUERROR as e:
    line = code[:mol].count('\n')+1
    letter = mol-code[:mol].rfind('\n')
    print(f"{e.message}({sourceCode==code and '최상단 함수' or '내부 함수'} {line}:{letter}~에서 발생)")
    exit(1)
  except Exception:
    raise MOLUERROR

run(sourceCode)

print('<RESULT>')
print('stack:', stack)
print('storage:', storage)