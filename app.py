import streamlit as st
import numpy as np
import plotly.graph_objects as go

# --- SÖZLÜK (TÜRKÇE / ENGLISH DICTIONARY) ---
TEXTS = {
    "TR": {
        "title": "📦 OptiPack: Dinamik Koli & Lojistik Optimizasyonu",
        "subtitle": "Bu uygulama, **Calculus (Türev ve Kısıtlı Optimizasyon)** kullanarak belirli bir ürün hacmini minimum hammadde ve lojistik maliyetiyle paketleyen en ideal boyutları hesaplar.",
        "lang_select": "Dil / Language",
        "section_1": "⚙️ 1. Problem Parametreleri",
        "vol_label": "Hedef Koli Hacmi (cm³):",
        "base_type_label": "Optimum Taban Geometrisi:",
        "opt_square": "Kare Taban (En Düşük Maliyet)",
        "opt_rect": "Dikdörtgen Taban (Hedef En/Boy Oranı)",
        "ratio_label": "Hedef En / Boy Oranı (y / x):",
        "ratio_caption": "Genişlik (y), derinliğin (x) {:.1f} katı olacaktır.",
        "cost_inputs": "Maliyet Girdileri (TL)",
        "base_cost": "Taban/Tavan Mukavva (TL / m²):",
        "side_cost": "Yan Yüzey Mukavva (TL / m²):",
        "ship_cost": "Desi Başı Kargo Ücreti (TL):",
        "section_2": "📊 2. Mevcut Koli Kıyaslaması",
        "user_x_square": "Mevcut Taban Kenarı (x cm):",
        "user_rect_title": "Mevcut Koli Boyutları:",
        "user_x_rect": "Derinlik (x cm):",
        "user_y_rect": "Genişlik (y cm):",
        "annual_boxes": "Yıllık Koli Üretim Adedi:",
        "opt_x": "Optimal Derinlik (x)",
        "opt_y": "Optimal Genişlik (y)",
        "opt_h": "Optimal Yükseklik (h)",
        "opt_cost": "Optimize Koli Maliyeti",
        "ratio_badge": "Oran: {:.1f}",
        "saving_alert": "💡 **Tasarruf Fırsatı:** Mevcut koli maliyetiniz **{:.2f} TL**, optimize koli **{:.2f} TL**.\n\nKoli başına **{:.2f} TL (%{:.1f})** tasarruf edebilirsiniz. Yıllık **{:,}** adet üretimde firmanıza net kazanç: **{:,.0f} TL**",
        "saving_optimal": "Kullandığınız koli boyutları zaten optimum noktaya çok yakın!",
        "chart_title": "📉 Calculus: Maliyet Eğrisi",
        "chart_opt_curve": "Optimum Eğrisi (Oran: {:.1f})",
        "chart_opt_pt": "Optimum (Türev = 0)",
        "chart_user_pt": "Sizin Koliniz",
        "chart_xaxis": "Derinlik x (cm)",
        "chart_yaxis": "Toplam Maliyet (TL)",
        "sim_title": "📦 3D Koli Karşılaştırması",
        "tab_proof": "📐 Matematiksel Model ve Analitik İspat (6 Adım)",
        "tab_guide": "📖 Grafiği ve Tasarrufu Nasıl Okumalısınız?",
        "guide_bullet_1": "* **Mavi Eğri:** Seçilen geometriye göre türetilen maliyet fonksiyonudur ($C(x)$).",
        "guide_bullet_2": "* **Kırmızı Nokta (Optimum):** Eğrinin en dip noktasıdır ($dC/dx = 0$). Hammadde ve lojistikte minimum maliyete ulaştığı kesin boyutlardır.",
        "guide_bullet_3": "* **Turuncu Elmas (Sizin Koliniz):** Şu anda kullandığınız koli boyutlarının maliyet seviyesini temsil eder.",
        "guide_bullet_4": "* **Aralarındaki Düşey Fark:** Koli başına ödenen israftır. Yıllık üretim hacmiyle çarpıldığında net finansal kaybı gösterir.",
        "proof_step1_title": "### 1. Problemin ve Değişkenlerin Tanımı",
        "proof_step1_text": "Kapalı bir dikdörtgenler prizması şeklindeki kolinin boyutları ve parametreleri:\n- **Derinlik:** $x$\n- **Genişlik:** $y$\n- **Yükseklik:** $h$\n- **Hedef Hacim:** $V$ (sabit skaler kısıt)\n- **Taban/Tavan Birim Fiyatı:** $c_1$ (TL/m²)\n- **Yan Yüzey Birim Fiyatı:** $c_2$ (TL/m²)\n\nTaban en/boy oranı $k$ katsayısına bağlıdır ($k > 0$):",
        "proof_step2_title": "### 2. Kısıt Fonksiyonu ve Değişken İndirgeme",
        "proof_step2_text": "Kolinin hacim denklemi $V = x \\cdot y \\cdot h$. $y = kx$ yazarak yüksekliği ($h$) serbest değişken olan $x$ cinsinden ifade ederiz:",
        "proof_step3_title": "### 3. Toplam Maliyet Fonksiyonunun Kurulması",
        "proof_step3_text": "Koli 6 kapalı yüzeyden oluşur:\n- **Taban ve Tavan:** $\\text{Alan} = 2kx^2$, $\\text{Maliyet} = 2 c_1 k x^2$\n- **Yan Yüzeyler:** $\\text{Alan} = 2(1 + k)xh = \\frac{2(1 + k)V}{kx}$, $\\text{Maliyet} = \\frac{2 c_2 (1 + k)V}{kx}$\n- **Hedef Maliyet Fonksiyonu $C(x)$:**",
        "proof_step4_title": "### 4. Kritik Noktanın Bulunması (Birinci Türev Testi)",
        "proof_step4_text": "$C(x)$ fonksiyonunun $x$'e göre birinci türevini alıp sıfıra eşitliyoruz ($dC/dx = 0$):",
        "proof_step5_title": "### 5. Minimum Noktası Doğrulaması (İkinci Türev Testi)",
        "proof_step5_text": "Kritik noktanın mutlak minimum olduğunu doğrulamak için ikinci türevi inceleriz. Tüm fiziksel parametreler pozitif ($x, k, V, c_1, c_2 > 0$) olduğu için $d^2C/dx^2 > 0$ daima sağlanır; eğri kesin dışbükeydir (strictly convex) ve bulunan nokta global minimumdur.",
        "proof_step6_title": "### 6. Özel Durum Kontrolü (Kare Taban Tutarlılığı)",
        "proof_step6_text": "$k = 1$ alındığında kare taban çözümü $x^* = \\sqrt[3]{\\frac{c_2}{c_1} V}$ doğrudan elde edilir ve formülün tutarlılığı teyit edilir."
    },
    "EN": {
        "title": "📦 OptiPack: Dynamic Packaging & Logistics Optimization",
        "subtitle": "This application uses **Calculus (Derivatives & Constrained Optimization)** to determine the optimal box dimensions that minimize raw material and logistics shipping costs for a target volume.",
        "lang_select": "Language / Dil",
        "section_1": "⚙️ 1. Problem Parameters",
        "vol_label": "Target Box Volume (cm³):",
        "base_type_label": "Optimal Base Geometry:",
        "opt_square": "Square Base (Lowest Cost)",
        "opt_rect": "Rectangular Base (Target Aspect Ratio)",
        "ratio_label": "Aspect Ratio (y / x):",
        "ratio_caption": "Width (y) will be {:.1f}x of depth (x).",
        "cost_inputs": "Cost Inputs",
        "base_cost": "Base/Top Corrugated Board ($ / m²):",
        "side_cost": "Side Walls Corrugated Board ($ / m²):",
        "ship_cost": "Shipping Rate per Volumetric Weight ($):",
        "section_2": "📊 2. Current Box Comparison",
        "user_x_square": "Current Base Edge (x cm):",
        "user_rect_title": "Current Box Dimensions:",
        "user_x_rect": "Depth (x cm):",
        "user_y_rect": "Width (y cm):",
        "annual_boxes": "Annual Box Production Volume:",
        "opt_x": "Optimal Depth (x)",
        "opt_y": "Optimal Width (y)",
        "opt_h": "Optimal Height (h)",
        "opt_cost": "Optimized Box Cost",
        "ratio_badge": "Ratio: {:.1f}",
        "saving_alert": "💡 **Cost Saving Opportunity:** Current box cost is **{:.2f}**, optimized box is **{:.2f}**.\n\nYou can save **{:.2f} ({:.1f}%)** per box. Annual net savings for **{:,}** units: **{:,.0f}**",
        "saving_optimal": "Your current box dimensions are already very close to the global optimum!",
        "chart_title": "📉 Calculus: Cost Curve & Derivative Point",
        "chart_opt_curve": "Optimal Cost Curve (Ratio: {:.1f})",
        "chart_opt_pt": "Optimum (dC/dx = 0)",
        "chart_user_pt": "Your Current Box",
        "chart_xaxis": "Depth x (cm)",
        "chart_yaxis": "Total Unit Cost",
        "sim_title": "📦 3D Box Simulation",
        "tab_proof": "📐 Mathematical Model & Analytical Proof (6 Steps)",
        "tab_guide": "📖 How to Read the Chart & Savings",
        "guide_bullet_1": "* **Blue Curve:** Total cost function derived from packaging geometry ($C(x)$).",
        "guide_bullet_2": "* **Red Dot (Global Optimum):** Trough of the curve ($dC/dx = 0$) where material and logistics expenses are minimized.",
        "guide_bullet_3": "* **Orange Diamond (Your Box):** Cost level of your current packaging specifications.",
        "guide_bullet_4": "* **Vertical Gap:** Marginal waste per unit. Multiplying this by annual volume reveals the total financial opportunity loss.",
        "proof_step1_title": "### 1. Problem Formulation & Variables",
        "proof_step1_text": "Closed rectangular cuboid packaging dimensions and constants:\n- **Depth:** $x$\n- **Width:** $y$\n- **Height:** $h$\n- **Target Volume:** $V$ (constant scalar constraint)\n- **Base/Top Board Price:** $c_1$\n- **Side Walls Board Price:** $c_2$\n\nBase aspect ratio is governed by positive multiplier $k$ ($k > 0$):",
        "proof_step2_title": "### 2. Constraint Function & Dimension Reduction",
        "proof_step2_text": "Box volume equation is $V = x \\cdot y \\cdot h$. Substituting $y = kx$ expresses height ($h$) in terms of single independent variable $x$:",
        "proof_step3_title": "### 3. Total Cost Function Formulation",
        "proof_step3_text": "The box comprises 6 enclosed surfaces:\n- **Base & Top:** $\\text{Area} = 2kx^2$, $\\text{Cost} = 2 c_1 k x^2$\n- **Side Walls:** $\\text{Area} = 2(1 + k)xh = \\frac{2(1 + k)V}{kx}$, $\\text{Cost} = \\frac{2 c_2 (1 + k)V}{kx}$\n- **Objective Cost Function $C(x)$:**",
        "proof_step4_title": "### 4. Critical Point Identification (First Derivative Test)",
        "proof_step4_text": "We compute the first derivative of $C(x)$ with respect to $x$ and set it to zero ($dC/dx = 0$):",
        "proof_step5_title": "### 5. Minimum Verification (Second Derivative Test)",
        "proof_step5_text": "Evaluating $d^2C/dx^2$: since all physical parameters are strictly positive ($x, k, V, c_1, c_2 > 0$), $d^2C/dx^2 > 0$ universally holds. The cost function is strictly convex, confirming $x^*$ as the global minimum.",
        "proof_step6_title": "### 6. Special Case Verification (Square Base Consistency)",
        "proof_step6_text": "Setting $k = 1$ yields $x^* = \\sqrt[3]{\\frac{c_2}{c_1} V}$, perfectly reproducing the single-variable square base optimum."
    }
}

st.set_page_config(
    page_title="OptiPack - Packaging Cost Optimization",
    page_icon="📦",
    layout="wide"
)

# --- DİL SEÇİMİ (SIDEBAR EN ÜST) ---
lang = st.sidebar.radio("🌐 Language / Dil", ["🇹🇷 Türkçe", "🇬🇧 English"])
t = TEXTS["TR"] if "Türkçe" in lang else TEXTS["EN"]

st.title(t["title"])
st.markdown(t["subtitle"])

# --- YAN PANEL: PARAMETRELER ---
st.sidebar.header(t["section_1"])

target_volume = st.sidebar.slider(
    t["vol_label"], 
    min_value=2000, 
    max_value=60000, 
    value=18000, 
    step=1000
)

base_type = st.sidebar.radio(
    t["base_type_label"], 
    [t["opt_square"], t["opt_rect"]]
)

if base_type == t["opt_square"]:
    k_ratio = 1.0
else:
    k_ratio = st.sidebar.slider(t["ratio_label"], min_value=1.1, max_value=3.0, value=1.5, step=0.1)
    st.sidebar.caption(t["ratio_caption"].format(k_ratio))

st.sidebar.subheader(t["cost_inputs"])
c_base = st.sidebar.number_input(t["base_cost"], value=30.0, step=1.0)
c_side = st.sidebar.number_input(t["side_cost"], value=18.0, step=1.0)
shipping_rate = st.sidebar.number_input(t["ship_cost"], value=10.0, step=0.5)

# --- MEVCUT KOLİ KIYASLAMASI ---
st.sidebar.header(t["section_2"])

if base_type == t["opt_square"]:
    user_x = st.sidebar.number_input(t["user_x_square"], value=14.0, step=1.0)
    user_y = user_x
else:
    st.sidebar.write(t["user_rect_title"])
    col_u1, col_u2 = st.sidebar.columns(2)
    with col_u1:
        user_x = col_u1.number_input(t["user_x_rect"], value=14.0, step=1.0)
    with col_u2:
        user_y = col_u2.number_input(t["user_y_rect"], value=22.0, step=1.0)

annual_boxes = st.sidebar.number_input(t["annual_boxes"], value=50000, step=5000)

# --- CALCULUS OPTİMUM ÇÖZÜCÜ ---
# x* = ( (1 + k) * c2 * V / (2 * c1 * k^2) )^(1/3)
optimal_x = (((1 + k_ratio) * c_side * target_volume) / (2 * c_base * (k_ratio ** 2))) ** (1 / 3)
optimal_y = optimal_x * k_ratio
optimal_h = target_volume / (optimal_x * optimal_y)

# Optimal Maliyet Hesaplama
opt_base_area = (2 * optimal_x * optimal_y) / 10000
opt_side_area = (2 * optimal_x * optimal_h + 2 * optimal_y * optimal_h) / 10000
opt_material_cost = (opt_base_area * c_base) + (opt_side_area * c_side)

desi = target_volume / 3000
shipping_cost = desi * shipping_rate
opt_total_cost = opt_material_cost + shipping_cost

# Mevcut Koli Maliyeti Hesaplama
user_h = target_volume / (user_x * user_y) if (user_x * user_y) > 0 else 1
user_base_area = (2 * user_x * user_y) / 10000
user_side_area = (2 * user_x * user_h + 2 * user_y * user_h) / 10000
user_total_cost = (user_base_area * c_base) + (user_side_area * c_side) + shipping_cost

diff_per_box = user_total_cost - opt_total_cost
annual_saving = max(0.0, diff_per_box * annual_boxes)
saving_percent = (diff_per_box / user_total_cost) * 100 if user_total_cost > 0 else 0

# --- METRİK KARTLARI ---
col1, col2, col3, col4 = st.columns(4)
col1.metric(t["opt_x"], f"{optimal_x:.2f} cm")
col2.metric(t["opt_y"], f"{optimal_y:.2f} cm", delta=t["ratio_badge"].format(k_ratio))
col3.metric(t["opt_h"], f"{optimal_h:.2f} cm")
col4.metric(t["opt_cost"], f"{opt_total_cost:.2f}")

# Tasarruf Kartı
if diff_per_box > 0.05:
    st.success(t["saving_alert"].format(user_total_cost, opt_total_cost, diff_per_box, saving_percent, annual_boxes, annual_saving))
else:
    st.info(t["saving_optimal"])

st.divider()

# --- GRAFİK VE 3D SİMÜLASYON ---
left_col, right_col = st.columns([1, 1])

with left_col:
    st.subheader(t["chart_title"])
    
    x_min = max(5.0, min(optimal_x, user_x) - 10)
    x_max = max(optimal_x, user_x) + 15
    x_vals = np.linspace(x_min, x_max, 250)
    
    y_vals = x_vals * k_ratio
    h_vals = target_volume / (x_vals * y_vals)
    b_areas = (2 * x_vals * y_vals) / 10000
    s_areas = (2 * x_vals * h_vals + 2 * y_vals * h_vals) / 10000
    costs = (b_areas * c_base) + (s_areas * c_side) + shipping_cost

    fig_cost = go.Figure()
    fig_cost.add_trace(go.Scatter(
        x=x_vals, y=costs, 
        mode='lines', 
        name=t["chart_opt_curve"].format(k_ratio), 
        line=dict(color='#2563eb', width=3)
    ))
    
    # Optimum nokta
    fig_cost.add_trace(go.Scatter(
        x=[optimal_x], y=[opt_total_cost], 
        mode='markers+text', 
        name=t["chart_opt_pt"],
        marker=dict(color='#dc2626', size=13),
        text=[f"Opt: {optimal_x:.1f} cm"],
        textposition="top center"
    ))
    
    # Mevcut koli noktası
    fig_cost.add_trace(go.Scatter(
        x=[user_x], y=[user_total_cost], 
        mode='markers+text', 
        name=t["chart_user_pt"],
        marker=dict(color='#f97316', size=13, symbol='diamond'),
        text=[f"Cur: {user_x:.1f} cm"],
        textposition="bottom center"
    ))
    
    fig_cost.update_layout(
        xaxis_title=t["chart_xaxis"], 
        yaxis_title=t["chart_yaxis"], 
        template="plotly_white",
        margin=dict(l=20, r=20, t=30, b=20)
    )
    st.plotly_chart(fig_cost, use_container_width=True)

with right_col:
    st.subheader(t["sim_title"])
    
    xb, yb, zb = optimal_x, optimal_y, optimal_h

    fig_3d = go.Figure(data=[
        go.Mesh3d(
            x=[0, xb, xb, 0, 0, xb, xb, 0],
            y=[0, 0, yb, yb, 0, 0, yb, yb],
            z=[0, 0, 0, 0, zb, zb, zb, zb],
            i=[7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
            j=[3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
            k=[0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
            opacity=0.65,
            color='#3b82f6',
            flatshading=True
        )
    ])
    fig_3d.update_layout(
        scene=dict(
            xaxis_title=f"{t['opt_x']} (cm)", 
            yaxis_title=f"{t['opt_y']} (cm)", 
            zaxis_title=f"{t['opt_h']} (cm)", 
            aspectmode='data'
        ),
        margin=dict(l=10, r=10, t=10, b=10)
    )
    st.plotly_chart(fig_3d, use_container_width=True)

# --- REHBER VE MATEMATİKSEL İSPAT BÖLÜMÜ ---
st.divider()

tab_ispat, tab_rehber = st.tabs([t["tab_proof"], t["tab_guide"]])

with tab_ispat:
    st.markdown(t["proof_step1_title"])
    st.markdown(t["proof_step1_text"])
    st.latex(r"y = k \cdot x")

    st.markdown(t["proof_step2_title"])
    st.markdown(t["proof_step2_text"])
    st.latex(r"V = x \cdot (kx) \cdot h = k x^2 h \implies h = \frac{V}{k x^2}")

    st.markdown(t["proof_step3_title"])
    st.markdown(t["proof_step3_text"])
    st.latex(r"C(x) = 2 c_1 k x^2 + \frac{2 c_2 (1 + k)V}{k} x^{-1}")

    st.markdown(t["proof_step4_title"])
    st.markdown(t["proof_step4_text"])
    st.latex(r"\frac{dC}{dx} = 4 c_1 k x - \frac{2 c_2 (1 + k)V}{k} x^{-2} = 0")
    st.latex(r"x^* = \sqrt[3]{\frac{(1 + k) c_2 V}{2 c_1 k^2}}")
    st.latex(r"y^* = k \cdot x^* \quad \text{and} \quad h^* = \frac{V}{k (x^*)^2}")

    st.markdown(t["proof_step5_title"])
    st.markdown(t["proof_step5_text"])
    st.latex(r"\frac{d^2C}{dx^2} = 4 c_1 k + \frac{4 c_2 (1 + k)V}{k x^3} > 0 \quad (\forall x > 0)")

    st.markdown(t["proof_step6_title"])
    st.markdown(t["proof_step6_text"])
    st.latex(r"x^* = \sqrt[3]{\frac{(1 + 1) c_2 V}{2 c_1 (1)^2}} = \sqrt[3]{\frac{c_2}{c_1} V}")

with tab_rehber:
    st.markdown(f"""
    {t['guide_bullet_1']}
    {t['guide_bullet_2']}
    {t['guide_bullet_3']}
    {t['guide_bullet_4']}
    """)