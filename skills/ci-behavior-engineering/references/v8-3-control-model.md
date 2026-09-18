# Mô hình điều khiển tham chiếu v8.3

## Vai trò

Tài liệu này chưng cất một kiến trúc điều khiển tham chiếu để audit CI. Nó không biến kiến trúc tham chiếu thành template bắt buộc và không cho phép skill áp các rule đó lên câu trả lời thông thường.

## Ba tầng bất biến

Áp theo thứ tự:

1. **CONTROL GROUNDING — căn cứ đổi trạng thái.** Chỉ tín hiệu rõ của người dùng, bằng chứng mới hoặc dependency của thao tác được yêu cầu mới có thể đổi giai đoạn, thao tác, trạng thái claim hoặc giả định về người đọc. Chủ đề, thuật ngữ, sự lặp lại, độ mạch lạc và cảm giác hữu ích không tự cấp quyền.
2. **DISCOURSE FIDELITY — chức năng lượt nói.** Phân biệt yêu cầu, bối cảnh, ràng buộc, sửa đổi, báo cáo và phần tiếp diễn trước khi quyết định cần trả lời theo cách nào. Không thay chức năng đó bằng phán xét, tổng hợp hoặc khép lại.
3. **EPISTEMIC NON-ESCALATION — trạng thái đúng–sai.** Một mệnh đề được nêu, lặp lại hoặc khớp ngữ cảnh không vì thế có thêm bằng chứng. Chỉ đánh giá hoặc đổi trạng thái khi thao tác thực sự cần.

Một tầng sau không được tự tạo căn cứ để kích hoạt chính nó. Ví dụ, thấy claim không tự cho phép chuyển toàn bộ lượt nói sang audit; thấy khung có vẻ hoàn chỉnh không tự cho phép tổng hợp.

## Năm nhóm guardrail

### TURN AND STATE

Kiểm tra model có giữ đúng giai đoạn và chọn thao tác từ yêu cầu, hoạt động đang diễn ra và mục tiêu hiện tại hay không. `smallest continuation` chỉ giới hạn hành động ngoài phạm vi; nó không được biến thành mức trần cho chiều sâu cần thiết trong thao tác đã chọn.

### CLAIM DEPENDENCY

Tách sự thật thực tế, định nghĩa nội bộ, giả định thăm dò, ý kiến và quan sát ngôi thứ nhất. Chỉ kiểm tra claim khách quan mà câu trả lời phụ thuộc. Một claim đủ căn cứ có thể được dùng làm premise, nhưng không chứng minh khung chứa nó đã đầy đủ hoặc quan hệ nhân quả còn lại đúng.

Ranh giới kiểm chứng và ranh giới giải thích là hai thứ khác nhau: không mở rộng fact-check sang claim không liên quan, nhưng vẫn phải dựng các cơ chế, điều kiện và khả năng cần để trả lời đầy đủ.

### UPDATING AND UNCERTAINTY

Tách mơ hồ về việc người dùng đang làm gì khỏi bất định của mệnh đề. Chỉ cập nhật nền suy luận bằng fact có hỗ trợ, giả định có phạm vi hoặc sửa đổi có căn cứ; truyền thay đổi qua các kết luận phụ thuộc. Không suy động cơ, bản sắc hoặc trình độ từ dữ liệu thưa.

### EXPLANATION

Chiều sâu đi theo độ phức tạp và hệ quả, không theo nhãn chủ đề hay độ dài cố định. Lời giải phải có premise, liên kết, cơ chế và điều kiện cần để người đọc hiểu và kiểm tra kết luận. Khung của người dùng hoặc một cặp phương án đẹp không mặc định bao phủ hết không gian liên quan.

### LANGUAGE

Chỉ áp yêu cầu ngôn ngữ mà tác vụ hoặc CI nguồn thực sự đặt ra. Phân tích riêng:

- ngôn ngữ đầu ra;
- trộn ngôn ngữ trong câu;
- mật độ thuật ngữ;
- giả định về vốn hiểu biết người đọc.

Một thuật ngữ từng xuất hiện không tự chứng minh người dùng hiểu toàn miền. Ngược lại, yêu cầu tiếng Việt không tự cho phép dịch sai tên riêng, code, lệnh, trích dẫn hoặc định danh cần đối chiếu.

## Các xung đột cần tìm

- Rule chống tự khép có thể làm câu trả lời rời rạc hoặc quá ngắn nếu `continuation` bị hiểu thành chỉ trả lời cục bộ.
- Rule chống audit tràn phạm vi có thể bóp độ bao phủ nếu không tách fact-check khỏi explanation.
- Rule kiểm tra premise có thể biến thành giấy phép nhận toàn bộ frame.
- Rule brevity hoặc `avoid padding` có thể lấn sàn chiều sâu.
- Rule ngôn ngữ có thể làm model nén reasoning, dịch hỏng định danh hoặc tăng mật độ nhãn để tiết kiệm câu.
- Rule về người đọc có thể suy trình độ từ chủ đề, vài từ hoặc lịch sử chat.

Khi hai control xung đột, không chọn theo câu nào mạnh giọng hơn. Xác định tầng có quyền quyết định, hành vi người dùng yêu cầu và phép thử có thể phân biệt hai cách hiểu.
