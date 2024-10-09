# DataFestAfrica-Hackathon-2024
Improving  Academic Outcome For Secondary Education

- Submission for #Data Rockstars
# Project Brief
- Preamble
An important general concern all over the African continent has been the sub-par quality of elementary and secondary education which has been further highlighted by the recent push to Computer-Based tests for students in ultimate classes (especially SSS3). In fairness, there has been some action taken by CSOs, governments and other bodies to improve the quality of education, and by extension, students’ performance. 
 
Recent statistics from JAMB (a Nigerian pre-tertiary examination governing body) shows that 76% (approx. 4 out of 5) of students who participated in the 2024 UTME scored less than 200 (50%). This interesting insight emphasizes the need to find proactive solutions to this problem. 

# Deliverables:
- Data Collection: Data was collected through the means of Generative AI
- Data warehouse dictionary:
    - Database: MYSQL
    - Data Warehouse Schema: Star Schema
      
                      Fact_Attendance: Stores attendance records.
                      Fact_Grades: Stores student grades.
                      Fact_Extra_curriculars: Stores participation in extracurricular activities.
                      Dimension Tables:
                      Dim_Students: Contains student details.
                      Dim_Parents: Contains parent details.
                      Dim_Resources: Contains resource details.
                      Dim_Time: Contains time-related dimensions (date, month, year).
    - Table Definitions and Data Types:
                      Students Table
                      
                      student_id (INT, PK)
                      first_name (VARCHAR(50))
                      last_name (VARCHAR(50))
                      gender (ENUM('Male', 'Female', 'Other'))
                      date_of_birth (DATE)
                      class (VARCHAR(10))
                      admission_date (DATE)
                      address (TEXT)
                      phone (VARCHAR(15))
                      email (VARCHAR(100))
                      Parents Table
                      
                      parent_id (INT, PK)
                      student_id (INT, FK)
                      parent_name (VARCHAR(100))
                      relationship (ENUM('Father', 'Mother', 'Guardian'))
                      income_level (ENUM('Poor', 'Middle Class', 'Upper Class'))
                      income (DECIMAL(15,2))
                      education_level (ENUM('Primary', 'Secondary', 'University'))
                      occupation (VARCHAR(100))
                      Attendance Table
                      
                      attendance_id (INT, PK)
                      student_id (INT, FK)
                      date (DATE)
                      present (BOOLEAN)
                      Grades Table
                      
                      grade_id (INT, PK)
                      student_id (INT, FK)
                      subject (VARCHAR(50))
                      score (DECIMAL(5,2))
                      term (VARCHAR(20))
                      Extracurricular Activities Table
                      
                      activity_id (INT, PK)
                      student_id (INT, FK)
                      activity_name (VARCHAR(100))
                      participation_level (ENUM('Low', 'Medium', 'High'))
                      frequency (ENUM('Daily', 'Weekly', 'Monthly'))
                      Resources Table
                      
                      resource_id (INT, PK)
                      resource_type (VARCHAR(100))
                      allocation_hours (INT)
                      total_resources (INT)
                      usage_frequency (ENUM('Daily', 'Weekly', 'Monthly'))
                      3. Data Warehouse Design
      - Analytical Models: Present the predictive models (if any) and analysis performed on the data
      - Report Dashboard: [Link To The PowerBI Dashboard](https://app.powerbi.com/view?r=eyJrIjoiZmIzM2FiZmMtMWI2Zi00OTdjLThjNDYtZWU4NzZkODkxNjBhIiwidCI6IjExODg4MzNmLTRiMTktNDYzYS04OThmLWM2ODMxNmRjOTQ1NiJ9)





  
