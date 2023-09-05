import requests


def get_request(endpoint: str, api_key: str, **kwargs) -> dict | str:
    """Make a GET request to The Odds API for the given endpoint.

    Parameters
    ----------
    endpoint : str
        The GET endpoint you wish to call. Options are "sports", "odds", "scores", "historical_odds", and "event_odds".
    api_key : str
        A valid The Odds API API key.

    Returns
    -------
    dict
        The return of the GET request.
    """
    base_endpoints = {
        "sports": "https://api.the-odds-api.com/v4/sports/?apiKey={api_key}",
        "odds": "https://api.the-odds-api.com/v4/sports/{sport}/odds/?apiKey={api_key}",
        "scores": "https://api.the-odds-api.com/v4/sports/{sport}/scores/?apiKey={api_key}",
        "historical_odds": "https://api.the-odds-api.com/v4/sports/{sport}/odds-history/?apiKey={api_key}",
        "event_odds": "https://api.the-odds-api.com/v4/sports/{sport}/events/{event_id}/?apiKey={api_key}",
    }
    arg_name_to_endpoint_arg_name = {
        "all": "all",
        "date": "date",
        "regions": "regions",
        "markets": "markets",
        "date_format": "dateFormat",
        "odds_format": "oddsFormat",
        "event_ids": "eventIds",
        "bookmakers": "bookmakers",
    }

    call_endpoint = base_endpoints.get(endpoint)

    if endpoint == "sports":
        call_endpoint = call_endpoint.format(api_key=api_key)
    elif endpoint in ["odds", "scores", "historical_odds"]:
        call_endpoint = call_endpoint.format(api_key=api_key, sport=kwargs.get("sport"))
    else:
        call_endpoint = call_endpoint.format(
            api_key=api_key, sport=kwargs.get("sport"), event_id=kwargs.get("event_id")
        )

    for arg_name, arg_value in locals()["kwargs"].items():
        if (
            arg_name not in ["endpoint", "api_key", "sport", "event_id"]
            and arg_value is not None
        ):
            if isinstance(arg_value, list):
                arg_value = ",".join(arg_value)

            if isinstance(arg_value, bool):
                arg_value = str(arg_value).lower()

            call_endpoint += (
                f"&{arg_name_to_endpoint_arg_name.get(arg_name)}={arg_value}"
            )

    r = requests.get(call_endpoint)

    try:
        response = r.json()
    except requests.exceptions.JSONDecodeError:
        response = r.text

    return response
