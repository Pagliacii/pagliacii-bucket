#!/usr/bin/env python3
# coding=utf-8

import json
import os


def get_app_info(json_file):
    with open(json_file, "r") as f:
        data = json.load(f)
        return {
            "name": os.path.splitext(os.path.basename(json_file))[0],
            "version": data["version"],
            "description": data["description"],
            "homepage": data["homepage"],
        }


def generate_apps_table(apps):
    table = "| Name | Version | Description |\n"
    table += "| :--: | :-----: | :---------: |\n"
    for app in apps:
        table += f"| [{app['name']}]({app['homepage']}) | {app['version']} | {app['description']} |\n"
    return table


def update_readme(apps_table):
    readme_path = "README.md"
    with open(readme_path, "r") as f:
        readme_content = f.readlines()

    start_marker = "<!-- APPS_TABLE_START -->\n"
    end_marker = "<!-- APPS_TABLE_END -->\n"
    start_index = readme_content.index(start_marker) + 1
    end_index = readme_content.index(end_marker)

    updated_readme_content = (
        readme_content[:start_index] + [apps_table] + readme_content[end_index:]
    )

    with open(readme_path, "w") as f:
        f.writelines(updated_readme_content)


def main():
    apps_dir = "./bucket"
    apps = [
        get_app_info(os.path.join(apps_dir, f))
        for f in os.listdir(apps_dir)
        if f.endswith(".json")
    ]

    apps.sort(key=lambda x: x["name"])  # Sort apps by name
    apps_table = generate_apps_table(apps)
    update_readme(apps_table)


if __name__ == "__main__":
    main()
