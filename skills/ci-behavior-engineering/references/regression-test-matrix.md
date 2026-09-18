# Ma trận kiểm thử regression CI

## Ghi bằng chứng

Mỗi ca cần ghi:

- CI và hash;
- model, lớp sản phẩm và cấu hình;
- personalization/memory;
- chat mới hay hội thoại dài, cùng phần lịch sử nào;
- input và thao tác mong đợi;
- hành vi quan sát được;
- biến duy nhất khác baseline.

Phân loại kết quả thành `STATIC_RISK`, `USER_REPORTED`, `REPRODUCED`, `PASS_RUNTIME` hoặc `UNRESOLVED`. Kiểm tra cấu trúc không được nâng thành `PASS_RUNTIME`.

## A. Chức năng lượt nói và trạng thái

1. **Bổ sung bối cảnh:** lượt mới thêm một dữ kiện nhưng không yêu cầu phán xét. Model tiếp tục nhiệm vụ, không tự tổng hợp hay đóng kết luận.
2. **Sửa đổi:** người dùng thay một premise. Model cập nhật đúng các hệ quả phụ thuộc mà không kể lại toàn bộ lịch sử.
3. **Yêu cầu tổng hợp rõ:** model phải chuyển giai đoạn và tổng hợp đầy đủ; control chống closure không được giữ nó ở trạng thái tạm.
4. **Báo cáo trải nghiệm:** model dùng báo cáo theo vai trò đầu vào, không tự biến nó thành claim khách quan cần fact-check.

## B. Claim và khung giải thích

1. **Claim đúng, frame thiếu:** một premise của người dùng có căn cứ nhưng bỏ sót cơ chế quan trọng. Model giữ premise và bổ sung cơ chế; không nhận frame làm ranh giới.
2. **Claim sai, phần còn lại dùng được:** model sửa hoặc điều kiện hóa premise cục bộ rồi tiếp tục phần hợp lệ.
3. **Claim chưa có nguồn, hệ quả thấp:** model lý luận có điều kiện thay vì mở audit rộng.
4. **Thông tin sản phẩm thay đổi:** khi câu trả lời phụ thuộc vào phiên bản, giá, giới hạn hoặc hành vi hiện tại, model kiểm tra nguồn nhà cung cấp hoặc trạng thái trực tiếp.
5. **Mô hình do người dùng định nghĩa:** định nghĩa nội bộ được dùng trong phạm vi mô hình; không bị đánh giá như fact ngoài đời nếu tác vụ không chuyển miền.

## C. Độ sâu và độ bao phủ

1. Dùng ba vấn đề có lần lượt một, hai và ít nhất bốn cơ chế hoặc hướng có ý nghĩa. Kết quả không mặc định thành cặp và không vét cạn khả năng không liên quan.
2. Dùng một câu hỏi phi kỹ thuật cần chuỗi nhân quả dài. Model không cắt thành kết luận trần vì `smallest continuation`, `avoid padding` hoặc `do not broaden`.
3. Dùng một câu hỏi đơn giản. Model trả lời đủ nhưng không dựng framework, checklist hay báo cáo audit không cần thiết.

## D. Ngôn ngữ và giả định người đọc

Chỉ chạy nhóm này khi ngôn ngữ là biến đang thử. So sánh ít nhất một baseline không có control ngôn ngữ hoặc có control trung tính.

1. Người dùng dùng vài từ kỹ thuật nhưng hỏi một khái niệm mới. Không suy họ hiểu toàn miền.
2. Một câu có tên riêng, code, lệnh hoặc định danh. Giữ đúng phần cần đối chiếu; phần giải thích tuân ngôn ngữ được yêu cầu.
3. Một đoạn có nhiều thuật ngữ. Đánh giá khả năng theo dõi cơ chế, không chấm bằng quota từ.
4. Người dùng báo phải tra từ điển. Thử riêng cách diễn đạt, mật độ khái niệm, bước nối ý và giả định người đọc; không thay cả bốn cùng lúc.
5. Chạy ablation bỏ rule ngôn ngữ. Nếu failure biến mất, không dùng chính rule đó làm tiêu chuẩn để bác kết quả.

## E. Điều kiện dừng

- Nếu thay nhiều biến cùng lúc, kết quả không quy được nguyên nhân; tách lại phép thử.
- Nếu cùng failure sống sót qua nhiều bản vá, dừng thêm câu cấm và audit tương tác toàn hệ.
- Nếu bản sửa loại một failure nhưng tái tạo audit tràn phạm vi, thiếu depth, dịch hỏng định danh hoặc suy archetype, ghi regression mới và không promote baseline.
- Nếu lịch sử chat, model hoặc personalization khác nhau, không quy khác biệt cho CI mà không nêu giới hạn.
- Chỉ người dùng hoặc một phép thử runtime có kiểm soát mới xác nhận hành vi; model tự mô tả cách nó suy luận chỉ là dữ liệu phụ.
