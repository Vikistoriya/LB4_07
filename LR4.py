import random
import matplotlib.pyplot as plt
import pandas as pd

def my_rand1(a, b, n):
 """Method 1: Using random.randint()
 """
 return [random.randint(a, b) for _ in range(n)]

def my_rand2(a, b, n):
 """Method 2: Using random.random()
 """
 return [int(random.random() * (b - a + 1)) + a for _ in range(n)]

def my_rand3(a, b, n):
 """Method 3: Using random.uniform()
 """
 return [int(random.uniform(a, b + 1)) for _ in range(n)]

def my_rand4(a, b, n):
 """Method 4: Using numpy.random.randint()
 """
 import numpy as np
 return np.random.randint(a, b + 1, size=n).tolist()

def my_rand5(a, b, n):
 """Method 5: Using numpy.random.rand()
 """
 import numpy as np
 return (np.random.rand(n) * (b - a + 1) + a).astype(int).tolist()

def my_rand6(a, b, n):
 """Method 6: Using random.choices()
 """
 return random.choices(range(a, b + 1), k=n)

def generate_and_plot(n_throws, methods, title):
 """
 Генерирует случайные числа с помощью разных методов и строит гистограммы
 """
 results = {}
 for method_name, method in methods.items():
  results[method_name] = method(1, 6, n_throws)

 df = pd.DataFrame(results)
 df.plot.hist(bins=6, alpha=0.7, color=['red', 'green', 'blue', 'cyan', 'magenta', 'yellow'], title=title)
 plt.xlabel('Value')
 plt.ylabel('Frequency')
 plt.show()

# Список методов, которые будут использоваться
methods = {
  "random.randint()": my_rand1,
  "random.random()": my_rand2,
  "random.uniform()": my_rand3,
  "numpy.random.randint()": my_rand4,
  "numpy.random.rand()": my_rand5,
  "random.choices()": my_rand6
}


# Выполнение кода для разных количеств бросков
n_throws_list = [100, 1000, 10000, 1000000]
for n_throws in n_throws_list:
 generate_and_plot(n_throws, methods, f"Гистограмма бросков кубика ({n_throws} бросков)")
