def caching_fibonacci():
    cache = {} #Створення порожній словник кешу
    def fibonacci(n): #Створення внуьрішньої функції 
        if n in cache: # Перевіряємо чи число вже є у кеші
            return cache[n]
        if n <= 1:
            return n
        #Обчислюємо число Фібоніччі за допомогою рекурсії
        result = fibonacci(n - 1) + fibonacci(n - 2)
        cache[n] = result #Зберігаємо результат у кеші 
        return result
    return fibonacci

fib = caching_fibonacci()

print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610