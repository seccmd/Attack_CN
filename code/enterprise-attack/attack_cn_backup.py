#!/usr/bin/env python3

from mitreattack.stix20 import MitreAttackData
import json
import os

# 第一阶段：生成带链接的 Markdown 表格
# 首先，我们需要获取所有的战术和技术，然后将技术按照战术进行分类，生成一个带有链接的 Markdown 表格。
client = MitreAttackData("./enterprise-attack.json")
# 获取所有战术和技术
tactics = client.get_tactics()
techniques = client.get_techniques(remove_revoked_deprecated=True)

# 定义战术的优先级顺序
tactic_priority = [
    "Reconnaissance", "Resource Development", "Initial Access", "Execution",
    "Persistence", "Privilege Escalation", "Defense Evasion", "Credential Access",
    "Discovery", "Lateral Movement", "Collection", "Command and Control",
    "Exfiltration", "Impact"
]
# 创建一个字典，存储每个战术对应的技术，并按照优先级排序
tactic_techniques = {tactic['name']: [] for tactic in sorted(tactics, key=lambda t: tactic_priority.index(t['name']) if t['name'] in tactic_priority else len(tactic_priority))}

# 遍历技术，将其关联到对应的战术，且技术不是子技术
for technique in techniques:
    if not technique.get('x_mitre_is_subtechnique', False):
        for kill_chain_phase in technique.get('kill_chain_phases', []):
            tactic_name = next((tactic['name'] for tactic in tactics if tactic['x_mitre_shortname'] == kill_chain_phase['phase_name']), None)
            if tactic_name:
                tactic_techniques[tactic_name].append(technique['name'])


# 生成带链接的 Markdown 表格
def generate_markdown_with_links(tactic_techniques, translations=None):
    # 表头
    markdown_table = "| " + " | ".join(tactic_techniques.keys()) + " |\n"
    markdown_table += "|" + "|".join(["---"] * len(tactic_techniques)) + "|\n"

    # 填充技术
    max_techniques = max(len(tech_list) for tech_list in tactic_techniques.values())

    for i in range(max_techniques):
        row = []
        for tactic, tech_list in tactic_techniques.items():
            if i < len(tech_list):
                technique_name = tech_list[i]
                if translations:
                    original_name = next((name for name, trans in translations.items() if trans["translated_name"] == technique_name), technique_name)
                else:
                    original_name = technique_name
                technique_id = next((ref['external_id'] for tech in techniques if tech['name'] == original_name for ref in tech.get('external_references', [])), None)
                if technique_id:
                    technique_link = f"[{technique_name}](https://attack.mitre.org/techniques/{technique_id})"
                else:
                    technique_link = technique_name  # 如果没有找到 technique_id，则只显示技术名称
                row.append(technique_link)
            else:
                row.append("")  # 如果当前战术没有更多技术，留空
        markdown_table += "| " + " | ".join(row) + " |\n"

    return markdown_table

# 生成并打印带链接的 Markdown 表格
markdown_table_with_links = generate_markdown_with_links(tactic_techniques)
#print(markdown_table_with_links)

# 如果需要保存到文件
with open("./Attack_CN/docs/mitre_attack_tactic_techniques_with_links.md", "w", encoding="utf-8") as file:
    file.write("""---
hide:
  - toc
  - title
  - footer
  - navigation
---

# ATT&CK 中文版 

""" + markdown_table_with_links)

# 第二阶段：翻译技术名称和描述
# 我要对这个表格进行翻译，怎么办？ 我想通过一个json文件来存储翻译后的技术名称和技术描述，json文件先保存在字符串中，对应的技术名称和技术描述和原始技术名称一一对应，然后再将这个json文件保存到本地文件中，这样就可以方便的进行翻译了。

def save_translations_to_json(techniques, file_path="./technique_translations.json"):
    # 创建一个字典来存储技术名称和描述的翻译
    translations = {
        technique['name']: {
            "translated_name": technique['name'],  # 使用原始技术名称
            "translated_description": technique.get('description', '')  # 使用原始技术描述
        }
        for technique in techniques
    }

    # 将翻译字典保存为 JSON 文件
    translations_json = json.dumps(translations, ensure_ascii=False, indent=4)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(translations_json)

# 调用函数保存翻译
# save_translations_to_json(techniques)

# 第三阶段：加载技术翻译
# 有了技术名称和描述的翻译后，我们可以加载这个翻译文件，然后将技术名称和描述替换为翻译后的文本。

def load_translations_from_json(file_path="./technique_translations_cn.json"):
    with open(file_path, "r", encoding="utf-8") as file:
        translations = json.load(file)
    return translations

# 加载翻译文件
translations = load_translations_from_json()

# 创建一个新的字典来存储翻译后的技术名称
translated_tactic_techniques = {tactic: [] for tactic in tactic_techniques}

# 更新技术名称为翻译后的名称
for tactic, tech_list in tactic_techniques.items():
    for original_name in tech_list:
        translated_name = translations.get(original_name, {}).get("translated_name", original_name)
        translated_tactic_techniques[tactic].append(translated_name)

# 生成并打印带链接的翻译后的 Markdown 表格
markdown_table_with_translations = generate_markdown_with_links(translated_tactic_techniques, translations)
print("=markdown_table_with_translations=")
print(translated_tactic_techniques)

# 如果需要保存到文件
with open("./Attack_CN/docs/mitre_attack_tactic_techniques_with_translations.md", "w", encoding="utf-8") as file:
    file.write("""---
hide:
  - toc
  - title
  - footer
  - navigation
---

# ATT&CK 中文版 

""" + markdown_table_with_translations)



# 第四阶段：每一个tactics生成一个markdown文件，包含技术名称和描述清单（目录结构：tactics名称为目录名，文件名为index.md）
# 生成每个战术的 Markdown 文件，包含技术名称和描述清单
def generate_tactic_markdown_files(tactic_techniques, translations, output_dir="./Attack_CN/docs/tactics"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for tactic, tech_list in tactic_techniques.items():
        tactic_dir = os.path.join(output_dir, tactic.replace(" ", ""))
        if not os.path.exists(tactic_dir):
            os.makedirs(tactic_dir)

        tactic_description = next((tactic['description'] for tactic in tactics if tactic['name'] == tactic), "")
        markdown_content = f"""---
sidebar_position: 11
hide:
  - toc
---

# {tactic}

=== "{tactic}"

{tactic_description}

## 技术： {len(tech_list)}

| 编号 | 名字 | 描述 |
| --- | --- | --- |
"""

        for original_name in tech_list:
            translated_name = translations.get(original_name, {}).get("translated_name", original_name)
            technique = next((tech for tech in techniques if tech['name'] == original_name), None)
            if technique:
                technique_id = next((ref['external_id'] for ref in technique.get('external_references', [])), None)
                translated_description = translations.get(original_name, {}).get("translated_description", technique.get('description', '')).replace('\n', ' ')
                markdown_content += f"| [{technique_id}](https://attack.mitre.org/techniques/{technique_id}) | {translated_name} | {translated_description} |\n"

        with open(os.path.join(tactic_dir, "index.md"), "w", encoding="utf-8") as file:
            file.write(markdown_content)

# 生成每个战术的 Markdown 文件
print(tactic_techniques)
generate_tactic_markdown_files(tactic_techniques, translations)
