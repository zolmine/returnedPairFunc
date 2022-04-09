from numba import jit
from newFunc import func2


func2Compiled = jit(forceobj=True) (func2)

func2Compiled("0x2e2DDe47952b9c7deFDE7424d00dD2341AD927Ca","0x8f3Cf7ad23Cd3CaDbD9735AFf958023239c6A063")