from typing import Iterable
import os



def prim_numbers(n: int) -> Iterable[int]:
    # Crazy implementation!
    with open(os.path.join(".", "src", "primes-to-100k.txt"), "r") as fp:
        prims = [int(l) for l in fp.readlines()]
    
    return [p for p in prims if p <= n]
