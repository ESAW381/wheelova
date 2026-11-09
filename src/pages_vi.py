# Vietnamese homepage (/vi). Keyword map: competitor export Nov 9 2026 (vòng quay may mắn, vòng quay random, vòng quay ngẫu nhiên, quay số, tạo vòng quay...).
from content_v2 import S_MDN

PALETTE = ["#6E56F0", "#E11D48", "#F59E0B", "#16A34A", "#2563EB", "#DB2777", "#0D9488", "#EA580C"]
TEN = ["An", "Bình", "Chi", "Dũng", "Hà", "Khoa", "Linh", "Minh", "Ngọc", "Phúc"]

JS = {
 "add2": "Thêm ít nhất hai lựa chọn", "spinning": "Đang quay…", "winner": "KẾT QUẢ", "pop": "CHÚC MỪNG! KẾT QUẢ LÀ",
 "empty": "Hãy thêm lựa chọn", "add2share": "Thêm ít nhất hai lựa chọn để chia sẻ", "copied": "Đã sao chép",
 "copy": "Sao chép", "copy_embed": "Sao chép mã", "share_title": "CHIA SẺ VÒNG QUAY", "embed_title": "NHÚNG VÒNG QUAY",
 "long": "Danh sách dài nên liên kết cũng dài ({n} ký tự). Liên kết vẫn hoạt động, nhưng một số ứng dụng nhắn tin có thể cắt bớt.",
 "iframe_title": "Vòng quay may mắn – Wheelova", "credit_pre": "Vòng quay của",
 "fs": "Toàn màn hình", "exitfs": "Thoát toàn màn hình", "openmenu": "Mở menu", "closemenu": "Đóng menu",
 "todark": "Chuyển sang chế độ tối", "tolight": "Chuyển sang chế độ sáng",
 "cleared": "Đã xóa danh sách.", "m_wheel": "Vòng", "m_option": "Lựa chọn", "m_max": "Tối đa 6 vòng quay", "m_add": "+ Thêm vòng quay", "m_spin": "Quay", "m_spinbtn": "QUAY", "removedw": "Đã loại «{w}» khỏi vòng quay.", "imported": "Đã nhập {n} lựa chọn.", "impcut": "Chỉ giữ lại 2.000 dòng đầu tiên.", "impempty": "Không tìm thấy lựa chọn nào trong tệp này.", "impbig": "Tệp quá lớn (tối đa 5 MB).", "impxls": "Hãy lưu bảng tính dưới dạng CSV trước, hoặc sao chép cột rồi dán vào.", "col": "Cột",
 "nrange": "Hãy nhập khoảng có số «Đến» lớn hơn số «Từ».", "nmax": "Tối đa 500 số mỗi vòng quay.",
 "replaced": "Đã thay danh sách.", "kept": "Đã lưu vòng quay được chia sẻ thành danh sách của bạn.",
 "csv_spin": "Lượt", "csv_winner": "Kết quả", "csv_time": "Thời gian", "load": "Mở", "loaded": "Đã mở", "del": "Xóa", "deleted": "Đã xóa",
 "needname": "Hãy đặt tên cho vòng quay trước.", "updated": "Đã cập nhật", "saved": "Đã lưu", "full": "Bạn có thể lưu tối đa 50 vòng quay. Hãy xóa bớt một vòng trước.",
}

NAV_VI = [("vi", "Vòng quay may mắn"), ("", "English"), ("es", "Español"), ("fr", "Français")]

R = lambda J: [
 ('<html lang="en">', '<html lang="vi">'),
 ('aria-label="Switch to light mode"', 'aria-label="' + J["tolight"] + '"'), ('aria-label="Open menu"', 'aria-label="Mở menu"'),
 ('aria-label="Fullscreen" title="Fullscreen (F)"', 'aria-label="Toàn màn hình" title="Toàn màn hình (F)"'),
 ('aria-label="Spinning wheel"', 'aria-label="Vòng quay"'), ('aria-label="Spin the wheel">SPIN<', 'aria-label="Quay vòng quay">QUAY<'),
 ('Press SPIN or the Space bar', 'Nhấn QUAY hoặc phím cách'), ('>Entries <span id="count"', '>Lựa chọn <span id="count"'),
 ('>Shuffle<', '>Trộn<'), ('>Sort<', '>Sắp xếp<'), ('>Clear<', '>Xóa hết<'),
 ('aria-label="Presets"', 'aria-label="Mẫu có sẵn"'),
 ("You're viewing a shared wheel. Your own saved list is untouched.", "Bạn đang xem vòng quay được chia sẻ. Danh sách của bạn vẫn giữ nguyên."), ('Back to my list', 'Quay lại danh sách của tôi'), ('>Keep this as my list<', '>Lưu thành danh sách của tôi<'),
 ('<summary>My saved wheels</summary>', '<summary>Vòng quay đã lưu</summary>'), ('placeholder="Name, e.g. Period 3" aria-label="Name for this wheel"', 'placeholder="Tên, ví dụ: Lớp 10A1" aria-label="Tên vòng quay"'),
 ('>Save list<', '>Lưu<'), ('Save this list under a name to switch between classes or groups. Stored only in this browser.', 'Lưu danh sách này với một cái tên để chuyển nhanh giữa các lớp hoặc nhóm. Chỉ lưu trong trình duyệt này.'),
 ('id="rcopy" type="button">Copy<', 'id="rcopy" type="button">Sao chép<'), ('>Undo<', '>Hoàn tác<'),
 ('One entry per line. Saved in your browser automatically.', 'Mỗi dòng một lựa chọn. Tự động lưu trong trình duyệt.'),
 ('Remove winner after each spin', 'Loại kết quả sau mỗi lượt quay'),
 ('<summary>Settings</summary>', '<summary>Cài đặt</summary>'), ('<label>Spin speed<', '<label>Tốc độ quay<'), ('<label>Wheel colors<', '<label>Màu vòng quay<'),
 ('id="impbtn" type="button">Import<', 'id="impbtn" type="button">Nhập tệp<'), ('<label>Column<', '<label>Cột<'), ('> First row is a header<', '> Dòng đầu là tiêu đề<'), ('type="button">Use column<', 'type="button">Dùng cột này<'), ('id="impno" type="button">Cancel<', 'id="impno" type="button">Hủy<'),
 ('>Pastel<', '>Màu pastel<'), ('>Grayscale<', '>Thang xám<'), ('>Color-blind friendly<', '>Thân thiện người mù màu<'), ('>Custom…<', '>Tự chọn…<'), ('>Ocean<', '>Đại dương<'), ('>Sunset<', '>Hoàng hôn<'), ('>Forest<', '>Rừng xanh<'), ('aria-label="Color ', 'aria-label="Màu '),
 ('> Read the result aloud<', '> Đọc to kết quả<'), ('>Fast<', '>Nhanh<'), ('>Normal<', '>Vừa<'), ('>Slow<', '>Chậm<'),
 ('Winner pop-up heading<input id="wmsg" maxlength="60" placeholder="WE HAVE A WINNER"', 'Tiêu đề cửa sổ kết quả<input id="wmsg" maxlength="60" placeholder="' + J["pop"] + '"'),
 ('</span>Sound<', '</span>Âm thanh<'),
 ('Share link</button>', 'Chia sẻ liên kết</button>'), ('Embed</button>', 'Nhúng</button>'),
 ('>Results <span id="rcount"', '>Kết quả <span id="rcount"'),
 ('WE HAVE A WINNER', J["pop"]), ('>Remove from wheel<', '>Loại khỏi vòng quay<'), ('>Close<', '>Đóng<'),
 ('SHARE THIS WHEEL', J["share_title"]),
 ('Anyone with this link can see your entries: they are encoded inside the link (not encrypted). Nothing is stored on our server, but the link stays in browser history and wherever you paste it, so avoid sharing private lists.', 'Ai có liên kết này đều xem được các lựa chọn của bạn: chúng được mã hóa trong liên kết (không phải mã hóa bảo mật). Chúng tôi không lưu gì trên máy chủ, nhưng liên kết vẫn nằm trong lịch sử trình duyệt và ở nơi bạn dán, vì vậy đừng chia sẻ danh sách riêng tư.'),
 ('for="shareurl">Link<', 'for="shareurl">Liên kết<'), ('id="sharecopy" type="button">Copy<', 'id="sharecopy" type="button">Sao chép<'),
 ('Embed code — paste into your website, blog or OBS browser source', 'Mã nhúng: dán vào website, blog hoặc nguồn trình duyệt (Browser source) trong OBS'), ('>Copy embed code<', '>Sao chép mã nhúng<'),
 ('margin-bottom:12px">Questions<', 'margin-bottom:12px">Câu hỏi thường gặp<'),
 ('Written by <span>', 'Tác giả: <span>'), ('Editor, Wheelova', 'biên tập viên Wheelova'), ('Last updated <time', 'Cập nhật <time'),
 ("Wheelova – Spin the wheel, trust the result", "Wheelova – Vòng quay may mắn"),
 ('content="Wheelova — spin the wheel, trust the result"', 'content="Wheelova — vòng quay may mắn"'),
]

VI = [
{
 "slug": "vi", "en": "", "key": "vi_home", "nav": "Vòng quay may mắn", "palette": PALETTE, "updated": "2026-11-09",
 "title": "Vòng quay may mắn – Vòng quay random online miễn phí | Wheelova",
 "description": "Vòng quay may mắn online miễn phí: nhập tên hoặc lựa chọn, quay và nhận kết quả ngẫu nhiên công bằng. Tạo vòng quay random cho lớp học, minigame, ăn gì. Không cần đăng ký.",
 "h1": "Vòng quay may mắn", "subhead": "Nhập lựa chọn, bấm quay và để may mắn quyết định. Miễn phí, không cần đăng ký, đã kiểm chứng với 1 triệu lượt quay.",
 "entries": TEN,
 "variants": [{"label": "10 tên", "entries": TEN}, {"label": "Có / Không", "entries": ["Có", "Không"]}, {"label": "Số 1–10", "entries": [str(i) for i in range(1, 11)]},
   {"label": "Hôm nay ăn gì?", "entries": ["Phở", "Bún chả", "Cơm tấm", "Bánh mì", "Bún bò Huế", "Lẩu", "Gà rán", "Mì Quảng"]},
   {"label": "Thật hay thách", "entries": ["Thật", "Thách"]}],
 "resultLabel": "KẾT QUẢ", "popLabel": "CHÚC MỪNG! KẾT QUẢ LÀ",
 "howTo": ["Nhập hoặc dán các lựa chọn, mỗi dòng một lựa chọn (hoặc bấm Nhập tệp để tải tệp CSV).", "Bấm QUAY hoặc phím cách.", "Xem kết quả trong cửa sổ. Bật «Loại kết quả sau mỗi lượt quay» nếu không muốn trùng."],
 "sections": [
  {"h2": "Vòng quay may mắn là gì?", "body":
   "**Vòng quay may mắn là một bánh xe ảo được chia thành các phần bằng nhau, mỗi phần là một lựa chọn bạn nhập vào, và dừng lại ngẫu nhiên ở một phần.** Bạn dùng nó để chọn tên, quay số trúng thưởng, trả lời có hay không, hoặc quyết định bất cứ điều gì mà không ai can thiệp được vào kết quả. Vì mọi người cùng nhìn vòng quay quay, kết quả được xem là công bằng.\n\n"
   "Công cụ này còn được gọi là **vòng quay random**, **vòng quay ngẫu nhiên**, **vòng xoay may mắn** hay **bánh xe may mắn**. Trên Wheelova, bạn **tự tạo vòng quay** theo ý mình: tự nhập lựa chọn, đổi màu, chỉnh tốc độ và lời chúc khi có kết quả."},
  {"h2": "Cách tạo vòng quay may mắn", "body":
   "1. **Nhập lựa chọn,** mỗi dòng một lựa chọn: tên, phần quà, con số hay nhiệm vụ. Bạn có thể dán một cột từ Excel hoặc Google Sheets, hoặc bấm **Nhập tệp** để tải tệp CSV.\n"
   "2. **Tùy chỉnh** trong **Cài đặt**: màu sắc (pastel, đại dương, hoàng hôn, rừng xanh, thang xám, thân thiện người mù màu hoặc màu tự chọn), tốc độ quay và tiêu đề cửa sổ kết quả.\n"
   "3. **Quay** bằng nút QUAY hoặc phím cách. Nhấn **F** để quay toàn màn hình khi chiếu lên máy chiếu hoặc TV.\n"
   "4. **Lưu hoặc chia sẻ:** lưu danh sách với một cái tên trong **Vòng quay đã lưu**, sao chép liên kết để gửi cho bạn bè, hoặc nhúng vòng quay vào website hay livestream bằng OBS.\n\n"
   "Không cần tài khoản, không cần tải ứng dụng: vòng quay chạy ngay trên trình duyệt của điện thoại, máy tính bảng và máy tính."},
  {"h2": "Vòng quay có thật sự ngẫu nhiên? Chúng tôi đã thử 1.000.000 lượt quay", "body":
   "Có. Mỗi lượt quay dùng hàm `crypto.getRandomValues()` của trình duyệt. Theo MDN Web Docs, các trình duyệt triển khai hàm này như một **bộ sinh số giả ngẫu nhiên an toàn về mặt mật mã**, được cấp entropy từ hệ thống, cùng loại nguồn dùng cho các tính năng bảo mật. Con số ngẫu nhiên quyết định vòng quay quay bao xa, và phần dừng dưới kim chỉ là kết quả.\n\n"
   "Để kiểm chứng, chúng tôi chạy đúng mã quay của Wheelova **1.000.000 lần** trên vòng quay 2, 6 và 10 lựa chọn:\n\n"
   "| Vòng quay | Số lượt | Kỳ vọng mỗi lựa chọn | Kết quả thực tế | Kiểm định khi bình phương |\n|---|---|---|---|---|\n"
   "| 2 lựa chọn (có/không) | 1.000.000 | 500.000 | 499.629 – 500.371 | p = 0,458 · không thiên lệch |\n"
   "| 6 lựa chọn (như xúc xắc) | 1.000.000 | 166.667 | 165.897 – 167.442 | p = 0,107 · không thiên lệch |\n"
   "| 10 lựa chọn (danh sách lớp) | 1.000.000 | 100.000 | 99.417 – 100.657 | p = 0,066 · không thiên lệch |\n\n"
   "Ở cả ba vòng quay, không lựa chọn nào lệch quá 0,7% so với kỳ vọng, và kiểm định khi bình phương không phát hiện thiên lệch (giá trị p lớn hơn 0,05 nghĩa là không có bằng chứng thiên lệch). Chúng tôi cũng không thấy mối liên hệ nào giữa lượt quay trước và lượt sau. Phương pháp, dữ liệu gốc và mã kiểm thử có trong [nghiên cứu đầy đủ](/is-the-wheel-random) (tiếng Anh), để bất kỳ ai cũng có thể tự kiểm tra lại."},
  {"h2": "Xác suất của vòng quay", "body":
   "Các phần có kích thước bằng nhau, nên xác suất của mỗi lựa chọn là **1 ÷ số lựa chọn**:\n\n"
   "| Số lựa chọn | Xác suất mỗi lựa chọn trong một lượt | Xác suất một lựa chọn cụ thể ra ít nhất một lần trong 10 lượt |\n|---|---|---|\n"
   "| 2 | 50% | 99,9% |\n| 3 | 33,3% | 98,3% |\n| 4 | 25% | 94,4% |\n| 6 | 16,7% | 83,8% |\n| 10 | 10% | 65,1% |\n| 20 | 5% | 40,1% |\n| 50 | 2% | 18,3% |\n\n"
   "Cột cuối được tính theo công thức 1 − (1 − 1/n)¹⁰, với điều kiện không loại kết quả khỏi vòng quay. Bạn có thể dùng các bảng này trong bài giảng hoặc bài viết, chỉ cần kèm liên kết về trang này."},
  {"h2": "Vì sao một kết quả ra nhiều lần liên tiếp?", "body":
   "Vì mỗi lượt quay là **độc lập**: vòng quay không nhớ kết quả trước. Với 2 lựa chọn, cùng một kết quả ra hai lần liên tiếp trong khoảng một nửa số lần. Trong 1 triệu lượt quay vòng có/không của chúng tôi:\n\n"
   "| Chuỗi cùng một kết quả | Số lần xảy ra | Kỳ vọng theo xác suất |\n|---|---|---|\n"
   "| 5 lần liên tiếp trở lên | 31.199 | khoảng 31.250 |\n| 10 lần liên tiếp trở lên | 944 | khoảng 977 |\n| 15 lần liên tiếp trở lên | 27 | khoảng 31 |\n| Chuỗi dài nhất | 19 | thường 19–20 trong 1 triệu lượt |\n\n"
   "Nghĩ rằng «sắp đến lượt» lựa chọn kia là **ngụy biện con bạc** (gambler's fallacy). Nếu muốn mỗi lựa chọn chỉ ra một lần, hãy bật **Loại kết quả sau mỗi lượt quay**."},
  {"h2": "Vòng quay có gian lận được không?", "body":
   "Wheelova không có cài đặt ẩn nào để chọn trước người thắng, và kết quả không bao giờ phụ thuộc vào vị trí hay tên của lựa chọn. Điều duy nhất có thể làm, **công khai trước mọi người**, là tăng tỉ lệ cho một lựa chọn bằng cách nhập nó nhiều lần: với «Có, Có, Không», Có được 2 trên 3 cơ hội (khoảng 67%).\n\n"
   "Vì vậy, khi quay số trúng thưởng công khai: hãy cho mọi người xem đầy đủ danh sách trước khi quay, xóa tên trùng nếu thể lệ không cho phép, và quay trực tiếp hoặc quay màn hình lại. Ai nắm danh sách là nắm tỉ lệ, nên danh sách cần được công khai."},
  {"h2": "Dùng vòng quay may mắn để làm gì?", "body":
   "| Mục đích | Mẫu gợi ý | Mẹo |\n|---|---|---|\n"
   "| Gọi tên học sinh trong lớp | 10 tên (thay bằng danh sách lớp) | Bật «Loại kết quả» để ai cũng đến lượt |\n"
   "| Quay số trúng thưởng, minigame livestream | Dán danh sách người tham gia | Công khai danh sách, xuất kết quả CSV để lưu lại |\n"
   "| Hôm nay ăn gì? | Hôm nay ăn gì? | Chỉ để những món cả nhóm đều chịu ăn |\n"
   "| Trả lời có hay không | Có / Không | Thêm «Có thể» hoặc chơi thắng 2 trong 3 |\n"
   "| Thật hay thách, vòng quay nhân phẩm | Thật hay thách | Thống nhất luật chơi trước khi quay |\n"
   "| Quay số ngẫu nhiên, lô tô | Số 1–10 | Nhập dãy số bạn cần, bật «Loại kết quả» để không trùng |"},
  {"h2": "Thay thế con quay trên Google", "body":
   "Nhiều người tìm «con quay trên Google». Wheelova là công cụ độc lập, không liên quan đến Google, và có thêm những thứ một công cụ tìm kiếm nhanh không có: **lựa chọn do bạn tự nhập**, loại kết quả sau mỗi lượt, lịch sử kết quả có thể xuất CSV, danh sách đã lưu, màu tùy chỉnh, chế độ toàn màn hình, liên kết chia sẻ và mã nhúng cho website hoặc livestream OBS."},
  {"h2": "Cảnh giác với «vòng quay trúng điện thoại miễn phí»", "body":
   "Wheelova là công cụ để **bạn tự quay danh sách của mình**. Chúng tôi không tổ chức sự kiện trúng thưởng, không phát quà và không bao giờ yêu cầu số điện thoại, mật khẩu hay tiền để «nhận giải». Nếu một trang web hứa trúng điện thoại hay thẻ cào chỉ sau một lượt quay rồi đòi thông tin cá nhân hoặc chuyển khoản, đó rất có thể là lừa đảo."},
  {"h2": "Quyền riêng tư: lựa chọn của bạn nằm trên thiết bị của bạn", "body":
   "Những gì bạn nhập được lưu trong trình duyệt, không gửi lên máy chủ của chúng tôi, và vòng quay được ẩn khỏi công cụ thống kê. Nếu bạn tạo liên kết chia sẻ, các lựa chọn nằm ngay trong liên kết (được mã hóa dạng ký tự, không phải mã hóa bảo mật), nên ai có liên kết cũng đọc được: đừng chia sẻ danh sách có thông tin riêng tư."},
  {"h2": "Ai đứng sau Wheelova", "body":
   "Wheelova là trang web độc lập cung cấp các công cụ ngẫu nhiên miễn phí. Nội dung do Sajid Ali, biên tập viên Wheelova, viết và kiểm tra; các thông tin về tính ngẫu nhiên dựa trên tài liệu của MDN và nghiên cứu của chính chúng tôi, có công bố dữ liệu mở. Nếu bạn thấy lỗi, hãy gửi email đến [support@wheelova.com](mailto:support@wheelova.com)."}
 ],
 "faq": [
  {"q": "Vòng quay may mắn có thật sự ngẫu nhiên không?", "a": "Có. Vòng quay dùng bộ sinh số an toàn về mặt mật mã của trình duyệt (crypto.getRandomValues), và trong thử nghiệm 1.000.000 lượt quay mỗi vòng, không có dấu hiệu thiên lệch."},
  {"q": "Làm sao để tạo vòng quay may mắn?", "a": "Nhập các lựa chọn, mỗi dòng một lựa chọn, hoặc nhập tệp CSV. Trong Cài đặt, chọn màu, tốc độ và tiêu đề kết quả. Lưu lại với một cái tên hoặc chia sẻ bằng liên kết."},
  {"q": "Có miễn phí không? Có cần đăng ký không?", "a": "Hoàn toàn miễn phí, không cần tài khoản và không cần tải ứng dụng."},
  {"q": "Làm sao để một kết quả không ra hai lần?", "a": "Bật «Loại kết quả sau mỗi lượt quay», hoặc bấm «Loại khỏi vòng quay» trong cửa sổ kết quả."},
  {"q": "Vòng quay có bị gian lận không?", "a": "Không có cài đặt ẩn nào. Cách duy nhất để thay đổi tỉ lệ là nhập một lựa chọn nhiều lần, và ai cũng thấy điều đó trong danh sách."},
  {"q": "Có thể nhập bao nhiêu lựa chọn?", "a": "Không giới hạn cố định. Khoảng 50 lựa chọn vẫn đọc rõ trên máy chiếu; liên kết chia sẻ chứa được tới 1.000 lựa chọn."},
  {"q": "Có dùng để quay số trúng thưởng trên livestream được không?", "a": "Được. Dán hoặc nhập danh sách người tham gia và quay trực tiếp, hoặc nhúng vòng quay vào OBS. Quy định về chương trình khuyến mại khác nhau tùy quốc gia và nền tảng, hãy kiểm tra quy định áp dụng cho bạn."},
  {"q": "Có dùng được trên điện thoại không?", "a": "Có, trên mọi trình duyệt hiện đại. Trên iPhone, mở Safari, bấm Chia sẻ → Thêm vào MH chính để mở như một ứng dụng."}
 ],
 "related": [],
 "sources": [S_MDN],
},
]
