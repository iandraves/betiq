from caller import get_request


def get_historical_odds(
    api_key: str,
    sport: str = "upcoming",
    regions: list = ["us", "us2", "uk", "au", "eu"],
    markets: list = ["h2h"],
    date: str = None,
):
    """Make a GET request to the odds endpoint for The Odds API.

    See: https://the-odds-api.com/liveapi/guides/v4/#get-odds.

    Parameters
    ----------
    api_key : str
        A valid The Odds API API key.
    sport : str, optional
        A sport key. See a list of available keys with get_sports(), by default "upcoming"
    regions : list, optional
        A list of regions to include bookmakers from, by default ["us", "us2", "uk", "au", "eu"]
    markets : list, optional
        A list of which odds markets to return. Valid markets are "h2h" (moneyline), "spreads" (points handicaps), "totals" (over/under) and "outrights" (futures), by default ["h2h"]
    date : str, optional
        The timestamp of the data snapshot to be returned, specified in ISO8601 format, for example 2021-10-18T12:00:00Z, by default None

    Returns
    -------
    dict
        The return of the GET request.
    """

    return get_request(
        endpoint="historical_odds",
        api_key=api_key,
        sport=sport,
        regions=regions,
        markets=markets,
        date=date,
    )
