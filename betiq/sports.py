from caller import get_request


def get_sports(api_key: str, all: bool = False) -> dict:
    """Make a GET request to the sports endpoint for The Odds API.

    See: https://the-odds-api.com/liveapi/guides/v4/#get-sports.

    Parameters
    ----------
    api_key : str
        A valid The Odds API API key.
    all : bool
        Whether or not to include both in and out of season sports in the response, by default False

    Returns
    -------
    dict
        The return of the GET request.
    """
    return get_request(endpoint="sports", api_key=api_key, all=all)
