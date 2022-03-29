from scipy import optimize


def u(Z, F, E, fee):
    txFee = 10000 - fee
    return (Z*txFee*F) / ((E*10000) + (Z*txFee))


def z(Y, D, C, fee):
    txFee = 10000 - fee
    return (Y*txFee*D) / ((C*10000) + (Y*txFee))


def y(X, B, A, fee):
    txFee = 10000 - fee
    return (X*txFee*B) / ((A*10000) + (X*txFee))


def w1(X, A, B, fee1, C, D, fee2, verbose=True):
    Y = y(X, B, A, fee1)
    Z = z(Y, D, C, fee2)
    W = Z - X
    # if verbose:
    #     print("The value of y is", Y)
    #     print("The value of z is", Z)
    #     print("Value of w is", W)
    return W


def w2(X, A, B, fee1, C, D, fee2, E, F, fee3, verbose=True):
    Y = y(X, B, A, fee1)
    Z = z(Y, D, C, fee2)
    U = u(Z, F, E, fee3)
    W = U - X
    # if verbose:
    #     print("The value of y is", Y)
    #     print("The value of z is", Z)
    #     print("The value of u is", U)
    #     print("Value of w is", W)
    return W


def find_x_and_w(w_fn, verbose=True, **kwargs):
    def f(x): return w_fn(X=x, **kwargs, verbose=False) * -1
    x = optimize.minimize_scalar(f, bounds=(0, None)).x
    w = w_fn(X=x, **kwargs, verbose=False)
    if verbose:
        print("The value of x is", x)
        print("The value of w is", w)
    return x, w


# print("##### W1")
# find_x_and_w(w1, A=11000, B=10000,fee1=12, C=10000, D=11500,fee2=24)

# print("\n##### W2")
# find_x_and_w(w2, A=11000, B=10000, fee1=5, C=10000,
#              D=9000, fee2=14, E=9200, F=12500, fee3=26)
