# scraper.py

from bs4 import BeautifulSoup

def fetch_case_details(case_type, case_number, filing_year):
    try:
        with open("faridabad_case_saved.html", "r", encoding="utf-8") as file:
            html = file.read()

        soup = BeautifulSoup(html, "lxml")

        table = soup.find("table")

        rows = table.find_all("tr")
        data = {}

        for row in rows:
            cols = row.find_all("td")
            if len(cols) == 2:
                key = cols[0].get_text(strip=True)
                value = cols[1].get_text(strip=True)
                data[key] = value

        return {
            "cnr": data.get("CNR Number", "N/A"),
            "petitioner": data.get("Petitioner and Advocate", "N/A"),
            "respondent": data.get("Respondent and Advocate", "N/A"),
            "filing_date": data.get("Filing Number & Date", "N/A"),
            "next_hearing_date": data.get("Next Hearing Date", "N/A"),
            "pdf_link": "https://example.com/dummy.pdf"
        }

    except Exception as e:
        return {"error": f"Error reading saved HTML: {str(e)}"}
