# Augmented Reality
***A basic augmented reality card based application in Python. This is a fork of [juangallostra's repo](https://github.com/juangallostra/augmented-reality).***

## A Brief History

When I first started learning OpenCV/Computer Vision and was looking for ideas to implement and/or implement OpenCV, I made the connection to Augmented Reality. And AR is something that has always fascinated me. So, when I realised I was in fact learning the know-how for AR, I just had to test it out. 


So, when I first started out, little did I know that I had loads more to learn before I could *"jump in"* :sweat_smile:. But I have to admit, this was ~~a good starting point~~ an interesting project to delve into, it taught me about keypoint feature extraction and orb matching.



**Updates**
-  Code works on Python3 only now
-  updated parameters in keypoint matching for improved accuracy. And a better filter for good matches. The updates and testing can be found in ```orbmatch.py``` and ```orbmatch_video.py```


<!--
## Usage [OLD]

* Place the image of the surface to be tracked inside the `reference` folder.
* On line 36 of `src/ar_main.py` replace `'model.jpg'` with the name of the image you just copied inside the `reference` folder.
* On line 40 of `src/ar_main.py` replace `'fox.obj'` with the name of the model you want to render. To change the size of the rendered model change the scale parameter (number `3`) in line 103 of `src/ar_main.py` by a suitable number. This might require some trial and error.
* Open a terminal session inside the project folder and run `python src/ar_main.py`


### Command line arguments [OLD]

* `--rectangle`, `-r`: Draws the projection of the reference surface on the video frame as a blue rectangle.
* `--matches`, `-m`: Draws matches between reference surface and video frame.

 
## Troubleshooting

**If you get the message**:

```
Unable to capture video
```
printed to your terminal, the most likely cause is that your OpenCV installation has been compiled without FFMPEG support. Pre-built OpenCV packages such as the ones downloaded via pip are not compiled with FFMPEG support, which means that you have to build it manually.

**If you get the error**:

```
Traceback (most recent call last):
File "src/ar_main.py", line 174, in
main()
File "src/ar_main.py", line 40, in main
obj = OBJ(os.path.join(dir_name, 'models/fox.obj'), swapyz=True)
File "[...]/augmented-reality/src/objloader_simple.py", line 16, in init
v = v[0], v[2], v[1]
TypeError: 'map' object is not subscriptable
```
The most likely cause is that you are trying to execute the code with Python 3 and the code is written in Python 2. The `map` function in Python 3 returns an iterable object of type map, and not a subscriptible list. To fix it, change the calls to `map()` by `list(map())` on lines 14, 19 and 24 of `src/objloader_simple.py`.  -->

## Explanation

See this blog entries for an in-depth explanation of the logic behind the code:

* [Part 1](https://bitesofcode.wordpress.com/2017/09/12/augmented-reality-with-python-and-opencv-part-1/)
* [Part 2](https://bitesofcode.wordpress.com/2018/09/16/augmented-reality-with-python-and-opencv-part-2/)


## Results

<span style="display:block;text-align:center">![A 3D model of a wolf on a Robotics club logo](output.gif)</span>

## References
- [RD Milligan](https://rdmilligan.wordpress.com/2015/10/15/augmented-reality-using-opencv-opengl-and-blender/)
- [3D Models](https://clara.io/library)
- 