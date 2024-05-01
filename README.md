link overleaf bài báo cáo của em https://www.overleaf.com/read/ffvjgzykdybr#8de761
# Download video trên Youtube
## Giới thiệu
phần mềm giúp người dùng dễ dàng tải xuống video từ YouTube. một phương pháp đơn giản để download video Youtube bằng Python. 
Có thể tải nhiều video trong một lần thao tác. Mặc dù library không vi phạm bản quyền, tuy nhiên chúng ta cũng cần có trách nhiệm với các video download từ Youtube.
## Cài đặt

### Điều kiện tiên quyết

Trước khi cài đặt ứng dụng, hãy đảm bảo bạn đã cài đặt các phần phụ thuộc sau bằng cách sử dụng ```pip install <package_name>``` :

- **tkinter**: để cài đặt thư viện tkinter giao diện đồ họa.
- **pytube**: để cài đặt thư viện pytube tải video.
### Chạy máy chủ

Để chạy máy chủ, hãy làm theo các bước sau:

1. Sao chép kho lưu trữ:

    ``` bash
    git clone https://github.com/BinhMinh0101/ApdownYt.git
    cd <repository_directory>
    ```

2. Cài đặt phụ thuộc:

    ``` bash
    cài đặt pip -r require.txt
    ```

3. Khởi động máy chủ:
    ``` bash
    python DownVideoo.py runserver
    ```
    hoặc
    ``` bash
    python3 DownVideoo.py runserver
    ```
Máy chủ bây giờ sẽ chạy cục bộ trên máy của bạn.

## Cách sử dụng

Khám phá một số chức năng cơ bản như:
- Nhấn nút Add URL để tự động hiện ra ô URL có nút delete xóa nếu muốn.
- Chấp nhận đầu vào URL video YouTube thông qua trường nhập.
- Cho phép người dùng chỉ định vị trí tải xuống (tùy chọn).
- Kích hoạt tải xuống video khi nhấp vào nút "Download All".
