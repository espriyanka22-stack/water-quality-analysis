# water-quality-analysis
This project analyzes water quality from an image using computer vision techniques. It estimates parameters like turbidity, pH, and salinity, and classifies whether the water is safe for drinking or farming.
💧 Water Quality Analysis Using Image Processing
📌 Overview

This project analyzes water quality from an image using computer vision techniques. It extracts visual features and estimates important parameters like turbidity, pH, and salinity, then classifies whether the water is suitable for drinking or farming.

⚠️ Note: This is a visual estimation system and not a replacement for laboratory testing.

🚀 Features

📷 Image-based water analysis

🌊 Turbidity estimation

⚗️ pH level approximation

🧂 Salinity estimation

🌿 Algae detection using green intensity

🫧 Foam/chemical detection

✅ Water suitability classification:

Drinking

Farming

🛠️ Technologies Used

Python

OpenCV (cv2)

NumPy

Matplotlib

⚙️ How It Works
1. Image Processing

Converts image into:

RGB (for display)

HSV (for color analysis)

Grayscale (for brightness & clarity)

2. Feature Extraction

Brightness → Light intensity

Clarity → Indicates turbidity

Green Level → Detects algae

Saturation → Color strength

Foam Ratio → Detects chemical presence

Hue → Water color analysis

3. Parameter Estimation

Turbidity (NTU)

pH level

Salinity (dS/m)

4. Classification

Drinking water safety check

Farming suitability check

📂 Project Structure
water-quality-analysis/
│── water_analysis.py
│── river water.jpeg
│── README.md
▶️ How to Run
Step 1: Install Dependencies
pip install opencv-python numpy matplotlib
Step 2: Add Image

Place your image (e.g., river water.jpeg) in the project folder

Step 3: Run the Program
python water_analysis.py
📊 Sample Output
------ IMAGE-BASED WATER QUALITY REPORT ------
Clarity: 0.45
Brightness: 120.3
Green Level: 140.2
Saturation: 90.5
Foam Ratio: 0.01
Hue: 65.3

Estimated Parameters:
Turbidity (NTU): 27.5
pH level (est): 7.13
Salinity (dS/m est): 1.88

Drinking Water:
✔ Possibly safe (visual estimate)

Farming Water:
✔ Suitable
How the Code Works
1. Import Libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt

cv2 → Image processing (OpenCV)

numpy → Numerical calculations

matplotlib → Display image

2. Load the Image
image_path = "river water.jpeg"
image = cv2.imread(image_path)

Reads the image from your project folder

If image not found → program exits

3. Convert Image Formats
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

RGB → for display

HSV → for color analysis

Gray → for brightness & clarity

4. Feature Extraction

These values are calculated from the image:

🔹 Brightness
brightness = np.mean(gray)

Average light intensity

🔹 Clarity (Turbidity Approximation)
p2, p98 = np.percentile(gray, (2, 98))
clarity = (p98 - p2) / 255

Low clarity → muddy water

🔹 Green Level (Algae Detection)
green_mean = np.mean(image_rgb[:, :, 1])

High value → possible algae

🔹 Saturation
saturation = np.mean(hsv[:, :, 1])

Indicates color intensity

🔹 Foam Detection
foam_ratio = np.mean(gray > 230)

Detects white patches (chemicals/foam)

🔹 Hue
hue = np.mean(hsv[:, :, 0])

Helps estimate water color

5. Estimate Water Parameters
turbidity = (1 - clarity) * 50
ph = 7 + (hue - 60) / 40
salinity = (brightness / 255) * 4

Turbidity → dirt level

pH → acidity/basicity

Salinity → dissolved salts

⚠️ These are approximate values, not lab-accurate.

6. Water Quality Classification
Drinking Water Check
if clarity < 0.3 → High turbidity
if green_mean > 150 → Algae
if foam_ratio > 0.02 → Chemicals
Farming Water Check
if clarity < 0.2 → Muddy
if green_mean > 180 → Heavy algae

If no issues → safe

Else → not safe

7. Output Results
print("Water Quality Report")

Displays:

Clarity, brightness, color values

Estimated turbidity, pH, salinity

Drinking & farming suitability

8. Display Image
plt.imshow(image_rgb)
plt.show()

Shows the analyzed image.

🚀 How to Run
pip install opencv-python numpy matplotlib
python your_file_name.py
📁 Project Structure (GitHub)
water-quality-analysis/
│── water_analysis.py
│── river water.jpeg
│── README.md

👩‍💻 Author

Priyanka S

Computer Science Engineering Student

Interested in AI, Image Processing & Web Development
