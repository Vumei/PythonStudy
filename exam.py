import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS 

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:",r.status_code)

response_dirt = r.json()

print("Total repositories:",response_dirt['total_count'])

repo_dicts = response_dirt['items']
print("Repositories returned:",len(repo_dicts))

repo_dict = repo_dicts[0]
print("\nKeys:",len(repo_dict))
for key in sorted(repo_dict.keys()):
	print(key)



