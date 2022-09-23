def two_sum ( arr: list , target: int ) -> list :
    for i in range ( len ( arr ) - 1 ) :
        for j in range ( i + 1 , len ( arr ) ) :
            if arr [ i ] + arr [ j ] == target :
                return [ i , j ]
        return [ -1 , -1 ]


def balance_pair(brackets: str) -> bool:
    # if brackets.strip() == "" or len(brackets) % 2 == 1:
      if not brackets or len(brackets) % 2 == 1:
          return False
      stack = []
      for bracket in brackets :
          if bracket in "{[(" :
              stack.append ( bracket )
          elif bracket in "}])" :
              peek = stack [ -1 ]
              if peek == "{" and bracket == "}" :
                  stack.pop ( )
              elif peek == "[" and bracket == "]" :
                  stack.pop ( )
              elif peek == "(" and bracket == ")" :
                  stack.pop()
              else:
                  return False
          else:
                return False

print(balance_pair("{[]}"))


