from .caller import get_request


def get_quota_stats(api_key: str) -> dict:
    """Returns API usage stats dictionary with requests used and requests remaining.

    See: https://the-odds-api.com/liveapi/guides/v4/#response-headers.

    Parameters
    ----------
    api_key : str
        A valid The Odds API API key.

    Returns
    -------
    dict
        A dictionary with requests used and requests remaining for the usage period.
    """
    raw_quota_stats = get_request(endpoint="quota", api_key=api_key)

    cleaned_quota_stats = {
        "requests_used": raw_quota_stats.get("X-Requests-Used"),
        "requests_remaining": raw_quota_stats.get("X-Requests-Remaining"),
    }

    return cleaned_quota_stats


def get_requests_remaining(api_key: str) -> int:
    """Returns the number of requests remaining for the usage period.

    See: https://the-odds-api.com/liveapi/guides/v4/#response-headers.

    Parameters
    ----------
    api_key : str
        A valid The Odds API API key.

    Returns
    -------
    int
        The number of requests remaining for the usage period.
    """
    return get_quota_stats(api_key=api_key).get("requests_remaining")


def get_requests_used(api_key: str) -> int:
    """Returns the number of requests used for the usage period.

    See: https://the-odds-api.com/liveapi/guides/v4/#response-headers.

    Parameters
    ----------
    api_key : str
        A valid The Odds API API key.

    Returns
    -------
    int
        The number of requests used for the usage period.
    """
    return get_quota_stats(api_key=api_key).get("requests_used")
