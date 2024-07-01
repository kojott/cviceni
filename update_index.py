import re

def update_html_file(file_path):
    with open(file_path, 'r') as file:
        html_content = file.read()

    # Update the title
    html_content = re.sub(r'<title>.*?</title>', '<title>Cvičení</title>', html_content)

    # Prepare the new content to be added in the head section
    new_head_content = """
<meta name="description" content="">
<meta name="keywords" content="">
<meta name="author" content="Swinging Dogs s.r.o.">
<meta property="og:title" content="">
<meta property="og:description" content="">
<meta property="og:url" content="https://cviceni.coininspector.pro">
<meta property="og:type" content="website">
<meta property="og:image" content="https://cviceni.coininspector.pro/app/static/logo.png">
<meta name="apple-mobile-web-app-title" content="Cvičení">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black">
<link rel="apple-touch-icon" href="https://cviceni.coininspector.pro/app/static/logo.png">
<link rel="apple-touch-icon" sizes="76x76" href="https://cviceni.coininspector.pro/app/static/logo.png">
<link rel="apple-touch-icon" sizes="120x120" href="https://cviceni.coininspector.pro/app/static/logo.png">
<link rel="apple-touch-icon" sizes="152x152" href="https://cviceni.coininspector.pro/app/static/logo.png">
<meta name="msapplication-TileImage" content="https://cviceni.coininspector.pro/app/static/logo.png">
<meta name="msapplication-TileColor" content="#222222">
<meta name="mobile-web-app-capable" content="yes">
"""

    # Insert the new content into the head section
    html_content = html_content.replace('</head>', new_head_content + '</head>')

    # Write the updated content back to the file
    with open(file_path, 'w') as file:
        file.write(html_content)

# Specify the path to your HTML file
file_path = '/usr/local/lib/python3.12/site-packages/streamlit/static/index.html'
update_html_file(file_path)
