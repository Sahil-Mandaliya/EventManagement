import re

def create_slug(input_string):
    # Convert to lowercase
    slug = input_string.lower()
    # Replace spaces and special characters with hyphens
    slug = re.sub(r'[\s\W]+', '-', slug)
    # Remove leading and trailing hyphens
    slug = slug.strip('-')
    return slug