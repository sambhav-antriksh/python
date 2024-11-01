#Smart way to find is the string a Palindrome
def is_pal(S):
  if len(S) == 1:
    return True
  if S[0] == S[-1]:
    return is_pal(S[1 : -1])
  else:
    return False
S='saippuakivikauppias' #a Finnish word meaning a dealer in lye or caustic soda.
print(is_pal(S))