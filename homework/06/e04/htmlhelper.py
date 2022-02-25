
def generate_html_page(title, content1, content2, content3, win):
  return f"""
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>{title}</title>
  </head>
  <body>
    {content1}
    {content2}
    {content3}
    <p>{win}</p>
  </body>
</html>"""

