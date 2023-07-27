


def KaisaEncrypt(ch, k):
    if (not isinstance(ch, str)) or len(ch) != 1:
        print("The first parameter must be a character!")
        return
    if (not isinstance(k, int)) or (not 1<=k<=25):
        print("The second parameter must be an integer between 1 and 25.")
        return
    if "a"<=ch<=chr(ord("z")-k):
        return chr(ord(ch)+k)

pass