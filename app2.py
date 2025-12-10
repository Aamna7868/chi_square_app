import streamlit as st
import scipy.stats as stats

st.title("🔍 Chi-Square Goodness of Fit Test")

# ---------------- Module 1: Data Input ----------------
st.header("Module 1: Input Data")
st.write("Enter observed and expected values for disease cases across groups.")

observed = st.text_input("Observed values (comma-separated)", "50,80,120,90,60")
expected = st.text_input("Expected values (comma-separated)", "60,70,110,100,60")
alpha = st.slider("Significance Level (α)", 0.01, 0.10, 0.05)

# ---------------- Module 2: Chi-Square Calculation ----------------
if st.button("Run Chi-Square Test"):
    st.header("Module 2: Test Calculation")
    try:
        obs = list(map(int, observed.split(",")))
        exp = list(map(int, expected.split(",")))

        if len(obs) != len(exp):
            st.error("⚠ Observed and Expected values must have the same number of elements.")
        else:
            # Step-by-step calculation
            contributions = [(o - e)**2 / e for o, e in zip(obs, exp)]
            
            st.subheader("Step-by-Step Calculation")
            for i, (o, e, c) in enumerate(zip(obs, exp, contributions), start=1):
                st.write(f"Group {i}: (({o} - {e})² / {e}) = {c:.4f}")
            
            chi2 = sum(contributions)
            p = 1 - stats.chi2.cdf(chi2, df=len(obs)-1)
            
            st.write(f"**Chi-Square Statistic (Σ((O-E)²/E)) = {chi2:.4f}**")
            st.write(f"**P-value = {p:.4f}**")

            # ---------------- Module 3: Hypothesis Decision ----------------
            st.header("Module 3: Hypothesis Decision")
            if p < alpha:
                st.error("❌ Reject Null Hypothesis: Data does NOT fit expected distribution.")
            else:
                st.success("✔ Fail to Reject Null Hypothesis: Data fits expected distribution.")

    except:
        st.warning("⚠ Enter valid numeric values separated by commas.")
