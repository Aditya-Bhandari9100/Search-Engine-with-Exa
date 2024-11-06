from exa_py import Exa

exa = Exa('9caaedff-1f8c-49b8-b14b-1e1e8f56b0bc')

query = input('Search here: ')

response = exa.search(
  query,
  num_results=5,
  type='keyword',
  include_domains=['https://www.instagram.com'],
)

for result in response.results:
  print(f'Title: {result.title}')
  print(f'URL: {result.url}')
  print()