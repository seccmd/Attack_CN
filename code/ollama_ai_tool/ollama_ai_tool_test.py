from ollama_ai_tool import get_response, ai_translate

# 示例 1：调用 get_response 函数
prompt = "Hello, how are you?"
response = get_response(prompt)
if response:
    print("Response:", response)
else:
    print("Failed to get response.")

# 示例 2：调用 ai_translate 函数
english_text = "I love you."
translated_text = ai_translate(english_text, target_language="日本语")
if translated_text:
    print("Translated Text:", translated_text)
else:
    print("Failed to translate text.")