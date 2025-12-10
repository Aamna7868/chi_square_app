import streamlit as st
import scipy.stats as stats

st.title("🔍 Chi-Square Goodness of Fit Test")

st.write("Check whether observed data matches expected data using Chi-Square test.")
st.write("Example: Disease cases in different age groups.")

# User inputs
observed = st.text_input("Observed values (comma-separated)", "50,80,120,90,60")
expected = st.text_input("Expected values (comma-separated)", "60,70,110,100,60")

# Significance level slider
alpha = st.slider("Significance Level (α)", 0.01, 0.10, 0.05)

# Run test button
if st.button("Run Test"):
    try:
        obs = list(map(int, observed.split(",")))
        exp = list(map(int, expected.split(",")))
        
        # Check lengths
        if len(obs) != len(exp):
            st.error("⚠ Observed and Expected values must have the same number of elements.")
        else:
            chi2, p = stats.chisquare(f_obs=obs, f_exp=exp)
            st.write(f"**Chi-Square Value:** {chi2:.4f}")
            st.write(f"**P-value:** {p:.4f}")
            
            if p < alpha:
                st.error("❌ Reject Null Hypothesis: Data does NOT fit expected distribution.")
            else:
                st.success("✔ Fail to Reject Null Hypothesis: Data fits expected distribution.")
    except:
        st.warning("⚠ Enter valid numeric values separated by commas.")

