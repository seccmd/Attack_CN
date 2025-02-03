
import requests

def generate_response(prompt):
    try:
        # Ollama 的 API 地址
        url = "http://localhost:11434/api/generate"
        
        # 请求体
        data = {
            "model": "deepseek-r1",  # 替换为你使用的模型名称
            "prompt": prompt,
            "stream": False  # 设置为 False 以获取完整响应
        }
        
        # 发送 POST 请求
        response = requests.post(url, json=data)
        
        # 检查响应状态
        if response.status_code == 200:
            # 解析响应内容
            response_data = response.json()
            return response_data.get("response", "")
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return ""
    except Exception as e:
        print(f"Error generating response: {e}")
        return ""

def create_random_sentence_with_ollama(prompt, n=3):
    try:
        random_word = "Create a sentence about fruit"
        response = generate_response(f"Context: {random_word}")
        
        return response
    except Exception as e:
        print(f"Error in create_random_sentence_with_ollama: {e}")
        raise


if __name__ == "__main__":
    ret = create_random_sentence_with_ollama("hello")
    print(ret)
