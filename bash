# 1. Gumawa ng folder at pumasok sa loob
mkdir pixel-art-converter
cd pixel-art-converter

# 2. Gumawa ng mga kinakailangang files
touch app.py requirements.txt .gitignore

# 3. (Optional) Gumawa at i-activate ang virtual environment
python -m venv venv
# Sa Windows (Git Bash / CMD):
source venv/Scripts/activate
# Sa Mac / Linux:
# source venv/bin/activate

# 4. I-install ang mga kailangan (Streamlit at Pillow)
pip install streamlit Pillow

# 5. Patakbuhin ang Streamlit app locally para i-test
streamlit run app.py
