---

title: Consortial billing plugin

---

# Consortial billing plugin

This plugin is also known as the **Supporters plugin**.

The OLH model depends on a network of libraries and library consortia
voluntarily contributing to the OLH’s publishing activities. This plugin helps
publishers using Janeway to manage supporter records and carry out the annual
billing process.

## Configuration

There are a few things to configure before the plugin can be used.

>[!Note]
>Developers can import a sample configuration. See the plugin’s README.

### Currencies

Currencies should be set up so that each one can tie into data fetched from the
World Bank. Each one needs the official currency code, a display symbol, and
currency region.

The plugin currently supports three currency regions: 

* Euro area (EMU)
* United Kingdom (GBR)
* United States (USA)

Here are example currency setups for these three regions.

| Code | Symbol | Region         |
|------|--------|----------------|
| EUR  | €      | Euro area      |
| GBP  | £      | United Kingdom |
| USD  | $      | United States  |

Note that you do not have to enter the exchange rate. Fetch World Bank exchange
rate data to populate this number.

### Support levels

Create support levels and set their display order. Exactly one must be the
default level.

| Name     | Order | Default |
|----------|-------|---------|
| Platinum | 1     | N       |
| Gold     | 2     | N       |
| Silver   | 3     | N       |
| Bronze   | 4     | N       |
| Standard | 5     | Y       |

### Billing agents

Create at least one billing agent. You can designate local billing agents for
one country each. There also must be one default agent, which will be assigned
to supporters in all countries not covered by a local billing agent.

The redirect URL controls whether the user who fills out the signup form will
be redirected to the billing agent’s website to complete the process.

| Name    | Country | Redirect URL        | Default |
|---------|---------|---------------------|---------|
| Lyrasis | Canada  |                     | N       |
| Lyrasis | USA     |                     | N       |
| Jisc    | UK      | https://example.com | N       |
| OLH     |         |                     | Y       |

### Base bands

There should be one base band for each combination of these dimensions of the
data model:

- Support level
- Billing setup

Let’s say there are 5 support levels. And let’s say there are 3 countries served by
external billing agents, plus a default process where you bill the rest of the
countries, for a total of 4 billing setups. Then you should have 4 * 5 = 20 base bands.

| Country & agent    | Platinum | Gold    | Silver  | Bronze | Standard |
|--------------------|----------|---------|---------|--------|----------|
| US & Lyrasis       | $28,840  | $19,230 | $14,420 | $9,610 | $2,980   |
| Canada & Lyrasis   | $19,350  | $12,900 | $9,680  | $6,450 | $2,000   |
| UK & Jisc          | £15,000  | £10,000 | £7,500  | £5,000 | £1,550   |
| Germany etc. & OLH | €19,280  | €12,850 | €9,640  | €6,420 | €1,990   |

For how the size affects the fee, see **Supporter sizes**.

The other variable that will come into play with fees calculated from base
bands, especially with the default billing agent and countries around the
world, is the GNI per capita. The supporter will also see the fee converted
into their preferred currency, based on the
current exchange rate data.

### Supporter sizes

Supporter sizes affect the calculation of _**Standard** bands only_ by means of the
multiplier. If the base band is set to a medium supporter size, then a large
university will see a slightly higher fee, and small college or research
institute will see a smaller fee.

| Name   | Description          | Multiplier |
|--------|----------------------|------------|
| Large  | 10,000+ students     | 1.33       |
| Medium | 5,000-9,999 students | 1.00       |
| Small  | 0-4,999 students     | 0.66       |

### Getting World Bank data

To get the World Bank data for exchange rates and GNI per capita, go to the
**Annual Update** section of the **Manager** page. The buttons at the top of
that section will check for and load up the latest data.
