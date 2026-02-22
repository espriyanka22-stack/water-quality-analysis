import cv2
import numpy as np
import matplotlib.pyplot as plt

# ---------- LOAD IMAGE ----------
image_path = "river water.jpeg"
image = cv2.imread(image_path)

if image is None:
    print("❌ Image not found!")
    exit()

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# ---------- FEATURE EXTRACTION ----------

# Brightness
brightness = np.mean(gray)

# Clarity (turbidity proxy)
p2, p98 = np.percentile(gray, (2, 98))
clarity = (p98 - p2) / 255

# Green dominance (algae proxy)
green_mean = np.mean(image_rgb[:, :, 1])

# Saturation
saturation = np.mean(hsv[:, :, 1])

# Foam / white patches
foam_ratio = np.mean(gray > 230)

# Hue average
hue = np.mean(hsv[:, :, 0])

# ---------- CHEMICAL ESTIMATION (Approximate) ----------
turbidity = round((1 - clarity) * 50, 2)       # NTU
ph = round(7 + (hue - 60) / 40, 2)              # visual pH
salinity = round((brightness / 255) * 4, 2)    # dS/m

# ---------- CLASSIFICATION ----------
drink_issues = []
farm_issues = []

if clarity < 0.3:
    drink_issues.append("High turbidity")

if green_mean > 150 and saturation > 100:
    drink_issues.append("Possible algae bloom")

if foam_ratio > 0.02:
    drink_issues.append("Possible chemical foam")

if hue < 20 or hue > 100:
    drink_issues.append("Abnormal water color")

if clarity < 0.2:
    farm_issues.append("Very muddy water")

if green_mean > 180:
    farm_issues.append("Heavy algae")

if foam_ratio > 0.03:
    farm_issues.append("Chemical contamination")

drinkable = len(drink_issues) == 0
farm_safe = len(farm_issues) == 0

# ---------- OUTPUT ----------
print("\n------ IMAGE-BASED WATER QUALITY REPORT ------")
print("Clarity:", round(clarity, 2))
print("Brightness:", round(brightness, 1))
print("Green Level:", round(green_mean, 1))
print("Saturation:", round(saturation, 1))
print("Foam Ratio:", round(foam_ratio, 3))
print("Hue:", round(hue, 1))

print("\nEstimated Parameters:")
print("Turbidity (NTU):", turbidity)
print("pH level (est):", ph)
print("Salinity (dS/m est):", salinity)

print("\nDrinking Water:")
if drinkable:
    print(" ✔ Possibly safe (visual estimate)")
else:
    print(" ✘ Not safe")
    for i in drink_issues:
        print("   -", i)

print("\nFarming Water:")
if farm_safe:
    print(" ✔ Suitable")
else:
    print(" ✘ Not suitable")
    for i in farm_issues:
        print("   -", i)

# ---------- SHOW IMAGE ----------
plt.imshow(image_rgb)
plt.title("Analyzed Water Image")
plt.axis("off")
plt.show()