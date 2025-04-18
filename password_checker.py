import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password is too short (minimum 8 characters).")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters for better strength.")

    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters for better strength.")

    # Number check
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add numbers to strengthen your password.")

    # Symbol check
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        feedback.append("Consider using special characters (e.g., !@#$).")

    # Weak patterns
    weak_patterns = ["password", "123", "qwerty", "abc", "letmein"]
    if any(pattern in password.lower() for pattern in weak_patterns):
        score -= 2
        feedback.append("Avoid common patterns like '123', 'password', or 'qwerty'.")

    print(f"\nPassword Score: {max(score, 0)}/5")

    if score >= 4:
        print("✅ Strong password!")
    elif score == 3:
        print("⚠️ Medium strength. Could be better.")
    else:
        print("❌ Weak password. Change it!")

    if feedback:
        print("\nSuggestions:")
        for note in feedback:
            print(" -", note)

if __name__ == "__main__":
    pwd = input("Enter a password to check: ")
    check_password_strength(pwd)
