import streamlit as st
import pandas as pd
import joblib

# Load the pre-trained model
loaded_model = joblib.load('best_decision_tree_model.sav')

# A Function to make predictions
def make_prediction(input_data):
    prediction = loaded_model.predict(input_data)
    return prediction


def main():
    st.title("Student Performance Prediction")
    
    
    st.write("""
    This application predicts student performance based on various input parameters. 
    Please fill in the details about the resources, teaching methods, and student information to receive a prediction.
    The model analyzes the information and provides insights on the expected performance of the student.
    """)

    st.subheader("Input Parameters")
    st.write("Fill in the following details:")

    # Create input fields for user inputs
    resource_type = st.selectbox("Resource Type", [
        'Library', 'Computer Lab', 'Science Lab', 'Sports Facilities', 'Art Room',
        'Music Room', 'Study Hall', 'Assembly Hall', 'Outdoor Field', 'Workshop Room',
        'Laboratory Equipment', 'Sports Equipment', 'Classroom Materials',
        'ICT Room', 'Guidance Counseling', 'Health Center', 'Canteen', 'Playground',
        'Storage Room', 'Media Center', 'Media Room', 'Language Lab', 'Robotics Lab',
        'Debate Room', 'Counseling Room', 'Parking Space', 'Gym', 'Staff Room',
        'First Aid Station', 'Conference Room', 'Art Gallery', 'Kitchen', 'Cafeteria',
        'Auditorium', 'Outdoor Classroom', 'Science Fair Area', 'Music Hall',
        'Theatre', 'Research Lab'
    ])
    
    usage_frequency = st.selectbox("Usage Frequency", ['Daily', 'Weekly', 'Bi-weekly', 'Monthly', 'Yearly'])
    
    subject = st.selectbox("Subject", [
        'Mathematics', 'English', 'Science', 'History', 'Geography', 'Physical Education', 
        'Arts', 'Music', 'Computer Science', 'Foreign Language'
    ])
    
    teaching_method = st.selectbox("Teaching Method", ['Interactive', 'Lecture', 'Hands-on', 'Discussion', 'Practical', 'Creative Projects', 'Immersive'])
    
    gender = st.selectbox("Gender", ['Male', 'Female'])
    class_name = st.selectbox("Class", ['SSS3'])  # Add your class names
    parent_name = st.text_input("Parent Name")
    relationship = st.selectbox("Relationship", ['Father', 'Mother'])
    income_level = st.selectbox("Income Level", ['Upper Class', 'Lower Upper Class', 'Middle Class', 'Lower Class', 'Poor'])
    education_level = st.selectbox("Education Level", ['University', 'Secondary', 'Primary'])
    occupation = st.text_input("Occupation")
    
    activity_name = st.selectbox("Activity Name", [
        'Football', 'Debate Club', 'Music Band', 'Drama Club', 'Art Club', 'Science Club',
        'Chess Club', 'Gardening Club', 'Coding Club', 'Basketball', 'Volleyball',
        'Running Club', 'Photography Club', 'Environment Club', 'Cooking Club',
        'Creative Writing Club', 'Robotics Club', 'Cultural Club', 'Peer Mentoring',
        'First Aid Training', 'Fashion Club', 'Community Service', 'Film Club',
        'Poetry Club', 'Hiking Club', 'Technology Club', 'Dance Club', 'Language Club',
        'History Club', 'Math Club', 'Fitness Club', 'Debate Team', 'Student Council',
        'Literary Society', 'Environmental Awareness', 'Social Justice Club', 
        'Entrepreneurship Club', 'Public Speaking Club', 'Wellness Club',
        'Mentorship Program', 'Coding Bootcamp', 'Nature Explorers', 'Youth Leadership',
        'Art Therapy', 'Public Health Club', 'Sports Leadership', 'Social Media Club',
        'Book Club', 'Research Club', 'Innovation Hub', 'Soccer Team', 'Choir',
        'Basketball Team', 'Environmental Club', 'Yearbook Committee'
    ])
    
    participation_level = st.selectbox("Participation Level", ['High', 'Medium', 'Low'])
    hours_per_week_y = st.number_input("Hours per Week (Y)", min_value=0)
    material_type = st.selectbox("Material Type", ['Textbook', 'Online Resource', 'Library Access'])
    access_level = st.selectbox("Access Level", ['High', 'Medium', 'Low'])
    frequency_of_use = st.number_input("Frequency of Use", min_value=0)

    allocation_hours = st.number_input("Allocation Hours", min_value=0)
    total_resources = st.number_input("Total Resources", min_value=0)
    student_feedback_rating = st.number_input("Student Feedback Rating", min_value=0.0, max_value=5.0)
    hours_per_week_x = st.number_input("Hours per Week (X)", min_value=0)
    income_monthly = st.number_input("Monthly Income", min_value=0)
    age_at_admission = st.number_input("Age at Admission", min_value=0)
    years_in_school = st.number_input("Years in School", min_value=0)

    # When the user clicks the button, make the prediction
    if st.button("Predict"):
        # Now create a DataFrame from user inputs
        input_data = pd.DataFrame({
            'resource_type': [resource_type],
            'usage_frequency': [usage_frequency],
            'subject': [subject],
            'teaching_method': [teaching_method],
            'gender': [gender],
            'class': [class_name],
            'parent_name': [parent_name],
            'relationship': [relationship],
            'income_level': [income_level],
            'education_level': [education_level],
            'occupation': [occupation],
            'activity_name': [activity_name],
            'participation_level': [participation_level],
            'hours_per_week_y': [hours_per_week_y],
            'material_type': [material_type],
            'access_level': [access_level],
            'frequency_of_use': [frequency_of_use],
            'allocation_hours': [allocation_hours],
            'total_resources': [total_resources],
            'student_feedback_rating': [student_feedback_rating],
            'hours_per_week_x': [hours_per_week_x],
            'income (monthly)': [income_monthly],
            'age_at_admission': [age_at_admission],
            'years_in_school': [years_in_school]
        })

        # Make prediction
        prediction = make_prediction(input_data)

        
        result = "Pass" if prediction[0] == 1 else "Fail"
        
        st.success(f"Prediction Result: {result}")

# Run the app
if __name__ == "__main__":
    main()
