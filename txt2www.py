#!/usr/bin/env python3
import os

def txt_to_html(input_file, output_file):
    try:
        with open(input_file, 'r') as txt_file:
            lines = txt_file.readlines()
        
        with open(output_file, 'w') as html_file:
            html_file.write("<html>\n<head>\n<title>{}</title>\n</head>\n<body>\n".format(os.path.basename(output_file)))
            html_file.write("<pre>\n")  # Use <pre> to preserve formatting
            html_file.writelines(lines)
            html_file.write("</pre>\n</body>\n</html>")
        
        print(f"Converted {input_file} to {output_file}")
    except FileNotFoundError:
        print(f"File {input_file} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Convert the files
txt_to_html('playback-servers.txt', 'playback-servers.html')
txt_to_html('playback-notify.txt', 'playback-notify.html')