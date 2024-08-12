import streamlit as st
import os
from PIL import Image
from dotenv import load_dotenv
import google.generativeai as genai
import base64
import io

# Load environment variables
load_dotenv()

# Configure API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Base input prompt for nutritional analysis
base_input_prompt = """
You are an expert in nutrition where you need to see the food items from the image
and calculate the total calories, also provide the details of every food item with calories intake
is below format

1. Item 1 - no of calories - protein contained in grams protein
2. Item 2 - no of calories - protein contained in grams protein
----
----
Finally, you can also mention whether the food is healthy or not and also mention the percentage split of ratio
of carbohydrates, fats, fiber, sugar, and other things required in a diet.
"""

def get_gemini_response(user_input, image, prompt):
    model = genai.GenerativeModel('gemini-1.5-pro')
    response = model.generate_content([user_input, image[0], prompt])
    return response.text

def input_image_setup(uploaded_file):
    try:
        image = Image.open(uploaded_file).convert('RGB')
        byte_array = io.BytesIO()
        image.save(byte_array, format='JPEG')
        byte_array = byte_array.getvalue()
        return [{"mime_type": uploaded_file.type, "data": byte_array}]
    except Exception as e:
        st.error(f"Failed to process the image file: {str(e)}")
        return None

def get_base64_encoded_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

def load_image(image_path):
    with open(image_path, "rb") as file:
        image = Image.open(file)
        byte_array = io.BytesIO()
        image.save(byte_array, format='PNG')
        byte_array.seek(0)
        return byte_array

# Set up the Streamlit app
st.set_page_config(page_title="Nutrition Meter", layout='wide')

# Display background
background_image_path = r"E:\Nutrition AI app\background.jpg"
image_base64 = get_base64_encoded_image(background_image_path)
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{image_base64}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Display logo
logo_image_path = r"E:\Nutrition AI app\logo.jpg"
logo_image = load_image(logo_image_path)
st.sidebar.image(logo_image, use_column_width=True)

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ['Home', 'App'])

if page == 'Home':
    st.header("Welcome to Nutrition Meter")
    st.write("""
        This application helps you track your daily nutrient intake and provides feedback on your diet.
        Created by Satyam Prashant.
    """)

elif page == 'App':
    st.header("Nutrition Meter")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    additional_info = st.text_area("Additional Information", "Type any specific details or requirements here.")
    
    if uploaded_file is not None:
        try:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image.", use_column_width=True)
        except Exception as e:
            st.error(f"Unable to display the image: {e}")

    submit = st.button("Analyze Nutritional Content")

    if submit and uploaded_file is not None:
        image_data = input_image_setup(uploaded_file)
        if image_data:
            # Append additional information to the base prompt
            full_prompt = f"{base_input_prompt} {additional_info}"
            response = get_gemini_response(full_prompt, image_data, full_prompt)
            st.subheader("Your Food Analysis")
            st.write(response)
