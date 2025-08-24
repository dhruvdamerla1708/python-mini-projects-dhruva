import numpy as np

def main():
    print('Welcome To Grid Analyzer\n')
    r = int(input('Enter the number of rows:'))
    c = int(input('Enter the number of columns:'))
    a = input(f'\nEnter {r*c} numbers seperated by space:\n').split(' ')
    new_a = [int(i) for i in a]
    arr = np.array(new_a)
    new_arr = arr.reshape(r, c)

    print(f'\nYour Grid:\n{new_arr}')
    print(f'\nGrid Summary:\n-Total Elements: {new_arr.size}\n-Grid Shape: {new_arr.shape}\n-Grid Dimesions: {new_arr.ndim}\n-Data Type: {new_arr.dtype}\n')

    print(f'Statistical Info:\n-Sum of all values: {np.sum(new_arr)}\n-Mean Value: {np.mean(new_arr)}\n-Minimum Value: {np.min(new_arr)}\n-Maximum Value: {np.max(new_arr)}\n')

    even = np.array([i for i in arr if i % 2 == 0])
    odd = np.array([i for i in arr if i % 2 == 1])

    print(f'Filtered Views:\n-Even numbers: {even}\n-Odd numbers: {odd}\n')

    print(f'Reshaped Grid({c},{r}):\n{arr.reshape(c, r)}\n')

main()
