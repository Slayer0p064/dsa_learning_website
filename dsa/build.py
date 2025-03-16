import os

# Define the directory and topics
template_dir = "templates/topics/"
topics = [
    "Arrays", "Strings", "Linked Lists", "Stacks", "Queues", "Recursion",
    "Sorting Algorithms", "Searching Algorithms", "Hashing", "Trees", "Graphs",
    "Dynamic Programming", "Greedy Algorithms", "Backtracking",
    "Bit Manipulation", "Trie (Prefix Tree)"
]

# Ensure the directory exists
os.makedirs(template_dir, exist_ok=True)

# HTML template for each topic
html_template = """<!DOCTYPE html>
<html>
<head>
    <title>{topic}</title>
</head>
<body>
    <h1>{topic}</h1>
    <p>Explanation and examples will be added here.</p>
    <a href=\"/\">Back to Home</a>
</body>
</html>"""

# Create an HTML file for each topic
for topic in topics:
    file_name = f"{topic.lower().replace(' ', '_').replace('(', '').replace(')', '')}.html"
    file_path = os.path.join(template_dir, file_name)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_template.format(topic=topic))
    
    print(f"Created: {file_path}")

print("All topic pages generated successfully!")
