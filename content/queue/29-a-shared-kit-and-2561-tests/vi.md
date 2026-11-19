---
title: Chúng tôi bảo vệ điều gì khi nâng cấp bộ công cụ dùng chung: cổng kiểm tra 2.561 bài kiểm thử
description: Mỗi lần Inkisle nâng cấp bộ công cụ dùng chung mà các ứng dụng của chúng tôi sử dụng, nó phải qua một cổng kiểm tra gồm định dạng, phân tích và toàn bộ kiểm thử. Vì sao chúng tôi không thay cả một tính năng của bộ công cụ, các bài kiểm thử về thời gian chao đảo ra sao khi tải nặng, những tệp nào đã thay đổi trong lần nâng cấp gần nhất và những gì chúng tôi chưa kiểm tra.
slug: a-shared-kit-and-2561-tests
lang: vi
translation_of: en
category: making-of
keywords: Inkisle, bộ công cụ dùng chung, kiểm thử, Game Center, nâng cấp, game di động
image_alt: Vài khối nhỏ cùng hình dạng nằm trong một khung, với một chấm xanh lá duy nhất lướt qua phía trên chúng.
---

Inkisle, game chiến lược chinh phục đảo của chúng tôi trên iOS, dùng một bộ công cụ dùng chung mà nhiều ứng dụng của chúng tôi dựa vào. Mỗi lần chúng tôi nâng phiên bản của bộ công cụ, một cổng kiểm tra chạy định dạng, phân tích tĩnh và toàn bộ bộ kiểm thử trước khi commit. Ngày 19 tháng 11, chúng tôi chuyển bộ công cụ từ 0.15.2 lên 0.15.3: cổng kiểm tra đã qua 2.561 bài kiểm thử (bỏ qua 8), và chỉ hai tệp thay đổi, `pubspec.yaml` và `pubspec.lock`. Bài viết này nói về cách con số đó được giữ vững và điều gì đã chao đảo trên đường đi. Trò chơi đang trong quá trình phát triển và chưa phát hành.

## Cổng kiểm tra có ba bước

Một tập lệnh chạy chúng theo thứ tự trước khi commit: định dạng mã không được thay đổi, phân tích tĩnh phải báo 0 vấn đề, và mọi bài kiểm thử phải qua. Nếu bước nào thất bại, chúng tôi không commit. Khi người khác nói "đã qua", chúng tôi tự chạy lại trước khi commit.

## Ngày 14 tháng 11: chúng tôi không thay cả tính năng của bộ công cụ

Việc chuyển bộ công cụ từ 0.12.0 lên 0.13.0 cho phép nó xử lý biệt danh và bảng xếp hạng Game Center. Chỉ thị của người phụ trách là mọi trò chơi phải cho người chơi đặt biệt danh ở lần mở đầu tiên và xuất hiện trên bảng xếp hạng Game Center. Chúng tôi **không thay bằng toàn bộ tính năng người chơi của bộ công cụ.** Chúng tôi có bốn lý do để nghĩ phiên bản của mình tốt hơn:

1. Biệt danh nằm trong bản ghi cài đặt, vốn đồng bộ giữa các thiết bị qua iCloud. Chuyển nó sang kho lưu trữ của bộ công cụ sẽ làm hỏng việc đồng bộ đó.
2. Chúng tôi đã có bảng biệt danh bằng 16 ngôn ngữ và các bài kiểm thử được cố định cho các tổ hợp ngôn ngữ và kích thước màn hình.
3. Các bảng xếp hạng là 24 bảng động, với giá trị suy ra từ bản ghi tiến trình đã đồng bộ. Chuyển chúng sẽ để lại hai nơi lưu điểm cao nhất.
4. Play Games trên Android vẫn cần thư viện mà nó đang dùng.

Vì vậy chỉ kết nối Game Center trên iOS được chuyển sang bộ công cụ, còn ID bảng, biệt danh đã lưu và điểm cao nhất được giữ nguyên. Việc gửi lại phần tồn đọng sau khi đăng nhập muộn và việc điền sẵn biệt danh bằng tên Game Center được đưa vào cùng lúc. Chúng tôi thêm 10 bài kiểm thử, và cổng kiểm tra sau đó qua 1.990 bài (bỏ qua 7).

## Các bài kiểm thử về thời gian chao đảo

Hai lần trong cổng kiểm tra này, một bài kiểm thử đo thời gian đã chao đảo khi tải nặng. Một bài kiểm thử ngân sách khung hình vẽ 800 con đường đã thất bại một lần khi các bài kiểm thử chạy song song, và trong lúc làm việc với iCloud, một bài kiểm thử ngân sách hiệu năng đã thất bại một lần. Cả hai đều qua khi chạy riêng hoặc khi chạy lại toàn bộ bộ kiểm thử. Chúng tôi coi đó là do tải, không phải do thay đổi của mình **[chưa xác minh; chúng tôi chưa truy ra nguyên nhân]**. Chúng tôi không nới lỏng các ngân sách.

## Ngày 19 tháng 11: hai tệp thay đổi

Phiên bản 0.15.3 giữ nguyên API công khai; nó làm cho việc đếm lại trong đồng bộ iCloud dừng sau khi gỡ bỏ và bổ sung tài liệu. Chúng tôi không đổi mã hay bài kiểm thử nào trong ứng dụng. Giới hạn kích thước mà ứng dụng dùng (512 KB) là chủ ý, nên chúng tôi giữ nguyên. Các tệp thay đổi là `pubspec.yaml` và `pubspec.lock`, và cổng kiểm tra qua ngay lần chạy đầu tiên, lần này không có chao đảo về thời gian. Số bài kiểm thử tăng từ 1.990 vào ngày 14 tháng 11 lên 2.561.

## Những điều chúng tôi chưa kiểm tra

- **Đăng nhập Game Center, gửi điểm, màn hình bảng xếp hạng và một vòng đi về của iCloud chưa được kiểm tra trên thiết bị thật [chưa xác minh].** Chúng tôi sẽ xem trong TestFlight.
- Giao diện ở 375px và 320px được bao phủ bởi kiểm thử widget ở 320×568 thay vì được xem trực tiếp **[chưa xác minh]**.
- Chúng tôi chưa tìm ra nguyên nhân gốc của các bài kiểm thử chao đảo khi tải nặng **[chưa xác minh]**.
- Các con số ở đây là kết quả cổng kiểm tra của ngày hôm đó, và số bài kiểm thử sẽ thay đổi về sau.

## Câu hỏi thường gặp

### Bộ công cụ dùng chung là gì?

Một gói mã mà nhiều ứng dụng của chúng tôi cùng sử dụng. Inkisle dùng các phần biệt danh, Game Center và đồng bộ iCloud của nó.

### Khi nâng cấp bộ công cụ, các bạn kiểm tra gì?

Một tập lệnh kiểm tra rằng định dạng không thay đổi, phân tích tĩnh báo 0 vấn đề và mọi bài kiểm thử đều qua. Nếu bước nào thất bại, chúng tôi không commit.

### Trò chơi đã phát hành chưa?

Chưa. Trò chơi vẫn đang trong quá trình phát triển và chưa phát hành.
