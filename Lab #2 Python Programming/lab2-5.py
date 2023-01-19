def only_english(string1):
    return "".join([text for text in string1 if ord("A")<= ord(text) <= ord("Z") or ord("a") <= ord(text) <= ord("z")  ])