# Exercise Image Manipulation

1. Import the library `Image` from `PIL`, `numpy` and `matplotlib.pyplot`.
2. Create a function named `show_image` that accepts two parameters: `image_array` which will be a numpy array storing an image, and `show_info` which defaults to `True`. This function must:

- Set variable `cmap` to `viridis`. If the `image_array`'s shape has 2 elements set it to `gray`.
- If `show_info` is `True` print the shape of the `image_array`.
- Show the `image_array` as an image, using appropriate cmap. Turn off any axis.

3. Use `PIL` to open the image `cat.jfif`. Convert it to a numpy array and display it with information.

4. Convert the image to grayscale. This can be done in to steps:

- Each channel (red, green, blue) must be multiplied by luminosity value and the results totaled. So from a 3D array, we end up with a 1D array of colours. Formula is $ grayscale = 0.2989*red + 0.5870*green + 0.1140*blue $
- Make sure to convert all values to `uint8`.

5. Flip the image vertically from left to right using numpy. Show it.

6. Create a function `crop_image` that accepts an `image_array`, and an other 4 paramters `start_row`, `end_row`, `start_col`, and `end_col`. Crop the image based on the passed parameters, show it, and return it.

7. Crop a part of the image and store it in `cropped_image`.

8. Convert the `cropped_image` to a `PIL Image`, and save it to file.
