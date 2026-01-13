import re
#* con los [] indicas de aqui a qui y el {} seria la repetición y necesita la r delante

"""
hay 3 funciones
match = al principio
search = es buscar en cualquier parte de la cadena
fullmatch = toda la cadena entera
"""

correcto = f""""
============================
Vamoos felicidades🎊
tu numero de telefono es correcto
============================
"""
incorrecto = f"""
=============================
tu numero es incorrecto,
muy mal, nos estas intentado engañar.
😔😔😔😔😔😔😔😔
=============================
"""
patron=r"[6-8][0-9]{8}"
num1 = "651112345"
num2 = "908654789"

#*esto es con el match valida al principio
#! ojo no poner un '==' porque no es true ni false, devuelve un objeto.
print(f"""
soy el match que busco siempre al principio
""")
if re.match(patron,num1):
    print(correcto)
    print("num1")
else:
    print(incorrecto)
    print("num1")

if re.match(patron,num2):
    print(correcto)
    print("num2")
else:
    print(incorrecto)
    print("num2")

#* con el search busca en cualquier parte en la cadena, cualquier cosa que coincida en el patrón
print(f"""
soy search busco cualquier validación que sea igual, no importan que donde este
""")
if re.search(patron,num1):
    print(correcto)
    print("num1")
else:
    print(incorrecto)
    print("num1")

if re.search(patron,num2):
    print(correcto)
    print("num2")
else:
    print(incorrecto)
    print("num2")

print(f"""
soy el fullMatch, yo si necesito que validez todo el patrón. Soy el mejor para validad
""")
if re.fullmatch(patron,num1):
    print(correcto)
    print("num1")
else:
    print(incorrecto)
    print("num1")

if re.fullmatch(patron,num2):
    print(correcto)
    print("num2")
else:
    print(incorrecto)
    print("num2")

print(f"""
Validamos letras, como los siguientes ejemplo
""")

#* esta es la forma de validar todas las expresiones relgulares con cadenas
#*aqui valida todas el abaccerario de mayuzculas, menores, la Ñ y todas las vocales acentuadas
patron2 = r"[A-Za-zÑàeòùÀÈÌÒÙ]{4,8}"
texto = "ABRDFGI8L"

if re.fullmatch(patron2, texto):
    print("es Valido")
else:
    print("No es valida")

print(f"""
Como en xml existe un tiene formatos como en esa forma
? algo o nada, es opcional, puede aparecer cero o mas veces
* puede aparecer ninguna o varias veces
+ igual que el * pero debe aparecer por lo menos una vez
""")
praton3=r"[0-9]{4}[\s|-]?[B-DF-HJL-NPR-TV-z]{3}"
matricula ="1234 MXP"

if re.fullmatch(praton3,matricula):
    print("Es valido")
else:
    print("No es valido")

patron4=r"[^579]" #* prohibe cualquier caracter de lo siguientes




"""
| Cuantificador | Significado          | Ejemplo  | Coincide con                         |
| ------------- | -------------------- | -------- | ------------------------------------ |
| `?`           | 0 o 1 vez (opcional) | `a?`     | `""` o `"a"`                         |
| `*`           | 0 o más veces        | `a*`     | `""`, `"a"`, `"aa"`, `"aaa"`         |
| `+`           | 1 o más veces        | `a+`     | `"a"`, `"aa"`, `"aaa"` (no `""`)     |
| `{n}`         | Exactamente n veces  | `a{3}`   | `"aaa"`                              |
| `{n,}`        | Al menos n veces     | `a{2,}`  | `"aa"`, `"aaa"`, `"aaaa"`            |
| `{n,m}`       | Entre n y m veces    | `a{2,4}` | `"aa"`, `"aaa"`, `"aaaa"` (no `"a"`) |

? → opcional, 0 o 1 vez
* → cualquier número, incluso cero
+ → al menos una vez
{n,m} → repeticiones exactas o en rango
() → agrupa para repetir bloques o alternancia
| → “o” lógico, funciona mejor con paréntesis para agrupar varias opciones
"""

# ? → opcional
print(bool(re.match(r"a?", "a")))    # True
print(bool(re.match(r"a?", "")))     # True

# * → 0 o más
print(bool(re.match(r"a*", "aaa")))  # True

# + → 1 o más
print(bool(re.match(r"a+", "")))     # False

# {n,m} → entre n y m
print(bool(re.match(r"a{2,4}", "aaa")))  # True

# () + cuantificador
print(bool(re.match(r"(ab){2}", "abab")))  # True

# | → alternancia
print(bool(re.match(r"a|b", "a")))  # True

# () + | → grupo alternativo
print(bool(re.match(r"(abc|de){2}", "abcde")))  # True