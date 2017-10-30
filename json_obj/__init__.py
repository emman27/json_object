"""
JSON Object
"""
import json


class MissingKeyError(KeyError):
    """
    Error raised when an expected key is missing
    """
    pass


class SchemaError(BaseException):
    """
    Error raised when a provided schema is incorrect
    """
    pass


class JSONObject(object):
    """
    Some documentation here.
    JSONObject is a JSON decoder that guarantees fields passed down are safe.
    Note that if using lists, the base assumption is that this list must be homogenous
    """

    def __init__(self, schema, strict=False):
        """
        Initializes a JSON Object.

        :param schema (dict | list): A dictionary or list containing the schema
        :kwargs strict (bool): In strict mode, raises a MissingKeyError if any key is missing
        :raises SchemaError: The Schema provided is not a valid JSON Schema

        >>> JSONObject([{'my_key': str}])
        >>> JSONObject({'my_key': str})
        """
        if not isinstance(schema, dict) or isinstance(schema, list):
            raise SchemaError("The Schema provided is invalid")
        self.schema = schema
        self.strict = strict

    def loads(self, json_data, strict=False):
        """
        Parses a JSON string into the object.

        :param json_data (str|dict|list): The JSON string to parse.
        :returns (dict|list): Returns the same type as the schema given
        :raises MissingKeyError: If in strict mode and a key is missing.
            If not, the key is set to the default 0-equivalent value
        """
        if isinstance(json_data, str):
            json_data = json.loads(json_data)

        parsed = {
            True: self._load_list,
            False: self._load_dict
        }[isinstance(self.schema, list)](json_data)

        return parsed

    def _load_list(self, unparsed):
        schema = self.schema[0]
        return [JSONObject(schema).loads(dat) for dat in unparsed]

    def _load_dict(self, unparsed):
        for key, value in self.schema.items():
            if isinstance(value, dict) or isinstance(value, list):
                unparsed[key] = JSONObject(
                    value,
                    strict=self.strict
                ).loads(
                    unparsed.get(
                        key,
                        type(value)()
                    )
                )
            elif unparsed.get(key) is None:
                if self.strict:
                    raise MissingKeyError("Key %s is missing" % key)
                unparsed[key] = value()
            else:
                unparsed[key] = value(unparsed.get(key))
        return unparsed
