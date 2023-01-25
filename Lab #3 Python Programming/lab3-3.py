def is_plusone_dictionary(d):
  index = False
  for key,value  in d.items() :
    if not index :
      index = key
    if key != index or value != key+1:
      return False
    index += 2
  return True