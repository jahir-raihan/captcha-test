# Automate data deletion  reqeust on whitepages.com - CloudFlare bypass

The main motive of this script was to automate the process of removing request  a persons data from whitepages.com

# Thought

Basically we use selenium for web automation, but some anti bots are not happy with it.
So in order to run our script successfully, we need something that can bypass anti-bot like cloud-flare check.

# Method to bypass

1. Used `undetected_chromedriver` package to bypass cloud-flare check on every step.

# Prerequisites

1. Python3 or above
2. Chrome driver [According to your device]
3. Install Chrome driver on Mac using [`brew install --cask chromedriver`] on terminal

## Packages required
1. `selenium`
2. `undetected_chromedriver`

# How to run
1. Navigate to script  folder in terminal
2. CD into `cd cloudflare-example`
3. Type `python3 solution.py` and hit Enter.
4. Or run it manually from a editor.
5. Change its inputs to use as you want


# Note

1. **Chrome version and driver versions should be compatible, else the script will break and will throw error.**
2. **High speed internet is required  as it installs chrome manager for every execution.**


# Recaptcha Bypass

There's a tons of ways to bypass/solve recaptcha, but the most convenient is to use an API to solve it by others

# Method to bypass

1. Used `2captcha-python` API to bypass recaptcha

# Prerequisites - Are same as before

## Packages required

1. Only `2captcha-python`

# How to Run

1. Navigate to script folder in terminal
2. CD into `captcha-example`
3. Type `python3 solution.py`
4. Or run it manually from a editor
5. Change its inputs to use as you want

# Note

1. **This package requires an API key, which you'll be required to buy**
2. **But the price is very little**
