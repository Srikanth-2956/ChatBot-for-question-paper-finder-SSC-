import streamlit as st

# Dictionary of question papers with URLs
question_papers = {
    "2017": {
        "Biology": "https://cdn1.byjus.com/wp-content/uploads/2020/06/Telangana-Class-10-Science-Paper-2-Question-Paper-2017.pdf",
        "Math": "https://cdn1.byjus.com/wp-content/uploads/2020/06/Telangana-Class-10-Maths-Paper-I-Previous-Year-Paper-March-2017.pdf",
        "Physics": "https://cdn1.byjus.com/wp-content/uploads/2020/06/Telangana-Class-10-Science-Paper-1-Previous-Year-Paper-2017.pdf",
        "Social": "https://byjus.com/telangana-board/ssc-class-10-previous-years-question-papers-social-science-paper-1-2017/"
    },
    "2018": {
        "Biology": "https://cdn1.byjus.com/wp-content/uploads/2020/06/Telangana-Class-10-Science-Paper-II-Previous-Year-Paper-2018.pdf",
        "Math": "https://cdn1.byjus.com/wp-content/uploads/2020/06/Telangana-Class-10-Maths-Paper-I-Previous-Year-Paper-2018.pdf",
        "Physics": "https://cdn1.byjus.com/wp-content/uploads/2020/06/Telangana-Class-10-Science-Paper-II-Previous-Year-Paper-2018.pdf",
        "Social": "https://cdn1.byjus.com/wp-content/uploads/2020/01/Telangana-Board-Class-10-Social-Science-Paper-I-Previous-Year-Paper-2018TM.pdf"
    },
    "2019": {
        "Biology": "https://cdn1.byjus.com/wp-content/uploads/2020/01/Telangana-Board-Class-10-Science-Paper-2-Previous-Year-Paper-2019.pdf",
        "Math": "https://cdn1.byjus.com/wp-content/uploads/2020/01/Telangana-Board-Class-10-Maths-Paper-1-Previous-Year-Paper-2019.pdf",
        "Physics": "https://cdn1.byjus.com/wp-content/uploads/2020/01/Telangana-Board-Class-10-Science-Paper-1-Previous-Year-Paper-2019.pdf",
        "Social": "https://cdn1.byjus.com/wp-content/uploads/2020/01/Telangana-Board-Class-10-Social-Science-Paper-II-Previous-Year-Paper-2019EM.pdf"
    },
    "2021": {
        "Biology": "https://drive.google.com/file/d/1kzIhiGP11n_jgwTX6Wxjr3d_mAAEhyAY/preview",
        "Math": "https://drive.google.com/file/d/1cz2OZIibmVY9k6_n9q6w1iFcQDSSphwg/view",
        "Physics": "https://drive.google.com/file/d/13dXEP6sHH18CmYT8lqzqL-K67R_eHvAf/preview",
        "Social": "https://www.mesc.gov.ws/wp-content/uploads/2022/06/SSC-Social-2021.pdf"
    },
    "2022": {
        "Biology": "https://www.selfstudys.com/books/telangana/state-books/class-10th/2022/general-science-biological-science-em-20e-set-a-2022/965617",
        "Math": "https://www.selfstudys.com/books/telangana/state-books/class-10th/2022/mathematics-em-15e-set-a-2022/965619",
        "Physics": "https://www.selfstudys.com/books/telangana/state-books/class-10th/2022/general-science-physical-science-em-19e-set-a-2022/965615",
        "Social": "https://www.selfstudys.com/books/telangana/state-books/class-10th/2022/social-studies-em-21e-set-a-2022/965618"
    },
    "2023": {
        "Biology": "https://www.mesc.gov.ws/wp-content/uploads/2022/06/SSC-Biology-2023.pdf",
        "Math": "https://www.mesc.gov.ws/wp-content/uploads/2022/06/SSC-Math-2023.pdf",
        "Physics": "https://www.mesc.gov.ws/wp-content/uploads/2022/06/SSC-Physics-2023.pdf",
        "Social": "https://www.mesc.gov.ws/wp-content/uploads/2022/06/SSC-Social-2023.pdf"
    }
}

# Function to get question paper URL
def get_question_paper(year, subject):
    subject = subject.capitalize()  # Capitalize the first letter of subject
    if year == "2020":
        return "Exams not conducted due to COVID-19."
    elif year in question_papers and subject in question_papers[year]:
        return question_papers[year][subject]
    else:
        return f"Sorry, I couldn't find the question paper for {year} {subject}."

# Streamlit app
def main():
    st.title("Question Paper Finder for Class 10")

    # Text input for year and subject
    year = st.text_input("Enter the year for question paper:")
    subject = st.text_input("Enter the subject for Question paper:")

    # Button to get the URL
    if st.button("Get Question Paper"):
        if year and subject:
            url = get_question_paper(year, subject)
            if "Sorry" not in url and "Exams" not in url:
                st.success(f"Here is the URL for the {subject} question paper: [Click here]({url})")
            elif "Exams" in url:
                st.info(url)
            else:
                st.error(url)
        else:
            st.warning("Please enter both year and subject.")

if __name__ == "__main__":
    main()
