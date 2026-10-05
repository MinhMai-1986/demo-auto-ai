# TECHNICAL SPECIFICATION \& IMPLEMENTATION PLAN

## 1\. MỤC TIÊU DỰ ÁN \& PHẠM VI (PROJECT OVERVIEW)

* **Mô tả tổng quan đề tài**: Xây dựng hệ thống phần mềm chuyên dụng hỗ trợ phân tích, tính toán chế độ xác lập, mô phỏng tổn thất và tối ưu hóa giải pháp giảm tổn thất điện năng trong hệ thống truyền tải và phân phối điện. Hệ thống đóng vai trò là công cụ tự động hóa giúp kỹ sư và sinh viên chuyên ngành Hệ thống điện thực hiện các bài toán lớn như phân bố công suất, tối ưu dung lượng bù công suất phản kháng, phân tích sụt áp và vận hành kinh tế.
* **Các yêu cầu cốt lõi cần giải quyết**:

  * Tự động hóa quá trình xây dựng sơ đồ thay thế, thành lập ma trận tổng dẫn thanh cái ($Y\_{bus}$) và ma trận tổng trở thanh cái ($Z\_{bus}$) cho mạng điện phức tạp hoặc mạng phân phối hình tia.
  * Phân tích và tính toán tổn thất công suất tác dụng ($\\Delta P$), tổn thất công suất phản kháng ($\\Delta Q$), độ sụt áp ($\\Delta U$) và tổn thất điện năng tích lũy ($\\Delta A$) trên các phân đoạn đường dây và máy biến áp.
  * Phân biệt và quản lý hai nhóm tổn thất: tổn thất kỹ thuật (tổn thất đồng $\\Delta P\_{Cu}$, tổn thất sắt $\\Delta P\_{Fe}$, tổn thất quầng quang) và tổn thất phi kỹ thuật (gian lận điện, sai số thiết bị đo đếm, sai lệch thời điểm ghi công tơ).
  * Giải bài toán tối ưu hóa bù công suất phản kháng ($Q\_{bù}$) tại các nút tải bằng phương pháp nhân tử Lagrange để giảm thiểu tổn thất công suất tác dụng.
  * Trực quan hóa trắc đồ điện áp (Voltage Profile) dọc theo chiều dài đường dây và xuất báo cáo chỉ tiêu kỹ thuật - kinh tế hỗ trợ công tác quy hoạch, điều độ.

## 2\. YÊU CẦU KỸ THUẬT \& CÔNG NGHỆ (TECHNICAL REQUIREMENTS)

* **Ngôn ngữ lập trình \& Thư viện sử dụng**:

  * **Ngôn ngữ cốt lõi**: Python (phiên bản 3.10+) đảm bảo tính cấu trúc, dễ mở rộng và tích hợp tốt với các thư viện tính toán số học.
  * **Thư viện tính toán đại số \& tối ưu**: `NumPy` và `SciPy` sử dụng để thao tác ma trận thưa, thành lập $Y\_{bus}/Z\_{bus}$, giải hệ phương trình phi tuyến (phương pháp Gauss-Seidel, Newton-Raphson) và thuật toán tối ưu hóa Lagrange.
  * **Thư viện quản lý dữ liệu**: `Pandas` để xử lý, chuẩn hóa dữ liệu nút (`busdata`), dữ liệu nhánh/đường dây (`linedata`) và dữ liệu nguồn phát (`gendata`).
  * **Giao diện người dùng (UI/Web App)**: `Streamlit` dựng ứng dụng web tương tác trực quan, cho phép người dùng cấu hình tham số, chạy tính toán và xem kết quả theo thời gian thực.
  * **Thư viện trực quan hóa**: `Matplotlib` và `Plotly` phục vụ vẽ đồ thị trắc đồ điện áp dọc đường dây, đồ thị phụ tải và đường cong khả năng mang tải (Loadability Curve).
* **Cấu trúc thư mục dự án đề xuất**:

```text
power\_grid\_loss\_reduction/
├── config/
│   ├── \_\_init\_\_.py
│   └── settings.py             # Cấu hình công suất cơ bản S\_base, điện áp định mức U\_dm
├── data/
│   ├── busdata.csv             # Dữ liệu nút (loại nút, P\_tai, Q\_tai, U\_dat, min/max Q)
│   ├── linedata.csv            # Dữ liệu nhánh (nút đầu, nút cuối, R, X, B/2, nấc phân áp)
│   └── gendata.csv            # Dữ liệu máy phát (nút nối, R\_g, X\_g)
├── src/
│   ├── \_\_init\_\_.py
│   ├── network\_models/
│   │   ├── \_\_init\_\_.py
│   │   ├── impedance\_matrix.py # Thành lập ma trận Ybus, Zbus (zbuild, zbuildpi)
│   │   └── line\_transformer.py # Quy đổi thông số p.u., sơ đồ thay thế Pi/T
│   ├── solvers/
│   │   ├── \_\_init\_\_.py
│   │   ├── power\_flow.py       # Phân bố công suất (Gauss-Seidel, Newton-Raphson, Radial)
│   │   ├── loss\_calculator.py  # Tính Delta P, Delta Q, Tau, Delta A%
│   │   └── reactive\_opt.py     # Tối ưu dung lượng bù Q\_bu bằng Lagrange
│   └── utils/
│       ├── \_\_init\_\_.py
│       ├── data\_loader.py      # Đọc/ghi và kiểm tra định dạng tập tin CSV/Excel
│       └── visualizer.py       # Vẽ trắc đồ điện áp vprofile và biểu đồ tổn thất
├── app/
│   └── main\_app.py             # Giao diện điều khiển Streamlit
├── tests/
│   ├── test\_matrix.py          # Kiểm thử Ybus/Zbus
│   ├── test\_power\_flow.py      # Kiểm thử trút công suất
│   └── test\_optimization.py    # Kiểm thử thuật toán bù Lagrange
├── requirements.txt            # Danh sách thư viện phụ thuộc
└── README.md                   # Hướng dẫn cài đặt và vận hành
```

## 3\. DANH SÁCH TÍNH NĂNG CHI TIẾT (FEATURE BREAKDOWN)

* **Chi tiết từng mô-đun/tính năng cần viết code**:

  1. **Mô-đun Quản lý Dữ liệu Lưới điện (`data\_loader.py` \& `line\_transformer.py`)**:

     * Đọc dữ liệu đầu vào từ các tập tin cấu hình chuẩn: `busdata` (chứa các thông số $P\_{tải}, Q\_{tải}, U\_{đặt}, Q\_{min}, Q\_{max}$), `linedata` (chứa $R, X, B/2$, nấc biến áp) và `gendata`.
     * Chuyển đổi toàn bộ thông số kỹ thuật từ đơn vị có tên ($\\Omega, \\text{km}, \\text{kV}, \\text{MVA}$) sang hệ đơn vị tương đối (p.u.) dựa trên $S\_{cơ bản}$ và $U\_{cơ bản}$ đã chọn.
     * Thành lập ma trận tổng dẫn thanh cái $Y\_{bus}$ (`lfybus`) và ma trận tổng trở thanh cái $Z\_{bus}$ (`zbuild`, `zbuildpi`) bằng thuật toán thêm nhánh từng bước.
  2. **Mô-đun Phân bố Công suất \& Giải Chế độ Vận hành (`power\_flow.py`)**:

     * *Đối với mạng điện phân phối hình tia (mạng mở)*: Sử dụng phương pháp tính lặp dòng điện/công suất từ cuối đường dây về nguồn, bỏ qua điện dung đường dây ngắn dưới $50\\text{ km}$, tính sụt áp $\\Delta U$ theo công thức gần đúng $\\Delta U = \\frac{P \\cdot R + Q \\cdot X}{U\_{đm}}$.
     * *Đối với mạng điện kín/truyền tải phức tạp*: Triển khai phương pháp Gauss-Seidel (`lfgauss`) hoặc Newton-Raphson (`lfnewton`) giải hệ phương trình phi tuyến để tìm điện áp nút ($|U\_k|, \\delta\_k$) và dòng công suất chạy trên từng nhánh.
     * Tự động kiểm tra điều kiện ràng buộc công suất phản kháng $Q$ tại các nút máy phát/nút điều chỉnh điện áp, tự động chuyển đổi loại nút khi vi phạm giới hạn $Q\_{min}, Q\_{max}$.
  3. **Mô-đun Phân tích Tổn thất Kỹ thuật \& Điện năng (`loss\_calculator.py`)**:

     * Tính tổn thất công suất tác dụng $\\Delta P$ và công suất phản kháng $\\Delta Q$ trên từng đoạn đường dây ($\\Delta P = 3 I^2 R$) và trong máy biến áp ($\\Delta P\_{B} = \\Delta P\_{Fe} + \\beta^2 \\Delta P\_{Cu}$).
     * Tính hệ số tổn thất $K\_{tt}$ dựa trên hệ số phụ tải $K\_{pt}$ theo công thức thực nghiệm $K\_{tt} = a \\cdot K\_{pt} + (1-a) \\cdot K\_{pt}^2$ (với $a = 0,2 \\div 0,3$).
     * Tính thời gian tổn thất công suất cực đại $\\tau = K\_{tt} \\cdot T$ (với $T = 8760\\text{ giờ}$) và tổn thất điện năng hàng năm $\\Delta A = \\Delta P\_{max} \\cdot \\tau$.
     * Xác định suất tổn thất điện năng $\\Delta A% = \\frac{\\Delta A}{A\_{truyền tải}} \\cdot 100%$.
  4. **Mô-đun Tối ưu hóa Bù Công suất Phản kháng (`reactive\_opt.py`)**:

     * Xây dựng hàm mục tiêu Lagrange $L = \\Delta P - \\lambda (\\sum Q\_{bù,i} - Q\_{bù,\\Sigma})$ nhằm phân bổ tổng dung lượng bù $Q\_{bù,\\Sigma}$ đến các nút tải sao cho tổng tổn thất công suất tác dụng $\\Delta P$ đạt cực tiểu.
     * Giải hệ phương trình đạo hàm riêng $\\frac{\\partial L}{\\partial Q\_{bù,i}} = 0$ kết hợp ma trận điện trở thanh cái $R\_{bus}$.
     * Triển khai vòng lặp kiểm tra và xử lý nghiệm âm: Nếu xuất hiện $Q\_{bù,k} < 0$, gán $Q\_{bù,k} = 0$ (nút $k$ không cần bù) và tái giải hệ phương trình $(n-1)$ ẩn còn lại.
  5. **Mô-đun Trực quan hóa \& Xuất Báo cáo (`visualizer.py` \& `main\_app.py`)**:

     * Mô phỏng trắc đồ điện áp dọc theo chiều dài phát tuyến (`vprofile`) ở các chế độ: không tải, tải định mức, tải SIL và ngắn mạch.
     * Xuất các chỉ tiêu kinh tế - kỹ thuật ra bảng biểu giao diện Web Streamlit.
* **Luồng xử lý dữ liệu (Workflow / Algorithm)**:

  1. **Bước 1**: Nhập tập tin dữ liệu cấu hình mạng điện (`busdata.csv`, `linedata.csv`, `gendata.csv`) $\\rightarrow$ Kiểm tra tính hợp lệ dữ liệu.
  2. **Bước 2**: Chuyển đổi tham số sang hệ p.u. $\\rightarrow$ Gọi hàm thành lập ma trận $Y\_{bus}$ và $Z\_{bus}$.
  3. **Bước 3**: Chạy mô-đun Phân bố công suất $\\rightarrow$ Xác định phân bố điện áp nút $|U\_k| \\angle \\delta\_k$ và dòng điện nhánh $I\_{ij}$.
  4. **Bước 4**: Tính tổn thất công suất đỉnh $\\Delta P\_{max}$, hệ số tổn thất $K\_{tt}$, thời gian tổn thất $\\tau$, và điện năng tổn thất $\\Delta A$.
  5. **Bước 5**: (Tùy chọn tối ưu) Nhập tổng dung lượng cần bù $Q\_{bù,\\Sigma} \\rightarrow$ Thực hiện thuật toán lặp Lagrange tìm phân bố $Q\_{bù,i}$ tối ưu $\\rightarrow$ Cập nhật lại chế độ điện áp và tính lượng tổn thất đã giảm.
  6. **Bước 6**: Xuất dữ liệu biểu đồ trắc đồ điện áp $V(x)$ và danh sách các thông số nghiệm thu lên giao diện Streamlit.

## 4\. KỊCH BẢN KIỂM THỬ \& NGHIỆM THU (VERIFICATION \& TEST CASES)

* **Test Case 1: Kiểm thử Mô-đun Thành lập Ma trận $Y\_{bus}$ và $Z\_{bus}$**

  * **Mục tiêu**: Xác nhận thuật toán dựng ma trận $Y\_{bus}$ và $Z\_{bus}$ hoạt động chính xác với cấu hình hệ thống điện mẫu.
  * **Đầu vào (Input)**: File `linedata` chứa hệ thống 4 nút với các điện kháng nhánh $j0,2; j0,4; j0,8; j0,4$ p.u..
  * **Các bước thực hiện**:

    1. Tải dữ liệu từ file `linedata.csv`.
    2. Thực hiện gọi hàm `ybus()` để lập ma trận tổng dẫn thanh cái.
    3. Thực hiện gọi hàm `zbuild()` để lập ma trận tổng trở thanh cái $Z\_{bus}$ với nút trung tính làm chuẩn.
  * **Kết quả mong đợi (Expected Output)**: Ma trận $Y\_{bus}$ đối xứng; Ma trận $Z\_{bus}$ thu được khớp với bảng kết quả lý thuyết (ví dụ các phần tử đường chéo $Z\_{11} = j0,240$; $Z\_{22} = j0,2275$; $Z\_{33} = j0,310$ p.u.).
* **Test Case 2: Kiểm thử Phân bố Công suất \& Sụt áp trên Mạng phân phối hình tia**

  * **Mục tiêu**: Kiểm tra tính đúng đắn của thuật toán tính sụt áp và phân bố dòng điện trên mạng mở hình tia.
  * **Đầu vào (Input)**: Mạng điện $35\\text{ kV}$ gồm 3 đoạn đường dây $A-b$ ($8\\text{ km}$), $b-c$ ($5\\text{ km}$), $c-d$ ($3\\text{ km}$) cung cấp cho các phụ tải $S\_b = 4000 + j3000\\text{ kVA}$, $S\_c = 3000 + j2000\\text{ kVA}$, $S\_d = 2000 + j2000\\text{ kVA}$.
  * **Các bước thực hiện**:

    1. Tính tổng công suất chảy trên từng phân đoạn đường dây.
    2. Áp dụng thuật toán tính sụt áp thành phần $U\_{Ad}%$.
    3. So sánh tổn thất điện áp tính toán được.
  * **Kết quả mong đợi (Expected Output)**: Độ sụt áp cực đại tại nút cuối $d$ đạt $U\_{Ad}% = 6,16%$ (khớp chính xác với lý thuyết) và độ lệch điện áp nằm trong giới hạn cho phép $\\pm 5%$.
* **Test Case 3: Kiểm thử Tối ưu hóa Bù Công suất Phản kháng bằng Lagrange**

  * **Mục tiêu**: Xác nhận thuật toán phân bố dung lượng bù $Q\_{bù}$ tối ưu giảm tối đa tổn thất công suất tác dụng và xử lý đúng nghiệm âm.
  * **Đầu vào (Input)**: Sơ đồ mạng điện phân phối 4 nút tải, ma trận điện trở $R\_{bus}$, tổng dung lượng bù cưỡng bức yêu cầu $Q\_{bù,\\Sigma} = 24,88\\text{ MVAR}$.
  * **Các bước thực hiện**:

    1. Thành lập hệ phương trình đạo hàm Lagrange.
    2. Giải hệ phương trình tuyến tính tìm các giá trị $Q\_{bù,i}$ ban đầu.
    3. Kiểm tra điều kiện nghiệm âm và vòng lặp tự động khử nút không cần bù.
  * **Kết quả mong đợi (Expected Output)**: Thuật toán hội tụ, tổng $\\sum Q\_{bù,i} = 24,88\\text{ MVAR}$, tất cả các dung lượng bù $Q\_{bù,i} \\ge 0$, và tổn thất công suất tác dụng $\\Delta P$ đạt giá trị nhỏ nhất.
* **Test Case 4: Kiểm thử Tính toán Tổn thất Điện năng $\\Delta A$ theo Thời gian Tổn thất $\\tau$**

  * **Mục tiêu**: Kiểm tra tính toán điện năng tổn thất hàng năm từ phụ tải cực đại và đồ thị phụ tải.
  * **Đầu vào (Input)**: Phụ tải cực đại $\\Delta P\_{max} = 150\\text{ kW}$, hệ số phụ tải $K\_{pt} = 0,6$, thời gian khảo sát $T = 8760\\text{ giờ}$.
  * **Các bước thực hiện**:

    1. Tính $K\_{tt} = 0,3 \\cdot K\_{pt} + 0,7 \\cdot K\_{pt}^2 = 0,3 \\cdot 0,6 + 0,7 \\cdot 0,36 = 0,432$.
    2. Tính $\\tau = K\_{tt} \\cdot T = 0,432 \\cdot 8760 = 3784,32\\text{ giờ}$.
    3. Tính tổn thất điện năng $\\Delta A = \\tau \\cdot \\Delta P\_{max}$.
  * **Kết quả mong đợi (Expected Output)**: Điện năng tổn thất $\\Delta A = 567.648\\text{ kWh}$, hàm tính toán phản ánh đúng công thức lý thuyết và không bị sai số làm tròn.

