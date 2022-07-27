

x = [1,2,123,3,4,5,6]

def linear_search(input_list,element):
    for item in input_list:
        if item == element:
            return input_list.index(item)
    
    return "Not found"

print(x)

# Insert
# list_name.insert(index,value_to_insert)

x.insert(0,11)
x.insert(len(x),7) # O(n)
print(x)

# Append
# Add element to the end of a list
# list_name.add(value_to_append)

x.append(8) # O(1)
print(x)

# Extend
# Add list to another list
new_list = [11,22,33]

x.extend(new_list) # O(n)
print(x) 

# Slice
# list[inicio:fin]
# Si el primer elemento es negativo, comienza a contar del final de la lista

print(x[4:6])
print(x[-1:])

# Pop method
# list.pop(index of element to pop)
# también retorna el elemento que sacó

print(x.pop(0))
print(x)

# Delete method
# del list[index]

del x[-1:]
print(x)

# Remove method
# quita un elemento con base en su contenido, no su índice

x.remove(11)
print(x)

# Find element in list
# in operator

if 22 in x:
    print(x.index(22))
else:
    print("not found")
    
print(linear_search(x,33))
print(linear_search(x,22))


# Sorting a list
# no hay necesidad de volver a asignar la lista

x.sort()
print(x)

# Guardar la copia de una lista
# Si asignamos la lista a cualquier otra variable, hace una copia por referencia

reference_copy = x
x.sort(reverse=True)

print(x)
print(reference_copy)

# Pero si lo copiamos de la siguiente manera, hace una copia por valor

value_copy = x[:]
x.sort()

print(x)
print(value_copy)

# Para revolver aleatoriamente un arreglo

from random import shuffle
shuffle(x)
print(x)