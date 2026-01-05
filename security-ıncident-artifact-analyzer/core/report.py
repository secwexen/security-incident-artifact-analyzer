"""
report.py

Module responsible for transforming parsed artifacts into structured reports.
"""

from typing import Dict, Any
import json
from pathlib import Path


class ReportGenerator:
    """
    Generates JSON and Markdown reports from aggregated analysis results.
    """

    def __init__(self, output_dir: str) -> None:
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def to_json(self, data: Dict[str, Any], filename: str = "report.json") -> Path:
        """
        Save results as a JSON file.

        :param data: Aggregated analysis results.
        :param filename: Output filename.
        :return: Path to the generated file.
        """
        output_path = self.output_dir / filename
        with output_path.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        return output_path

    def to_markdown(self, data: Dict[str, Any], filename: str = "report.md") -> Path:
        """
        Save results as a Markdown summary.

        :param data: Aggregated analysis results.
        :param filename: Output filename.
        :return: Path to the generated file.
        """
        output_path = self.output_dir / filename

        lines = ["# Security Incident Artifact Analyzer Report", ""]
        for category, value in data.items():
            lines.append(f"## {category}")
            lines.append("")
            lines.append(f"Entries: {len(value) if isinstance(value, list) else 'N/A'}")
            lines.append("")

        output_path.write_text("\n".join(lines), encoding="utf-8")
        return output_path
