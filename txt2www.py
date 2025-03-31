#!/usr/bin/env python3
import os
from datetime import datetime

def txt_to_html(input_file, output_file):
    try:
        # Get the current date and time
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        with open(input_file, 'r') as txt_file:
            lines = txt_file.readlines()
        
        with open(output_file, 'w') as html_file:
            html_file.write("<html>\n<head>\n<title>{}</title>\n</head>\n<body>\n".format(os.path.basename(output_file)))
            html_file.write(f"<p><strong>Generated on:</strong> {current_time}</p>\n")  # Add timestamp
            html_file.write("<pre>\n")  # Use <pre> to preserve formatting
            html_file.writelines(lines)
            html_file.write("</pre>\n</body>\n</html>")
        
        print(f"Converted {input_file} to {output_file}")
    except FileNotFoundError:
        print(f"File {input_file} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Convert the files
txt_to_html('playback-updates.txt', 'playback-updates.html')
txt_to_html('playback-notify.txt', 'playback-notify.html')