import json
from ollama_ai_tool import ai_translate  # 假设你已经封装了 ai_translate 函数

def translate_json_data(input_file: str, output_file: str, target_language: str = "中文"):
    """
    读取 JSON 文件，翻译 translated_name 和 translated_description 字段，并保存到新文件。

    :param input_file: 输入的 JSON 文件路径
    :param output_file: 输出的 JSON 文件路径
    :param target_language: 目标语言，默认为 "中文"
    """
    try:
        # 读取 JSON 文件
        with open(input_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        # 遍历 JSON 数据并翻译
        for key, value in data.items():
            # 翻译 translated_name
            if "translated_name" in value:
                translated_name = ai_translate(value["translated_name"], target_language=target_language)
                if translated_name:
                    value["translated_name"] = translated_name
                else:
                    print(f"Failed to translate 'translated_name' for key: {key}")

            # 翻译 translated_description
            if "translated_description" in value:
                translated_description = ai_translate(value["translated_description"], target_language=target_language)
                if translated_description:
                    value["translated_description"] = translated_description
                else:
                    print(f"Failed to translate 'translated_description' for key: {key}")

        # 将翻译后的数据写入新文件
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        print(f"Translation completed. Results saved to {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

# 示例调用
if __name__ == "__main__":
    input_file = "input.json"  # 输入的 JSON 文件路径
    output_file = "output.json"  # 输出的 JSON 文件路径
    target_language = "日本语日文"  # 目标语言

    # 调用翻译函数
    translate_json_data(input_file, output_file, target_language)