import pandas as pd
import jinja2
import os


if __name__ == '__main__':
  papers = pd.read_csv('papers.csv', keep_default_na=False)
  print(papers)

  environment = jinja2.Environment(loader=jinja2.FileSystemLoader('./'))
  base_template = environment.get_template('base_template.html')

  home_template = environment.get_template('home_template.html')
  home_html = home_template.render()
  home_html = base_template.render(content=home_html, tab='home', page_name='Home')
  with open(os.path.join('..', 'index.html'), 'w') as output_file:
    output_file.write(home_html)

  research_template = environment.get_template('research_template.html')
  research_html = research_template.render(papers=papers)
  research_html = base_template.render(content=research_html, tab='research', page_name='Research')
  with open(os.path.join('..', 'research.html'), 'w') as output_file:
    output_file.write(research_html)

  teaching_template = environment.get_template('teaching_template.html')
  teaching_html = teaching_template.render()
  teaching_html = base_template.render(content=teaching_html, tab='teaching', page_name='Teaching')
  with open(os.path.join('..', 'teaching.html'), 'w') as output_file:
    output_file.write(teaching_html)
