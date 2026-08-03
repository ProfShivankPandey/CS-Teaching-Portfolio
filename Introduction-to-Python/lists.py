# Creating and modifying a list
languages = ["Python", "Java", "C++"]
languages.append("JavaScript")  # Add item
languages.insert(1, "C")        # Insert at specific index

print(f"Updated Language List: {languages}")
print(f"First element: {languages[0]}")
print(f"Total languages: {len(languages)}")

# Iterating through a list
print("\nAvailable Languages:")
for lang in languages:
    print(f"- {lang}")