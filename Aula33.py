"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""
string = "luiz Otavio"
outra_variavel = f'{string[0:3]}ABC{string[4:]}'
#string[3]= "ABC"S
print(outra_variavel)
print(string.capitalize())
print(string.zfill(100))
