--a. Hai truy vấn kết nối nhiều bảng (JOIN)
--Câu 1: Liệt kê tên nhân viên, tên phòng ban và công việc của họ.
SELECT NV.TenNV, NV.CongViec, PB.TenPB
FROM NhanVien NV
JOIN PhongBan PB ON NV.MaPB = PB.MaPB
--kq: 5 rows
 
--Câu 2: Liệt kê tên nhân viên, tên phòng ban và tên nhà cung cấp mà phòng ban đó liên hệ.
SELECT NV.TenNV, PB.TenPB, NCC.TenNCC
FROM NhanVien NV
JOIN PhongBan PB ON NV.MaPB = PB.MaPB
JOIN PhongBan_NCC PBNCC ON PB.MaPB = PBNCC.MaPB
JOIN NhaCungCap NCC ON PBNCC.MaNCC = NCC.MaNCC
-- kq: 10 rows
 
--b. Hai câu lệnh UPDATE
--Câu 3: Cập nhật công việc của nhân viên tên 'Nam Em' thành 'Trưởng phòng Nhân Sự'
UPDATE NhanVien
SET CongViec = N'Trưởng phòng Nhân Sự'
WHERE TenNV = N'Nam Em'
 
--Câu 4: Cập nhật số điện thoại của phòng ban "Phong Ke Toan" thành '0909999999'
UPDATE PhongBan
SET SoDienThoai = '0909999999'
WHERE TenPB = N'Phong Ke Toan'
--kq: 0 row
 
--c. Hai câu lệnh DELETE
---Câu 5: Xóa các phòng ban không có nhân viên nào
DELETE FROM PhongBan
WHERE MaPB NOT IN (
    SELECT DISTINCT MaPB FROM NhanVien )
--kq: 0 row
 
--Câu 6: Xóa các nhà cung cấp không có mối liên kết nào với bảng PhongBan_NCC
DELETE FROM NhaCungCap
WHERE NOT EXISTS (
    SELECT 1 
    FROM PhongBan_NCC 
    WHERE PhongBan_NCC.MaNCC = NhaCungCap.MaNCC )
--kq: 0 row
 
--d. Hai câu lệnh GROUP BY
--Câu 7: Liệt kê mã phòng ban và số lượng nhân viên tương ứng. Chỉ hiển thị các phòng có số lượng nhân viên lớn hơn hoặc bằng trung bình toàn bộ phòng ban.
SELECT MaPB, COUNT(*) AS SoLuongNV
FROM NhanVien
GROUP BY MaPB
HAVING COUNT(*) >= (
    SELECT AVG(SL) FROM (
        SELECT COUNT(*) AS SL FROM NhanVien GROUP BY MaPB ) AS sub ); 
--kq: 5 rows
 

--Câu 8: Liệt kê các chức danh công việc đang được đảm nhận và số lượng tương ứng, sắp xếp giảm dần theo số lượng.
SELECT CongViec, COUNT(*) AS SoLuong
FROM NhanVien
GROUP BY CongViec
HAVING COUNT(*) > 0
ORDER BY SoLuong DESC;
--kq: 5 rows
 
--e. Hai câu lệnh SUBQUERY
--Câu 9: Liệt kê tên các phòng ban có làm việc với nhà cung cấp đặt tại Hà Nội.
SELECT pb.TenPB
FROM PhongBan pb
WHERE pb.MaPB IN (
    SELECT MaPB
    FROM PhongBan_NCC pncc
    JOIN NhaCungCap ncc ON pncc.MaNCC = ncc.MaNCC
    WHERE ncc.DiaChi = 'Hà Nội'
);
--kq: 1 row
 
--Câu 10: Liệt kê tên, ngày kết hôn và công việc của các nhân viên có ngày kết hôn sớm hơn ngày kết hôn trung bình
SELECT nv.TenNV, vc.NgayKetHon, nv.CongViec
FROM VoChong vc
JOIN NhanVien nv ON vc.MaNV = nv.MaNV
WHERE vc.NgayKetHon < (
    SELECT '2016-06-19' );
--kq: 3 rows
 
--f. Hai câu lệnh bất kỳ
--Câu 11: Liệt kê tên nhân viên và tên phòng ban của những người có vợ/chồng cũng làm việc trong công ty và cùng một phòng ban.
SELECT nv.TenNV, pb.TenPB
FROM NhanVien nv
JOIN VoChong vc ON nv.MaNV = vc.MaNV
JOIN PhongBan pb ON nv.MaPB = pb.MaPB
WHERE vc.MaVC IN (
    SELECT MaNV FROM NhanVien WHERE MaPB = nv.MaPB );
--kq: 5 rows
 
--Câu 12: Liệt kê các tiểu bang có tổng kinh phí dự án lớn hơn trung bình các tiểu bang, bao gồm tên miền và tổng kinh phí.
SELECT Mien, SUM(KinhPhi) AS TongKinhPhi
FROM DuAn
GROUP BY Mien
HAVING SUM(KinhPhi) > (
    SELECT AVG(Tong) FROM (
        SELECT SUM(KinhPhi) AS Tong FROM DuAn GROUP BY Mien
    ) AS sub);
--kq: 1 row
