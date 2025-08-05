import sys # For getting text file info from cmd line
import numpy as np # MATH!

class Ray:
    def __init__(self, eye, obj):
        # Ray class that creates a ray given a starting point and a endpoint 
        self.eye = np.array(eye, dtype=float)
        self.obj = np.array(obj, dtype=float)

    def ray_t(self, t):
        # return a point at "t", given the variable "t"
        return self.eye + t * self.obj

class Sphere:
    def __init__(self, name, pos, scale, color, ka, kd, ks, kr, n):
        # Sphere class creates a sphere out of all the sphere info from text file
        self.name = name
        self.pos = np.array(list(map(float, pos)))
        self.scale = np.array(list(map(float, scale)))
        self.color = np.array(list(map(float, color)))
        self.ka = float(ka)
        self.kd = float(kd)
        self.ks = float(ks)
        self.kr = float(kr)
        self.n = int(n)

class Light:
    def __init__(self, name, pos, intensity):
        # Light class to create a point of light using light info from text file
        self.name = name
        self.pos = np.array(list(map(float, pos)))
        self.intensity = np.array(list(map(float, intensity)))

def set_px(px, row, col, color):
    # Given a pixel location, we'll set that pixel to the color given [r,g,b]
    px[-row, col] = color

def check_shadow(shadow_ray, spheres, max_light_dist):
    # For checking whether the object is in shadow
    for sphere in spheres:
        # go through all the spheres and see whether or not the sphere intersects with the shadow ray given
        shadow_t = intersect_sphere(shadow_ray, sphere)
        # If the ray is between 0 & maximum light distance given, then it is in shadow (True)
        if 0 < shadow_t < max_light_dist:
            return True
    # Otherwise, not in shadow (False)
    return False

def intersect_sphere(ray, sphere):
    # Given a ray and a sphere (object), we check if they interact using quadratic formula
    # from Lecture 12 (slide 37)
    # From eye to sphere position to get direction
    direction = ray.eye - sphere.pos 
    # Quadratic coefficients (see Lecture 12 slide 38)
    A = np.dot(ray.obj, ray.obj)
    B = 2.0 * np.dot(direction, ray.obj)
    C = np.dot(direction, direction) - 1.0
    # We'll check whether this is less than, equal to, or greater than zero
    discriminant = B**2 - 4 * A * C
    # 
    if discriminant < 0:
        # No intersection
        return -1  
    elif discriminant == 0:
        # One interaction on the edge, returns quadratic formula with discriminant=0
        t = -B / (2.0 * A)
        return t
    else:
        # Two solutions, two interactions with sphere, returns minimum t value
        sqrt_disc = np.sqrt(discriminant)
        t1 = (-B - sqrt_disc) / (2.0 * A)
        t2 = (-B + sqrt_disc) / (2.0 * A)
        return min(t1, t2)


def scale(sx,sy,sz):
    # Create a 4x4 inverse scaling matrix to scale the spheres
    # we'll use this to scale the spehres in raytrace
    return np.array([
        [1/sx, 0, 0, 0],
        [0, 1/sy, 0, 0],
        [0, 0, 1/sz, 0],
        [0, 0, 0, 1]
    ])

def raytrace(ray, spheres, lights, recursion_limit):
    # Raytrace recursive function
    # Given a ray, spheres, and lights from the text file we can can return color values back function call
    # closest t value that can be used in the ray equation must be initiallized to infinity since we haven't looped through the spheres yet
    # The closest sphere would be none for the same reason
    closest_t = float('inf')
    closest_sphere = None
    
    for sphere in spheres:
        # Going through all the spheres in the text file
        # First we scale the sphere given the scale function made earlier and the scaling factors given in the file for each sphere. (Scaling matrix found in lecture 3 slides)
        scale_x, scale_y, scale_z = sphere.scale
        scaling_matrix = scale(scale_x, scale_y, scale_z)
        # Next, we also want to transform the ray itself (Lecture 12, slide 45) to then intersect with the scaled sphere. 
        transformed_eye = np.matmul(scaling_matrix, np.append(ray.eye, 1))[:3]
        transformed_obj = np.matmul(scaling_matrix, np.append(ray.obj, 0))[:3]
        transformed_ray = Ray(transformed_eye, transformed_obj)
        # Next, we want to create a sphere object that is the scaled version of our current sphere
        # Convert position to homogeneous coordinates for multiplication and creation of scaled position coordinates
        pos_homogeneous = np.array([*sphere.pos, 1])
        scaled_pos = np.matmul(scaling_matrix, pos_homogeneous)[:3]
        sphere_scaled = Sphere(sphere.name, scaled_pos, sphere.scale, sphere.color, sphere.ka, sphere.kd, sphere.ks, sphere.kr, sphere.n)
        # Use intersect_sphere to find where the transformed ray & sphere intersect
        t_h = intersect_sphere(transformed_ray, sphere_scaled)
        # if it's between the closest_t and 0 then we update our closest_t and closest sphere to be t_h and current sphere
        if 0 < t_h < closest_t:
            closest_t = t_h
            closest_sphere = sphere
    
    # If we go through all the spheres and there is no closest sphere, this means we just return the background color
    if closest_sphere is None:
        return np.array(data['BACK'])*255
        # return (data['BACK'][0]*255, data['BACK'][1]*255, data['BACK'][2]*255)
    
    # We want the intersection point of the closest sphere to be used later when dealing with shadows and reflections
    intersection_pt = ray.ray_t(closest_t)
    
    # Ambient color from assignment description
    pixel_color = closest_sphere.ka * np.array(data['AMBIENT']) * closest_sphere.color
    for light in lights:
        # Now, we'll iterate through all the points of lights and deal with shadows and ADS lighting
        # First we calculate the normal vector using the intersection point and closest sphere position to create the normalized normal vector
        N_vec = (intersection_pt - closest_sphere.pos) / np.linalg.norm(intersection_pt - closest_sphere.pos)
        # The V vector from the eye to the intersection point to be used in dot product
        V = (ray.eye - intersection_pt) / np.linalg.norm(ray.eye - intersection_pt)
        # The light vector from the light source to the intersection point used in making the shadow ray
        light_vec = (light.pos - intersection_pt) / np.linalg.norm(light.pos - intersection_pt)
        # R vector (lecture 11, slide 15) to be used in specular calculation
        R_vec = 2 * (np.dot(N_vec, light_vec)) * N_vec - light_vec
        R_vec /= np.linalg.norm(R_vec)
        # maximum light distance is just the unnormalized light vector, we will be using this in the check_shadow function
        max_light_dist = np.linalg.norm(light.pos - intersection_pt)
        # The shadow ray from the intersection point to the light vector with added offset
        shadow_ray = Ray(intersection_pt + N_vec * 1e-4, light_vec)
        if check_shadow(shadow_ray, spheres, max_light_dist):
            # We use the check shadow function to see if we are in, or not in a shadow
            # If we are in a shadow then we continue to the to the next light since there's no contribution from the diffuse or specular components, but only the ambient
            continue
        # Next, we want to calculate the diffuse and specular components using the formula given.
        # Two dot products that will be needed and we make sure they're positive
        NdotL = max((np.dot(N_vec, light_vec),0))
        RdotV = max((np.dot(R_vec, V),0))

        # Diffuse contribution
        pixel_color += closest_sphere.kd * np.array(light.intensity) * NdotL * closest_sphere.color
        # Specular contribution
        pixel_color += closest_sphere.ks * np.array(light.intensity) * (RdotV**closest_sphere.n)
    # Finally, we handle the reflection recursively
    # We first have the recursion base case where if we've already done enough recursions (limit=3), or the constant Kr is zero then we can just return the pixel colors we have calculated so far
    if recursion_limit <= 0 or closest_sphere.kr == 0:
        return np.array(pixel_color)*255
    # Otherwise, we'll calculate the reflected ray and pass it to raytrace
    # See lecture 12, slide 48 for the equation used for reflection ray
    # Calculating the components required for the ray
    c = ray.obj 
    v = c - 2 * np.dot(N_vec, c) * N_vec
    v /= np.linalg.norm(v)
    # The reflected ray is analogous to the origin of the shadow ray.
    reflected_origin = intersection_pt + N_vec * 1e-4
    reflected_ray = Ray(reflected_origin,v)
    # Raytrace the reflection ray, decrementing the recursion limit each time
    reflected_color = np.array(raytrace(reflected_ray, data['SPHERES'], data['LIGHTS'], recursion_limit - 1))
    # Add the reflection contribution to the pixel color and return the result
    pixel_color += closest_sphere.kr * reflected_color

    return np.array(pixel_color)*255

# We're mimicing the render (or main, if you prefer) function we used in javascript, now in python to start the code
def render(data):
    # Given the 'data' collected from the text file we'll create the image
    H, W = data['RES'] # Resolution H x W
    n = -data['NEAR'] # Near plane
    recursion_limit = 3 
    # Create an array of W and H indicies for the width and height
    u = np.linspace(data['LEFT'], data['RIGHT'], W)
    v = np.linspace(data['BOTTOM'], data['TOP'], H)
    # set up the eye
    eye = [0, 0, 0]
    # pixels multi-dimensional array initialized to zeros
    pixels = np.zeros((H, W, 3), dtype=float)
    # as per the psudo-code given in lecture 12, slide 52, we iterate through each row/col and set the pixel color
    for row in range(W):
        for col in range(H):
            # Direction of ray towards the pixel
            direction = np.array([u[col], v[row], n])
            # Create ray, raytrace, then set pixel color
            ray = Ray(eye, direction)
            color = raytrace(ray, data['SPHERES'], data['LIGHTS'], recursion_limit)
            set_px(pixels, row, col, color)
    # Use the given save_imageP3 function to create the ppm image
    save_imageP3(W, H, data['OUTPUT'], pixels)

# Output in P3 format, a text file containing:
# P3
# ncolumns nrows
# Max colour value (for us, and usually 255)
# r1 g1 b1 r2 g2 b2 .....
# converted to python from the C++ source file given
def save_imageP3(Width, Height, fname, pixels):
    maxVal = 255
    try:
        with open(fname, "w") as fp:
            fp.write("P3\n")
            fp.write(f"{Width} {Height}\n")
            fp.write(f"{maxVal}\n")
            for row in range(Height):
                for col in range(Width):
                    fp.write(f"{pixels[row, col][0]} {pixels[row, col][1]} {pixels[row, col][2]} ")
                fp.write("\n")
    except IOError:
        print(f"Unable to open file '{fname}'")

# We'll first get the text file from the cmd line input
if len(sys.argv) != 2:
    print("Need txt file input")
else:
    input_file = sys.argv[1]
    data = {
        'NEAR': None,
        'LEFT': None,
        'RIGHT': None,
        'BOTTOM': None,
        'TOP': None,
        'RES': None,
        'AMBIENT': None,
        'BACK': None,
        'OUTPUT': None,
        'SPHERES': [],
        'LIGHTS': []
    }
    # Read the input file and tokenize the lines
    with open(input_file, 'r') as f:
        lines = f.readlines()

    for line in lines:
        tokens = line.split()
        if not tokens:
            continue
        key = tokens[0]
        # Use the start of each sentence in the text file as the keys and put the appropriate data in 'data'
        if key in data:
            if key == 'RES':
                data[key] = (int(tokens[1]), int(tokens[2]))
            elif key in ['LEFT', 'RIGHT', 'BOTTOM', 'TOP', 'NEAR']:
                data[key] = int(tokens[1])
            elif key == 'AMBIENT' or key == 'BACK':
                data[key] = tuple(map(float, tokens[1:]))
            elif key == 'OUTPUT':
                data[key] = tokens[1]
        elif key == 'SPHERE':
            sphere = Sphere(tokens[1], tokens[2:5], tokens[5:8], tokens[8:11], tokens[11], tokens[12], tokens[13], tokens[14], tokens[15])
            data['SPHERES'].append(sphere)
        elif key == 'LIGHT':
            light = Light(tokens[1], tokens[2:5], tokens[5:8])
            data['LIGHTS'].append(light)
    # This calls the render function with data to create the image
    render(data)
