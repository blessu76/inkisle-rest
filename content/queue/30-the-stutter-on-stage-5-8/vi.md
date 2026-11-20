---
title: Giật lag ở màn 5-8: lỗi nằm ở màn hình, không phải engine game
description: Màn 5-8 của Inkisle bị giật. Chúng tôi đo trước khi động vào bất cứ thứ gì, thấy chi phí nằm ở việc vẽ màn hình chứ không phải luật chơi, và giảm chi phí một khung hình từ 3,4 xuống 1,3 ms trên máy tính. Chúng tôi đã đổi gì, giữ nguyên gì và chưa kiểm tra gì trên điện thoại.
slug: the-stutter-on-stage-5-8
lang: vi
translation_of: en
category: making-of
keywords: Inkisle, hiệu năng, giật lag, thời gian khung hình, thiết kế game, game di động, tối ưu hóa
image_alt: Bốn thanh màu tím cao ở bên trái và bốn thanh màu san hô thấp ở bên phải, ở giữa có một mũi tên và một đường nét đứt đánh dấu ngân sách.
---

Inkisle, game chiến thuật chinh phục đảo cho iOS của chúng tôi, bị giật ở màn 5-8 khi thử nghiệm. Phỏng đoán dễ nhất là engine game, phần di chuyển hạm đội và quyết định chiếm đảo, đã trở nên quá nặng. Chúng tôi đo trước. Vấn đề không phải engine mà là màn hình bao quanh nó. Sau thay đổi, chi phí một khung hình ở màn 5-8 giảm từ 3,4 ms xuống 1,3 ms trên máy tính của chúng tôi. Game vẫn đang được phát triển và chưa phát hành, và các con số này không đo trên điện thoại [chưa xác minh].

## Chúng tôi đã đo gì

Một khung hình có hai loại việc: đưa luật chơi tiến thêm một tick, và dựng rồi vẽ màn hình. Ở màn 5-8, một tick của luật chơi trung bình chỉ tốn 3 đến 5 micro giây. Màn hình tốn gấp khoảng một nghìn lần.

Phần lớn chi phí màn hình đó đến từ ba nguyên nhân:

1. **Toàn bộ HUD bị dựng lại ở mỗi khung hình.** Bộ điều khiển game báo thay đổi ở mỗi khung hình, nên thanh sức mạnh, chữ mục tiêu, bảng kết quả, thanh tỉ lệ, huy hiệu, thanh lựa chọn, lớp phủ khủng hoảng và nút thủy triều đều bị dựng lại dù không có gì đổi. Khoảng 2,5 ms trong 3,4 ms dành cho việc dựng widget.
2. **Nhãn số trượt khỏi cache.** Khóa cache chứa độ trong suốt và kích thước chính xác của từng con số, mà chúng thay đổi liên tục trong lúc lan chiếm đảo hoặc mờ dần. Vì vậy mỗi khung hình lại tạo bố cục mới, và khi cache vượt quá 600 mục thì bị xóa sạch, khiến một khung hình phải bố trí lại mọi thứ. Thời gian vẽ ở 1 phần trăm khung hình chậm nhất gấp 5 đến 10 lần mức trung bình.
3. **Việc nhỏ lặp lại.** Mỗi hạm đội tra màu mực hai lần, vị trí và bán kính của mỗi đảo bị tính lại cho từng hạm đội, và một cache shader dùng khóa dạng chữ.

## Chúng tôi đã đổi gì

- HUD giờ chỉ lắng nghe một tín hiệu nhỏ, phát ra khi thứ nó hiển thị thay đổi, như tick, tạm dừng, tốc độ, trạng thái khủng hoảng, mục tiêu hoặc gợi ý. Việc vẽ vẫn diễn ra ở mỗi khung hình như trước.
- Nhãn số được làm tròn theo các bậc thô (độ trong suốt 32 bậc, kích thước theo phần tư pixel) để cache trúng, và khi đầy thì chỉ bỏ nửa cũ hơn.
- Các lần tra cứu lặp lại chỉ tính một lần mỗi khung hình, và khóa shader đổi từ chuỗi sang bản ghi.

Việc làm tròn kích thước và độ trong suốt không nhìn thấy được bằng mắt.

## Các con số

Đo trên máy tính, ở màn hình 375 × 667, trong một chế độ chỉ phù hợp để so sánh trước và sau.

| | trước | sau |
|---|---|---|
| Màn 5-8, cả khung hình, trung bình | 3.433 µs | 1.267 µs |
| Màn 5-8, cả khung hình, 1% chậm nhất | 10.803 µs | 5.182 µs |
| Màn 5-8, vẽ, trung bình | 818 µs | 201 µs |
| Màn 5-8, vẽ, 1% chậm nhất | 4.540 µs | 1.284 µs |

Một game 60 khung hình mỗi giây có khoảng 16,6 ms cho mỗi khung hình, nên ngay cả trước thay đổi, công việc vẫn nằm trong ngân sách đó trên máy tính. Vì thế cảm giác giật mà chúng tôi thấy có thể còn một nguyên nhân khác (xem bên dưới).

## Chúng tôi giữ nguyên gì

Chúng tôi không đổi một dòng nào của luật chơi hay mã cân bằng. Chỉ lớp màn hình thay đổi: cách bộ điều khiển báo cập nhật, widget nào lắng nghe và các cache vẽ. Cùng một seed vẫn cho cùng kết quả 600 tick, và các kiểm tra sẵn có về ảnh chuẩn, chơi có tính xác định và mô phỏng bot vẫn xanh.

Chúng tôi cũng để lại một chi phí có thật cho sau này. Dự báo khủng hoảng chạy trên luồng màn hình: ở màn nặng nhất chúng tôi đo được, 17-3, nó trung bình 3,4 ms và 1 phần trăm chậm nhất lên tới 11,8 ms, có thể gây một cú khựng nhỏ mỗi nửa giây. Chia việc đó ra nhiều khung hình sẽ cho cùng kết quả, nhưng có nguy cơ làm đổi quyết định, nên lần này chúng tôi không làm. Ở màn 5-8 nó tốn 0,17 ms và không đáng kể.

## Chúng tôi đã thêm gì

Một benchmark cho engine không cần màn hình, và một bài kiểm tra hiệu năng với giới hạn trên rộng rãi. Nó bắt loại thoái lui mà chi phí bùng nổ theo số hạm đội hoặc mỗi khung hình cấp phát quá nhiều bộ nhớ. Chúng tôi cố ý để giới hạn rộng, vì giới hạn chặt sẽ thất bại mỗi khi máy kiểm tra bận. Theo mặc định, các bài nặng nhất bị bỏ qua và chỉ chạy khi được yêu cầu.

## Những gì chúng tôi chưa kiểm tra

- **Tốc độ khung hình trên điện thoại thật, ở 60 hay 120 khung hình mỗi giây, chưa được kiểm tra [chưa xác minh].** Con số của chúng tôi là chi phí luồng màn hình trên máy tính, không phải chi phí đồ họa trên thiết bị.
- **Màn sương và các lớp dải chưa được đo và chưa được thay đổi [chưa xác minh].** Chúng được vẽ bằng làm mờ toàn màn hình, tốn ở chip đồ họa chứ không phải bộ xử lý. Nếu màn 5-8 vẫn giật trên điện thoại, đây là nghi phạm đầu tiên của chúng tôi.
- Chúng tôi chưa xem kết xuất trên trình duyệt ở 320, 375, 768 và 1280 px, vì không bố cục nào thay đổi [chưa xác minh].
- Việc thao tác nhạy hơn chỉ là kỳ vọng của chúng tôi [chưa xác minh].

## FAQ

### Vì sao màn 5-8 trong Inkisle bị giật?

Phép đo của chúng tôi chỉ ra việc màn hình bị dựng lại và nhãn số bị bố trí lại ở mỗi khung hình, chứ không phải luật chơi. Chúng tôi đã sửa; tốc độ khung hình trên điện thoại thật chưa được kiểm tra.

### Tối ưu hóa có thay đổi cách chơi không?

Không. Chúng tôi không đụng đến luật chơi hay mã cân bằng, và cùng một seed cho kết quả giống như trước.

### Trên điện thoại còn giật không?

Chúng tôi chưa biết. Các con số của chúng tôi đến từ máy tính. Chúng tôi sẽ kiểm tra trên thiết bị thật qua TestFlight.
