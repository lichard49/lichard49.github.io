import pandas as pd
import jinja2
import os


if __name__ == '__main__':
  data = {
    'employment': pd.read_csv(os.path.join('data', 'employment.csv'), keep_default_na=False),
    'education': pd.read_csv(os.path.join('data', 'education.csv'), keep_default_na=False),
    'awards': pd.read_csv(os.path.join('data', 'awards.csv'), keep_default_na=False),
    'papers': pd.read_csv(os.path.join('data', 'papers.csv'), keep_default_na=False),
    'talks': pd.read_csv(os.path.join('data', 'talks.csv'), keep_default_na=False),
    'teaching': pd.read_csv(os.path.join('data', 'teaching.csv'), keep_default_na=False),
    'mentorship': pd.read_csv(os.path.join('data', 'mentorship.csv'), keep_default_na=False),
    'service': pd.read_csv(os.path.join('data', 'service.csv'), keep_default_na=False),
  }

  environment = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))
  base_template = environment.get_template('base_template.html')

  home_template = environment.get_template('home_template.html')
  home_html = home_template.render()
  home_html = base_template.render(content=home_html, tab='home', page_name='Home')
  with open(os.path.join('index.html'), 'w') as output_file:
    output_file.write(home_html)

  research_template = environment.get_template('research_template.html')
  research_html = research_template.render(papers=data['papers'])
  research_html = base_template.render(content=research_html, tab='research', page_name='Research')
  with open(os.path.join('research.html'), 'w') as output_file:
    output_file.write(research_html)

  teaching_template = environment.get_template('teaching_template.html')
  teaching_html = teaching_template.render()
  teaching_html = base_template.render(content=teaching_html, tab='teaching', page_name='Teaching')
  with open(os.path.join('teaching.html'), 'w') as output_file:
    output_file.write(teaching_html)

  cv_template = environment.get_template('cv_template.html')
  cv_html = cv_template.render(**data)
  with open(os.path.join('cv.html'), 'w') as output_file:
    output_file.write(cv_html)
