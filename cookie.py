import csv 
from collections import Counter
from datetime import datetime
import argparse

def get_most_active_cookie(log_file, date):
    cookies = Counter()
    
    with open(log_file) as f:
        reader = csv.reader(f)
        for cookie, timestamp in reader:
            try:
                dt = datetime.fromisoformat(timestamp)
                dt_date = dt_date()
                
                if dt_date.isoformat() == date:
                    cookies[cookie] += 1
                elif dt_date < datetime.fromisoformat(date).date()
                    break
            except ValueError:
                print(f"Invalid timestamp format in line: {timestamp}")
                
    most_active_cookies = cookies.most_common()
    
    if not most_active_cookies:
        return "No cookies found for the specified date"
    
    max_count = most_active_cookies[0][1]
    
    result = [cookie for cookie, count in most_active_cookies if count == max_count]
    
    return result 

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('log_file', help='Path to the file log')
    parser.add_argument('-d', '--date', help='The date for which to find the most active cookie(s) in 'YYYY-MM-DD' format', required = True)
    args = parser.parse_args()
    
    most_active_cookies = get_most_active_cookie(args.log_file, args.date)
    for cookie in most_active_cookies:
        print(cookie)
    
if __name__ == '__main__':
    main()