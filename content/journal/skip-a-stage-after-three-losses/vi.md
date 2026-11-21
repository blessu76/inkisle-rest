---
title: Bỏ qua màn sau ba lần thua: một lời đề nghị nhẹ nhàng có cái giá
description: Trong Inkisle, thua cùng một màn ba lần sẽ có lời đề nghị bỏ qua màn đó với giá 3 Ink. Khi nào lời đề nghị xuất hiện, những màn nào được loại trừ, màn bị bỏ qua hiện thế nào trên hải đồ và được lưu ra sao.
slug: skip-a-stage-after-three-losses
lang: vi
translation_of: en
category: making-of
keywords: Inkisle, bỏ qua màn, độ khó, thiết kế game, dữ liệu lưu, game di động
image_alt: Một tấm hải đồ có một hòn đảo được đánh dấu bằng lá cờ san hô nhỏ, và một đường chấm chấm đi vòng qua nó để tới hòn đảo kế tiếp.
published: 2026-11-21T12:30+09:00
---

Trong Inkisle, game chiến thuật chinh phục đảo cho iOS của chúng tôi, thua cùng một màn ba lần sẽ hiện ra câu hỏi: "Bỏ qua màn này và thử lại sau?" Bỏ qua tốn 3 Ink. Màn bị bỏ qua có một lá cờ trên hải đồ và có thể chơi lại bất cứ lúc nào. Game vẫn đang được phát triển và chưa phát hành, và chúng tôi chưa thấy bảng hỏi này trên thiết bị thật.

## Vì sao đề nghị bỏ qua

Một số màn vẫn khó dù đã chỉnh độ khó. Chúng tôi không muốn người chơi dừng lại ở một hòn đảo. Lời đề nghị cho phép họ đi tiếp rồi quay lại sau, thay vì bỏ game.

## Khi nào hỏi

- Bảng hỏi xuất hiện sau **lần thua thứ ba** ở cùng một màn, khi bảng kết quả đã yên vị (1,1 giây).
- Nếu người chơi từ chối, game không hỏi ở lần thua thứ 4 và thứ 5. Game hỏi lại ở lần thứ **6, thứ 9** và cứ thế. Hỏi mọi lần thì phiền; chỉ hỏi một lần thì bỏ sót người vẫn đang kẹt.
- Số lần thua được đếm theo từng màn. Thắng màn đó thì đếm về 0. Những lần thua ở màn đã qua hoặc đã bỏ qua không được tính.

## Giá là bao nhiêu

Bỏ qua tốn **3 Ink**, chính là Ink người chơi đã kiếm được trong game hoặc mua. Không thêm loại tiền hay sản phẩm mới nào. Giá trị này là một hằng số duy nhất trong mã, và nội dung bảng hỏi, nút bấm cùng liên kết tới cửa hàng đều theo nó.

Lúc đầu chúng tôi đặt 1 Ink, rồi nâng lên 3 sau khi chủ sở hữu yêu cầu từ 2 đến 3. Nếu người chơi có dưới 3 Ink, nút bỏ qua đổi thành "Hết Ink, mở cửa hàng" và mở bảng cửa hàng có sẵn. Từ 3 Ink trở lên, nút bỏ qua trở lại.

## Những màn nào bị loại trừ

- Màn 1-1 đến 1-4, đoạn hướng dẫn không có Ink. Bỏ qua ở đó nghĩa là không bao giờ học được cách điều khiển.
- Màn 1-5, nơi game tặng Ink đầu tiên.
- Màn cuối, vì không có màn kế tiếp để mở.
- Các màn trùm được tính.

## Màn bị bỏ qua nghĩa là gì

- Màn kế tiếp mở ra, còn màn bị bỏ qua có **0 sao**. Bỏ qua không phải là qua màn, nên không thể mua sao.
- Trên hải đồ, nút màn có lá cờ san hô. Trình đọc màn hình đọc thêm "đã bỏ qua". Thẻ màn ghi: "Màn này đã bị bỏ qua. Hãy thử lại khi bạn sẵn sàng."
- Nếu sau đó thắng, lá cờ biến mất và sao được ghi bình thường.
- Một vùng biển chỉ hoàn thành khi các màn của nó đã qua, nên màn có cờ vẫn phải thắng để hoàn thành vùng biển.
- Đoạn kết chỉ mở khi thắng thật, nên bỏ qua màn 10-8 không mở nó.

## Được lưu như thế nào

Bản ghi tiến trình hiện có được thêm hai khóa tùy chọn: số lần thất bại theo từng màn và danh sách các màn đã bỏ qua. Nếu cả hai trống, các khóa không được ghi, nên bản lưu cũ vẫn giống từng byte. Khi đọc, id lạ và giá trị âm hoặc chữ bị loại bỏ, và màn đã qua sẽ mất dấu bỏ qua, vì việc qua màn được ưu tiên.

Khi gộp iCloud, số lần thất bại lớn hơn được giữ, danh sách bỏ qua được hợp lại, và việc qua màn trên thiết bị khác được ưu tiên. Gộp lại cùng một bản chụp không thay đổi gì, và có một bài kiểm tra xác nhận điều này.

## Những gì chúng tôi chưa kiểm tra

- Bảng hỏi và lá cờ trên thiết bị thật hoặc trình giả lập. Kiểm tra widget ở chiều rộng 375 và 320 px không thấy tràn ở 16 cột ngôn ngữ, nhưng chúng tôi chưa xem ảnh chụp màn hình.
- Liệu bản app cũ ghi đè bản chụp iCloud có làm mất hai khóa mới hay không. Nếu có, các màn đã qua và sao vẫn còn, chúng tôi cho rằng chỉ mất dấu bỏ qua.
- Các bản dịch ngoài tiếng Hàn và tiếng Anh chưa được người bản ngữ xem lại.

## FAQ

### Khi nào Inkisle đề nghị bỏ qua màn?

Sau khi thua cùng một màn ba lần, và lại hỏi sau lần thua thứ 6, thứ 9 và cứ thế nếu bạn tiếp tục. Các màn đầu, màn quà 1-5 và màn cuối được loại trừ.

### Bỏ qua tốn bao nhiêu và có nhận sao không?

Tốn 3 Ink. Màn bị bỏ qua cho 0 sao. Nếu sau đó thắng, bạn nhận sao như bình thường.

### Bỏ qua có hoàn thành vùng biển hay mở đoạn kết không?

Không. Vùng biển chỉ hoàn thành khi các màn đã qua, và đoạn kết chỉ mở khi thắng thật.
