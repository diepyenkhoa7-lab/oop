"""Làm sạch dữ liệu bán hàng và xuất báo cáo theo khu vực."""
from pathlib import Path
import sys

import numpy as np
import pandas as pd

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


PROJECT_DIR = Path(__file__).resolve().parent.parent
INPUT_FILE = PROJECT_DIR / "sales_data.csv"
REPORT_FILE = PROJECT_DIR / "baocao_doanhthu_khuvuc.csv"

RAW_SALES = {
    "MaDon": ["HD01", "HD02", "HD03", "HD04", "HD02", "HD05", "HD06", "HD07"],
    "KhuVuc": [
        "Mien Bac", "Mien Nam", "Mien Trung", "Mien Bac",
        "Mien Nam", "Mien Nam", "Mien Bac", "Mien Trung",
    ],
    "SanPham": [
        "Laptop", "Dien Thoai", "May Tinh Bang", "Laptop",
        "Dien Thoai", "Tai Nghe", "Laptop", "May Tinh Bang",
    ],
    "SoLuong": [2, 5, np.nan, 1, 5, 10, 3, 2],
    "DonGia": [15000000, 8000000, 12000000, 15000000, 8000000, 500000, np.nan, 12000000],
}


def create_sample_sales_file() -> None:
    """Tạo sales_data.csv theo dữ liệu mẫu trong đề."""
    pd.DataFrame(RAW_SALES).to_csv(INPUT_FILE, index=False, encoding="utf-8")


def main() -> None:
    create_sample_sales_file()
    df = pd.read_csv(INPUT_FILE)

    print("Kích thước dữ liệu ban đầu:", df.shape)
    print("\nSố ô khuyết ban đầu:")
    print(df.isnull().sum())

    df = df.drop_duplicates().copy()
    df["SoLuong"] = df["SoLuong"].fillna(df["SoLuong"].median())
    df["DonGia"] = df["DonGia"].fillna(df["DonGia"].mean())

    df["ThanhTien"] = df["SoLuong"] * df["DonGia"]
    df["PhanLoaiDon"] = df["ThanhTien"].apply(
        lambda thanh_tien: "Don Hang Lon"
        if thanh_tien >= 20_000_000
        else "Don Hang Thuong"
    )

    don_mien_bac_gia_tri_cao = df[
        (df["KhuVuc"] == "Mien Bac") & (df["ThanhTien"] >= 15_000_000)
    ]
    print("\nĐơn hàng miền Bắc có thành tiền từ 15.000.000 trở lên:")
    print(don_mien_bac_gia_tri_cao.to_string(index=False))

    report = (
        df.groupby("KhuVuc")
        .agg(
            TongDoanhThu=("ThanhTien", "sum"),
            DoanhThuTrungBinh=("ThanhTien", "mean"),
            SoLuongDonHang=("MaDon", "count"),
        )
        .sort_index()
    )
    report.to_csv(REPORT_FILE, index=True, encoding="utf-8-sig")

    print("\nBáo cáo doanh thu theo khu vực:")
    print(report)
    print(f"\nĐã xuất báo cáo: {REPORT_FILE.name}")


if __name__ == "__main__":
    main()

