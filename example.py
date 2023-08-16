from apigenerator import generate_new_api_key, get_hello_message

api_key = generate_new_api_key()
print(f"Сгенерирован новый API-ключ: {api_key}")

api_key_input = input("Введите API-ключ: ")
hello_message = get_hello_message(api_key_input)
print(hello_message)



