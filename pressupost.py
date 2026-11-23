def my_function(parametro: list):
    # Se haran cositas
    parametro[2] += 4

def my_funcion2(parametro: int):
    parametro += 4
    

my_variable = [1, 2, 3, 4, 5, 6]
my_variable2 = 5

print(my_variable) # [1, 2, 3, 4, 5, 6]
print(my_variable2) # 5

my_function(my_variable)
my_funcion2(my_variable2)

print(my_variable) #[1, 2, 7, 4, 5, 6]
print(my_variable2) #5
