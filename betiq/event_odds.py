from .caller import get_request


def get_event_odds(
    api_key: str,
    event_id: str,
    sport: str = "upcoming",
    regions: list = ["us", "us2", "uk", "au", "eu"],
    markets: list = ["h2h"],
    date_format: str = "iso",
    odds_format: str = "decimal",
    event_ids: list = None,
    bookmakers: list = None,
):
    """Make a GET request to the event odds endpoint for The Odds API.

    See: https://the-odds-api.com/liveapi/guides/v4/#get-event-odds.

    Parameters
    ----------
    api_key : str
        A valid The Odds API API key.
    event_id: str
        The id of an upcoming or live game. Event ids can be found in the "id" field in the response of a get_odds() call.
    sport : str, optional
        A sport key. See a list of available keys with get_sports(), by default "upcoming"
    regions : list, optional
        A list of regions to include bookmakers from, by default ["us", "us2", "uk", "au", "eu"]
    markets : list, optional
        A list of which odds markets to return. Valid markets are "h2h" (moneyline), "spreads" (points handicaps), "totals" (over/under) and "outrights" (futures), by default ["h2h"]
    date_format : str, optional
        A string specifying the desired format of the timestamps in the response. Valid formats are "unix" and "iso", by default "iso"
    odds_format : str, optional
        A string specifying the desired format of the odds in the response. Valid formats are "decimal" and "american", by default "decimal"
    event_ids : list, optional
        A list of game ids to filter the response by, by default None
    bookmakers : list, optional
        A list of bookmakers to filter the response by, by default None

    Returns
    -------
    dict
        The return of the GET request.
    """

    return get_request(
        endpoint="event_odds",
        api_key=api_key,
        event_id=event_id,
        sport=sport,
        regions=regions,
        markets=markets,
        date_format=date_format,
        odds_format=odds_format,
        event_ids=event_ids,
        bookmakers=bookmakers,
    )
