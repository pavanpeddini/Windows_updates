
def fetch_windows_history():  
    historical_data = [
        {"version": "Windows 1.0", "release_date": "November 1985", "description": "GUI Introduction"},
        {"version": "Windows 2.0", "release_date": "December 1987", "description": "Improved graphics"},
        {"version": "Windows 3.0", "release_date": "May 1990", "description": "Enhanced Performance"},
        {"version": "Windows 95", "release_date": "August 1995", "description": "Start menu Debut"},
        {"version": "Windows 98", "release_date": "June 1998", "description": "USB Support"},
        {"version": "Windows 2000", "release_date": "February 2000", "description": "Business Focus"},
        {"version": "Windows XP", "release_date": "October 2001", "description": "Stability Upgrade"},
        {"version": "Windows Vista", "release_date": "January 2007", "description": "Aero Glass "},
        {"version": "Windows 7", "release_date": "October 2009", "description": "Enhanced Usability"},
        {"version": "Windows 8", "release_date": "October 2012", "description": "Touch Optimization"},
        {"version": "Windows 10", "release_date": "July 2015", "description": "Unified Platform"},
        {"version": "Windows 11", "release_date": "Ocotber 2021", "description": "Modernized Interface"},
       
    ]
    return historical_data

def process_windows_history(data):
    """
    Function to process historical Windows data
    
    Args:
        data (list): Historical data about Windows changes and history
        
    Returns:
        dict: Processed Windows history data in a structured format
    """
    processed_data = {}
    for entry in data:
        version = entry['version']
        processed_data[version] = {
            'release_date': entry['release_date'],
            'description': entry['description']
        }
    return processed_data
