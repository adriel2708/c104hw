import cv2

# Read the image file
img = cv2.imread("solar-system.jpg")

# Display the image
cv2.imshow("output", img)

# Wait for a key press
cv2.waitKey(0)
 

cv2.putText(img,
             "sun",
               (20,300),
                cv2.FONT_HERSHEY_COMPLEX,
                0.5,
                 (255,255,255)
                 )


for planet in planet_labels:
    position = planet['position']
    label = planet['label']
    cv2.putText(img, label, position, font, font_scale, (0, 255, 0), font_thickness)

# Save the modified image
cv2.imwrite("Solar_system_with_name.jpg", img)