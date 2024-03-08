import numpy as np

# evaluate at x = 2
function_1 = np.poly1d([2,3,0,1])
print(np.poly1d(function_1))
print(function_1(2))

#%%
#find the deriv
# evaluate deriv at 1
import numpy as np
function_2 = np.poly1d([1,1])
function_2_deriv = np.polyder(function_2)
print(function_2(1))

#Part 2
#%%
import numpy as np

# Input coefficients, as a string
coefficients_str = input("Enter the coefficients of the polynomial separated by commas: ")
coefficients = [float(coeff) for coeff in coefficients_str.split(',')]
f = np.poly1d(coefficients)  # turn coefficients into polynomial
print("Polynomial: ", f)  

x_1 = float(input("Give a value for x_1: "))

def eval_poly(poly, x):
    return np.polyval(poly, x)

def eval_der(poly, x):   #evaluate derivative
    der = np.polyder(poly)
    return np.polyval(der, x)

def newtons_method(poly, x_n, iteration=1): 
    f_x_n = eval_poly(poly, x_n)    #formula for Newton's method
    f_x_p = eval_der(poly, x_n)
    x_n_p = x_n - f_x_n / f_x_p

    print(f"x_{iteration}={x_n_p:.3f}")

    if abs(x_n_p - x_n) < 0.001:    
        return int(x_n_p * 1000) / 1000  #stabilized thousandths, 3 decimal places
    else:
        return newtons_method(poly, x_n_p, iteration + 1)

print("The final value with stabilized thousandths is:", newtons_method(f, x_1))
roots = np.roots(coefficients)
print(roots)   #outputs roots of polynomial
