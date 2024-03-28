a = "A"
b = "B"
c = 1.1
string = "a = {nome3} b = {nome2} c = {nome3:.2f}"
formato = string.format(
    
    a, nome2=  b, nome3 = c # Nomeação de parâmetros, vira regra
    
    )
print (formato)

# Quando der erro "Outside of range" quer dizer 
# não tem dado atribuído