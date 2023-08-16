# api-generator-module
Project description: The generator module API is a simple Python library that provides functions for working with API keys. The library allows you to generate new API keys, save them and check their validity to access certain functions or resources. The library was created for the test!

# Main functions:
generate_new_api_key(): This function generates a new API key using the standard Python secrets module. The keys consist of 16 random characters and are unique for each generation.

get_hello_message(api_key): This function takes an API key as a parameter and checks if it exists in the dictionary of saved API keys. If the key exists in the dictionary, the function returns a "hello" message, indicating that the key was validated successfully. If the key is not found, the function returns an "Invalid API key" message indicating an invalid key.

# Why is this library needed?
For a test. I wanted to see how API-keys work in Python.

# How to use?
You need to download the file "apigenerator.py". If you want to see a finished example, also download "example.py".
