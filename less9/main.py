
import random
import multiprocessing


def end_func(response):
    print('end func:', response)


def out(x, y, z):
    print(f"value: {x} {y} {z}")
    return x, y, z


if __name__ == "__main__":
    with multiprocessing.Pool(multiprocessing.cpu_count() * 3) as p:
        p.starmap(out, [(1, 2, 3), (4, 5, 6)])
        p.close()
        p.join()
