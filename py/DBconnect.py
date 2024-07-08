import sqlite3


class quanlydiemHeDH:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE ql_MonHoc (
                MaMH TEXT PRIMARY KEY,
                TenMH TEXT,
                SoTrinh INTEGER,
                HinhThucThi TEXT,
                HocKy INTEGER,
                MaKhoa TEXT
            )
        """)

        self.cursor.execute("""
            CREATE TABLE ql_Diem (
                MaSV TEXT PRIMARY KEY,
                TenSV TEXT,
                MaMH TEXT,
                MaLop TEXT,
                DiemLan1 REAL,
                DiemLan2 REAL,
                DiemTrungBinh REAL,
                XepLoai TEXT
            )
        """)

        self.cursor.execute("""
            CREATE TABLE ql_Khoa (
                MaKhoa TEXT PRIMARY KEY,
                TenKhoa TEXT
            )
        """)

        self.cursor.execute("""
            CREATE TABLE ql_Lop (
                MaKhoa TEXT PRIMARY KEY,
                MaLop TEXT,
                TenLop TEXT
            )
        """)

        self.cursor.execute("""
            CREATE TABLE ql_HoSoSV (
                MaSV TEXT PRIMARY KEY,
                TenSV TEXT,
                Tuoi INTEGER,
                GioiTinh TEXT,
                DiaChi TEXT,
                Email TEXT,
                SDT TEXT,
                MaLop TEXT
            )
        """)

        self.cursor.execute("""
            CREATE TABLE ql_TaiKhoan (
                User TEXT PRIMARY KEY,
                Password TEXT,
                LoaiTaiKhoan TEXT CHECK(LoaiTaiKhoan IN ('Admin', 'SinhVien'))
            )
        """)

        self.conn.commit()

    def insert_data(self):
        self.cursor.executemany("""
                    INSERT INTO ql_MonHoc VALUES (?, ?, ?, ?, ?, ?)
                """, [
            ('MH01', 'Toán cao cấp', 4, 'Thi viết', 1, 'K01'),
            ('MH02', 'Triết', 3, 'Thi viết', 2, 'K02'),
            ('MH03', 'Lập trình Java', 4, 'Thi thực hành', 1, 'K03'),
            ('MH04', 'Python', 3, 'Thi viết', 2, 'K04'),
            ('MH05', 'Tư tưởng HCM', 2, 'Thi viết', 1, 'K05'),
            ('MH06', 'Tiếng anh CN', 2, 'Thi viết', 2, 'K06')
        ])

        self.cursor.executemany("""
                    INSERT INTO ql_Diem VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, [
            ('SV01', 'Nguyễn Văn An', 'MH01', 'DCCntt', 7.5, 8.0, 7.83, 'A'),
            ('SV02', 'Trần Thị Phương Linh', 'MH02', 'DcMarketing', 8.0, 8.5, 8.17, 'A'),
            ('SV03', 'Phạm Văn Công', 'MH03', 'DcMarketing', 7.0, 7.5, 7.17, 'A'),
            ('SV04', 'Lê Thị Đào', 'MH04', 'DCDulich', 8.5, 9.0, 8.83, 'A'),
            ('SV05', 'Hoàng Văn Hoàng', 'MH05', 'DCCntt', 7.5, 8.0, 7.83, 'A'),
            ('SV06', 'Ngô Thị Hạnh', 'MH06', 'DCCntt', 8.0, 8.5, 8.17, 'A')
        ])

        self.cursor.executemany("""
                    INSERT INTO ql_Khoa VALUES (?, ?)
                """, [
            ('K01', 'Khoa Công nghệ thông tin'),
            ('K02', 'Khoa Marketing'),
            ('K03', 'Khoa Du lịch'),
            ('K04', 'Khoa Oto'),
            ('K05', 'Khoa Dược'),
            ('K06', 'Khoa Luật')
        ])

        self.cursor.executemany("""
                    INSERT INTO ql_Lop VALUES (?, ?, ?)
                """, [
            ('K01', 'DCCntt', 'Cntt'),
            ('K02', 'DcMarketing', 'Marketing'),
            ('K03', 'DCDulich', 'Dulich'),
            ('K04', 'DCOto', 'Oto'),
            ('K05', 'DCDuoc', 'Duoc'),
            ('K06', 'DCLuat', 'Luat')
        ])

        self.cursor.executemany("""
                    INSERT INTO ql_HoSoSV VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, [
            ('SV01', 'Nguyễn Văn An', 20, 'Nam', 'Hà Nội', 'sv01@example.com', '0123456789', 'DCCntt'),
            ('SV02', 'Trần Thị Phương Linh', 21, 'Nữ', 'Hải Phòng', 'sv02@example.com', '0123456790', 'DcMarketing'),
            ('SV03', 'Phạm Văn Công', 22, 'Nam', 'Đà Nẵng', 'sv03@example.com', '0123456709', 'DcMarketing'),
            ('SV04', 'Lê Thị Đào', 23, 'Nữ', 'Cần Thơ', 'sv04@example.com', '0123456907', 'DCDulich'),
            ('SV05', 'Hoàng Văn Hoàng', 24, 'Nam', 'TP HCM', 'sv05@example.com', '0123456970', 'DCCntt'),
            ('SV06', 'Ngô Thị Hạnh', 25, 'Nữ', 'Nghệ An', 'sv06@example.com', '0123456798', 'DCCntt')
        ])

        self.cursor.executemany("""
                    INSERT INTO ql_TaiKhoan VALUES (?, ?, ?)
                """, [
            ('admin', 'admin123', 'Admin'),
            ('SV01', 'sv01@123', 'SinhVien'),
            ('SV02', 'sv02@123', 'SinhVien'),
            ('SV03', 'sv03@123', 'SinhVien'),
            ('SV04', 'sv04@123', 'SinhVien'),
            ('SV05', 'sv05@123', 'SinhVien'),
            ('SV06', 'sv06@123', 'SinhVien')
        ])

        self.conn.commit()


db = quanlydiemHeDH('ql_DiemHeDH.db')
db.create_tables()
db.insert_data()
