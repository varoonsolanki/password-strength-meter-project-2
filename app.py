import streamlit as st
import random
import string

#  Common password blacklist
common_passwords = [
    "password", "password123", "123456", "qwerty", 
    "abc123", "letmein", "welcome", "admin123"
]

#  Password strength checking function
def check_password_strength(password):
    score = 0
    feedback = []

    # Check against common passwords
    if password.lower() in common_passwords:
        return 0, ["Password is too common and easily guessable!"]

    # Criteria checks
    length = len(password) >= 8
    uppercase = any(c.isupper() for c in password)
    lowercase = any(c.islower() for c in password)
    digit = any(c.isdigit() for c in password)
    special_char = any(c in '!@#$%^&*' for c in password)

    # Calculate score
    score = sum([length, uppercase, lowercase, digit, special_char])

    # Generate feedback
    if not length:
        feedback.append("Password should be at least 8 characters long")
    if not uppercase:
        feedback.append("Add at least one uppercase letter")
    if not lowercase:
        feedback.append("Add at least one lowercase letter")
    if not digit:
        feedback.append("Add at least one digit")
    if not special_char:
        feedback.append("Add at least one special character (!@#$%^&*)")

    return score, feedback

#  Password generator function
def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + '!@#$%^&*'
    while True:
        password = ''.join(random.choice(characters) for _ in range(length))
        # Ensure all criteria are met
        if (any(c.isupper() for c in password) and
            any(c.islower() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in '!@#$%^&*' for c in password)):
            return password

# Streamlit GUI implementation
def main():
    st.title("🔐 Password Strength Meter")
    st.markdown("Check and improve your password security")

    # Password input
    password = st.text_input("Enter your password:", type="password")

    # Check strength button
    if st.button("Check Strength"):
        if not password:
            st.error("Please enter a password")
        else:
            score, feedback = check_password_strength(password)
            
            # Display results with color coding
            col1, col2 = st.columns([0.2, 0.8])
            with col1:
                if score == 0:
                    st.error("Weak ❌")
                elif score <= 2:
                    st.error(f"Weak ({score}/5)")
                elif score <= 4:
                    st.warning(f"Moderate ({score}/5)")
                else:
                    st.success(f"Strong ({score}/5)")
            
            # Display feedback
            if score < 5:
                st.subheader("Improvement Suggestions:")
                for item in feedback:
                    st.error(f"- {item}")
            else:
                st.balloons()
                st.success("Great job! This is a strong password!")

    # Password generator
    st.markdown("---")
    if st.button("Generate Strong Password"):
        generated_password = generate_strong_password()
        st.code(generated_password)
        st.success("Generated a strong password! Copy and use this!")

# Run the application

if __name__ == "__main__":
    main()