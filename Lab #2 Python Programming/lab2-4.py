def count_minus(str):
    return len([number for number in [int(text)for text in str.split()] if number < 0])