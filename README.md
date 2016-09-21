# WeatherGetter
A Python snippet that would pull the current weather condition for a given location.

# Weather Explanation
The result of this program could be interpreted according to the following table
(A copy from <http://www.weather.gov/forecast-icons>)

| Output | Weather   |
| ------ | --------- |
| skc    | Clear     |
| few    | 25% cloud |
| sct    | 50% cloud |
| bkn    | 75% cloud |
| ovc    | Cloudy    |
| sn     | Snow      |
| ra_sn  | Rain snow |
| raip   | Icy rain  |
| fzra   | Freeze rain |
| ra_fzra | Freeze rain with rain |
| fzra_sn | Freeze rain with snow |
| ip     | Ice       |
| snip   | Snow Ice  |
| minus_ra | Light rain |
| ra     | Rain      |
| sh_ra  | Heavy rain |
| hi_shwrs | Shower in vicinity |
| tsra   | Thunderstorm |
| scttsra | Scattered Thunderstorm |
| hi_tsra | Thunderstorm in vicinity |
| fc     | Funnel cloud |
| tor    | Tornado   |
| du     | Dust      |
| fu     | Smoke     |
| cold   | Cold      |
| blizzard | Blizzard |
| fg     | Fog       |

Notes:
Add n prefix: use night version.
Add wind_ to skc to ovc: Use windy version.

The following weather icons have no night version.

| Output     | Weather           |
| ---------- | ----------------- |
| hur_warn   | Hurricane warning |
| hur_watch  | Hurricane watch   |
| ts_warn    | Tropical storm warning |
| ts_watch   | Tropical storm watch |
| ts_nowarn  | Tropical storm becoming hurricane |
| hz         | Haze              |
| hot        | Hot               |
