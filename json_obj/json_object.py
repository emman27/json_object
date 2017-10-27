"""
JSON Object
"""
import json


class MissingKeyError(KeyError):
    """
    Error raised when an expected key is missing
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

        >>> JSONObject([{'my_key': str}])
        >>> JSONObject({'my_key': str})
        """
        assert isinstance(schema, dict) or isinstance(schema, list)
        self.schema = schema
        self.strict = strict

    def loads(self, json_data, strict=False):
        """
        Parses a JSON string into the object.

        :param json_data (str): The JSON string to parse.
        :returns dict|list: Returns the same type as the schema given
        :raises MissingKeyError: If in strict mode and a key is missing. If not, the key is set to the default 0-equivalent value
        """
        unparsed = json.loads(json_data)

        parsed = {
            True: self._load_list,
            False: self._load_dict
        }[isinstance(self.schema, list)](unparsed)

        return parsed

    def _load_list(self, unparsed):
        return unparsed

    def _load_dict(self, unparsed):
        for key, value in self.schema.items():
            if unparsed.get(key) is None:
                if self.strict:
                    raise MissingKeyError("Key %s is missing" % key)
                unparsed[key] = value()
            else:
                unparsed[key] = value(unparsed.get(key))
        return unparsed
