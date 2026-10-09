# 📦 OptiPack: Packaging & Logistics Cost Optimization with Calculus
*Calculus ile Koli & Lojistik Maliyet Optimizasyonu*

[🇬🇧 English Version](#english) | [🇹🇷 Türkçe Versiyon](#turkce-versiyon)

---
<a id="english"></a>
## English

OptiPack is an interactive analytical simulation tool designed to minimize packaging dimensions and logistics freight costs using **Multivariable Calculus** and **Constrained Optimization** techniques.

### 🚀 Key Features
- **Analytical Optimization:** Identifies the global minimum dimensions ($x^*, y^*, h^*$) under a constant target volume ($V$) constraint via 1st and 2nd derivative tests.
- **Flexible Geometries:** Supports both square base ($k = 1$) and custom aspect ratio rectangular bases ($y = kx$).
- **Financial Impact & ROI:** Quantifies unit and annual cost savings by comparing current box dimensions against the mathematically optimal configuration.
- **Interactive Visualizations:** Renders real-time 3D parametric boxes and convex cost curves powered by Plotly.
- **Rigorous Proof:** Features a comprehensive 6-step analytical derivation and convexity verification.
- **Bilingual Interface:** Instant language switching between English and Turkish.

### 📐 Mathematical Formulation
Given target volume $V$, aspect ratio $y = kx$, base cost $c_1$, and side wall cost $c_2$:

$$\text{Objective Cost Function: } C(x) = 2 c_1 k x^2 + \frac{2 c_2 (1 + k)V}{k x}$$

Setting the first derivative to zero ($\frac{dC}{dx} = 0$) yields the unique global minimum:

$$x^* = \sqrt[3]{\frac{(1 + k) c_2 V}{2 c_1 k^2}}, \quad y^* = k \cdot x^*, \quad h^* = \frac{V}{k (x^*)^2}$$

### 🛠️ Tech Stack
- **Python 3.x**
- **Streamlit** (Interactive Web UI)
- **Plotly** (Dynamic 3D Simulation & Convex Curves)
- **NumPy & SciPy & SymPy** (Numerical & Analytical Computation)

### 💻 Local Setup & Execution
1. Clone the repository:
   ```bash
   git clone [https://github.com/pinarkirbasoglu/optipack-calculus.git](https://github.com/pinarkirbasoglu/optipack-calculus.git)
   cd optipack-calculus

---

<a id="turkce-versiyon"></a>
## Türkçe Versiyon

OptiPack; paketleme boyutlarını ve lojistik navlun masraflarını **Çok Değişkenli Analiz (Multivariable Calculus)** ve **Kısıtlı Optimizasyon** tekniklerini kullanarak en aza indirmek için tasarlanmış etkileşimli bir analitik simülasyon aracıdır.

### 🚀 Temel Özellikler
- **Analitik Optimizasyon:** Sabit hedef hacim ($V$) kısıtı altında, 1. ve 2. türev testleri aracılığıyla küresel minimum boyutları ($x^*, y^*, h^*$) belirler.
- **Esnek Geometriler:** Hem kare tabanlı ($k = 1$) hem de istenen en-boy oranına sahip dikdörtgen tabanlı ($y = kx$) kutu tasarımlarını destekler.
- **Finansal Etki ve Yatırım Getirisi (ROI):** Mevcut kutu boyutları ile matematiksel olarak optimal olan yapılandırmayı karşılaştırarak birim ve yıllık maliyet tasarrufunu hesaplar.
- **Etkileşimli Görselleştirmeler:** Plotly altyapısıyla gerçek zamanlı parametrik 3D kutu modelleri ve dışbükey (konveks) maliyet eğrileri sunar.
- **Titiz Matematiksel İspat:** Kapsamlı 6 adımlı analitik türetme ve konvekslik (minimum nokta) doğrulamasını içerir.
- **Çift Dilli Arayüz:** Türkçe ve İngilizce dilleri arasında anında geçiş imkânı sağlar.

### 📐 Matematiksel Formülasyon
Hedef hacim $V$, en-boy oranı $y = kx$, taban malzeme birim maliyeti $c_1$ ve yan yüzey malzeme birim maliyeti $c_2$ verildiğinde:

$$\text{Hedef Maliyet Fonksiyonu: } C(x) = 2 c_1 k x^2 + \frac{2 c_2 (1 + k)V}{k x}$$

Birinci türevi sıfıra eşitlemek ($\frac{dC}{dx} = 0$), benzersiz küresel minimumu verir:

$$x^* = \sqrt[3]{\frac{(1 + k) c_2 V}{2 c_1 k^2}}, \quad y^* = k \cdot x^*, \quad h^* = \frac{V}{k (x^*)^2}$$

### 🛠️ Kullanılan Teknolojiler
- **Python 3.x**
- **Streamlit** (Etkileşimli Web Arayüzü)
- **Plotly** (Dinamik 3D Simülasyon ve Konveks Eğriler)
- **NumPy, SciPy & SymPy** (Sayısal ve Analitik Hesaplama)

### 💻 Yerel Kurulum ve Çalıştırma
1. Depoyu (repository) klonlayın:
```bash
git clone [https://github.com/pinarkirbasoglu/optipack-calculus.git](https://github.com/pinarkirbasoglu/optipack-calculus.git)
cd optipack-calculus