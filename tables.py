from flask_table import Table, Col


class Results(Table):
    code = Col('FLIGHT_CODE', show=False)
    source = Col('SOURCE')
    destination = Col('DESTINATION')
    arrival = Col('ARRIVAL')
    departure = Col('DEPARTURE')
    status = Col('STATUS')
    duration = Col('DURATION')
    f_type = Col('FLIGHTTYPE')
    layover = Col('LAYOVER_TIME')
    stops = Col('NO_OF_STOPS')
    a_id = Col('AIRLINEID', show=False)