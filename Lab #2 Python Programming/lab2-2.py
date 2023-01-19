def count_char_in_string(x,c):
  return [len([text for text in list if text == c]) for list in x]