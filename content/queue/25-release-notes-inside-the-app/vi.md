---
title: Ghi chú phát hành trong ứng dụng: một bảng 12 ngôn ngữ và kiểm tra độ dài
description: Ghi chú phát hành của Inkisle là một bảng nằm trong Cài đặt, không phải trang web. Cách viết ghi chú của từng bản dựng bằng 12 ngôn ngữ, các kiểm tra số lượng và độ dài mục, và lỗi kiểm thử từng hiển thị một bảng trống.
slug: release-notes-inside-the-app
lang: vi
translation_of: en
category: making-of
keywords: Inkisle, ghi chú phát hành, bản địa hóa, đa ngôn ngữ, kiểm thử, game di động
image_alt: Một tờ giấy trồi lên từ đáy màn hình, phía trên là mười hai thẻ ngôn ngữ nhỏ xếp thành hàng.
---

Ghi chú phát hành của Inkisle, game chiến lược chinh phục đảo của chúng tôi trên iOS, là một bảng trong ứng dụng, mở từ Cài đặt, không phải trang web. Ghi chú của mỗi bản dựng được viết bằng 12 ngôn ngữ, và một script kiểm tra xác nhận số lượng mục và độ dài. Kiểm tra cho bản dựng 34 báo 0 lỗi và 0 cảnh báo. Trò chơi vẫn đang phát triển và chưa phát hành.

## Chúng tôi đã bỏ trang web

Ban đầu màn hình chính có liên kết "Ghi chú phát hành" và nút thông tin (ⓘ). Ở bản dựng 32, chúng tôi bỏ cả hai. Nội dung của cửa sổ thông tin (chính sách bảo mật, điều khoản, phiên bản, giấy phép mã nguồn mở, đơn vị vận hành, liên hệ và thông báo 16+) đã chuyển vào Cài đặt, còn ghi chú phát hành trở thành một bảng mở từ dòng "Ghi chú phát hành" ở đó. Trang ghi chú phát hành trên website cũng đã được gỡ vào ngày 15 tháng 11. Không có trang web riêng, văn bản trong ứng dụng là nguồn duy nhất.

Bảng này dùng cùng khung với các cửa sổ bật lên khác của chúng tôi (InkSheet). Chiều cao tối đa là 60% màn hình, dòng tiêu đề và dấu X đóng (48×48) được giữ cố định, và chỉ phần nội dung bên trong bảng được cuộn.

## Một bản dựng, một tệp, 12 ngôn ngữ

Với mỗi bản dựng, `release_notes/<build>.json` chứa tiêu đề, phần giới thiệu và các mục bằng 12 ngôn ngữ (ko, en, ja, zh-Hant, es, pt-BR, fr, de, id, th, vi, tr). Các tệp này được gộp vào `assets/release_notes.json`, đi kèm ứng dụng, và bảng đọc từ đó.

## Kiểm tra độ dài và số lượng

Một script kiểm tra đọc các tệp và báo cáo các vi phạm quy tắc.

- **RN06:** một mục phải có tối đa 200 ký tự. Văn bản tiếng Đức quá dài, nên mục kết thúc mùa ở bản dựng 34 đã được rút gọn còn 183 ký tự. Ở bản dựng 31, chúng tôi tách một mục mua thành hai để nằm trong giới hạn.
- **RN05:** nên có 3 đến 6 mục. Đây chỉ là cảnh báo và không chặn việc phát hành. Các cảnh báo còn lại nằm ở các bản dựng cũ chỉ có 1 hoặc 2 mục; chúng là ghi chép trung thực về những gì đã được viết, nên chúng tôi giữ nguyên.
- Một bài kiểm thử sẽ thất bại nếu không có mục cho phiên bản và số bản dựng hiện tại, vì vậy mỗi lần tăng số bản dựng đều phải viết ghi chú 12 ngôn ngữ trước.
- Script tải lên iOS chạy kiểm tra ghi chú phát hành trước cổng xanh (định dạng, phân tích, kiểm thử).

## Bài kiểm thử thấy một bảng trống

Hai bài kiểm thử của bảng ghi chú phát hành bắt đầu thấy bảng trống. Nguyên nhân nằm ở bài kiểm thử, không phải ứng dụng. Gói là một tệp tài nguyên thật, và khi tệp lớn dần, `pumpAndSettle`, hàm chờ màn hình ổn định, kết thúc trước khi việc đọc tệp hoàn tất. Chúng tôi sửa các bài kiểm thử để mở bảng, chờ 300 ms bằng `runAsync` rồi vẽ lại. Mã của ứng dụng không thay đổi.

## Những điều chúng tôi chưa kiểm tra

- Bản dịch ngoài tiếng Hàn và tiếng Anh được dịch bằng máy và chưa được người bản ngữ xem lại [chưa xác minh].
- Chúng tôi chưa thấy bảng mở ở 60% trên thiết bị thật. Các kiểm thử widget ở 375×667 và 320×568 thay thế cho việc đó [chưa xác minh].

## Câu hỏi thường gặp

### Tôi tìm ghi chú phát hành của Inkisle ở đâu?

Trong ứng dụng, chạm vào dòng "Ghi chú phát hành" ở Cài đặt, một bảng sẽ mở ra. Không có trang web riêng. Trò chơi chưa phát hành.

### Các ghi chú được viết bằng bao nhiêu ngôn ngữ?

12 ngôn ngữ. Ngoài tiếng Hàn và tiếng Anh, phần còn lại được dịch bằng máy và chưa được xem lại.

### Điều gì xảy ra nếu một mục quá dài?

Nếu một mục vượt quá 200 ký tự, script kiểm tra sẽ báo lỗi, và chúng tôi rút gọn hoặc tách nó thành hai mục.
