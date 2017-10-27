# JSON Object Strict Typing [![CircleCI](https://circleci.com/gh/emman27/json_object.svg?style=svg)](https://circleci.com/gh/emman27/json_object) [![Known Vulnerabilities](https://snyk.io/test/github/emman27/json_object/badge.svg)](https://snyk.io/test/github/emman27/json_object) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/8babe432d6ee4518adc07998a5b67636)](https://www.codacy.com/app/eygohlolz/json_object?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=emman27/json_object&amp;utm_campaign=Badge_Grade)

Provides json unmarshalling to strict types for Python

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
