import argparse
import cv2
import os

def find_size(cam_distance, pixels, focal_length):
	return pixels * cam_distance / focal_length

if __name__ == "__main__":
        ap = argparse.ArgumentParser()
        ap.add_argument("-p", "--path", type = str, required = True,
                        help="path image and bounding box coordinates")
        ap.add_argument("-n", "--num_images", type=int, required = True,
                help = "number of images")
        ap.add_argument("-d", "--cam_dist", type=float, required = True,
                help = "distance of camrera from the object")
        
        args = ap.parse_args()
        KNOWN_DISTANCE = args.cam_dist
        image_path = args.path
        with open("./focal_length.txt","r") as f:
                focal_length = float(f.read())
        image_numbers = args.num_images
        
        for i in range(1, image_numbers + 1):
                img = cv2.imread(image_path + f'/{i}.jpeg')
                
                with open(image_path + f'/{i}.txt', 'r') as f:
                        coordinates = f.read().rstrip().split('\n')

                for c in coordinates:
                        x, y, w, h = map(int, c.rstrip().split(" "))
                        width = round(find_size(KNOWN_DISTANCE, w, focal_length)*2.54, 2)
                        height = round(find_size(KNOWN_DISTANCE, h, focal_length)*2.54,2)
                        
                        #box
                        img = cv2.line(img, (x,y), (x+w, y), (199, 91, 205), 3)
                        img = cv2.line(img, (x+w,y),(x+w,y+h), (199, 91, 205), 3)
                        img = cv2.line(img, (x+w,y+h), (x,y+h), (199, 91, 205), 3)
                        img = cv2.line(img, (x,y+h),(x,y), (199, 91, 205), 3)

                        #height
                        img = cv2.rectangle(img, (x+5,y+h//2+5),(x+95,y+h//2-30), (0,0,0), -1)
                        img = cv2.putText(img, str(height),(x+5,y+h//2),
                                cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255), 1, cv2.LINE_AA)
                        #width
                        img = cv2.rectangle(img, (x+w//2-10,y+20), (x+w//2+90,y-10), (0,0,0), -1)
                        img = cv2.putText(img, str(width), (x+w//2-10,y+20), cv2.FONT_HERSHEY_SIMPLEX,
                                          1, (255,255,255), 1, cv2.LINE_AA)
                cv2.imwrite(image_path + f'/res_{i}.jpg',img)
