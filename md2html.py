import markdown
import sys

def convert_md_to_html(md_filepath,html_filepath):
    with open(md_filepath,'r',encoding='utf-8') as md_file:
        md_content = md_file.read()
    html_content = markdown.markdown(md_content)
    with open(html_filepath,'w',encoding='utf-8') as html_file:
        html_file.write(html_content)

if __name__=="__main__":
    md_filepath = "/Users/dongming/projects/ml4re/README.md"
    html_filepath = "/Users/dongming/projects/ml4re/index.html"
    convert_md_to_html(md_filepath,html_filepath)
    print("Markdown file has been converted to HTML file")
    