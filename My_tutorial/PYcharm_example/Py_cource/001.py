def shout(word="да"):
    return word.capitalize()+"!!!"
 
print (shout())
# выведет: 'Да!'
 
# Так как функция - это объект, вы связать её с переменнной,
# как и любой другой объект
scream = shout
 
# Заметьте, что мы не используем скобок: мы НЕ вызываем функцию "shout",
# мы связываем её с переменной "scream". Это означает, что теперь мы
# можем вызывать "shout" через "scream":
 
print (scream())
# выведет: 'Да!'

# Более того, это значит, что мы можем удалить "shout", и функция всё ещё
# будет доступна через переменную "scream"
 
del shout
try:
    print (shout())
except NameError as e:
    print (e)
    #выведет: "name 'shout' is not defined"
 
print (scream())
# выведет: 'Да!'

def getTalk(type="shout"):
 
    # Мы определяем функции прямо здесь
    def shout(word="да"):
        return word.capitalize()+"!"
 
    def whisper(word="да") :
        return word.lower()+"...";
 
    # Затем возвращаем необходимую
    if type == "shout":
        # Заметьте, что мы НЕ используем "()", нам нужно не вызвать функцию,
        # а вернуть объект функции
        return shout
    else:
        return whisper
 
# Как использовать это непонятное нечто?
# Возьмём функцию и свяжем её с переменной
talk = getTalk()
 
# Как мы можем видеть, "talk" теперь - объект "function":
print (talk)
# выведет: <function shout at 0xb7ea817c>
 
# Который можно вызывать, как и функцию, определённую "обычным образом":
print (talk())
 
# Если нам захочется - можно вызвать её напрямую из возвращаемого значения:
print (getTalk("whisper")())
# выведет: да...



def doSomethingBefore(func):
    print ("Я делаю что-то ещё, перед тем как вызвать функцию, которую ты мне передал")
    print (func())
 
doSomethingBefore(scream)

#выведет:
# Я делаю что-то ещё, перед тем как вызвать функцию, которую ты мне передал
# Да!
