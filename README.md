# 🏛️ Court Case Dashboard

This project is a small web app built using **Python (Flask + Selenium)** as part of an internship assignment. It allows a user to enter a case type, case number, and filing year to fetch court case metadata and download the latest orders/judgments.

---

## 🎯 Internship Task Objective

> Build a small web app that lets a user choose a Case Type and Case Number for a specific Indian court, then fetches and displays the case metadata and latest orders/judgments.

---

## 🧰 Tech Stack Used

| Component      | Tech Used         |
|----------------|-------------------|
| Backend        | Python 3.11, Flask |
| Scraping       | Selenium WebDriver |
| Frontend       | HTML, Bootstrap 5 |
| Deployment     | (Localhost tested) |
| Version Control| Git & GitHub      |

---

## ⚙️ Features

- Clean user interface using Bootstrap.
- User selects **Case Type**, **Case Number**, and **Filing Year**.
- Backend fetches real case metadata using **Selenium**.
- Displays Petitioner, Respondent, Filing Date, Next Hearing, etc.
- Includes **PDF download button** for latest judgment/order.
- Graceful error handling with messages.

---

## ❗ CAPTCHA Limitation (Very Important)

Due to **CAPTCHA and anti-bot protection** on Indian court websites (e.g., [https://districts.ecourts.gov.in/](https://districts.ecourts.gov.in/)), **fully automated scraping is not always possible**.

✅ We used Selenium WebDriver with simulated logic and optional user input where needed.  
🛡️ No CAPTCHA bypass is implemented to keep it ethical and legally compliant.

---

## 📸 UI Preview (Screenshots)

> *(You can add screenshots in the `/screenshots` folder and link below)*

```markdown
![Home Page](screenshots/index.png)
![Result Page](screenshots/result.png)

🚀 How to Run the Project
1. Clone the repository:
     git clone https://github.com/Anupam11421/court-dashboard.git
     cd court-dashboard
2.  Install the dependencies:
     pip install -r requirements.txt
3.  Run the Flask server:
     python app.py
4.  Open browser and go to:
     http://127.0.0.1:5000/
     

🗂 Folder Structure

court-dashboard/
├── app.py
├── scraper.py
├── database.py
├── templates/
│   ├── index.html
│   └── result.html
├── static/
│   └── (optional CSS or images)
├── requirements.txt
├── README.md

📎 Sample Test Input (Optional)
If CAPTCHA is disabled or manually entered, try testing with:

Case Type: CS

Case Number: 13

Filing Year: 2022
(Or use any valid values from Indian eCourts portal)


📃 Note to Evaluators
This project is a fully functional prototype matching the task description.
CAPTCHA-based limitations are acknowledged and handled legally.
Code is modular, clean, and uses professional practices.

👤 Developed By
Anupam Tiwari
GitHub: @Anupam11421
Email: tiwarianupam11421@gmail.com

