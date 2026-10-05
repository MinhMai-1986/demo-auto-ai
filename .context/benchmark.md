# BENCHMARK CONTEXT: GIẢM TỔN THẤT ĐIỆN NĂNG TRONG HỆ THỐNG ĐIỆN

---

# PHẦN 1: QUY CHUẨN GIÁO TRÌNH (TÀI LIỆU GỐC TỪ 3 FILE PDF)

Bản tổng hợp trích xuất toàn bộ Lý thuyết, Công thức toán học, Bảng số liệu và Quy chuẩn tính toán từ 3 giáo trình nền tảng:
1. *Giáo trình Lưới điện* (Trần Bách, NXB Giáo dục, 2007)
2. *Hệ thống Truyền tải và Phân phối điện* (Hồ Văn Hiền, NXB ĐHQG TP.HCM, 2004)
3. *Giáo trình Cung cấp điện* (Nguyễn Xuân Phú, Nguyễn Công Hiền, Nguyễn Bội Khuê)

---

## 1.1 Khái niệm & Phân loại Tổn thất Điện năng

### 1.1.1 Định nghĩa và Bản chất Vật lý
Tổn thất điện năng trong hệ thống điện bao gồm tổn thất công suất tác dụng ($\Delta P$), tổn thất công suất phản kháng ($\Delta Q$) và tổn thất điện năng tích lũy ($\Delta A$). Đây là chỉ tiêu kinh tế - kỹ thuật phản ánh chất lượng vận hành và trình độ quản lý lưới điện.

### 1.1.2 Biểu thức Tính toán Tổn thất Công suất tác dụng ($\Delta P$)
- **Tổn thất Joule-Lenz trên đường dây 3 pha cân bằng**:
  $$\Delta P = 3 I^2 R = \frac{P^2 + Q^2}{U^2} R = \frac{S^2}{U^2} R$$
  *Trong đó:*
  - $I$: Dòng điện hiệu dụng pha ($A$)
  - $R$: Điện trở 1 pha đường dây ($\Omega$)
  - $P, Q, S$: Công suất tác dụng ($kW$), phản kháng ($kVAR$), toàn phần ($kVA$) truyền tải trên đường dây
  - $U$: Điện áp dây vận hành ($kV$)

- **Đối với phát tuyến có phụ tải hỗn hợp (Tập trung + Phân bố đều)**:
  $$\Delta P_d = \frac{P_{tt}^2 + Q_{tt}^2}{U^2} R + \frac{1}{3} \frac{P_{pb}^2 + Q_{pb}^2}{U^2} R$$
  *Trong đó:*
  - $P_{tt}, Q_{tt}$: Công suất phụ tải tập trung tại cuối tuyến
  - $P_{pb}, Q_{pb}$: Tổng công suất phụ tải phân bố đều dọc tuyến
  - Hệ số $\frac{1}{3}$: Quy đổi tổn thất công suất của phụ tải phân bố đều tương đương phụ tải tập trung cuối tuyến.

### 1.1.3 Biểu thức Tính toán Tổn thất Công suất phản kháng ($\Delta Q$)
- **Tổn thất công suất phản kháng trên điện kháng đường dây**:
  $$\Delta Q = 3 I^2 X = \frac{P^2 + Q^2}{U^2} X$$
- **Đối với phát tuyến có phụ tải hỗn hợp**:
  $$\Delta Q_d = \frac{P_{tt}^2 + Q_{tt}^2}{U^2} X + \frac{1}{3} \frac{P_{pb}^2 + Q_{pb}^2}{U^2} X$$
  *Trong đó:* $X$ là điện kháng 1 pha của đường dây ($\Omega$).

### 1.1.4 Quy trình Tính Sụt áp ($\Delta U$) và Độ Sụt áp Tương đối ($\Delta U\%$)
- **Sụt áp tuyệt đối tại nút cuối phát tuyến trung áp**:
  $$\Delta U = \frac{(P_{tt} + 0,5 P_{pb}) R + (Q_{tt} + 0,5 Q_{pb}) X}{U_{đm}}$$
  *Hệ số $0,5$*: Quy đổi sụt áp của phụ tải phân bố đều dọc tuyến.
- **Độ sụt áp tương đối phần trăm**:
  $$\Delta U\% = \frac{\Delta U}{U_{đm}} \times 100\%$$

### 1.1.5 Tổn thất Công suất và Điện năng trong Máy biến áp
Trạm biến áp phân phối gồm $n$ máy biến áp vận hành song song:
- **Tổn thất không tải (sắt / từ hóa)**:
  - Tổn thất công suất tác dụng không tải: $\Delta P_0$ ($kW$)
  - Tổn thất công suất phản kháng không tải:
    $$\Delta Q_0 = \frac{i_0\%}{100} S_{đmTB} \quad (kVAR)$$
- **Tổn thất có tải (đồng / ngắn mạch)**:
  - Tổn thất công suất tác dụng ngắn mạch: $\Delta P_k$ ($kW$)
  - Tổn thất công suất phản kháng ngắn mạch:
    $$\Delta Q_k = \frac{u_k\%}{100} S_{đmTB} \quad (kVAR)$$
- **Tổn thất quy đổi xét đương lượng kinh tế $k_{kt}$** ($kW/kVAR$):
  $$\Delta P_0' = \Delta P_0 + k_{kt} \cdot \Delta Q_0$$
  $$\Delta P_k' = \Delta P_k + k_{kt} \cdot \Delta Q_k$$
  *(Giá trị $k_{kt}$ nằm trong khoảng $0,02 \div 0,15 \text{ kW/kVAR}$, thường lấy trung bình $0,05 \div 0,10 \text{ kW/kVAR}$)*.
- **Tổng tổn thất công suất cực đại trong trạm $n$ máy biến áp song song**:
  $$\Delta P_B = n \Delta P_0 + \Delta P_k \frac{1}{n} \left(\frac{S_{pt}}{S_{đmTB}}\right)^2$$

### 1.1.6 Tích lũy Tổn thất Điện năng theo Thời gian ($\Delta A$)
- **Công thức tính điện năng tổn thất tích lũy năm**:
  $$\Delta A = \Delta P_{max} \cdot \tau \quad (kWh/năm)$$
  *Trong đó:*
  - $\Delta P_{max}$: Tổn thất công suất cực đại ($kW$)
  - $\tau$: Thời gian tổn thất công suất cực đại ($giờ/năm$)
- **Thời gian sử dụng công suất cực đại ($T_{max}$)**:
  $$T_{max} = \frac{A_{năm}}{P_{max}} \quad (giờ/năm)$$
- **Công thức kinh nghiệm Kezevits xác định $\tau$ theo $T_{max}$**:
  $$\tau = \left(0,124 + 10^{-4} T_{max}\right)^2 \times 8760 \quad (giờ/năm)$$
- **Hệ số phụ tải ($K_{pt}$) và Hệ số tổn thất ($K_{tt}$)**:
  $$K_{pt} = \frac{T_{max}}{8760}, \quad K_{tt} = \frac{\tau}{8760}$$
  *Mối quan hệ Buller-Woodrow:*
  $$K_{tt} = a K_{pt} + (1-a) K_{pt}^2 \quad (với \ a = 0,2 \div 0,3)$$

---

## 1.2 Nguyên lý & Công thức Các Giải pháp Giảm Tổn thất

### 1.2.1 Giải pháp Bù Công suất Phản kháng (Tụ bù tĩnh)
- **Nguyên lý**: Tụ bù tĩnh phát công suất phản kháng $Q_c$ tại chỗ, triệt tiêu dòng điện phản kháng $I_q$ truyền tải trên phát tuyến, làm giảm dòng tổng $I = \sqrt{I_p^2 + I_q^2}$, từ đó giảm tổn thất nhiệt $\Delta P \sim I^2$ và giảm sụt áp $\Delta U$.
- **Xác định dung lượng tụ bù $Q_c$ nâng hệ số công suất từ $\cos\varphi_1$ lên $\cos\varphi_2$**:
  $$Q_c = P_\Sigma \cdot (\tan\varphi_1 - \tan\varphi_2)$$
  *Trong đó:* $\tan\varphi_1 = \tan(\arccos \cos\varphi_1)$, $\tan\varphi_2 = \tan(\arccos \cos\varphi_2)$.
- **Các thông số vận hành chế độ sau bù**:
  $$Q_2 = Q_1 - Q_c$$
  $$S_2 = \sqrt{P_\Sigma^2 + Q_2^2}$$
  $$I_2 = \frac{S_2}{\sqrt{3} U_{đm}}$$
  $$\Delta P_{d2} = \frac{P_\Sigma^2 + (Q_1 - Q_c)^2}{U^2} R$$
  $$\Delta A_{TK} = (\Delta P_{d1} - \Delta P_{d2}) \times \tau$$

### 1.2.2 Giải pháp Vận hành Kinh tế Máy biến áp Song song
- **Nguyên lý**: Trong trạm gồm 2 máy biến áp vận hành song song, khi phụ tải nhỏ, tổn thất sắt không tải $\Delta P_0$ chiếm ưu thế; khi phụ tải lớn, tổn thất đồng ngắn mạch $\Delta P_k$ tăng theo bình phương tải. Việc chuyển đổi số lượng máy biến áp vận hành giúp tối thiểu hóa tổng tổn thất $\Delta P_T$.
- **Ngưỡng phụ tải kinh tế (Phụ tải chuyển đổi $S_{pt,tưu}$)**:
  $$S_{pt,tưu} = S_{đmTB} \times \sqrt{\frac{2 \Delta P_0'}{\Delta P_k'}} = S_{đmTB} \times \sqrt{2 \frac{\Delta P_0 + k_{kt} \Delta Q_0}{\Delta P_k + k_{kt} \Delta Q_k}}$$
- **Quy tắc điều độ vận hành**:
  - Khi phụ tải thực tế $S_{pt} < S_{pt,tưu}$: Đóng vận hành **01 máy biến áp** (cắt 01 máy để triệt tiêu tổn thất không tải).
  - Khi phụ tải thực tế $S_{pt} \ge S_{pt,tưu}$: Đóng vận hành **02 máy biến áp song song** (chia tải để giảm tổn thất ngắn mạch).

---

## 1.3 Quy chuẩn Mô hình hóa & Tính toán Ma trận Lưới điện

### 1.3.1 Sơ đồ Thay thế Phần tử Mạng điện
- **Đường dây**: Sơ đồ thay thế hình $\Pi$ thu gọn bao gồm điện trở $R = r_0 L$, điện kháng $X = x_0 L$, và dung dẫn $B = b_0 L$.
- **Máy biến áp**: Tổng trở $Z_B = R_B + j X_B$ quy đổi về cấp điện áp nghiên cứu:
  $$R_B = \frac{\Delta P_k U_{đm}^2 10^3}{S_{đmTB}^2} \quad (\Omega), \quad X_B = \frac{u_k\% U_{đm}^2 10}{S_{đmTB}} \quad (\Omega)$$

### 1.3.2 Ma trận Tổng dẫn Thanh cái ($Y_{bus}$) & Ma trận Tổng trở Thanh cái ($Z_{bus}$)
- **Thành lập Ma trận $Y_{bus}$**:
  - Phần tử đường chéo $Y_{kk} = \sum y_{kj}$ (tổng tổng dẫn nối với nút $k$).
  - Phần tử ngoài đường chéo $Y_{ij} = -y_{ij}$ (tổng dẫn nhánh nối giữa nút $i$ và nút $j$).
- **Thành lập Ma trận $Z_{bus}$**: Sử dụng thuật toán thêm nhánh từng bước (`zbuild`, `zbuildpi`) lấy nút trung tính làm chuẩn.

### 1.3.3 Tối ưu hóa Bù Công suất Phản kháng bằng Phương pháp Lagrange
- **Hàm mục tiêu**: Cực tiểu hóa tổng tổn thất công suất tác dụng:
  $$\min \Delta P = \sum_{i,j} I_{ij}^2 R_{ij}$$
- **Ràng buộc**: Tổng dung lượng bù bằng dung lượng yêu cầu:
  $$\sum_{i=1}^{m} Q_{bù,i} = Q_{bù,\Sigma}$$
- **Hàm Lagrange**:
  $$L(Q_{bù,i}, \lambda) = \Delta P(Q_{bù,i}) - \lambda \left(\sum Q_{bù,i} - Q_{bù,\Sigma}\right)$$
- **Xử lý nghiệm âm**: Giải hệ $\frac{\partial L}{\partial Q_{bù,i}} = 0$. Nếu xuất hiện $Q_{bù,k} < 0$, gán $Q_{bù,k} = 0$ và tái giải hệ phương trình $(m-1)$ ẩn còn lại.

---

# PHẦN 2: TỔNG HỢP BÀI VIẾT BÁO CÁO (TỪ 2 FILE WORD)

Tổng hợp toàn bộ nội dung từ 2 tài liệu bài viết đồ án:
1. `NotebookLM_bao_cao_hoan_chinh_giam_ton_that_dien_nang.docx`
2. `NotebookLM_phieu_khoa_du_lieu_va_outline_bao_cao.docx`

---

## 2.1 Bảng Dữ liệu Tính toán Đã khóa Chính thức (Ground-Truth Baseline)

*Bảng thông số kỹ thuật đã kiểm toán độc lập dựa trên 4 giáo trình chuẩn và khóa cứng làm cơ sở cho toàn bộ tính toán.*

| STT | Thông số hệ thống | Ký hiệu | Đơn vị | Giá trị | Nguồn tài liệu & Vị trí | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | Điện áp định mức phát tuyến | $U_{đm}$ | kV | **22** | Hồ Văn Hiền, Ví dụ 9.6, Tr. 364 | CÓ NGUỒN |
| **2** | Chiều dài tuyến đường dây | $L$ | km | **10** | Hồ Văn Hiền, Ví dụ 9.6, Tr. 364 | CÓ NGUỒN |
| **3** | Loại dây dẫn trên không | - | - | **AC-120** | Hồ Văn Hiền, Ví dụ 9.6, Tr. 364 | CÓ NGUỒN |
| **4** | Điện trở đơn vị dây AC-120 | $r_0$ | $\Omega$/km | **0,27** | Hồ Văn Hiền, Ví dụ 9.6, Tr. 364 | CÓ NGUỒN |
| **5** | Điện kháng đơn vị dây AC-120 | $x_0$ | $\Omega$/km | **0,35** | Skill-Training (Mục 2) / Trần Bách | CÓ NGUỒN |
| **6** | Tổng điện trở phát tuyến 22 kV | $R_d$ | $\Omega$ | **2,70** | Tính từ $r_0 \cdot L = 0,27 \times 10$ | ĐÃ CHỨNG MINH |
| **7** | Tổng điện kháng phát tuyến 22 kV | $X_d$ | $\Omega$ | **3,50** | Tính từ $x_0 \cdot L = 0,35 \times 10$ | ĐÃ CHỨNG MINH |
| **8** | Công suất phụ tải phân bố đều | $S_{pb}$ | kVA | **8000** | Hồ Văn Hiền, Ví dụ 9.6, Tr. 364 | CÓ NGUỒN |
| **9** | Công suất phụ tải tập trung cuối tuyến | $S_{tt}$ | kVA | **3000** | Hồ Văn Hiền, Ví dụ 9.6, Tr. 364 | CÓ NGUỒN |
| **10** | Hệ số công suất ban đầu | $\cos\varphi_1$ | - | **0,80** | Hồ Văn Hiền, Ví dụ 9.6, Tr. 364 | CÓ NGUỒN |
| **11** | Hệ số công suất yêu cầu sau bù | $\cos\varphi_2$ | - | **0,95** | Skill-Training / Nguyễn Xuân Phú | CÓ NGUỒN |
| **12** | Thời gian vận hành năm của tụ bù | $T$ | giờ/năm | **8760** | Hồ Văn Hiền / Nguyễn Xuân Phú | CÓ NGUỒN |
| **13** | Thời gian dùng CS cực đại | $T_{max}$ | giờ/năm | **4000** | Nguyễn Xuân Phú, Ví dụ 6.8, Tr. 122 | CÓ NGUỒN |
| **14** | Thời gian tổn thất cực đại | $\tau$ | giờ/năm | **2405,4** | Nguyễn Xuân Phú (Công thức Kezevits) | ĐÃ CHỨNG MINH |
| **15** | Số lượng MBA trạm phân phối | $n$ | máy | **2** | Nguyễn Xuân Phú, Ví dụ 5.3, Tr. 80 | CÓ NGUỒN |
| **16** | Dung lượng định mức 01 MBA | $S_{đmTB}$ | kVA | **560** | Nguyễn Xuân Phú, Ví dụ 5.3, Tr. 80 | CÓ NGUỒN |
| **17** | Tổn thất không tải 01 MBA | $\Delta P_0$ | kW | **2,50** | Nguyễn Xuân Phú, Ví dụ 5.3, Tr. 80 | CÓ NGUỒN |
| **18** | Tổn thất ngắn mạch 01 MBA | $\Delta P_k$ | kW | **9,40** | Nguyễn Xuân Phú, Ví dụ 5.3, Tr. 80 | CÓ NGUỒN |
| **19** | Dòng điện không tải 01 MBA | $i_0\%$ | % | **6,00** | Nguyễn Xuân Phú, Ví dụ 5.3, Tr. 80 | CÓ NGUỒN |
| **20** | Điện áp ngắn mạch 01 MBA | $u_k\%$ | % | **5,50** | Nguyễn Xuân Phú, Ví dụ 5.3, Tr. 80 | CÓ NGUỒN |
| **21** | CSPK không tải 01 MBA | $\Delta Q_0$ | kVAR | **33,60** | Tính từ $(i_0\%/100) \cdot S_{đmTB} = 0,06 \times 560$ | ĐÃ CHỨNG MINH |
| **22** | CSPK ngắn mạch 01 MBA | $\Delta Q_k$ | kVAR | **30,80** | Tính từ $(u_k\%/100) \cdot S_{đmTB} = 0,055 \times 560$ | ĐÃ CHỨNG MINH |
| **23** | Đương lượng kinh tế CSPK | $k_{kt}$ | kW/kVAR | **0,10** | Nguyễn Xuân Phú, Ví dụ 5.3, Tr. 80 | CÓ NGUỒN |
| **24** | Tổn thất sắt MBA quy đổi ($k_{kt}=0,1$) | $\Delta P_0'$ | kW | **5,86** | $\Delta P_0 + k_{kt} \cdot \Delta Q_0 = 2,5 + 0,1 \times 33,6$ | ĐÃ CHỨNG MINH |
| **25** | Tổn thất đồng MBA quy đổi ($k_{kt}=0,1$) | $\Delta P_k'$ | kW | **12,48** | $\Delta P_k + k_{kt} \cdot \Delta Q_k = 9,4 + 0,1 \times 30,8$ | ĐÃ CHỨNG MINH |
| **26** | Ngưỡng phụ tải kinh tế 2 MBA | $S_{pt,tưu}$ | kVA | **542,68** | $560 \times \sqrt{2 \times 5,86 / 12,48}$ (Đính chính 512 kVA) | ĐÃ ĐÍNH CHÍNH |

---

## 2.2 Bảng So sánh Tổng hợp Chỉ tiêu Kỹ thuật TH1 - TH2 - TH3

*Bảng kết quả tính toán đối chứng giữa 3 trường hợp vận hành:*
- **TH1**: Hiện trạng ban đầu (chưa bù $Q_c$, 02 MBA vận hành song song liên tục).
- **TH2**: Chỉ áp dụng giải pháp Bù công suất phản kháng ($Q_c = 3707,60 \text{ kVAR}$).
- **TH3**: Bù công suất phản kháng kết hợp Vận hành kinh tế máy biến áp song song.

| Chỉ tiêu kỹ thuật - vận hành | Đơn vị | TH1 (Hiện trạng) | TH2 (Bù CSPK) | TH3 (Bù + VHKT MBA) | Mức cải thiện (TH3 vs TH1) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Hệ số công suất ($\cos\varphi$)** | - | 0,80 | 0,95 | 0,95 | **Tăng +0,15** |
| **Dung lượng tụ bù tĩnh ($Q_c$)** | kVAR | 0,00 | 3707,60 | 3707,60 | Đặt tại Nút 1 cuối tuyến |
| **Dòng điện đầu tuyến ($I_{đầu}$)** | A | 288,68 | 243,09 | 243,09 | **Giảm 45,59 A (-15,8%)** |
| **Sụt áp tuyệt đối ($\Delta U$)** | V | 1355,45 | 917,35 | 917,35 | **Giảm 438,10 V** |
| **Sụt áp tương đối ($\Delta U\%$)** | % | 6,16% | 4,17% | 4,17% | **Giảm 1,99%** (từ 6,16% xuống 4,17%) |
| **Tổn thất CS đường dây ($\Delta P_d$)** | kW | 169,21 | 123,85 | 123,85 | **Giảm 45,36 kW (-26,8%)** |
| **Tổn thất CS trạm MBA ($\Delta P_B$)** | kW | 12,49 | 12,49 | 12,49 | Trùng nhau ở tải cực đại ($1000 \text{ kVA} > 542,68 \text{ kVA}$) |
| **Tổng tổn thất CS cực đại ($\Delta P_\Sigma$)** | kW | 181,70 | 136,34 | 136,34 | **Giảm 45,36 kW (-25,0%)** |
| **Tổn thất điện năng dây ($\Delta A_d$)** | kWh/năm | 407.018 | 297.909 | 297.909 | **Giảm 109.109 kWh (-26,8%)** |
| **Tổn thất điện năng MBA ($\Delta A_B$)** | kWh/năm | 30.043 | 30.043 | 15.043* | Giảm 15.000 kWh (*Giả định mô phỏng*) |
| **Tổng tổn thất điện năng năm ($\Delta A_\Sigma$)** | kWh/năm | 437.061 | 327.952 | 312.952* | Giảm 124.109 kWh (-28,4%) |
| **Điện năng tiết kiệm thực tế ($\Delta A_{TK}$)** | kWh/năm | **0** | **109.109** | **109.109** | **Tiết kiệm 109.109 kWh/năm** |
| **Tiền điện tiết kiệm hàng năm ($C_{TK}$)** | VNĐ/năm | 0 | THIẾU DỮ LIỆU | THIẾU DỮ LIỆU | $C_{TK} = 109.109 \times c_0$ (Cần đơn giá $c_0$) |

---

### 2.2.1 Nguyên tắc Bắt buộc về Trung thực Dữ liệu (Grounded Data Integrity)
1. **Mức tiết kiệm thực tế khẳng định**: Mức điện năng tiết kiệm thực tế DUY NHẤT được xác nhận chính xác cho đề tài là **109.109 kWh/năm** (đạt được từ giải pháp bù công suất phản kháng $Q_c = 3707,60 \text{ kVAR}$ trên phát tuyến 22 kV).
2. **Phân định rõ con số 15.000 kWh/năm**: Lượng tiết kiệm 15.000 kWh/năm tại trạm MBA trong TH3 chỉ được trình bày dưới dạng *"Mô hình giả định lý thuyết / minh họa phương pháp"*. TUYỆT ĐỐI KHÔNG khẳng định đây là kết quả thực tế do **THIẾU DỮ LIỆU ĐỒ THỊ PHỤ TẢI $S(t)$ THEO THỜI GIAN THỰC**.
3. **Đính chính sai sót giáo trình**: Ngưỡng phụ tải kinh tế vận hành trạm 02 MBA 560 kVA được đính chính chính xác là **542,68 kVA** (đính chính lỗi in $512 \text{ kVA}$ trong Giáo trình Nguyễn Xuân Phú, Tr. 80).

---

## 2.3 Outline Chi tiết Toàn bộ Báo cáo Cuối kỳ (4 Chương + Mở đầu / Kết luận)

### MỞ ĐẦU
1. **Tính cấp thiết của đề tài**: Tầm quan trọng của tổn thất điện năng trong hệ thống điện; ý nghĩa kinh tế - kỹ thuật của việc giảm tổn thất trên lưới truyền tải và phân phối.
2. **Mục tiêu nghiên cứu**: Hệ thống hóa cơ sở lý thuyết; đánh giá định lượng mức giảm tổn thất công suất ($\Delta P$), sụt áp ($\Delta U\%$) và tổn thất điện năng ($\Delta A$).
3. **Đối tượng và Phạm vi nghiên cứu**: Phát tuyến phân phối trung áp 22 kV và Trạm biến áp 22/0,4 kV. Tập trung hoàn toàn vào tổn thất kỹ thuật ở chế độ xác lập.
4. **Phương pháp nghiên cứu**: Tích hợp mô hình đại số, sơ đồ thay thế hình $\Pi$ thu gọn, tính toán 3 pha cân bằng và phân tích so sánh đối chứng (Before-After).

### CHƯƠNG 1: CƠ SỞ LÝ THUYẾT VỀ TỔN THẤT ĐIỆN NĂNG IN HỆ THỐNG ĐIỆN
- **1.1 Khái quát hệ thống điện và vị trí phát sinh tổn thất**: Cấu trúc Nguồn $\rightarrow$ Truyền tải $\rightarrow$ Phân phối $\rightarrow$ Hộ tiêu thụ.
- **1.2 Khái niệm tổn thất điện năng**: Định nghĩa $\Delta P, \Delta Q, \Delta A$ theo Định luật Joule-Lenz.
- **1.3 Phân loại tổn thất điện năng**: Tổn thất biến đổi (đồng, dây dẫn $\sim I^2$) và tổn thất cố định (sắt không tải $\Delta P_0$).
- **1.4 Biểu thức tổn thất công suất tác dụng trên đường dây**: Công thức $\Delta P = \frac{P^2+Q^2}{U^2} R$.
- **1.5 Biểu thức tổn thất công suất phản kháng trên đường dây**: Công thức $\Delta Q = \frac{P^2+Q^2}{U^2} X$.
- **1.6 Tổn thất công suất trong máy biến áp**: Tổn thất không tải $\Delta P_0, \Delta Q_0$, ngắn mạch $\Delta P_k, \Delta Q_k$ và đương lượng $k_{kt}$.
- **1.7 Tích lũy tổn thất điện năng theo thời gian**: Công thức $\Delta A = \Delta P_{max} \cdot \tau$.
- **1.8 Các chỉ tiêu đánh giá tổn thất**: Chỉ tiêu $T_{max}, \tau$, hệ số $K_{pt}, K_{tt}$, công thức Buller-Woodrow và Kezevits.
- **1.9 Các yếu tố ảnh hưởng đến tổn thất**: Hệ số $\cos\varphi$, điện áp $U$, điện trở $R$, sự nhấp nhô phụ tải và lệch pha.

### CHƯƠNG 2: NGUYÊN NHÂN VÀ PHƯƠNG PHÁP TÍNH TỔN THẤT
- **2.1 Phân tích nguyên nhân gây tổn thất kỹ thuật**: Dòng $Q$ lớn, sụt áp $U$, MBA vận hành non tải/quá tải, bán kính cấp điện lớn.
- **2.2 Mô hình sơ đồ thay thế đường dây**: Mô hình hình $\Pi$, phụ tải tập trung cuối tuyến và phụ tải phân bố đều.
- **2.3 Phương pháp tính dòng điện và công suất 3 pha**: Xác định $S = \sqrt{P^2+Q^2}$ và $I = \frac{S}{\sqrt{3} U}$.
- **2.4 Quy trình tính tổn thất $\Delta P, \Delta Q$ cho phát tuyến phụ tải hỗn hợp**: Áp dụng hệ số $\frac{1}{3}$ cho phụ tải phân bố.
- **2.5 Quy trình tính tổn thất điện áp $\Delta U, \Delta U\%$**: Áp dụng hệ số $0,5$ cho phụ tải phân bố.
- **2.6 Phương pháp tính tổn thất điện năng theo $\tau$**: Áp dụng công thức Kezevits $\tau = (0,124 + 10^{-4} T_{max})^2 \times 8760$.
- **2.7 Quy trình tính tổn thất trạm máy biến áp**: Phương pháp tính trạm $n$ máy biến áp vận hành song song.
- **2.8 Nguyên lý bù công suất phản kháng**: Bù ngang bằng tụ bù tĩnh $Q_c$ phát tại chỗ triệt tiêu dòng $Q$.
- **2.9 Phương pháp tính dung lượng tụ bù và chế độ sau bù**: Công thức $Q_c = P (\tan\varphi_1 - \tan\varphi_2)$, tính lại $I_2, \Delta P_{d2}, \Delta U_2\%$.
- **2.10 Nguyên lý và công thức vận hành kinh tế máy biến áp song song**: Xác định ngưỡng $S_{pt,tưu} = 542,68 \text{ kVA}$.
- **2.11 Tiêu chí so sánh đối chứng TH1 – TH2 – TH3**: Bảng tiêu chí so sánh, phân tách kết quả thực tế và mô phỏng.

### CHƯƠNG 3: CÁC GIẢI PHÁP KỸ THUẬT VÀ VẬN HÀNH GIẢM TỔN THẤT ĐIỆN NĂNG
- **3.1 Giải pháp bù công suất phản kháng**: Tụ bù tĩnh $Q_c = 3707,60 \text{ kVAR}$ đặt tại Nút 1 cuối tuyến.
- **3.2 Giải pháp vận hành kinh tế máy biến áp song song**: Quy trình đóng/cắt tự động theo ngưỡng $S_{pt,tưu} = 542,68 \text{ kVA}$.
- **3.3 Các giải pháp cải tạo kết cấu lưới điện và tối ưu vận hành**: Nâng cấp điện áp $U$, chọn tiết diện dây theo mật độ dòng kinh tế $j_{kt}$, san phẳng đồ thị phụ tải, hoán đảo pha.
- **3.4 Phương pháp đánh giá hiệu quả kỹ thuật và kinh tế**: Mức giảm tổn thất $\Delta P_{giảm}$, điện năng tiết kiệm $\Delta A_{TK}$, tiền điện tiết kiệm $C_{TK} = \Delta A_{TK} \cdot c_0$, thời gian hoàn vốn $T_{hv}$.

### CHƯƠNG 4: TÍNH TOÁN ÁP DỤNG MẪU VÀ ĐÁNH GIÁ HIỆU QUẢ GIẢM TỔN THẤT ĐIỆN NĂNG
- **4.1 Đặt bài toán và Dữ liệu đầu vào**: Phát tuyến 22 kV AC-120 ($10 \text{ km}$), $S_{pb} = 8000 \text{ kVA}$, $S_{tt} = 3000 \text{ kVA}$, $\cos\varphi_1 = 0,80$; Trạm 02 MBA 560 kVA.
- **4.2 Tính toán Trường hợp 1 – Hiện trạng (TH1)**: $I_1 = 288,68 \text{ A}$, $\Delta P_{d1} = 169,21 \text{ kW}$, $\Delta U_1\% = 6,16\%$, $\Delta A_{\Sigma 1} = 437.061 \text{ kWh/năm}$.
- **4.3 Tính toán Trường hợp 2 – Bù CSPK (TH2)**: $Q_c = 3707,60 \text{ kVAR}$, $I_2 = 243,09 \text{ A}$ (-15,8%), $\Delta U_2\% = 4,17\%$, $\Delta P_{d2} = 123,85 \text{ kW}$ (-26,8%), tiết kiệm đường dây **109.109 kWh/năm**.
- **4.4 Tính toán Trường hợp 3 – Kết hợp Bù CSPK & VHKT MBA (TH3)**: $S_{pt,tưu} = 542,68 \text{ kVA}$. Giải thích thời điểm đỉnh tải $S_{pt,max} = 1000 \text{ kVA} > 542,68 \text{ kVA}$ phải chạy cả 2 máy.
- **4.5 Bảng so sánh tổng hợp chỉ tiêu kỹ thuật và Đánh giá hiệu quả**: Bảng tổng hợp so sánh TH1-TH2-TH3.
- **4.6 Phân tích Hạn chế và Kiến nghị bổ sung dữ liệu**:
  1. Trang bị hệ thống đo đếm tự động (AMI) thu thập đồ thị phụ tải thời gian thực $S(t)$ của trạm MBA.
  2. Bổ sung biểu giá điện EVN ($c_0$) và báo giá thiết bị tụ bù ($K_c$) để tính toán chỉ tiêu kinh tế ($C_{TK}, T_{hv}$).

### KẾT LUẬN VÀ KHUYẾN NGHỊ
1. **Kết luận**:
   - Khẳng định mức tiết kiệm điện năng đường dây **109.109 kWh/năm** đạt được từ giải pháp bù $Q_c = 3707,60 \text{ kVAR}$.
   - Khẳng định ngưỡng phụ tải kinh tế đính chính trạm 02 MBA 560 kVA là **542,68 kVA**.
2. **Khuyến nghị & Hướng phát triển**:
   - Đề xuất ứng dụng giải pháp tụ bù tĩnh trên các phát tuyến 22 kV tương tự.
   - Bổ sung đo đếm AMI $S(t)$ và đơn giá EVN $c_0$.
   - Mở rộng quy mô tính toán bằng các phần mềm chuyên dụng (ETAP, PSS/E, MATLAB Power System Toolbox).
