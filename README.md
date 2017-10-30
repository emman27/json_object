# JSON Object Strict Typing [![CircleCI](https://circleci.com/gh/emman27/json_object.svg?style=svg)](https://circleci.com/gh/emman27/json_object) [![Known Vulnerabilities](https://snyk.io/test/github/emman27/json_object/badge.svg)](https://snyk.io/test/github/emman27/json_object) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/8babe432d6ee4518adc07998a5b67636)](https://www.codacy.com/app/eygohlolz/json_object?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=emman27/json_object&amp;utm_campaign=Badge_Grade)

### Summary
Provides json unmarshalling to strict types for Python. This ensures you always get safe dictionaries for usage. This allows you to always do the below without worrying about KeyErrors.

```
schema = JSONObject(...)
json_parsed = schema.loads(json_unparsed)
json_parsed['my_key']['my_next_key']
```

Currently supports basic Python primitives: `str`, `list`, `dict`, `float`, `int`, `bool`

Coming soon: Python DateTime support

### Usage
First, start by declaring your schema of objects you expect to get. For example, if I expect to get a user representation,

```
user_schema = JSONObject({
    username: str,
    id: int,
    name: str,
    active: bool,
    permissions: [
        {
            'resource': 'string',
            'action': 'string',
        }
    ]
})

# Make the relevant API call...
req = requests.get('...')
data = user_schema.loads(req.json()) # The loads signature is indifferent between json.loads(s) and s itself.

# You can now do things like
for perm in data['permissions']:
    print(perm['resource'])
# safely without worrying about KeyErrors
```

### Example
```
from json_obj import JSONObject

>>> schema = {
  'a': str,
  'b': int,
  'c': float,
  'd': boolean,
}
>>> loader = JSONObject(schema)
>>> loader.loads({
  'a': 34,
  'b': True,
})

{
  'a': '34',
  'b': 1,
  'c': 0.0,
  'd': False,
}

```
