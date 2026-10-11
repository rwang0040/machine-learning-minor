"""Create personal B01/B02 unit copies without overwriting student work."""

from pathlib import Path
import argparse
import json
import re
import shutil


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "student_id", help="学号或个人标识，只用字母、数字、下划线、连字符"
    )
    args = parser.parse_args()
    if not re.fullmatch(r"[A-Za-z0-9_-]{1,64}", args.student_id):
        parser.error("个人标识格式不正确")
    root = Path(__file__).resolve().parents[1]
    destination = root / "work" / args.student_id
    units = ["split-evaluation", "linear-regression"]
    if destination.exists():
        parser.error(f"目录已存在，不覆盖：{destination}")
    for unit in units:
        if not (root / "units" / unit / "labs").is_dir():
            parser.error(f"缺少实验模板：{unit}")
    try:
        destination.mkdir(parents=True, exist_ok=False)
    except FileExistsError:
        parser.error(f"目录已存在，不覆盖：{destination}")
    for unit in units:
        shutil.copytree(root / "units" / unit, destination / "units" / unit)
    release = json.loads((root / "RELEASE.json").read_text(encoding="utf-8"))
    (destination / "work-info.json").write_text(
        json.dumps(
            {
                "release_id": release["release_id"],
                "template_files": {
                    k: v
                    for k, v in release["files"].items()
                    if "/labs/" in k or "/data/" in k
                },
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"个人副本已建立：{destination}")


if __name__ == "__main__":
    main()
