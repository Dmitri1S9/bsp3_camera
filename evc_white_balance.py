# Copyright TU Wien (2022) - EVC: Task3
# Computer Vision Lab
# Institute of Computer Graphics and Algorithms

import numpy as np

def evc_white_balance(input_image: np.ndarray, white: np.ndarray) -> np.ndarray:
    """evc_white_balance performs white balancing manually.
    
      INPUT
      input_image ... image
      white       ... a color (as RGB vector) that should become the new white
    
      OUTPUT
      result      ... result after white balance"""
    
    
    ### STUDENT CODE
    # TODO: perform white balancing using the 'white' variable
	  # HINT: Make sure the program does not crash if 'white' is zero!
    # NOTE: pixels brighter than 'white' will have values > 1.
    #       This requires a normalization which will be performed
    #       during the histogram clipping.
    # NOTE: The following line can be removed. It prevents the framework
    #       from crashing.
    r_white, g_white, b_white = white
    result = np.copy(input_image)
    r_white = 1e-10 if r_white == 0 else r_white
    g_white = 1e-10 if g_white == 0 else g_white
    b_white = 1e-10 if b_white == 0 else b_white

    result[:, :, 0] /= r_white
    result[:, :, 1] /= g_white
    result[:, :, 2] /= b_white
    ### END STUDENT CODE
    
    result = np.minimum(result, 1)
    return result
