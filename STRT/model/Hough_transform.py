# taken from https://github.com/alyssaq/hough_transform/blob/master/hough_transform.py

import cv2
import numpy as np
from scipy import misc

def hough_line_img(img, angle_step=1):
    """
    Hough transform for lines
    Input:
    img - 2D binary image with nonzeros representing edges
    angle_step - Spacing between angles to use every n-th angle
      between -90 and 90 degrees. Default step is 1.
    Returns:
    accumulator - 2D array of the hough transform accumulator
    theta - array of angles used in computation, in radians.
    rhos - array of rho values. Max size is 2 times the diagonal
           distance of the input image.
    """
    # Rho and Theta ranges
    thetas = np.deg2rad(np.arange(-90.0, 90.0, angle_step))
    width, height = img.shape
    diag_len = np.ceil(np.sqrt(width * width + height * height))
    rhos = np.linspace(-diag_len, diag_len, diag_len * 2.0)
    
    # Cache some reusable values
    cos_t = np.cos(thetas)
    sin_t = np.sin(thetas)
    num_thetas = len(thetas)
    
    # Hough accumulator array of theta vs rho
    accumulator = np.zeros((2 * diag_len, num_thetas), dtype=np.uint64)
    y_idxs, x_idxs = np.nonzero(img)  # (row, col) indexes to edges
    
    # Vote in the hough accumulator
    for i in range(len(x_idxs)):
        x = x_idxs[i]
        y = y_idxs[i]
    
    for t_idx in range(num_thetas):
        # Calculate rho. diag_len is added for a positive index
        rho = round(x * cos_t[t_idx] + y * sin_t[t_idx]) + diag_len
        accumulator[rho, t_idx] += 1
    
    return accumulator, thetas, rhos


def hough_line_event(event, track_id=None, angle_step=1):
    """
    Hough transform for lines
    Input:
    event - Event class object from model.global_coords.data_structures
    angle_step - Spacing between angles to use every n-th angle
      between -90 and 90 degrees. Default step is 1.
    Returns:
    accumulator - 2D array of the hough transform accumulator
    theta - array of angles used in computation, in radians.
    rhos - array of rho values. Max size is 2 times the diagonal
           distance of the input image.
    """
    pixelize_step = 0.055
    rho_scale = 20
    
    xs = [int(h.x/pixelize_step / rho_scale) for h in event.hits]
    ys = [int(h.y/pixelize_step / rho_scale) for h in event.hits]
    xmin = min(xs)
    xmax = max(xs)
    ymin = min(ys)
    ymax = max(ys)
    
    track = event.get_track(track_id)
    if track is not None:
        xs = map(lambda i: xs[i], track.hit_indices)
        ys = map(lambda i: ys[i], track.hit_indices)
    
    # Rho and Theta ranges
    thetas = np.deg2rad(np.arange(-90.0, 90.0, angle_step))
    width = xmax - xmin
    height = ymax - ymin
    diag_len = np.ceil(np.sqrt(width * width + height * height))
    rhos = np.linspace(-diag_len, diag_len, diag_len)
    
    # Cache some reusable values
    cos_t = np.cos(thetas)
    sin_t = np.sin(thetas)
    num_thetas = len(thetas)
    
    # Hough accumulator array of theta vs rho
    accumulator = np.zeros((2*diag_len+1, num_thetas), dtype=np.uint64)
    y_idxs, x_idxs = ys, xs
    
    rho_inds = []
    # Vote in the hough accumulator
    for i in range(len(x_idxs)):
        x = x_idxs[i] - xmin
        y = y_idxs[i] - ymin
     
        for t_idx in range(num_thetas):
            # Calculate rho. diag_len is added for a positive index
            rho = round(x * cos_t[t_idx] + y * sin_t[t_idx]) + diag_len
#             rho_inds.append(rho)
            accumulator[rho, t_idx] += 1
    dump_lines(event)
    return accumulator, thetas, rhos


# def show_hough_line(img, accumulator):
#     import matplotlib.pyplot as plt
#     
#     fig, ax = plt.subplots(1, 2, figsize=(10, 10))
#     
#     ax[0].imshow(img, cmap=plt.cm.gray)
#     ax[0].set_title('Input image')
#     ax[0].axis('image')
#     
#     ax[1].imshow(
#         accumulator, cmap='jet',
#         extent=[np.rad2deg(thetas[-1]), np.rad2deg(thetas[0]), rhos[-1], rhos[0]])
#     ax[1].set_aspect('equal', adjustable='box')
#     ax[1].set_title('Hough transform')
#     ax[1].set_xlabel('Angles (degrees)')
#     ax[1].set_ylabel('Distance (pixels)')
#     ax[1].axis('image')
#     
#     #plt.axis('off')
#     plt.savefig('imgs/output.png', bbox_inches='tight')
#     plt.show()
    

def dump_lines(event):
    pixelize_step = 0.055
    
    xs = [int(h.x/pixelize_step) for h in event.hits]
    ys = [int(h.y/pixelize_step) for h in event.hits]
    xmin = min(xs)
    xmax = max(xs)
    ymin = min(ys)
    ymax = max(ys)
    bin_img = np.zeros((ymax-ymin+1, xmax-xmin+1), dtype=np.uint8)
    for i in range(len(xs)):
        xp = xs[i] - xmin
        yp = ys[i] - ymin
        bin_img[yp, xp] = 1

    lines = cv2.HoughLinesP(image=bin_img,
                            rho=0.02,
                            theta=np.pi/500, 
                            threshold=10,
                            lines=np.array([]))

  
  
  
