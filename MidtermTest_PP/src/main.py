"""Hệ thống quản lý học viên và khóa học của trung tâm Anh ngữ."""


class Nguoi:
    def __init__(self, ma_id: str, ho_ten: str, email: str) -> None:
        self.ma_id = ma_id
        self.ho_ten = ho_ten
        self.email = email

    def hien_thi_thong_tin(self) -> str:
        return f"Mã: {self.ma_id} | Họ tên: {self.ho_ten} | Email: {self.email}"

    def __str__(self) -> str:
        return f"[{self.ma_id}] {self.ho_ten}"


class HocVien(Nguoi):
    def __init__(self, ma_id: str, ho_ten: str, email: str) -> None:
        super().__init__(ma_id, ho_ten, email)
        self.danh_sach_khoa: set[str] = set()
        self.__tong_hoc_phi = 0

    @property
    def tong_hoc_phi(self) -> int:
        return self.__tong_hoc_phi

    @tong_hoc_phi.setter
    def tong_hoc_phi(self, gia_tri: int) -> None:
        if gia_tri < 0:
            raise ValueError("Tổng học phí không được âm!")
        self.__tong_hoc_phi = gia_tri

    def dang_ky_khoa_hoc(self, ten_khoa: str, hoc_phi: int) -> bool:
        if hoc_phi <= 0:
            raise ValueError("Học phí phải lớn hơn 0!")
        if not ten_khoa or not ten_khoa.strip():
            raise ValueError("Tên khóa học không được để trống!")
        if ten_khoa in self.danh_sach_khoa:
            return False
        self.danh_sach_khoa.add(ten_khoa)
        self.__tong_hoc_phi += hoc_phi
        return True

    def hien_thi_thong_tin(self) -> str:
        return (
            f"{super().hien_thi_thong_tin()} | "
            f"Số khóa đã đăng ký: {len(self.danh_sach_khoa)} | "
            f"Tổng học phí: {self.tong_hoc_phi}"
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, HocVien):
            return NotImplemented
        return self.ma_id == other.ma_id

    def __hash__(self) -> int:
        return hash(self.ma_id)


class GiangVien(Nguoi):
    def __init__(self, ma_id: str, ho_ten: str, email: str,
                 chuyen_mon: str, luong_theo_gio: float) -> None:
        super().__init__(ma_id, ho_ten, email)
        self.chuyen_mon = chuyen_mon
        self.__luong_theo_gio = 0.0
        self.luong_theo_gio = luong_theo_gio

    @property
    def luong_theo_gio(self) -> float:
        return self.__luong_theo_gio

    @luong_theo_gio.setter
    def luong_theo_gio(self, gia_tri: float) -> None:
        if gia_tri < 0:
            raise ValueError("Lương theo giờ không được âm!")
        self.__luong_theo_gio = gia_tri

    def hien_thi_thong_tin(self) -> str:
        return (
            f"{super().hien_thi_thong_tin()} | Chuyên môn: {self.chuyen_mon} | "
            f"Lương/giờ: {self.luong_theo_gio:,.0f}"
        )


class QuanLyTrungTam:
    def __init__(self) -> None:
        self.ds_hoc_vien: dict[str, HocVien] = {}

    def them_hoc_vien(self, hoc_vien: HocVien) -> None:
        self.ds_hoc_vien[hoc_vien.ma_id] = hoc_vien

    def tim_hoc_vien(self, ma_id: str) -> HocVien | None:
        return self.ds_hoc_vien.get(ma_id)

    def __len__(self) -> int:
        return len(self.ds_hoc_vien)


def _demo() -> None:
    try:
        hv1 = HocVien("HV01", "Nguyen Van A", "a@gmail.com")
        hv1.dang_ky_khoa_hoc("Python Basic", 1_500_000)
        hv1.dang_ky_khoa_hoc("Python Basic", 1_500_000)
        print(hv1.hien_thi_thong_tin())
        print("Khóa học:", hv1.danh_sach_khoa)
        print("Tổng học phí:", hv1.tong_hoc_phi)

        trung_tam = QuanLyTrungTam()
        trung_tam.them_hoc_vien(hv1)
        print("Số học viên:", len(trung_tam))
        print("Tra cứu HV01:", trung_tam.tim_hoc_vien("HV01"))
    except ValueError as loi:
        print("Lỗi validation:", loi)


if __name__ == "__main__":
    _demo()

