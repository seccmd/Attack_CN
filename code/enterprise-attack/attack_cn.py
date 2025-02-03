#!/usr/bin/env python3

from mitreattack.stix20 import MitreAttackData
import json
import os

# 全局 MitreAttackData 对象，保存全部数据
class MitreAttackManager:
    def __init__(self, data_path, translation_path=None, tactic_translation_path=None, version="enterprise-attack-16.1"):
        self.client = MitreAttackData(data_path)
        self.tactics = self.client.get_tactics()
        self.techniques = self.client.get_techniques(remove_revoked_deprecated=True)
        self.translations = self.load_translations(translation_path) if translation_path else {}
        self.tactic_translations = self.load_translations(tactic_translation_path) if tactic_translation_path else {}
        self.version = f"{version}"
        self.docs_dir = f"./Attack_CN/docs/{self.version}"

    def load_translations(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def save_translations(self, file_path):
        translations = {
            technique['name']: {
                "translated_name": technique['name'],
                "translated_description": technique.get('description', '')
            }
            for technique in self.techniques
        }
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(translations, file, ensure_ascii=False, indent=4)

    def get_tactic_techniques(self):
        tactic_priority = [
            tactic for tactic in self.tactic_translations.keys()
        ]

        tactic_techniques = {tactic['name']: [] for tactic in sorted(self.tactics, key=lambda t: tactic_priority.index(t['name']) if t['name'] in tactic_priority else len(tactic_priority))}
        for technique in self.techniques:
            #if not technique.get('x_mitre_is_subtechnique', False):
            for kill_chain_phase in technique.get('kill_chain_phases', []):
                tactic_name = next((tactic['name'] for tactic in self.tactics if tactic['x_mitre_shortname'] == kill_chain_phase['phase_name']), None)
                if tactic_name:
                    tactic_techniques[tactic_name].append(technique['name'])
        return tactic_techniques

    def generate_markdown_with_links(self, tactic_techniques):
        header_links = [
            f"[{self.tactic_translations.get(tactic, {}).get('translated_name', tactic)}](tactics/{tactic.replace(' ', '')}.md)"
            for tactic in tactic_techniques.keys()
        ]
        markdown_table = "| " + " | ".join(header_links) + " |\n"
        markdown_table += "|" + "|".join(["---"] * len(tactic_techniques)) + "|\n"
        max_techniques = max(len(tech_list) for tech_list in tactic_techniques.values())
        for i in range(max_techniques):
            row = []
            for tactic, tech_list in tactic_techniques.items():
                if i < len(tech_list):
                    technique_name = tech_list[i]
                    original_name = next((name for name, trans in self.translations.items() if trans["translated_name"] == technique_name), technique_name)
                    technique_id = next((ref['external_id'] for tech in self.techniques if tech['name'] == original_name for ref in tech.get('external_references', [])), None)
                    technique_link = f"[{technique_name}](techniques/{technique_id}.md)" if technique_id else technique_name
                    row.append(technique_link)
                else:
                    row.append("")
            markdown_table += "| " + " | ".join(row) + " |\n"
        return markdown_table

    def generate_tactic_markdown_files(self, tactic_techniques):
        output_dir = os.path.join(self.docs_dir, "tactics")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        for tactic, tech_list in tactic_techniques.items():
            translated_tactic_name = self.tactic_translations.get(tactic, {}).get("translated_name", tactic)
            tactic_description = self.tactic_translations.get(tactic, {}).get("translated_description", "")
            markdown_content = f"""---
hide:
  - toc
---

# {translated_tactic_name}

{tactic_description}

### 技术： {len(tech_list)}

| 编号 | 名字 | 描述 |
| --- | --- | --- |
"""
            sorted_tech_list = sorted(tech_list, key=lambda name: next((ref['external_id'] for tech in self.techniques if tech['name'] == name for ref in tech.get('external_references', [])), ''))
            for original_name in sorted_tech_list:
                translated_name = self.translations.get(original_name, {}).get("translated_name", original_name)
                technique = next((tech for tech in self.techniques if tech['name'] == original_name), None)
                if technique:
                    technique_id = next((ref['external_id'] for ref in technique.get('external_references', [])), None)
                    translated_description = self.translations.get(original_name, {}).get("translated_description", technique.get('description', '')).replace('\n', ' ')
                    markdown_content += f"| [{technique_id}](../techniques/{technique_id}.md) | {translated_name} | {translated_description} |\n"
            with open(os.path.join(output_dir, f"{tactic.replace(' ', '')}.md"), "w", encoding="utf-8") as file:
                file.write(markdown_content)

    def generate_technique_markdown_files(self):
        output_dir = os.path.join(self.docs_dir, "techniques")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        for technique in self.techniques:
            technique_id = next((ref['external_id'] for ref in technique.get('external_references', [])), None)
            if technique_id:
                translated_name = self.translations.get(technique['name'], {}).get("translated_name", technique['name'])
                translated_description = self.translations.get(technique['name'], {}).get("translated_description", technique.get('description', '')).replace('\n', ' ')
                markdown_content = f"""---
hide:
  - toc
---

# {translated_name}

{translated_description}
"""
                with open(os.path.join(output_dir, f"{technique_id}.md"), "w", encoding="utf-8") as file:
                    file.write(markdown_content)

# 初始化 MitreAttackManager 对象
manager = MitreAttackManager("./enterprise-attack.json", "./technique_translations_cn.json", "./tactic_translations_cn.json")

# 获取战术和技术
tactic_techniques = manager.get_tactic_techniques()

# 生成并保存带链接的 Markdown 表格
markdown_table_with_links = manager.generate_markdown_with_links(tactic_techniques)
with open(os.path.join(manager.docs_dir, "index_en.md"), "w", encoding="utf-8") as file:
    file.write("""---
hide:
  - toc
  - title
  - footer
  - navigation
---

# ATT&CK 中文版 

""" + markdown_table_with_links)

# 生成并保存带翻译的 Markdown 表格
translated_tactic_techniques = {tactic: [manager.translations.get(name, {}).get("translated_name", name) for name in tech_list] for tactic, tech_list in tactic_techniques.items()}
markdown_table_with_translations = manager.generate_markdown_with_links(translated_tactic_techniques)
with open(os.path.join(manager.docs_dir, "index.md"), "w", encoding="utf-8") as file:
    file.write("""---
hide:
  - toc
  - title
  - footer
  - navigation
---

# ATT&CK 中文版 

""" + markdown_table_with_translations)

# 生成每个战术的 Markdown 文件
manager.generate_tactic_markdown_files(tactic_techniques)

# 生成每个技术的 Markdown 文件
manager.generate_technique_markdown_files()
