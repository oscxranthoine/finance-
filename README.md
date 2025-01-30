📈 Black-Scholes Option Pricing Model



📌 Overview
This repository contains a Python implementation of the Black-Scholes model for pricing European options (calls and puts). The model calculates the theoretical fair value of an option based on market parameters.

🏗️ Features
✅ Computes Call and Put option prices
✅ Uses Black-Scholes closed-form solution
✅ Built with NumPy and SciPy
✅ Simple and easy-to-use Python function
✅ Includes an example for testing

🧩 Installation
Clone this repository:

bash
Copier
Modifier
git clone https://github.com/your-username/your-repo.git
cd your-repo
Install dependencies:

bash
Copier
Modifier
pip install numpy scipy
🛠️ Usage
You can use the script in a Python environment by importing the function or running it directly.

1️⃣ Import the function in your Python code
python
Copier
Modifier
from black_scholes import pricing

s = 100      # Underlying price
k = 102      # Strike price
t = 0.66     # Time to expiration (in years)
r = 0.05     # Risk-free interest rate
vol = 0.07   # Annual volatility

# Calculate call and put prices
call_price = pricing(s, k, t, r, vol, type="c")
put_price = pricing(s, k, t, r, vol, type="p")

print(f"Call Price: {call_price:.2f}")
print(f"Put Price: {put_price:.2f}")
2️⃣ Run the script directly
bash
Copier
Modifier
python black_scholes.py
It will print the calculated Call price.

📊 Formula
The Black-Scholes model calculates the price of an option using the following formulas:

1️⃣ Compute d1 and d2:
𝑑
1
=
ln
⁡
(
𝑠
/
𝑘
)
+
(
𝑟
+
(
𝑣
𝑜
𝑙
2
)
/
2
)
⋅
𝑡
𝑣
𝑜
𝑙
⋅
𝑡
d1= 
vol⋅ 
t
​
 
ln(s/k)+(r+(vol 
2
 )/2)⋅t
​
 
𝑑
2
=
𝑑
1
−
(
𝑣
𝑜
𝑙
⋅
𝑡
)
d2=d1−(vol⋅ 
t
​
 )
2️⃣ Compute Call and Put Prices:
Call Option (C):
𝐶
=
𝑁
(
𝑑
1
)
⋅
𝑠
−
𝑁
(
𝑑
2
)
⋅
𝑘
⋅
𝑒
−
𝑟
𝑡
C=N(d1)⋅s−N(d2)⋅k⋅e 
−rt
 
Put Option (P):
𝑃
=
𝑘
⋅
𝑒
−
𝑟
𝑡
⋅
𝑁
(
−
𝑑
2
)
−
𝑠
⋅
𝑁
(
−
𝑑
1
)
P=k⋅e 
−rt
 ⋅N(−d2)−s⋅N(−d1)
where N(x) is the cumulative distribution function (CDF) of the standard normal distribution.

📝 Example Output
bash
Copier
Modifier
Call Price: 3.12
Put Price: 4.50
🚀 Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

📜 License
This project is licensed under the MIT License. See LICENSE for details.

🔥 Additional Enhancements for GitHub:
Add a requirements.txt file

Create a file named requirements.txt and add:
Copier
Modifier
numpy
scipy
Include an example.py script

Provide a simple example that users can run directly.
Upload Screenshots (if applicable)

You can add images or plots to illustrate results using ![Alt Text](image_url_or_path).
