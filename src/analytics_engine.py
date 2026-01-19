# Appendix: Core Analytical Functions

def calculate_ghost_child_risk(district_summary):
    """
    Estimates School Dropout Risk by comparing Birth Cohort vs School-Entry Bio Updates.
    Formula: 1 - (Bio_Updates_5_17 / (Enrol_0_5 / 5))
    """
    # Estimated Annual Cohort from 0-5 Enrolment
    cohort = district_summary['age_0_5'] / 5.0
    cohort = cohort.replace(0, 1) # Avoid ZeroDiv
    
    # Calculate Risk
    dropout_risk = 1 - (district_summary['bio_age_5_17'] / cohort)
    return dropout_risk

def calculate_dormancy_score(district_summary):
    """
    Identifies 'Digital Dark Zones' where Adult Population is high but Updates are low.
    Formula: Adult_Enrol / (Adult_Updates + 1)
    """
    admin_dormancy = district_summary['age_18_greater'] / (district_summary['demo_age_17_'] + 1)
    return admin_dormancy
