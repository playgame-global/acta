from collections import namedtuple
from .errors import InvalidACTASpecParameterError


IMMUTABLE_OBJECT_FIELDS = ['actor', 'verb', 'obj', 'meta', 'handler_function']


class ActaSpecBuilder(object):
    _actor = ''
    _verb = ''
    _obj = ''
    _meta = {}
    _handler_function = None

    def __init__(self, actor, verb, obj, meta, handler_function):
        self._actor = actor
        self._verb = verb
        self._obj = obj
        self._meta = meta
        self._handler_function = handler_function

    @property
    def actor(self):
        if not isinstance(self._actor, str):
            raise InvalidACTASpecParameterError(
                'Actor must be an str instance')
        if not self._actor:
            raise InvalidACTASpecParameterError('Actor must not be empty')

        return self._actor

    @property
    def verb(self):
        if not isinstance(self._verb, str):
            raise InvalidACTASpecParameterError('Verb must be an str instance')
        if not self._actor:
            raise InvalidACTASpecParameterError('Verb must not be empty')

        return self._verb

    @property
    def obj(self):
        if not isinstance(self._obj, str):
            raise InvalidACTASpecParameterError(
                'Object must be an str instance')
        if not self._actor:
            raise InvalidACTASpecParameterError('Object must not be empty')

        return self._obj

    @property
    def meta(self):
        if not isinstance(self._meta, dict):
            raise InvalidACTASpecParameterError(
                'Meta must be an instance of dict')

        required_fields = self._meta.get('required_fields')
        if not isinstance(required_fields, list):
            raise InvalidACTASpecParameterError(
                'Required Fields must be an instance of list')
        if len(required_fields) == 0:
            raise InvalidACTASpecParameterError(
                'Required Fields must not be empty')

        return self._meta

    @property
    def handler_function(self):
        if not hasattr(self._handler_function, '__call__'):
            raise InvalidACTASpecParameterError(
                'Handler Function must be a callable')

        return self._handler_function

    def build(self):
        return ActaSpec(self.actor, self.verb, self.obj, self.meta, self.handler_function)


class ActaSpec(namedtuple('ActaSpec', IMMUTABLE_OBJECT_FIELDS)):
    __slots__ = ()

    def to_dict(self):
        return {
            self.verb: {
                'actor': self.actor,
                'object': self.obj,
                'meta': self.meta,
                'handler': self.handler_function
            }
        }
