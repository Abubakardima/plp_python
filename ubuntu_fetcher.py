import requests
import os
from urllib.parse import urlparse
import hashlib

def fetch_image(url):
    """
    Fetches an image from the given URL and saves it into 'Fetched_Images'.
    Includes duplicate checking and safe filename generation.
    """

    try:
        # Create directory if it doesn't exist
        os.makedirs("Fetched_Images", exist_ok=True)

        # Fetch the image
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise exception for bad status codes

        # Check if the content type is an image before saving
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"✗ Skipped (not an image): {url}")
            return

        # Extract filename from URL or generate one
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        if not filename:
            # Use a hash of the URL if no filename is present
            filename = hashlib.md5(url.encode()).hexdigest() + ".jpg"

        filepath = os.path.join("Fetched_Images", filename)

        # Prevent saving duplicate files
        if os.path.exists(filepath):
            print(f"⚠ Skipped duplicate: {filename}")
            return

        # Save the image in binary mode
        with open(filepath, 'wb') as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An error occurred: {e}")


def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Get multiple URLs separated by spaces
    urls = input("Please enter image URL(s) (separate multiple with spaces): ").split()

    for url in urls:
        fetch_image(url)

    print("\nConnection strengthened. Community enriched.")
    print("Ubuntu: I am because we are.")


if __name__ == "__main__":
    main()
