# ShapeshiftPy

A high-performance, deterministic 2D and 3D geometric shape generation and rendering engine built using pure numerical matrix manipulations with NumPy and Matplotlib. 

ShapeshiftPy bypasses high-level computer vision and graphic framework shortcuts (like OpenCV drawing primitives). Instead, it maps complex geometric spaces entirely from scratch using vectorized linear algebra, algebraic distance inequalities, and coordinate transformations.

---

## Core Tech Stack

- **Python 3.11+** - Primary systems interface.
- **NumPy** - Used for speed and organization.
- **Matplotlib** - Coordinate space plotting and boundary verification.

---

## Installation & Local Deployment

1. **Clone the Repository:**
   ```bash
   git clone https://github.com
   cd ShapeshiftPy
   ```

2. **Initialize and Activate Your Environment:**
   ```powershell
   # Windows PowerShell
   python -m venv .basicnumpy
   .\.basicnumpy\Scripts\Activate.ps1
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch the Engine:**
   ```bash
   python main.py
   ```
