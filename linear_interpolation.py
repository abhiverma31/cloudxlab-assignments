import matplotlib.pyplot as plt
import numpy as np

# Exercise
# Create magnify image
# factor: convert 2 pixels to these many pixels
# For example, factor = 4, convert 2 -> 4 pixels
# Image: numpy array represening a greyscale
def magnify(image_py, factor):
    
    #image_py = image.toList()
    rows = len(image_py)
    columns = len(image_py[0])
    
    outer_matrix = []
    # rows
    for i, item in enumerate(image_py):
        # item is a list
        new_row = []         
        for j, item_ in enumerate(item):
            if (j < len(item) - 1):
                diff = item[j+1] - item[j]
                interval = diff / (factor - 1)
                appended_pixels = add_new_pixels(item_, interval, factor - 1)
                for cell in appended_pixels:
                    new_row.append(cell)
                
        #print()                        
        appended_pixels = []
        new_row.insert(0, image_py[i][0])        
        outer_matrix.append(new_row)
    
    return outer_matrix
            
            
def add_new_pixels(item_, interval, factor):
    new_row = []
    
    new_pixel = item_
    m = 0
    while m < factor:
        new_pixel += interval
        new_row.append(new_pixel)
        m += 1
    
    #print(new_row)    
    return new_row

def linear_interpolation(img_py, factor):
    # row interpolation
    image_matrix = magnify(img_py, factor)
    transpose = np.array(image_matrix).T
    
    # column interpolation
    image_matrix = magnify(transpose.tolist(), factor)
    #print(np.array(image_matrix).T.astype(int))
    return np.array(image_matrix).T.astype(int)

def test_linear_interpolation():
    bird = plt.imread("eagle_bird.jpg")    
    red_bird_2d = bird[:,:,0]
    # python list
    red_bird_2d = red_bird_2d.tolist()
    
    scaled_up_image = linear_interpolation(red_bird_2d, 4)
    # plt.imshow(red_bird_2d, cmap='gray')
    # plt.show()
    # print()
    # plt.imshow(scaled_up_image, cmap='gray')
    # #plt.imshow(img)
    # plt.show()
    
    plt.figure()
    plt.imshow(red_bird_2d, cmap='gray')
    plt.title("Original")
    #plt.show()

    plt.figure()
    plt.imshow(scaled_up_image, cmap='gray')
    plt.title("Scaled Up")
    
    plt.show()
    

if __name__ == "__main__":
    test_linear_interpolation()
    