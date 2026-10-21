import time

start = time.perf_counter()
total = sum(range(1_000_000_000))
end = time.perf_counter()
print(total)
print(f"Time taken : {end-start}")