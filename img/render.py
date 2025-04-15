import yaml
import jinja2


if __name__ == '__main__':
  with open('data.yml', 'r') as file:
    data = yaml.safe_load(file)

  environment = jinja2.Environment(loader=jinja2.FileSystemLoader("./"))
  template = environment.get_template('cv.html')

  papers = list(reversed(data['papers']))
  full_papers = [paper for paper in papers if paper['review'] == 'full']
  for id, paper in enumerate(full_papers):
    paper['id'] = f'P{len(full_papers) - id}'
  data['full_papers'] = full_papers

  light_papers = [paper for paper in papers if paper['review'] == 'light']
  for id, paper in enumerate(light_papers):
    paper['id'] = f'L{len(light_papers) - id}'
  data['light_papers'] = light_papers

  output = template.render(**data)

  with open('out.html', 'w') as file:
    file.write(output)
