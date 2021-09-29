# Website Credentials Scraping

A Flask server that returns website credentials

## Usage
To use the api you only need to put the website url on url param. 

example:

  .../?url=https://github.com/pultzlucas/templo

it returns...

```json
{
  "description": "Templo is a template manager that provide you more flexibility and agility at software development time. - GitHub - pultzlucas/templo: Templo is a template manager that provide you more flexibility and agility at software development time.",
  "favicon_url": "https://github.githubassets.com/favicons/favicon.svg",
  "status": "success",
  "title": "GitHub - pultzlucas/templo: Templo is a template manager that provide you more flexibility and agility at software development time."
}
```
