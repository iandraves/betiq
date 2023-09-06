from .caller import get_request


def get_scores(
    api_key: str,
    sport: str,
    days_from: int = None,
    date_format: str = "iso",
    event_ids: list = None,
) -> dict:
    """Make a GET request to the scores endpoint for The Odds API.

    See: https://the-odds-api.com/liveapi/guides/v4/#get-scores.

    Parameters
    ----------
    api_key : str
        A valid The Odds API API key.
    sport : str
        A sport key. See a list of available keys with get_sports()
    days_from : int, optional
        A number 1 to 3 specifying the number of days ine the past from which to return completed games, by default None
    date_format : str, optional
        A string specifying the desired format of the timestamps in the response. Valid formats are "unix" and "iso", by default "iso"
    event_ids : list, optional
        A list of game ids to filter the response by, by default None

    Returns
    -------
    dict
        The return of the GET request.
    """

    return get_request(
        endpoint="scores",
        api_key=api_key,
        sport=sport,
        days_from=days_from,
        date_format=date_format,
        event_ids=event_ids,
    )
