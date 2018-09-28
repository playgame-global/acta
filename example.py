# Create a spec
from acta import ActaSpecBuilder
from sanic import Sanic
from sanic.response import json
from acta import validate_request


meta = {
    'required_fields': [
        'currency',
        'number',
        'origin',
        'dates',
        'passengers'
    ]
}


def handler_function():
    # Well, handle it?
    pass


acta_spec = ActaSpecBuilder(actor='person',
                            verb='flight-search-with-budget',
                            obj='currency-number',
                            meta=meta,
                            handler_function=handler_function).build()

# Dictionary
flight_search_spec = acta_spec.to_dict()

acta_specs = {}.update(flight_search_spec)

app = Sanic(__name__)


@app.route('/events')
async def events(request):
    '''
    {
        "actor": {
            "id": "2fe614af-266b-4773-a066-3b518763380b"
            "kind": "person"
        },
        "action": "flight-search-with-budget",
        "object": {
            "id": "IDR-1500000",
            "kind": "currency-number"
        },
        "meta": {
            "currency": "IDR",
            "number": 1500000,
            "origin": {
                "latitude": -6.1273181,
                "longitude": 106.123123
            },
            "dates": {
                "outbound": "2017-05-26",
                "inbound": "2017-05-28"
            },
            "passengers": {
                "adults": 1,
                "children": 0,
                "infants": 0
            }
        }
    }
    '''
    body = request.json
    verb = body.get('action')

    handler = await validate_request(spec=acta_specs.get(verb),
                                     request=body)

    return await handler(request)
