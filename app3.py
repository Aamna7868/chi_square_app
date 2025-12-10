import streamlit as st
import scipy.stats as stats

# ---------------- App Title ----------------
st.title("📊 Chi-Square Goodness of Fit Test - Detailed Explanation")

# ---------------- Question / Data ----------------
st.header("Problem Statement / Question")
st.write("""
Suppose a study records the number of patients suffering from a certain disease in different age groups in a city.
We want to check if the observed data fits the expected distribution.

**Data:**

| Age Group | Observed Cases | Expected Cases |
|-----------|----------------|----------------|
| 0-10      | 50             | 60             |
| 11-20     | 80             | 70             |
| 21-30     | 120            | 110            |
| 31-40     | 90             | 100            |
| 41-50     | 60             | 60             |

**Hypotheses:**

- **Null Hypothesis (H₀):** The observed data fits the expected distribution.  
- **Alternative Hypothesis (H₁):** The observed data does not fit the expected distribution.
""")

# ---------------- Module 1: Data Input ----------------
st.header("Module 1: Input Data")
st.write("You can also enter your own data as **comma-separated values**.")

# Input boxes for observed and expected values
observed = st.text_input("Observed values (comma-separated)", "50,80,120,90,60")
expected = st.text_input("Expected values (comma-separated)", "60,70,110,100,60")

# Significance level slider
alpha = st.slider("Significance Level (α)", 0.01, 0.10, 0.05)

# ---------------- Module 2: Chi-Square Calculation & Conclusion ----------------
if st.button("Run Chi-Square Test"):
    st.header("Module 2: Calculation & Conclusion")
    try:
        # Convert comma-separated strings to lists of integers
        obs = list(map(int, observed.split(",")))
        exp = list(map(int, expected.split(",")))

        if len(obs) != len(exp):
            st.error("⚠ Observed and Expected values must have the same number of elements.")
        else:
            st.subheader("Step 1: Step-by-Step Calculation of Chi-Square Contributions")
            contributions = []
            for i, (o, e) in enumerate(zip(obs, exp), start=1):
                c = (o - e)**2 / e
                contributions.append(c)
                st.write(f"Group {i}: ((Observed - Expected)² / Expected) = (({o}-{e})² / {e}) = {c:.4f}")

            chi2 = sum(contributions)
            df = len(obs) - 1
            p_value = 1 - stats.chi2.cdf(chi2, df)

            st.subheader("Step 2: Chi-Square Statistic & P-Value")
            st.write(f"**Chi-Square Statistic = Σ((O-E)²/E) = {chi2:.4f}**")
            st.write(f"**Degrees of Freedom = {df}**")
            st.write(f"**P-Value = {p_value:.4f}**")

            st.subheader("Step 3: Hypothesis Decision")
            st.write(f"Significance Level (α) = {alpha}")
            if p_value < alpha:
                st.error("❌ Reject Null Hypothesis (H₀): Observed data does NOT fit the expected distribution.")
                st.write("✅ Therefore, we accept the Alternative Hypothesis (H₁).")
            else:
                st.success("✔ Fail to Reject Null Hypothesis (H₀): Observed data fits the expected distribution.")
                st.write("✅ Therefore, the Null Hypothesis (H₀) is accepted.")

            st.subheader("Step 4: Conclusion")
            st.write("""
Based on the Chi-Square test:
- Each group’s contribution to the Chi-Square statistic was calculated.
- The total Chi-Square value and P-value were compared with the chosen significance level.
- This determines which hypothesis is accepted.
""")

    except:
        st.warning("⚠ Please enter valid numeric values separated by commas (e.g., 50,80,120,90,60).")
