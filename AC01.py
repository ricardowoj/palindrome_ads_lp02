def eh_palindrome(txt):
    for i in range(len(txt)):
        if (txt[i] != txt[len(txt) - i - 1]):
            return False
        return True

inputs = ['arara', 'elefante', 'banana', 'caraarac']
palindromos = list()

for p in inputs:
    if(eh_palindrome(p)):
        palindromos.append(p)

print(palindromos)