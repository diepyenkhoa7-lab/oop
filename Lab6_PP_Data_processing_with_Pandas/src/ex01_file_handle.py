"""Chuyển log mượn sách dạng text sang CSV và Excel."""
import csv
import sys
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Font

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


PROJECT_DIR = Path(__file__).resolve().parent.parent
INPUT_FILE = PROJECT_DIR / "log_muonsach.txt"
CSV_FILE = PROJECT_DIR / "danhsach_muonsach.csv"
EXCEL_FILE = PROJECT_DIR / "sach_chua_tra.xlsx"
FIELDS = ["MaSV", "HoTen", "TenSach", "NgayMuon", "TrangThai"]

SAMPLE_LOG = """SV001|Nguyễn Văn An|Lập trình Python|2026-09-01|Chưa trả
SV002|Trần Thị Bích|Giải tích 1|2026-09-03|Đã trả
SV001|Nguyễn Văn An|Cơ sở dữ liệu|2026-09-05|Chưa trả
SV003|Lê Hoàng Nam|Lập trình Python|2026-09-10|Đã trả
SV004|Phạm Minh Khoa|Vật lý đại cương|2026-09-12|Chưa trả
"""


def create_sample_log() -> None:
    """Tạo file log đầu vào theo dữ liệu mẫu của đề."""
    with INPUT_FILE.open("w", encoding="utf-8", newline="") as file:
        file.write(SAMPLE_LOG)


def convert_log_to_csv() -> None:
    """Đọc log phân tách bằng | và ghi các bản ghi thành CSV."""
    with INPUT_FILE.open("r", encoding="utf-8") as source, CSV_FILE.open(
        "w", encoding="utf-8-sig", newline=""
    ) as target:
        writer = csv.DictWriter(target, fieldnames=FIELDS)
        writer.writeheader()

        for line_number, line in enumerate(source, start=1):
            line = line.strip()
            if not line:
                continue
            values = [value.strip() for value in line.split("|")]
            if len(values) != len(FIELDS):
                raise ValueError(f"Dòng {line_number} có {len(values)} trường, cần {len(FIELDS)}.")
            writer.writerow(dict(zip(FIELDS, values)))


def export_unreturned_books() -> int:
    """Lọc các sách chưa trả và xuất Excel với hàng tiêu đề in đậm."""
    with CSV_FILE.open("r", encoding="utf-8-sig", newline="") as source:
        unreturned = [row for row in csv.DictReader(source) if row["TrangThai"] == "Chưa trả"]

    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "ChuaTra"
    sheet.append(FIELDS)
    for cell in sheet[1]:
        cell.font = Font(bold=True)
    for row in unreturned:
        sheet.append([row[field] for field in FIELDS])

    for column_cells in sheet.columns:
        width = max(len(str(cell.value or "")) for cell in column_cells) + 2
        sheet.column_dimensions[column_cells[0].column_letter].width = width

    workbook.save(EXCEL_FILE)
    return len(unreturned)


def main() -> None:
    create_sample_log()
    convert_log_to_csv()
    count = export_unreturned_books()
    print(f"Đã tạo: {INPUT_FILE.name}, {CSV_FILE.name}, {EXCEL_FILE.name}")
    print(f"Số bản ghi sách chưa trả: {count}")


if __name__ == "__main__":
    main()

