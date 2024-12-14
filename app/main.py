import requests

def main():
    # Example of using v0.dev API
    url = "https://v0.dev/api/generate"
    headers = {
        "Authorization": "Bearer YOUR_API_KEY",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": "Generate a simple Python function to add two numbers"
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print("Generated Code:", response.json()["code"])
    else:
        print("Error:", response.status_code, response.text)

if __name__ == "__main__":
    main()
