#!/usr/bin/env python3
import os
from datetime import datetime

def txt_to_html(input_file, output_file_base):
    try:
        # Get the current date and time
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # Format for filenames
        output_file = f"{output_file_base}_{current_time}.html"  # Append timestamp to filename
        
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

# Convert the files with absolute paths
txt_to_html('/home/ansible/playback-updates.txt', '/home/ansible/playback-updates')
txt_to_html('/home/ansible/playback-notify.txt', '/home/ansible/playback-notify')