import streamlit as st
import string
import random
import re

# Set page configuration
st.set_page_config(page_title="Password Strength Checker", page_icon="🔐", layout="centered")

# ------------------ PASSWORD GENERATOR FUNCTION ------------------ #
def password_generator(length, use_digit, use_special):
    characters = string.ascii_letters  # A-Z and a-z

    if use_digit:
        characters += string.digits  # Add 0-9
    if use_special:
        characters += string.punctuation  # Add special chars like @, #, !

    return ''.join(random.choice(characters) for _ in range(length))

# ------------------ PASSWORD STRENGTH CHECKER FUNCTION ------------------ #
def password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    if score == 4:
        return "✅ **Strong Password!**", "Strong", feedback
    elif score == 3:
        return "⚠️ **Moderate Password** - **Consider adding more security features.**", "Moderate", feedback
    else:
        return "❌ **Weak Password** - **Improve using the suggestions below.**", "Weak", feedback


# ------------------ PASSWORD STRENGTH CHECKER UI ------------------ #
st.title("🔐 Password Strength Checker")
st.markdown("""Welcome to the Password Strength Checker!
            Use this tool to evaluate the strength of your password and get suggestions for improvement.✨""")

password = st.text_input("Enter your password!", type="password")

if st.button("Check Strength"):
    if password:
        result, strength, feedback = password_strength(password)

        if strength == "Strong":
            st.success(result)
            st.balloons()
        elif strength == "Moderate":
            st.warning(result)
            for tip in feedback:
                st.info(tip)
        else:
            st.error(result)
            for tip in feedback:
                st.warning(tip)
    else:
        st.warning("Please enter a password!")

# ------------------ PASSWORD GENERATOR UI ------------------ #
st.title("🔑 Password Generator")

length = st.slider("Select your password length", min_value=8, max_value=20, value=12)
use_digit = st.checkbox("Include Digits")
use_special = st.checkbox("Use Special Characters")

if st.button("Generate Password"):
    password = password_generator(length, use_digit, use_special)
    st.success(f"Your Password is: `{password}`")
