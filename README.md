# Ray-Tracer

A Python-based ray tracer for image creation and rendering.  
This project demonstrates ray tracing concepts and supports a variety of test cases for visual verification. The code is thoroughly commented to explain the image creation process.

---

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
- [Performance](#performance)
- [Viewing Images](#viewing-images)
- [Coding Style](#coding-style)
- [Test Cases & Results](#test-cases--results)
- [Additional Notes](#additional-notes)

---

## Features

- Written in Python
- Well-commented and clean code for clarity
- Supports multiple test cases and image generation
- Output images in `.ppm` format for easy viewing

---

## Getting Started

1. **Dependencies**:
    - Python 3.x
    - `numpy` and `sys` modules (install via `pip` if needed)

2. **Execution**:
    - Open a terminal in the project directory.
    - Run:
      ```
      python RayTracer.py testIllum.txt
      ```
      This command uses `RayTracer.py` to parse `testIllum.txt` and creates the corresponding image.

---

## Performance

Below are the benchmark times for generating each image on my laptop:

| Image Name    | Generation Time |
|---------------|----------------|
| ambient       | 1:08           |
| background    | 1:44           |
| behind        | 0:57           |
| diffuse       | 1:06           |
| illum         | 1:26           |
| imgplane      | 0:31           |
| intersection  | 1:30           |
| parsing       | 1:05           |
| reflection    | 1:07           |
| sample        | 1:06           |
| shadow        | 0:59           |
| specular      | 1:07           |

---

## Viewing Images

- All generated `.ppm` images are available in the project folder.
- Images can be viewed in [GIMP](https://www.gimp.org/) or using [this online PPM viewer](https://www.cs.rhodes.edu/welshc/COMP141_F16/ppmReader.html).  
  *Note: Results may vary between viewers.*

- **Want to skip image creation time?**  
  All `.ppm` images are pre-generated and available for easy viewing in the repository.

---

## Coding Style

- Code is well-designed, clean, and commented.
- Functions are used for clarity and maintainability.
- Anyone with moderate Python experience should be able to interpret and modify the code.

---

## Test Cases & Results

Each test case demonstrates a unique rendering feature. Images are visually verified against reference images.

- **AMBIENT:** perfectly aligns with `keyAmbient.png`
- **BACKGROUND:** perfectly aligns with `keyBackground.png`
- **BEHIND:** perfectly aligns with `keybehind.png`
- **DIFFUSE:** almost-perfectly aligns with `keyDiffuse.png` (shadows are a bit darker)
- **ILLUM:** almost-perfectly aligns with `keyIllum.png` (shadows are a bit darker; GIMP renders more "crisp")
- **IMGPLANE:** perfectly aligns with `keyImgPlane.png`
- **INTERSECTION:** perfectly aligns with `keyIntersection.png`
- **PARSING:** almost-perfectly aligns with `keyParsing.png` (GIMP makes it crisper; online viewer shows different shadow edges)
- **REFLECTION:** almost-perfectly aligns with `keyReflection.png` (reflections look pointy in GIMP; red sphere shows in GIMP but not in online viewer)
- **SAMPLE:** same result as PARSING
- **SHADOW:** almost-perfectly aligns with `keyShadow.png` (shadows darker; blue sphere shadow is curved)
- **SPECULAR:** almost-perfectly aligns with `keySpecular.png` (color spots are smaller, but intensity matches)

---

## Additional Notes

- Please refer to the code comments for a deeper understanding of the ray-tracing process.
- If you have questions, suggestions, or would like to contribute, feel free to open an issue or pull request.

---

## License

This project is for educational purposes. Please contact the repository owner for usage inquiries.
