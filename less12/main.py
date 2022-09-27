import multiprocessing
import time
from multiprocessing import Pipe


def getter(pipe):
    out, inp = pipe
    inp.close()
    while True:
        try:
            print("data: ", out.recv())
        except:
            break


def setter(sequence, inp):
    for item in sequence:
        time.sleep(0.4)
        inp.send(item)


if __name__ == "__main__":
    output_c, input_c = Pipe()
    g = multiprocessing.Process(target=getter, args=((output_c, input_c),))
    g.start()

    setter([1, 2, 3, 4, 5], input_c)
    output_c.close()
    input_c.close()
