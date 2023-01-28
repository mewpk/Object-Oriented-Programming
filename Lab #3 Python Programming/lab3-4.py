def char_count(str):
  stringDict = {}
  for ch in str :
    try : 
      stringDict[ch] += 1
    except : stringDict.update({ch : 1})
  return stringDict