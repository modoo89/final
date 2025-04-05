import pandas as pd

def generate_simulation_data(kb_price):
    months = 40 * 12
    products = [
        {"시트명": "은행(비규제/1주택)-DSR40%", "LTV": 0.7, "금리": 0.042},
        {"시트명": "은행(비규제/다주택)-DSR40%", "LTV": 0.6, "금리": 0.042},
        {"시트명": "보험사(비규제/1주택)-DSR50%", "LTV": 0.7, "금리": 0.045},
        {"시트명": "보험사(비규제/다주택)-DSR50%", "LTV": 0.6, "금리": 0.045},
        {"시트명": "은행(규제/1주택)-DSR40%", "LTV": 0.5, "금리": 0.042},
        {"시트명": "은행(규제/다주택)-DSR40%", "LTV": 0.4, "금리": 0.042},
        {"시트명": "보험사(규제/1주택)-DSR50%", "LTV": 0.5, "금리": 0.045},
        {"시트명": "보험사(규제/다주택)-DSR50%", "LTV": 0.4, "금리": 0.045},
        {"시트명": "은행&보험사(규제/다주택매수)", "LTV": 0.3, "금리": 0.042},
        {"시트명": "상호금융(선순위)-DSRX", "LTV": 0.85, "금리": 0.046, "이자만": True},
        {"시트명": "상호금융(후순위)-DSRX", "LTV": 0.80, "금리": 0.050, "이자만": True},
    ]

    result = []
    for p in products:
        loan = int(kb_price * p["LTV"]) * 10000
        monthly = int(loan * (p["금리"] / 12)) if p.get("이자만") else                   int(loan * ((p["금리"]/12) * (1 + p["금리"]/12) ** months) / ((1 + p["금리"]/12) ** months - 1))
        income = "소득필요없음" if p.get("이자만") else f"{loan // 7:,}원/년"
        result.append({
            "시트명": p["시트명"],
            "LTV": f"{int(p['LTV']*100)}%",
            "금리": f"{p['금리']*100:.1f}%",
            "월 원리금": f"{monthly:,}원",
            "필요소득": income
        })
    return pd.DataFrame(result)