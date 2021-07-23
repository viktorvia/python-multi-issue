from multiprocessing import Pool, set_start_method

def f(x):
    return x*x

if __name__ == '__main__':
    set_start_method('spawn')
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))
        p.close()
        p.join()
