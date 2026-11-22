---
title: Một cái kết chỉ phát một lần, và ngọn hải đăng để xem lại
description: Cái kết mùa 1 của Inkisle tự phát đúng một lần, vào lần đầu qua màn cuối của hồi 30. Chúng tôi đặt quy tắc xem lại ra sao, người chơi đã qua màn và cái kết hồi 10 được xử lý thế nào, và những gì chúng tôi chưa kiểm tra ở bản dịch cũng như trên thiết bị thật.
slug: an-ending-that-plays-once
lang: vi
translation_of: en
category: making-of
keywords: Inkisle, mùa 1, cái kết, kết mở, hải đăng, thiết kế game, game di động
image_alt: Một hòn đảo đơn độc trên mặt biển lặng với một ngọn hải đăng đang sáng, và tuyến đường trên hải đồ dừng lại trước nó.
published: 2026-11-22T16:00+09:00
---

Cái kết mùa 1 của Inkisle, game chiến thuật chinh phục đảo của chúng tôi trên iOS, tự phát một lần, vào lần đầu qua màn 8 của hồi 30. Để xem lại, người chơi chạm vào ngọn hải đăng ở đầu hồi 30. Cái kết không có lời khép lại; dấu duy nhất là "Inkisle · Season 1". Bài viết này nói ít về những gì cái kết hiện ra, mà nhiều hơn về lúc nào nó phát và lúc nào không, và cách chúng tôi chốt các quy tắc đó. Game đang trong quá trình phát triển và chưa phát hành.

## Bốn quy tắc

Đây là các quy tắc xem lại chúng tôi đặt ra khi đưa cái kết vào.

- **Một lần, ở lần qua màn đầu tiên.** Nó tự phát ngay lúc thắng màn 8 của hồi 30 lần đầu.
- **Không bao giờ tự phát nữa.** Thắng lại cùng màn đó, hay khởi động lại ứng dụng, không tự động phát nó.
- **Bỏ qua được bất cứ lúc nào.** Một lần chạm đưa tới khung hình tĩnh cuối cùng, và thiết bị bật giảm chuyển động sẽ bắt đầu ở khung hình tĩnh.
- **Xem lại là ngọn hải đăng.** Một ngọn hải đăng nằm ở đầu hồi 30, và chạm vào nó sẽ phát lại đúng cái kết đó.

Dù cái kết ngắn hơn 30 giây, chúng tôi quyết định rằng "một lần, ngay sau khi thắng" là một món quà còn "mỗi lần thắng" là sự làm phiền.

## "Đã xem" được ghi ở đâu

Việc nó đã phát hay chưa được lưu thành một khóa cốt truyện trong dữ liệu lưu. Khóa của cái kết mùa được **cố ý tách riêng** khỏi khóa của cái kết hồi 10. Nếu cả hai dùng chung một khóa, người chơi đã xem cái kết hồi 10 có thể bị tính là đã xem cái kết mùa. Có một bài kiểm thử kiểm tra điều này: xem cái kết hồi 10 không chạm vào khóa của mùa.

## Người chơi đã qua màn

Có người có thể đã qua màn 8 của hồi 30 trước khi cái kết tồn tại. Với bản lưu đó, thời điểm qua màn lần đầu đã trôi qua, nên không có gì tự phát và chỉ ngọn hải đăng xuất hiện. Chúng tôi chọn không ép một khoảnh khắc đã qua, và để người chơi bấm khi họ muốn.

Trong cùng thay đổi này, ngọn hải đăng của hồi 10 được chuyển lên đầu hồi 10, nơi nó thuộc về.

## Các bài kiểm thử chốt điều gì

Cái kết có 18 bài kiểm thử. Những bài gắn với các quy tắc này:

- Nó phát đúng một lần ở chiến thắng đầu tiên của màn 8 hồi 30, và không phát khi người chơi vào lại.
- Không có gì phát ở màn 7 hồi 30 hay màn 8 hồi 29.
- Bản lưu đã qua màn 8 hồi 30 không nhận phát tự động, chỉ có ngọn hải đăng.
- Ở 375px và 320px trong kiểm thử widget, phát, bỏ qua và thoát giữa chừng đều hoạt động.
- Văn bản của cả 12 ngôn ngữ vừa khít không bị tràn.

## Không có lời khép lại

Dòng cuối, bằng tiếng Hàn, là "Nước sâu in bóng." (「깊은 물이 비친다.」). Không phiên bản ngôn ngữ nào mang một từ như "Hết", và dấu ở phía dưới là "Inkisle · Season 1". Các quy tắc xem lại xuất phát từ cùng một ý nghĩ: câu chuyện khép lại, nhưng ứng dụng thì không. Sau hồi 30, người chơi vẫn có thể chơi lại các hồi, thu thập ba sao và xem các bảng điểm.

## Những gì chúng tôi chưa kiểm tra

- **Văn bản cái kết ở 10 ngôn ngữ khác tiếng Hàn và tiếng Anh được dịch bằng máy và chưa được rà soát.** Khi chỉ có vài dòng trên màn hình, chất lượng bản dịch lộ ra ngay.
- Hiệu ứng mờ dần chậm, chữ vàng và âm lượng tiếng chuông chưa được xem trên thiết bị thật.
- Giao diện ở 375px và 320px chỉ được kiểm tra trong kiểm thử widget, mà phông chữ thử nghiệm rộng hơn nhiều so với phông thật.
- Có mùa 2 hay không chưa được quyết định, và chưa có ngày phát hành.

## FAQ

### Cái kết tự phát bao nhiêu lần?

Một lần, vào lần đầu qua màn 8 của hồi 30. Sau đó người chơi chạm vào ngọn hải đăng ở đầu hồi 30 để xem lại.

### Có thể bỏ qua cái kết không?

Có. Một lần chạm nhảy tới khung hình tĩnh cuối cùng, và khi bật giảm chuyển động thì nó bắt đầu ở khung hình tĩnh.

### Văn bản cái kết đã được rà soát ở mọi ngôn ngữ chưa?

Chưa. Các bản dịch khác tiếng Hàn và tiếng Anh được dịch bằng máy và chưa được rà soát.
