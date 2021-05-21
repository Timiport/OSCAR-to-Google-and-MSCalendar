def getCourseList():
    """
    Convert Dictionary list of course to a list

    Returns:
        list : a list for the types of courses in OSCAR
    """
    courseDescription = []
    for courseName, description in courseDict.items():
        courseDescription.append(courseName + ": " + description)
    return courseDescription
    
courseDict = {
    'ACCT': 'Accounting',
    'AE': 'Aerospace Engineering',
    'AS': 'Air Force Aerospace Studies',
    'APPH': 'Applied Physiology',
    'ASE': 'Applied Systems Engineering',
    'ARBC': 'Arabic',
    'ARCH': 'Architecture',
    'BIOL': 'Biology',
    'BMEJ': 'Biomedical Engineering Joint Emory PKU',
    'BME': 'Biomedical Engineering',
    'BMEM': 'Biomedical Engineering Joint Emory',
    'BC': 'Building Construction',
    'CETL': 'Center Enhancement Teach/Learn',
    'CHBE': 'Chemical & Biomolecular Engineering',
    'CHEM': 'Chemistry',
    'CHIN': 'Chinese',
    'CP': 'City Planning',
    'CEE': 'Civil and Environmental Engineering',
    'COA': 'College of Architecture',
    'COE': 'College of Engineering',
    'CX': 'Computational Mod, Sim, & Data',
    'CSE': 'Computational Science and Engineering',
    'CS': 'Computer Science',
    'COOP': 'Co-op',
    'UCGA': 'Cross-enrollment',
    'EAS': 'Earth and Atmospheric Sciences',
    'ECON': 'Economics',
    'ECE': 'Electrical and Computer Engineering',
    'ENGL': 'English',
    'FS': 'Foreign Studies',
    'FREN': 'French',
    'GT': 'Georgia Tech',
    'GTL': 'Georgia Tech Lorraine',
    'GRMN': 'German',
    'HPS': 'Health Performance Science',
    'HS': 'Health Systems',
    'HIST': 'History',
    'HTS': 'History, Technology, and Society',
    'ISYE': 'Industrial and Systems Engineering',
    'ID': 'Industrial Design',
    'INTA': 'International Affairs',
    'IL': 'International Logistics',
    'INTN': 'Internship',
    'JAPN': 'Japanese',
    'KOR': 'Korean',
    'LS': 'Learning Support',
    'LING': 'Linguistics',
    'LCC': 'Literature, Communication, and Culture',
    'MGT': 'Management',
    'MOT': 'Management of Technology',
    'MSE': 'Materials Science and Engineering',
    'MATH': 'Mathematics',
    'ME': 'Mechanical Engineering',
    'MP': 'Medical Physics',
    'MSL': 'Military Science and Leadership',
    'ML': 'Modern Languages',
    'MUSI': 'Music',
    'NS': 'Naval Science',
    'NRE': 'Nuclear and Radiological Engineering',
    'PERS': 'Persian',
    'PHIL': 'Philosophy',
    'PHYS': 'Physics',
    'POL': 'Political Science',
    'PTFE': 'Polymer, Texture, and Fiber Engineering',
    'DOPP': 'Professional Practice',
    'PSYC': 'Psychology',
    'PUBP': 'Public Policy',
    'RGTR': 'Regent\'s Reading Skills',
    'RGTE': 'Regent\'s Writing Skills',
    'RUSS': 'Russian',
    'SOC': 'Sociology',
    'SPAN': 'Spanish'
}


