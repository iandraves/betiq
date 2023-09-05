# betiq

[![CI](https://github.com/iandraves/betiq/actions/workflows/python-publish.yml/badge.svg)](https://github.com/iandraves/betiq/actions/workflows/python-publish.yml)

[![CI](https://github.com/iandraves/betiq/actions/workflows/static.yml/badge.svg)](https://github.com/iandraves/betiq/actions/workflows/static.yml)

An unofficial SDK for [The Odds API v4](https://the-odds-api.com/).

<img src="https://iandraves.github.io/betiq/_static/logo.png" alt="The Odds API logo" width="200"/>

## Installation

```bash
pip install betiq
```

## Usage

```py
import betiq

odds = betiq.get_odds(api_key={THE_ODDS_API_API_KEY})

print(odds) # Dictionary with the latest odds data
```

## Documentation

[Read the docs](https://iandraves.github.io/betiq).