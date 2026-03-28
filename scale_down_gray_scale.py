import matplotlib.pyplot as plt
import numpy as np

# do it the traditional way using python loops
# will attempt it using a numpy later 
def scale_down_by_half(arr):
    m = 0
    n = 0
    rows = len(arr)
    columns = len(arr[0])

    block_of_4 = []
    inner_array = []

    sum = 0
    while m < rows - 1:
        while n < columns - 1:
            sum += arr[m][n] + arr[m+1][n] + arr[m][n+1] + arr[m+1][n+1]
            n = n + 2                
            #print(sum/4)
            inner_array.append(sum/4)
            #block_of_4.append(sum/4)
            sum = 0
        block_of_4.append(inner_array)
        inner_array = []    
        m += 2
        n = 0
        
    return block_of_4


def test_scale_down():
    bird = plt.imread("eagle_bird.jpg")
    red_bird = bird[:,:,0]
    red_bird_2d_pythonic = red_bird.tolist()

    red_bird_scaled_down = scale_down_by_half(red_bird_2d_pythonic)
    red_bird_scaled_down = np.array(red_bird_scaled_down)

    print(f"Original shape -> {bird.shape}, Scaled down shape -> {red_bird_scaled_down.shape}")

if __name__ == "__main__":
    test_scale_down()
    