import math
import collections
import string
import time

def shannon_entropy(password):
    if not password:
        return 0
    freq = collections.Counter(password)
    length = len(password)
    entropy = -sum((count / length) * math.log2(count / length) for count in freq.values())
    return round(entropy * length, 2)

def character_set_size(password):
    char_sets = {
        'lowercase': any(c in string.ascii_lowercase for c in password),
        'uppercase': any(c in string.ascii_uppercase for c in password),
        'digits': any(c in string.digits for c in password),
        'symbols': any(c in string.punctuation for c in password)
    }
    size = 0
    if char_sets['lowercase']:
        size += 26
    if char_sets['uppercase']:
        size += 26
    if char_sets['digits']:
        size += 10
    if char_sets['symbols']:
        size += 32  # Approximate number of punctuation characters
    return size

def estimate_crack_time(possibilities, guesses_per_second=1e9):
    seconds = possibilities / guesses_per_second
    units = [("years", 60 * 60 * 24 * 365),
             ("days", 60 * 60 * 24),
             ("hours", 60 * 60),
             ("minutes", 60),
             ("seconds", 1)]
    for unit_name, unit_seconds in units:
        if seconds >= unit_seconds:
            value = seconds / unit_seconds
            return f"{value:,.2f} {unit_name}"
    return "less than a second"


def password_strength_score(entropy):
    if entropy < 40:
        return "VERY WEAK"
    elif entropy < 60:
        return "WEAK"
    elif entropy < 80:
        return "MEDIUM"
    else:
        return "STRONG"

def analyze_password(password):
    length = len(password)
    charset_size = character_set_size(password)
    
    # Total possible combinations
    total_combinations = charset_size ** length if charset_size else 0
    entropy_bits = round(math.log2(total_combinations), 2) if total_combinations else 0
    
    # Shannon entropy
    shannon = shannon_entropy(password)
    
    # Crack time estimation
    time_to_crack = estimate_crack_time(total_combinations) if total_combinations else "Instantly"
    
    # Strength classification
    strength = password_strength_score(entropy_bits)

    # Output
    print("\n--- Garuda Entropy Analyzer ---")
    print(f"[+] Password: {password}")
    print(f"[+] Length: {length}")
    print(f"[+] Character Set Size: {charset_size}")
    print(f"[+] Shannon Entropy: {shannon} bits")
    print(f"[+] Entropy Estimate: {entropy_bits} bits")
    print(f"[+] Crack Time Estimate: {time_to_crack}")
    print(f"[+] Strength: {strength}")
    
    if strength in ["VERY WEAK", "WEAK"]:
        print("\n[!] Suggestions to Improve:")
        print(" - Use a longer password (12+ characters)")
        print(" - Mix uppercase, lowercase, numbers, and symbols")
        print(" - Avoid common patterns or dictionary words")

# ---- Main Execution ----
if __name__ == "__main__":
    user_input = input("Enter a password/key to analyze: ")
    analyze_password(user_input)
