import pkgutil

from packA.subA import sa2

search_path = ['.']  # Используйте None, чтобы увидеть все модули, импортируемые из sys.path
all_modules = [x[1] for x in pkgutil.iter_modules(path=search_path)]
print(all_modules)

c = sa2.sa2_func()
