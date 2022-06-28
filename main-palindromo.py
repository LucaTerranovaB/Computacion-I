def palindromo(palabra):

# Recorrer palabra 
    for i in range(0, int(len(palabra))):

# Comparar palabra con inversa de palabra

        if palabra[i] != palabra[-i-1]:
            return False
        
        return True
# Ingresar palabra para la funcion
palabra = input("Escriba una palabra : ")
print(palindromo(palabra))