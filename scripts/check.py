#!/usr/bin/env python3
"""Repository consistency checks run by CI and before every release.

Usage: python3 scripts/check.py [--tag vX.Y.Z]
"""

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LINK = re.compile(r"\]\(([^)\s#]+)(?:#[^)]*)?\)|src=\"([^\"]+)\"")
errors = []


def fail(message):
    errors.append(message)


def frontmatter(path):
    text = path.read_text()
    match = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not match:
        fail(f"{path.relative_to(ROOT)}: missing frontmatter")
        return {}
    fields = {}
    for line in match.group(1).splitlines():
        key, _, value = line.partition(":")
        fields[key.strip()] = value.strip()
    return fields


def check_skills():
    skills = sorted(ROOT.glob("plugins/*/skills/*/SKILL.md"))
    if not skills:
        fail("no skills found")
    for path in skills:
        rel = path.relative_to(ROOT)
        fields = frontmatter(path)
        folder = path.parent.name
        name = fields.get("name", "")
        description = fields.get("description", "")
        if name != folder:
            fail(f"{rel}: name '{name}' does not match folder '{folder}'")
        if not name.endswith("-playbook"):
            fail(f"{rel}: name '{name}' must end with -playbook")
        if not description:
            fail(f"{rel}: missing description")
        if len(description) > 1024:
            fail(f"{rel}: description is {len(description)} characters (max 1024)")
        if "<" in description or ">" in description:
            fail(f"{rel}: description must not contain < or >")


def check_links():
    files = [ROOT / "README.md", ROOT / "CHANGELOG.md", *ROOT.glob("plugins/*/skills/**/*.md"), *ROOT.glob("assets/**/*.md")]
    for path in files:
        for match in LINK.finditer(path.read_text()):
            target = match.group(1) or match.group(2)
            if re.match(r"[a-z]+:", target) or target.startswith("/"):
                continue
            if not (path.parent / target).resolve().exists():
                fail(f"{path.relative_to(ROOT)}: broken link {target}")


def check_versions(tag):
    versions = {}
    for manifest in sorted(ROOT.glob("plugins/*/.*-plugin/plugin.json")):
        versions[str(manifest.relative_to(ROOT))] = json.loads(manifest.read_text()).get("version")
    for market in [ROOT / ".claude-plugin/marketplace.json", ROOT / ".agents/plugins/marketplace.json"]:
        for entry in json.loads(market.read_text()).get("plugins", []):
            if "version" in entry:
                fail(f"{market.relative_to(ROOT)}: entry '{entry['name']}' must not set a version (plugin.json is the source of truth)")
    changelog = re.search(r"^## \[(\d+\.\d+\.\d+)\]", (ROOT / "CHANGELOG.md").read_text(), re.M)
    versions["CHANGELOG.md"] = changelog.group(1) if changelog else None
    if tag:
        versions["git tag"] = tag.removeprefix("v")
    if len(set(versions.values())) != 1 or None in versions.values():
        details = ", ".join(f"{k}={v}" for k, v in versions.items())
        fail(f"versions disagree: {details}")


def check_assets():
    credits = (ROOT / "assets/portraits/CREDITS.md").read_text()
    for image in sorted((ROOT / "assets/portraits").glob("*.png")):
        base = image.name.removesuffix("-320.png").removesuffix(".png")
        if f"`{base}.png`" not in credits:
            fail(f"assets/portraits/{image.name}: no entry in CREDITS.md")
    tracked = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True, check=True).stdout.split()
    for rel in tracked:
        path = ROOT / rel
        if path.suffix in {".md", ".json"} and path.exists() and "PERMISSION PENDING" in path.read_text():
            fail(f"{rel}: contains PERMISSION PENDING material")
    for plugin in sorted(ROOT.glob("plugins/*/.claude-plugin")):
        if not (plugin / "icon.png").exists():
            fail(f"{plugin.relative_to(ROOT)}: missing icon.png")


def main():
    tag = None
    if "--tag" in sys.argv:
        tag = sys.argv[sys.argv.index("--tag") + 1]
    check_skills()
    check_links()
    check_versions(tag)
    check_assets()
    if errors:
        print("\n".join(f"✘ {e}" for e in errors))
        sys.exit(1)
    print("✔ all checks passed")


if __name__ == "__main__":
    main()
