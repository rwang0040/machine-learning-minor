"""Create personal B01/B02/B03/B04 unit copies without overwriting student work."""

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
    parser.add_argument(
        "--unit",
        action="append",
        choices=[
            "split-evaluation",
            "linear-regression",
            "regularization",
            "decision-tree",
        ],
        help="仅添加指定实验单元，可用于已有个人目录；不覆盖已有单元",
    )
    args = parser.parse_args()
    if not re.fullmatch(r"[A-Za-z0-9_-]{1,64}", args.student_id):
        parser.error("个人标识格式不正确")
    root = Path(__file__).resolve().parents[1]
    destination = root / "work" / args.student_id
    units = list(
        dict.fromkeys(
            args.unit
            or [
                "split-evaluation",
                "linear-regression",
                "regularization",
                "decision-tree",
            ]
        )
    )
    if destination.exists() and not args.unit:
        parser.error(f"目录已存在，不覆盖：{destination}")
    for unit in units:
        if not (root / "units" / unit / "labs").is_dir():
            parser.error(f"缺少实验模板：{unit}")
    for unit in units:
        if (destination / "units" / unit).exists():
            parser.error(f"单元目录已存在，不覆盖：{destination / 'units' / unit}")
    destination.mkdir(parents=True, exist_ok=True)
    for unit in units:
        shutil.copytree(root / "units" / unit, destination / "units" / unit)
    release = json.loads((root / "RELEASE.json").read_text(encoding="utf-8"))
    info_path = destination / "work-info.json"
    info = (
        json.loads(info_path.read_text(encoding="utf-8"))
        if info_path.exists()
        else {"release_id": release["release_id"], "template_files": {}}
    )
    info["template_files"].update(
        {
            k: v
            for k, v in release["files"].items()
            if any(k.startswith(f"units/{unit}/") for unit in units)
            and ("/labs/" in k or "/data/" in k or "/project/" in k)
        }
    )
    info.setdefault("updates", []).append(
        {"release_id": release["release_id"], "units": units}
    )
    info_path.write_text(
        json.dumps(
            info,
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"个人副本已建立：{destination}")


if __name__ == "__main__":
    main()
