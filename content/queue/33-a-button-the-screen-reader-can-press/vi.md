---
title: Nút mà trình đọc màn hình có thể kích hoạt
description: Biểu tượng đóng và ngọn hải đăng trong Inkisle có nhãn để đọc, nhưng thiếu thao tác trợ năng. Chúng tôi kiểm tra cả lời đọc lẫn kết quả khi kích hoạt nút.
slug: a-button-the-screen-reader-can-press
lang: vi
translation_of: en
category: making-of
keywords: Inkisle, trợ năng, trình đọc màn hình, giao diện, kiểm thử widget
image_alt: Hai tấm thẻ nhỏ có dấu X và biểu tượng hải đăng, mỗi nút được viền đánh dấu tiêu điểm.
---

Inkisle là trò chơi chiến thuật chiếm đảo đang được phát triển. Khi rà soát trợ năng, chúng tôi xem trò chơi mô tả các nút như thế nào cho trình đọc màn hình. Hai nút đáng chú ý là dấu X để đóng bảng và ngọn hải đăng trên hải đồ để phát lại đoạn kết. Chúng tôi đang phát triển trò chơi cho iOS.

## Từ tên đến thao tác

Hai nút đã có tên. Tuy nhiên, khi chúng tôi thay mô tả mặc định của biểu tượng, nút trong cây trợ năng của Flutter mất thao tác chạm ở chính phần tử chứa tên. Chúng tôi gắn thao tác vào cùng phần tử có nhãn. Trong kiểm thử, kích hoạt Đóng sẽ đóng bảng và kích hoạt hải đăng sẽ mở đoạn kết.

## Nghe một lần là đủ

Chúng tôi cũng kiểm tra thông tin nào được đọc hai lần. Nút chọn tỷ lệ hạm đội đưa cùng một tỷ lệ phần trăm vào nhãn và chữ trên màn hình. Nút bỏ qua đoạn mở đầu và các dấu mốc có số trên hải đồ cũng bị lặp tương tự. Mỗi nút giữ lại một nhãn đọc, chứa thông tin người chơi cần để nhận biết nút đó.

## Câu hỏi thường gặp (FAQ)

### Đã kiểm thử bằng trình đọc màn hình trên điện thoại chưa?

Các bài kiểm thử widget đã kiểm tra nhãn và thao tác trợ năng. Chúng tôi chưa xác minh những thay đổi trên điện thoại bằng VoiceOver hoặc TalkBack.

### Ngọn hải đăng trên hải đồ dùng để làm gì?

Kích hoạt ngọn hải đăng để phát lại đoạn kết.
