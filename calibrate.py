import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help="path to the input image")
ap.add_argument("-d", "--cam_dist", type=float, required = True,
                help = "distance of camrera from the object")
ap.add_argument("-w", "--width", type=float, required = True,
                help="Known width of the object")
ap.add_argument("-p", "--pixel_length", type=float,
                help="length of object in image as pixels")

args = ap.parse_args()
KNOWN_DISTANCE = args.cam_dist
KNOWN_WIDTH = args.width
if(args.image or args.pixel_length):
    if(args.pixel_length):
        pixels = args.pixel_length
    else:
        pass
else:
    print("Image or pixel length required")
    raise

focal_length = pixels * KNOWN_DISTANCE / KNOWN_WIDTH
with open("focal_length.txt", "w") as f:
    f.write(str(focal_length))
