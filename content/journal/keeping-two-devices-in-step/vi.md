---
title: Giữ hai thiết bị đồng bộ: chuyển đồng bộ iCloud vào bộ ứng dụng dùng chung
description: Tiến trình, mực và cài đặt của Inkisle vốn đã được khớp giữa các thiết bị qua iCloud. Ngày 16 tháng 11, chúng tôi chuyển cây cầu đó vào một bộ ứng dụng dùng chung. Cách chúng tôi giữ nguyên dữ liệu đã lưu, các quy tắc hợp nhất không bao giờ thu nhỏ, cách xử lý dấu hiệu mua hàng, và những gì chúng tôi chưa kiểm tra trên thiết bị thật.
slug: keeping-two-devices-in-step
lang: vi
translation_of: en
category: making-of
keywords: Inkisle, iCloud, đồng bộ giữa các thiết bị, dữ liệu lưu, hợp nhất, game di động
image_alt: Hai màn hình khác kích thước được nối bằng một sợi chỉ mảnh, các hòn đảo trên cả hai bản đồ được tô cùng màu.
published: 2026-11-23T13:45+09:00
---

Trong Inkisle, game chiến lược chinh phục đảo của chúng tôi trên iOS, tiến trình, mực và các cài đặt chính (ngôn ngữ và biệt danh) được khớp giữa các thiết bị cùng Apple ID thông qua kho khóa-giá trị iCloud của chính người chơi. Việc đồng bộ này đã có sẵn. Điều chúng tôi làm vào ngày 16 tháng 11 không phải là xây dựng nó, mà là chuyển một cây cầu do chính chúng tôi viết vào bộ ứng dụng dùng chung, và nỗi lo lớn nhất là không làm mất dù chỉ một giá trị đã lưu. Chúng tôi chưa kiểm tra vòng đi-về giữa một iPhone và một iPad thật. Trò chơi đang được phát triển và chưa phát hành.

## Những gì chúng tôi đã chuyển

Chỉ thị của người phụ trách hôm đó là việc đồng bộ dữ liệu game giữa các thiết bị Apple phải là bắt buộc và phải nằm trong bộ ứng dụng dùng chung. Chúng tôi thấy quyền khóa-giá trị iCloud đã được bật sẵn, cùng một cầu nối Swift và một lớp bọc lưu trữ của riêng mình đang chạy trong ứng dụng. Vì vậy:

| Phần | Điều đã thay đổi |
|---|---|
| Cầu nối | Xóa cầu nối Swift và lớp bọc của riêng mình, rồi chuyển sang kho lưu trữ nền tảng của bộ ứng dụng: iCloud trên iOS, chỉ cục bộ ở nơi khác |
| Khóa và mã hóa | Giữ nguyên các khóa lưu trữ, cách mã hóa chuỗi và định danh lưu trữ |
| Trước khi đọc | Trên iOS, đánh thức đồng bộ một lần ngay trước khi đọc (đồng bộ vẫn tiếp tục nếu bước này thất bại) |
| Cài đặt dự án | Thêm cả khả năng iCloud vào tệp dự án |

## Không làm mất dữ liệu

Vì khóa và định dạng được giữ nguyên, bản dựng mới đọc được những gì bản dựng cũ ghi, và bản dựng cũ đọc được những gì bản dựng mới ghi. Chúng tôi chốt cả hai chiều bằng kiểm thử: đọc một khối định dạng cũ bằng mã mới, đọc một khối mới bằng mã cũ và đọc một khối cài đặt cũ. Chỉ có mã bị xóa; các giá trị đã lưu không bị đụng đến.

## Hợp nhất không bao giờ thu nhỏ

Khi hai thiết bị có tiến trình khác nhau, chúng tôi giữ cách hợp nhất riêng của ứng dụng. Bộ ứng dụng cũng có một bộ hợp nhất, nhưng chúng tôi không dùng. Cách hợp nhất của ứng dụng vốn chỉ tăng, và giữ nguyên khóa và định dạng sẽ an toàn hơn khi để nó như cũ.

- Số sao và kỷ lục tốt nhất của mỗi màn lấy giá trị lớn hơn.
- Tiến trình lấy thiết bị đã đi xa hơn, còn mực và cài đặt chỉ được gộp lại, không bao giờ thu nhỏ.
- Nếu giá trị trên đám mây khác với lần gần nhất chúng tôi đẩy lên, chúng tôi đẩy lại, để phục hồi sau một bản dựng cũ đã ghi đè cùng khóa.

## Chuyện gì đã xảy ra với dấu hiệu mua hàng

Một bài trước nói rằng việc mở khóa không chuyển sang thiết bị khác. Công việc này đã thay đổi điều đó. Khối đồng bộ giờ mang theo một dấu hiệu cho biết Mở khóa tất cả biển đã được mua, và thiết bị khác đọc được dấu hiệu này cũng sẽ mở. Dấu hiệu **chỉ tăng.** Một khối không có nó sẽ không gỡ nó đi; chúng tôi đẩy lại.

Đây là thay đổi thiết kế theo chỉ thị "đồng bộ bắt buộc" của người phụ trách, và nó có một giới hạn: một khi dấu hiệu đã đồng bộ, việc hoàn tiền không gỡ nó trên các thiết bị khác. Cách xử lý hoàn tiền được để lại như một quyết định về chính sách. Bản thân luồng mua hàng cũng chưa được chạy trên thiết bị thật.

## Dung lượng và kiểm thử

Kho khóa-giá trị iCloud có giới hạn tổng (1 MB). Khối đồng bộ của một bản lưu đã hoàn thành cả 240 màn chơi nặng khoảng 6,3 KB, và một bài kiểm thử giữ nó dưới 16 KB. 14 kiểm thử mới bao gồm khóa và mã hóa không đổi, việc hợp nhất hai thiết bị, dấu hiệu mua hàng lan ra và không bao giờ bị gỡ, việc ở lại cục bộ khi ngoại tuyến hoặc chưa đăng nhập, và việc hợp nhất sau khi trực tuyến trở lại. Trên bốn tệp kiểm thử đám mây, 77 kiểm thử đã đạt.

## Những gì chúng tôi chưa kiểm tra

- **Việc đồng bộ thật giữa iPhone và iPad chưa được kiểm tra.** Chỉ có thể thấy điều này trên thiết bị thật hoặc TestFlight.
- Việc xóa không lan sang các thiết bị khác, vì đồng bộ này chỉ hợp nhất.
- Android không áp dụng. Dữ liệu ở lại trên thiết bị.
- Nếu một bản dựng cũ trên thiết bị khác ghi đè cùng khóa, dấu hiệu mua hàng có thể biến mất trong chốc lát, và bản dựng mới sẽ đẩy lại nó.
- Chính sách quyền riêng tư giờ đã mô tả việc đồng bộ này: dữ liệu game được giữ trong iCloud của chính người chơi, không phải trên máy chủ của chúng tôi, và có thể tắt trong cài đặt thiết bị.

## FAQ

### Tiến trình Inkisle có được lưu trên máy chủ không?

Không. Nó được khớp giữa các thiết bị cùng Apple ID thông qua kho khóa-giá trị iCloud của chính người chơi, và không được gửi đến máy chủ của chúng tôi.

### Có thể tắt đồng bộ không?

Có. Tắt iCloud của ứng dụng này trong cài đặt iOS sẽ dừng đồng bộ và để dữ liệu chỉ nằm trên thiết bị.

### Có đồng bộ trên Android không?

Không. Trên Android, dữ liệu ở lại trên thiết bị.
