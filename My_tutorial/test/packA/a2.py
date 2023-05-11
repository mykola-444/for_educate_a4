import pkgutil
import sys

from .a1 import a1_func

print(sys.path)

search_path = ['.']  # Используйте None, чтобы увидеть все модули, импортируемые из sys.path
all_modules = [x[1] for x in pkgutil.iter_modules(path=search_path)]
print(all_modules)


def a2_func():
    print("Выполняем a2_func()")


fdf = a1_func()
