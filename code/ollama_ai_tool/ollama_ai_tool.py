import requests
import logging
import re
from typing import Optional

# 配置日志
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Ollama API 的基础 URL
BASE_URL = "http://127.0.0.1:11434/api/"
BASE_URL = "http://146.56.139.5:11434/api/"

# 默认模型名称
#DEFAULT_MODEL = "deepseek-r1"
#DEFAULT_MODEL = "deepseek-r1:1.5b"
DEFAULT_MODEL = "llama3:8b"

def ollama_api(prompt: str, model: str = DEFAULT_MODEL, stream: bool = False) -> Optional[dict]:
    """
    封装为一个 OLLAMA API 函数，输入参数为提示词，输出为 API 的完整响应。
    
    :param prompt: 输入的提示词
    :param model: 使用的模型，默认为 DEFAULT_MODEL
    :param stream: 是否流式输出，默认为 False
    :return: API 的完整响应（JSON 格式），如果出错则返回 None
    """
    try:
        api_params = {
            "model": model,
            "prompt": prompt,
            "stream": stream
        }
        logger.debug(f"Sending request to Ollama API with params: {api_params}")
        # 发送 POST 请求
        response = requests.post(BASE_URL + "generate", json=api_params)
        response.raise_for_status()  # 检查 HTTP 状态码
        logger.debug("API request successful")
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"API request failed: {e}")
        return None

def remove_think_tags(response_text: str) -> str:
    """
    删除字符串中的 <think> 标签及其之间的全部内容。
    
    :param response_text: 输入的字符串
    :return: 删除 <think> 标签及其内容后的字符串
    """
    # 使用正则表达式匹配 <think> 标签及其内容
    response_text = re.sub(r"<think>.*?</think>", "", response_text, flags=re.DOTALL)
    return response_text.strip()  # 去除多余的空格

def get_response(prompt: str, model: str = DEFAULT_MODEL) -> Optional[str]:
    """
    调用 ollama_api() 函数，并提取返回的 JSON 数据中的 response 字段。
    删除 response 中的 <think> 标签及其内容。
    
    :param prompt: 输入的提示词
    :param model: 使用的模型，默认为 DEFAULT_MODEL
    :return: 处理后的 response 字段值，如果出错则返回 None
    """
    api_response = ollama_api(prompt, model=model)
    if api_response is None:
        return None

    try:
        response_text = api_response.get("response", "No response found")
        # 删除 <think> 标签及其内容
        response_text = remove_think_tags(response_text)
        logger.debug(f"Processed response: {response_text}")
        return response_text
    except AttributeError as e:
        logger.error(f"Failed to process API response: {e}")
        return None

def ai_translate(text: str, target_language: str = "中文", model: str = DEFAULT_MODEL) -> Optional[str]:
    """
    AI 翻译功能，将输入的英文文本翻译为目标语言（默认中文）。
    
    :param text: 输入的英文文本
    :param target_language: 目标语言，默认为 "中文"
    :param model: 使用的模型，默认为 DEFAULT_MODEL
    :return: 翻译后的文本，如果出错则返回 None
    """
    try:
        # 构造翻译提示词
        prompt = f"你是一名专业的翻译专家，你的任务只是将内容进行翻译，不需要输出其他思考信息或过程信息\n"
        prompt += f"本次翻译内容为 计算机领域和网络安全攻防领域\n"
        prompt += f"翻译以下内容为{target_language}:\n"
        prompt += f"{text}"
        logger.debug(f"Translation prompt: {prompt}")
        # 调用 get_response 函数获取翻译结果
        translated_text = get_response(prompt, model=model)
        return translated_text
    except Exception as e:
        logger.error(f"Translation failed: {e}")
        return None

# 示例调用
if __name__ == "__main__":
    # 示例 1：调用 get_response 函数
    prompt = "Hello, how are you?"
    response = get_response(prompt)
    if response:
        print("Response:", response)
    else:
        print("Failed to get response.")

    # 示例 2：调用 ai_translate 函数
    english_text = "Hello, how are you?"
    translated_text = ai_translate(english_text, target_language="中文")
    if translated_text:
        print("Translated Text:", translated_text)
    else:
        print("Failed to translate text.")