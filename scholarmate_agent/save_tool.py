import csv
import json
from pathlib import Path
from google.adk.tools import FunctionTool

DEFAULT_CSV_PATH = Path(__file__).resolve().parents[1] / "scholarships_output.csv"


def save_scholarships_to_csv(ranked_scholarships: str) -> str:
    """
    Save ranked scholarships to a CSV file.
    Input comes in as JSON string.
    """
    try:
        data = json.loads(ranked_scholarships)
    except Exception:
        return "Error: Could not parse JSON for scholarships."

    if not isinstance(data, list):
        return "Error: Expected a JSON list but received something else."

    fieldnames = [
        "name",
        "provider",
        "country",
        "degree_level",
        "field",
        "deadline",
        "funding",
        "reason_match",
        "link",
    ]

    with open(DEFAULT_CSV_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for item in data:
            row = {key: item.get(key, "") for key in fieldnames}
            writer.writerow(row)

    return f"Saved {len(data)} scholarships to: {DEFAULT_CSV_PATH}"


save_scholarships_to_csv = FunctionTool(
    save_scholarships_to_csv
)