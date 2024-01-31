#!/usr/bin/python3
import re
import argparse
import yaml
import os

def convert_to_telegram_md(text):
    # Замена синтаксиса заголовков
    text = re.sub(r'^#+\s(.+)$', r'*\1*', text, flags=re.MULTILINE)
    # Замена синтаксиса жирного шрифта
    text = text.replace('***', '**')
    return text

def extract_sections(md_file_path, sections, include_content):
    with open(md_file_path, 'r', encoding='utf-8') as file:
        content = file.readlines()

    extracted = {}
    current_section = None

    for line in content:
        if re.match(r'^#+\s', line):
            section_name = line.strip('#').strip()
            if not sections or section_name in sections:
                current_section = section_name
                extracted[current_section] = ""
            else:
                current_section = None
        elif current_section and include_content:
            extracted[current_section] += line

    # Удаление последовательных пустых строк
    for section in extracted:
        extracted[section] = re.sub(r'\n\s*\n', '\n\n', extracted[section])

    return extracted

def generate_yaml_config(sections, file_name):
    with open(file_name, 'w') as file:
        yaml.dump({"sections": list(sections)}, file, default_flow_style=False)

def read_yaml_config(file_name):
    try:
        with open(file_name, 'r') as file:
            config = yaml.safe_load(file)
            return config.get('sections', [])
    except FileNotFoundError:
        return []

def main():
    parser = argparse.ArgumentParser(description="Extract sections from a Markdown file.")
    parser.add_argument("file", help="Markdown file path")
    parser.add_argument("-c", "--content", help="Include section contents", action="store_true")
    parser.add_argument("-g", "--generate", help="Generate YAML config file based on section list", action="store_true")
    parser.add_argument("-t", "--telegram", help="Convert to Telegram Markdown format", action="store_true")
    args = parser.parse_args()

    md_file_name, _ = os.path.splitext(os.path.basename(args.file))
    config_file_name = f"{md_file_name}_config.yaml"

    if args.generate:
        all_sections = extract_sections(args.file, [], False)
        generate_yaml_config(all_sections.keys(), config_file_name)
        print(f"Config file generated: {config_file_name}")
        return

    sections_to_extract = read_yaml_config(config_file_name)
    extracted_content = extract_sections(args.file, sections_to_extract, args.content)

    for section, content in extracted_content.items():
        if args.telegram:
            content = convert_to_telegram_md(content)
        print(f"## {section}")
        if args.content:
            print(content)

if __name__ == "__main__":
    main()
