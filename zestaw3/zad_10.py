
def roman2Int(roman): 
  values =	{"I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000}
  values=dict(zip(["I","V","X","L","C","D","M"],[1,5,10,50,100,500,1000]))
  total = 0
  prev=values[roman[0]]
  
  for item in roman[1:]:
    current_value = values[item]
    if (prev >= current_value): 
      total = total + prev
    else:
      total = total - prev
    prev=current_value
  total=total+prev
 
  return total
  
assert roman2Int("MMMDCCXXIV")==3724

