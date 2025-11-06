import streamlit as st
import pandas as pd

# Конфигурација на страницата
st.set_page_config(page_title="Ангел 3 - Преглед", layout="wide")

st.title("📊 Табела: Ангел 3 (Read-only)")

excel_file = "Ангел 3.xlsx"  # Името мора да биде исто како фајлот што ќе го качиш

try:
    xlsx = pd.ExcelFile(excel_file)
    sheet_names = xlsx.sheet_names

    sheet = st.sidebar.selectbox("📄 Одбери лист:", sheet_names)
    df = pd.read_excel(excel_file, sheet_name=sheet)

    st.write(f"**Вкупно редови:** {len(df)}")
    st.dataframe(df, use_container_width=True)

    st.info("Овој приказ е само за читање. Измените во табелата не се дозволени.", icon="🔒")

except FileNotFoundError:
    st.error("Фајлот 'Ангел 3.xlsx' не е пронајден. Качете го во истата папка со app.py.")
except Exception as e:
    st.error(f"Настана грешка при вчитување на Excel фајлот: {e}")
