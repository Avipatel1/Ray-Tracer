# Ray-Tracer
Ray tracer in python
The code comments thoroughly explain how the image creation process works.
----------------------------------------------------------------------------------------
To execute: Be in the folder of the python file, go to command line and execute as example below:
	    -In cmd line:  python .\RayTracer.py .\testIllum.txt
	    -This will use raytracer.py to parse and create the image from testIllum.txt
----------------------------------------------------------------------------------------
These are the times it takes to generate each image for my laptop:
Using python with numpy and sys imports (pip install if needed)
----------------------------------------------------------------------------------------
min:sec - image name
1:08 - ambient
1:44 - background
0:57 - behind
1:06 - diffuse
1:26 - illum
0:31 - imgplane
1:30 - intersection
1:05 - parsing
1:07 - reflection
1:06 - sample
0:59 - shadow
1:07 - specular
----------------------------------------------------------------------------------------
All of the images can be viewed on GIMP (or online viewer, but results might vary for this)
----------------------------------------------------------------------------------------
Want to skip the image creation time? ->All the .ppm images are generated and in the folder for easy viewing!
----------------------------------------------------------------------------------------
[2] Coding Style (i.e. well designed, clean, & commented code with functions) -Done
- The code is in python and is very clean and well commented such that any person with moderate python understanding can interpret it
----------------------------------------------------------------------------------------
[2] x 12 For each of the given test cases. We will visually verify each and check your code. The name of each test case file is a hint at what we are looking for. - Done
----------------------------------------------------------------------------------------
AMBIENT: perfectly aligns with keyAmbient.png
----------------------------------------------------------------------------------------
BACKGROUND: perfectly aligns with keyBackground.png
----------------------------------------------------------------------------------------
BEHIND: perfectly aligns with keybehind.png
----------------------------------------------------------------------------------------
DIFFUSE: almost-perfectly aligns with keyDiffuse.png (The shadows are a bit darker in mine, but it seems fine to me, judge for 	 	 yourself)
----------------------------------------------------------------------------------------
ILLUM: almost-perfectly aligns with keyIllum.png (The shadows are a bit darker, and GIMP makes the image more "crisp", while 	using https://www.cs.rhodes.edu/welshc/COMP141_F16/ppmReader.html, makes this image look a little better). Again, I think 	it looks fine, but judge for yourself
----------------------------------------------------------------------------------------
IMGPLANE: perfectly aligns with keyImgPlane.png
----------------------------------------------------------------------------------------
INTERSECTION: perfectly aligns with keyIntersection.png
----------------------------------------------------------------------------------------
PARSING: almost-perfectly aligns with keyParsing.png (GIMP makes this a bit crisper, but https://www.cs.rhodes.edu/welshc/COMP141	_F16/ppmReader.html makes it look a bit better). The shadow on the red sphere is round in mine, but straight in the key 	as well. Looks fine to me, but judge it yourself
----------------------------------------------------------------------------------------
REFLECTION: almost-perfectly aligns with keyReflection.png (GIMP makes the reflections pointy, otherwise it looks fine)
	And for some reason (https://www.cs.rhodes.edu/welshc/COMP141_F16/ppmReader.html) doesn't show the red sphere, but GIMP 	does.
----------------------------------------------------------------------------------------
SAMPLE: Same result as PARSING
----------------------------------------------------------------------------------------
SHADOW: almost-perfectly aligns with keyShadow.png (The shadows are a bit darker, and the blue sphere shadow is curved and not straight. Other than those two issues, it looks fine.)
----------------------------------------------------------------------------------------
SPECULAR: almost-perfectly aligns with keySpecular.png (The colors are a bit smaller, but same intensity as key. Otherwise, it 	looks fine)
----------------------------------------------------------------------------------------
[-4 Marks if not] Provide a readme.txt that describes what you have done, what you have omitted, and any other information that will help the grader evaluate your work, including what is stated below. - Done
