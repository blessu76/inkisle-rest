---
title: Hai biển miễn phí và một lần mở khóa: cách chúng tôi đơn giản hóa thanh toán
description: Inkisle giữ biển 1 và 2 miễn phí và mở phần còn lại bằng một lần mua duy nhất, Mở khóa tất cả biển. Mực tiêu hao được thiết lập như thế nào, cách khóa được tính trong mã, những ranh giới chúng tôi đặt ra cho việc khôi phục và hoàn tiền, và những điều chúng tôi chưa kiểm tra.
slug: two-free-seas-and-one-unlock
lang: vi
translation_of: en
category: making-of
keywords: Inkisle, mua trong ứng dụng, không tiêu hao, biển miễn phí, khôi phục giao dịch, game di động
image_alt: Hai hòn đảo đang mở, phía sau là một dãy đảo có ổ khóa, và một chiếc chìa khóa nằm ngang qua dãy đảo đó.
---

Inkisle, game chiến lược chinh phục đảo của chúng tôi trên iOS, nay giữ biển 1 và 2 miễn phí và mở biển 3 đến 30 (28 biển) bằng một lần mua duy nhất, Mở khóa tất cả biển. Mực tiêu hao đã có trong cấu hình bán hàng, nhưng chưa phát hành và chưa kiểm tra trên thiết bị. Sáu vật phẩm tiền boa giữ nguyên. Sản phẩm trên cửa hàng đang ở bước đăng ký, nhưng chưa gửi xét duyệt và chưa kiểm tra trên thiết bị thật, nên việc mua hàng chưa được xác nhận. Trò chơi đang được phát triển và chưa phát hành. Bài viết này không nêu giá cả hay ngày phát hành.

## Điều gì đã thay đổi

Thiết kế đầu tiên làm mọi màn chơi đều miễn phí, còn mực giúp giảm độ khó được bán dưới dạng vật phẩm nhỏ tiêu hao. Ngày 15 tháng 11, người phụ trách đã thay đổi điều này. **Biển 1 và 2 miễn phí, và Mở khóa tất cả biển là lần mua một lần không tiêu hao.** Mực tiêu hao (gói 5 và 15) đã có trong cấu hình bán hàng, nhưng chưa phát hành và chưa kiểm tra trên thiết bị. Mực cũng kiếm được qua sao: mỗi 5 sao được 1, và đánh bại trùm được 2. Mực đã mua trước đó vẫn dùng được.

## Khóa được tính toán

Số biển bị khóa không được gõ cứng trong mã. Nó bằng tổng số biển trừ đi số biển miễn phí. Hiện tại là 30 − 2 = 28. Khi thêm biển, dòng chữ "mở N biển" trên bảng mua sẽ tự cập nhật. Nội dung bán hàng chúng tôi chuẩn bị hứa rằng các biển mới cũng được bao gồm.

- Trên bản đồ, các màn từ biển 3 trở đi có ổ khóa đỏ, và chạm vào sẽ mở cửa hàng thay vì màn chơi.
- Mua hoặc khôi phục sẽ mở tất cả.
- Sau khi thắng, nếu màn tiếp theo nằm trong biển bị khóa, trò chơi sẽ quay về bản đồ.

## Ứng dụng phải chạy được khi chưa có sản phẩm

Nếu cửa hàng chưa có sản phẩm, hoặc việc tra giá thất bại, chỉ nút mua bị tắt và hiện ghi chú "sắp ra mắt". Ứng dụng không bị lỗi. Giá được tra lại mỗi lần bảng mở ra, nên khi sản phẩm đã có thì hoạt động mà không cần đổi mã. Đó chính là tình trạng hiện tại của chúng tôi. Việc thiết lập sản phẩm đang bị chặn ở phía cửa hàng, nên chúng tôi chưa bao giờ chạy luồng mua thật.

## Những ranh giới chúng tôi cố ý đặt ra

| Trường hợp | Hành vi |
|---|---|
| Người chơi đã qua biển 2 | Bị khóa. Hồ sơ và sao vẫn còn, và mua hoặc khôi phục sẽ mở lại |
| Thiết bị khác | Tiến độ đến qua iCloud, nhưng việc mở khóa thì không. Hãy chạm "Khôi phục giao dịch" ở đó |
| Hoàn tiền | Chúng tôi không thu lại quyền truy cập |
| "Mở tất cả" trên TestFlight | Gỡ khóa tiến độ nhưng không gỡ khóa thanh toán, để có thể kiểm thử luồng mua trong sandbox |

Không thu lại quyền truy cập sau khi hoàn tiền vừa là lựa chọn, vừa là giới hạn. Gói `in_app_purchase` của Flutter không có trạng thái nào báo cáo việc hoàn tiền, và ở quy mô này chúng tôi quyết định không xác minh biên lai trên máy chủ. Nhận định đó là một ước tính **[chưa xác minh]**.

## Những điều chúng tôi chưa kiểm tra

- Chúng tôi chưa mua hoặc khôi phục trên thiết bị thật **[chưa xác minh]**. Hiện chỉ có kiểm thử widget (ổ khóa, cửa hàng, mua, mở khóa) và kiểm tra cấu hình StoreKit.
- Giao diện ở 375px và 320px được bao phủ bởi kiểm thử widget, không phải trình giả lập **[chưa xác minh]**.
- Android dùng cùng luồng mã, nhưng vì chưa đăng ký sản phẩm nên chúng tôi không thể kiểm thử thanh toán ở đó **[chưa xác minh]**.
- Nội dung mua hàng bằng 11 ngôn ngữ khác tiếng Hàn được dịch bằng máy **[chưa xác minh]**.

## Câu hỏi thường gặp

### Phần nào của Inkisle miễn phí?

Biển 1 và 2. 28 biển còn lại sẽ mở cùng lúc khi mua Mở khóa tất cả biển. Trò chơi chưa phát hành.

### Tôi phải mua mấy lần?

Một lần. Đây là lần mua không tiêu hao, được thiết kế để cả các biển mới cũng được bao gồm.

### Tiền boa có ảnh hưởng đến trò chơi không?

Không. Sáu vật phẩm tiền boa không mang lại lợi thế nào trong trò chơi và giữ nguyên như hiện tại.
