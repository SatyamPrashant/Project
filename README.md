**Nutrition App Using Gemini Pro**
**Overview**
The Nutrition Meter Application harnesses advanced AI technology, allowing users to
evaluate the nutritional content of their meals by simply uploading images. This tool is
designed to support users in maintaining a balanced diet by providing detailed
information on calorie counts and nutritional breakdowns.
**Key Features**
● Nutritional Analysis: Leverages AI to recognize food items from images and
calculates total calorie intake, along with a detailed breakdown of proteins,
carbohydrates, and fats.
● Health Monitoring: Enables users to track their diet by offering insights into the
healthiness of their meals and suggesting nutritional improvements.
Technology Stack
● Streamlit: Facilitates the creation of a user-friendly web interface.
● Pillow (PIL): Manages tasks related to image processing.
● dotenv: Handles the management of environment variables.
● Google Generative AI: Drives the backend AI model, generating detailed
nutritional analysis based on food images.
Setup and Installation
**Prerequisites**
● Python 3.8 or later
● Anaconda (recommended for environment management)
● Gemini API Key
Installation Steps
Create a Conda Environment:
Set Up .env File:
Inside your project folder, create a .env file to store your GOOGLE_API_KEY.
Generate a Requirements File:
Generate a requirements.txt file to include all the necessary Python packages.
Install Required Packages:
pip install -r requirements.txt
Create the Streamlit Application File:
Make sure app.py is set up by this step as the dependencies are installed.
Run the Application:
streamlit run app.py
Usage Instructions
1. Access the Application.
2. Start by uploading an image of your meal.
3. Input any specific dietary preferences or additional details in the provided
section.
4. Submit for Analysis.
The AI will process the image and generate a comprehensive report on the nutritional
content, assessing the healthiness based on the food's nutrient profile.
AI in Health Management
AI significantly enhances our capability to manage health through sophisticated image
recognition and data analysis. This application processes visual and textual data to
provide accurate nutritional insights, empowering users to make well-informed dietary
choices.
