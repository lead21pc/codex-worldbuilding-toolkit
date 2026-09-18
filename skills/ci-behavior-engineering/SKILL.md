---
name: ci-behavior-engineering
description: Thiết kế, audit, sửa, rút gọn hoặc kiểm thử ChatGPT Custom Instructions dựa trên regression hành vi quan sát được và kiến trúc điều khiển kiểu v8.3. Dùng cho CI hành vi; không dùng cho CI/CD, chỉnh văn phong thông thường, hoặc tự áp v8.3 lên mọi tác vụ.
---

# CI behavior engineering

## Mục đích và ranh giới

Dùng skill này để nghiên cứu hành vi của Custom Instructions, không dùng nó như một bộ Custom Instructions toàn cục. v8.3 là kiến trúc tham chiếu để tách quyền đổi trạng thái, chức năng lượt nói, trạng thái claim và các guardrail; không phải mẫu bắt buộc cho mọi CI.

Giữ đúng thao tác người dùng yêu cầu:

- `AUDIT`: tìm nguyên nhân và đề xuất; không sửa file.
- `DESIGN`: thiết kế CI hoặc control mới; không tự cài hay thay baseline.
- `PATCH`: sửa regression đã được khoanh vùng.
- `COMPACT`: rút gọn nhưng giữ nghĩa và thứ tự quyền hạn.
- `TEST`: chuẩn bị hoặc đánh giá phép thử hành vi.

Không kết hợp các thao tác nếu không cần. Approval cho một bản vá không cấp quyền tạo branch, ghi changelog, commit, push, merge, cài skill hoặc thay artifact khác. Với thử nghiệm nội bộ, không thực hiện các hành động đó nếu người dùng chưa yêu cầu rõ.

## Căn cứ trước khi sửa

Xác định hành vi quan sát được, hành vi mong đợi, baseline gần nhất còn tốt và thay đổi đầu tiên có lỗi. Phân biệt:

- lỗi runtime đã tái hiện;
- báo cáo runtime của người dùng;
- nguy cơ từ câu chữ hoặc xung đột rule;
- giả thuyết chưa kiểm tra.

Kiểm tra cấu trúc, hash hoặc độ dài không chứng minh hành vi runtime. Nếu không có đủ bằng chứng để chọn nguyên nhân, đề xuất phép thử có khả năng phân biệt thay vì thêm rule.

## Đường audit bắt buộc

Với mỗi phát hiện, trình bày:

`câu chữ hiện tại → trigger/input → cách model có thể hiểu → hành vi lỗi → vì sao control hiện tại không chặn được`

Sau đó phân loại câu liên quan thành nguyên nhân trực tiếp, tác nhân khuếch đại hoặc control chống lỗi. So sánh diff nhỏ nhất giữa bản tốt và bản lỗi; không suy nguyên nhân từ toàn bộ phiên bản khi chỉ một phần thay đổi.

Khi lỗi liên quan nhiều tầng hoặc kiến trúc, đọc [mô hình điều khiển v8.3](references/v8-3-control-model.md). Không để một guardrail tự tạo trigger hoặc quyền hạn bằng tín hiệu mà nó đang kiểm soát.

## Kỷ luật bản vá

Sửa nguyên nhân nhỏ nhất nhưng đầy đủ. Không tích lũy câu cấm cho từng biểu hiện nếu một xung đột quyền hạn hoặc phân loại sai giải thích được chúng.

- Giữ một biến nhân quả cho mỗi phép thử. Khi nhiều biến thể đang thử cùng chia sẻ regression, áp bản vá chung giống nhau và giữ nguyên khác biệt có chủ đích.
- Không coi một tiền đề đã được hỗ trợ là bằng chứng rằng toàn bộ khung giải thích của người dùng đầy đủ.
- Giới hạn phạm vi fact-check không được giới hạn cơ chế, điều kiện hoặc khả năng cần để giải thích đầy đủ.
- Tách ngôn ngữ đầu ra, code-switching, mật độ thuật ngữ và giả định về kiến thức người đọc. Không dùng một classifier để thay cho cả bốn.
- Không tự thêm hạn mức số lượng thuật ngữ. Nếu người dùng yêu cầu thử hạn mức, coi đó là biến thử nghiệm chứ không phải baseline đã chứng minh.
- Khi cùng failure tiếp tục sau nhiều bản vá, dừng thêm rule. Audit xung đột toàn hệ và chạy ablation bằng cách bỏ hoặc trung hòa control nghi ngờ.

Nếu bản vá vượt giới hạn ký tự, nén phần lặp, ví dụ và tiêu đề trước. Không âm thầm làm yếu bất biến, độ sâu hoặc điều kiện kiểm chứng. Tạo artifact phiên bản mới thay vì chép đè khi người dùng chưa yêu cầu thay thế.

## Kiểm thử và bàn giao

Khi review CI hoàn chỉnh, sửa cơ chế hoặc đánh giá runtime, đọc [ma trận regression](references/regression-test-matrix.md) và chỉ chọn các ca liên quan. Phải có ca thuận, ca chống và ablation khi một control có thể là nguồn bias.

Giữ cố định model, lớp sản phẩm, personalization/memory, lịch sử hội thoại và mọi câu CI ngoài biến đang thử. Định nghĩa kết quả quan sát được trước khi chạy. Không chấm bằng việc xuất hiện đúng câu mẫu hoặc số lượng từ đơn thuần.

Dùng `scripts/inspect-ci.ps1` khi cần kiểm tra UTF-8, BOM, line ending, khoảng trắng cuối dòng, ký tự, byte, hash hoặc diff dòng. Script chỉ kiểm tra cấu trúc; không dùng kết quả của nó để tuyên bố PASS hành vi.

Báo kết quả theo bốn phần: phát hiện hoặc thay đổi; bằng chứng; kiểm tra đã chạy; phần runtime hoặc rủi ro còn chưa xác minh.
