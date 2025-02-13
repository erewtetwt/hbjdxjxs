import timeit
code_to_test = """
for i in range(100000):
    y=10&1
"""
execution_time = timeit.timeit(code_to_test, number=1000)
print(f"Время выполнения: {execution_time / 1000:.8f} секунд")
