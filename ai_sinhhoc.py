import streamlit as st

# =====================================
# 🤖 Chatbot AI Sinh học Tổng Hợp (THPT + Nâng cao)
# =====================================

sinhhoc = {
    # ===== PHÂN TỬ SINH HỌC =====
    "phan tu sinh hoc": {
        "adn": "ADN là vật chất di truyền, mang thông tin di truyền và quyết định tính trạng sinh vật.",
        "adn cau truc": "ADN có cấu trúc xoắn kép, gồm các nucleotide với base A - T và G - C bắt cặp bổ sung.",
        "arn": "ARN tham gia tổng hợp protein, có nhiều loại: mARN, tARN, rARN.",
        "arn cau truc": "ARN thường là sợi đơn, base gồm A, U, G, C (U thay cho T).",

        "protein": "Protein là đại phân tử cấu tạo từ các axit amin, tham gia nhiều chức năng sống.",
        "protein bac 1": "Cấu trúc bậc 1: chuỗi polypeptit các axit amin nối với nhau.",
        "protein bac 2": "Cấu trúc bậc 2: hình thành xoắn α và gấp nếp β nhờ liên kết hidro.",
        "protein bac 3": "Cấu trúc bậc 3: xoắn gấp không gian ba chiều đặc trưng.",
        "protein bac 4": "Cấu trúc bậc 4: nhiều chuỗi polypeptit kết hợp thành một protein hoàn chỉnh.",

        "carbohydrate": "Carbohydrate là nguồn năng lượng chính và tham gia cấu tạo tế bào.",
        "monosaccharide": "Monosaccharide: đường đơn (glucose, fructose, galactose).",
        "disaccharide": "Disaccharide: đường đôi (sucrose, lactose, maltose).",
        "polysaccharide": "Polysaccharide: tinh bột, glycogen, cellulose, kitin.",

        "lipid": "Lipid là hợp chất hữu cơ không tan trong nước, cấu tạo màng và dự trữ năng lượng.",
        "lipid don gian": "Lipid đơn giản: mỡ, dầu (glycerol + acid béo).",
        "phospholipid": "Phospholipid: cấu tạo màng sinh chất (đầu ưa nước, đuôi kỵ nước).",
        "steroid": "Steroid: cholesterol, hormone steroid (estrogen, testosterone).",

        "nucleotide": "Nucleotide gồm: đường (ribose/deoxyribose), nhóm phosphate và base nitơ.",
        "base nito": "Base nitơ gồm 2 loại: purin (A, G) và pyrimidin (T, C, U).",
    },

    # ===== QUÁ TRÌNH DI TRUYỀN (THPT) =====
    "qua trinh di truyen": {
        "nhan doi adn": {
            "tong quan": "Nhân đôi ADN tạo ra hai phân tử ADN giống hệt từ một phân tử ADN ban đầu, diễn ra ở pha S.",
            "co che": "Cơ chế bán bảo tồn: mỗi phân tử ADN con gồm 1 mạch cũ và 1 mạch mới.",
            "buoc": "1. Mở xoắn nhờ helicase.\n2. ADN polymerase gắn nucleotide theo NTBS (A-T, G-X).\n3. Mạch 3'→5' tổng hợp liên tục, mạch 5'→3' tổng hợp gián đoạn (đoạn Okazaki).\n4. Ligase nối các đoạn Okazaki.",
            "ket qua": "Tạo 2 phân tử ADN con giống ADN mẹ."
        },
        "phien ma": {
            "tong quan": "Phiên mã là tổng hợp ARN dựa trên khuôn mẫu ADN, diễn ra trong nhân (sinh vật nhân thực).",
            "buoc": "1. Mở xoắn ADN tại gen cần phiên mã.\n2. ARN polymerase lắp nucleotide theo NTBS (A-U, T-A, G-X, X-G).\n3. ARN kéo dài theo chiều 5'→3'.\n4. ARN hoàn thành, tách khỏi ADN.",
            "ket qua": "Tạo ARN (mARN chủ yếu). Ở sinh vật nhân thực, mARN được xử lý: gắn mũ 5’, đuôi poly-A, cắt intron."
        },
        "dich ma": {
            "tong quan": "Dịch mã là tổng hợp chuỗi polipeptit (protein) dựa trên thông tin mARN, diễn ra ở ribosome.",
            "buoc": "1. Khởi đầu: mARN gắn vào ribosome, tARN mang Met khớp AUG.\n2. Kéo dài: tARN mang aa đến, ribosome nối aa bằng liên kết peptit.\n3. Kết thúc: gặp codon kết thúc (UAA, UAG, UGA), chuỗi polipeptit giải phóng.",
            "ket qua": "Tạo chuỗi polipeptit → gấp cuộn thành protein."
        }
    },

    # ===== CẤU TRÚC TẾ BÀO =====
    "te bao": {
        "tong quan": "Tế bào là đơn vị cấu tạo và chức năng cơ bản của sự sống.",
        "nhan so": "Tế bào nhân sơ (prokaryote): không có nhân thật, ADN vòng nằm ở vùng nhân.",
        "nhan thuc": "Tế bào nhân thực (eukaryote): có nhân thật sự bao bởi màng nhân.",

        "te bao dong vat": {
            "mang sinh chat": "Bao quanh tế bào, kiểm soát trao đổi chất.",
            "nhan te bao": "Chứa ADN và điều khiển mọi hoạt động.",
            "ti the": "Ti thể hô hấp hiếu khí, tạo ATP.",
            "ribosome": "Tổng hợp protein.",
            "bo may golgi": "Chế biến, đóng gói và vận chuyển sản phẩm.",
            "lysosome": "Tiêu hóa nội bào, phá hủy bào quan hỏng.",
            "khung xuong te bao": "Giữ hình dạng và vận chuyển nội bào."
        },
        "te bao thuc vat": {
            "mang sinh chat": "Điều khiển trao đổi chất.",
            "thanh te bao": "Bằng cellulose, giúp tế bào cứng cáp.",
            "nhan te bao": "Điều khiển hoạt động sống.",
            "luc lap": "Chứa diệp lục, nơi diễn ra quang hợp.",
            "ti the": "Tạo ATP qua hô hấp tế bào.",
            "ribosome": "Tổng hợp protein.",
            "bo may golgi": "Chế biến và vận chuyển sản phẩm.",
            "khong bao": "Không bào trung tâm lớn, điều hòa áp suất và dự trữ chất."
        },
        "vi khuan": {
            "mang sinh chat": "Kiểm soát trao đổi chất.",
            "thanh te bao": "Peptidoglycan tạo thành vách cứng.",
            "roi": "Giúp vi khuẩn di chuyển.",
            "pili": "Giúp vi khuẩn bám dính và trao đổi gen.",
            "ribosome": "Ribosome 70S tổng hợp protein.",
            "vung nhan": "Chứa ADN dạng vòng.",
            "bao tu": "Một số loài tạo bào tử để tồn tại khi khắc nghiệt."
        },
        "nam": {
            "thanh te bao": "Chủ yếu cấu tạo từ kitin.",
            "ti the": "Tạo năng lượng ATP.",
            "ribosome": "Tổng hợp protein.",
            "bo may golgi": "Chế biến và vận chuyển.",
            "khong bao": "Dự trữ và điều hòa áp suất.",
            "mang sinh chat": "Kiểm soát trao đổi chất.",
            "nhan te bao": "Chứa ADN, có màng nhân bao bọc."
        }
    },

    # ===== QUANG HỢP =====
    "quang hop": {
        "tong quan": "Quang hợp là quá trình cây xanh, tảo, vi khuẩn lam dùng ánh sáng mặt trời để tạo glucose và O2.",
        "la xanh": "Lá xanh là cơ quan chính quang hợp.",
        "luc lap": "Lục lạp chứa diệp lục, nơi diễn ra quang hợp.",
        "diep luc": "Sắc tố hấp thụ ánh sáng đỏ và xanh lam.",
        "pha sang": "Pha sáng: diễn ra ở tilacoit, tạo ATP, NADPH và O2.",
        "pha toi": "Pha tối (chu trình Calvin): diễn ra ở chất nền (stroma), sử dụng ATP, NADPH để tổng hợp glucose."
    }
}


# === CHATBOT CHẠY TRÊN STREAMLIT ===
st.title("🤖 AI Sinh học tổng hợp (cấp 3 + nâng cao)")
cauhoi = st.text_input("Bạn hãy nhập câu hỏi về Sinh học (hoặc gõ 'thoat' để thoát):")

if st.button("Hỏi"):
    if cauhoi.lower() == "thoat":
        st.write("AI: Hẹn gặp lại nhé!")
    else:
        found = False
        for nhom, chitiet in sinhhoc.items():
            if isinstance(chitiet, dict):
                for key, value in chitiet.items():
                    if isinstance(value, dict):
                        for subkey, subval in value.items():
                            if subkey in cauhoi.lower() or key in cauhoi.lower() or nhom in cauhoi.lower():
                                st.write(f"**AI ({subkey})**: {subval}")
                                found = True
                    else:
                        if key in cauhoi.lower() or nhom in cauhoi.lower():
                            st.write(f"**AI ({key})**: {value}")
                            found = True
            else:
                if nhom in cauhoi.lower():
                    st.write(f"**AI ({nhom})**: {chitiet}")
                    found = True

        if not found:
            st.write("AI: Xin lỗi, tôi chưa có kiến thức về điều này.")
