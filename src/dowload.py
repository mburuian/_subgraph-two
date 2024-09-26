import requests
import os

# Create a directory to save avatars
os.makedirs('avatars', exist_ok=True)

# Download 100 avatars
for i in range(100):
    response = requests.get(f'https://picsum.photos/seed/{i}/40')
    with open(f'avatars/avatar_{i}.jpg', 'wb') as f:
        f.write(response.content)

print("Downloaded 100 avatars!")
