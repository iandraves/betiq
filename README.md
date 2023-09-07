# betiq

[![CI](https://github.com/iandraves/betiq/actions/workflows/pypi-publish.yml/badge.svg)](https://github.com/iandraves/betiq/actions/workflows/pypi-publish.yml)

[![CI](https://github.com/iandraves/betiq/actions/workflows/docs-publish.yml/badge.svg)](https://github.com/iandraves/betiq/actions/workflows/docs-publish.yml)

An unofficial SDK for [The Odds API v4](https://the-odds-api.com/).

<img src="https://iandraves.github.io/betiq/_static/logo.png" alt="The Odds API logo" width="200"/>

## Installation

```bash
pip install betiq
```

## Usage

```py
import betiq

odds = betiq.get_odds(
    api_key={THE_ODDS_API_API_KEY},
    sports=["upcoming"],
    regions=["us", "us2", "uk", "au", "eu"],
    markets=["h2h"],
    date_format="iso",
    odds_format="decimal",
)

print(odds) # Dictionary with the latest odds data
```

## Documentation

[Read the docs](https://iandraves.github.io/betiq).