# Adopting IBPDI when you report in MITS

You already report in **MITS**. You're taking on **IBPDI**. This briefing is generated from CORA's crosswalks: what you'll recognise, what's genuinely new, and — most importantly — where the two standards look equal but aren't.

- **20** concepts appear in both — recognise, but reconcile the caveats.
- **5** are new territory IBPDI carries that MITS never modelled.
- **8** stay home — MITS concepts IBPDI won't carry.

## ① Recognise, but reconcile (20)

Concepts both standards model. Rows flagged ⚠️ carry a `partial`/`divergent` mapping — the values look comparable but differ in scope or grain. Read the note before joining them.

| Concept | MITS | IBPDI | Watch out |
|---|---|---|---|
| ⚠️ lease_end_date | `LeaseType/ExpectedMoveOutDate` · 🟡 partial | `RentalContract/RentEndDate` · 🟢 close | **MITS:** MITS distinguishes ``ExpectedMoveOutDate`` (contractual / planned) from ``ActualMoveOut`` (observed). The crosswalk targets the contractual end — consumers wanting move-out-as-observed should reference ``ActualMoveOut``. Confidence ``partial`` reflects this contractual-vs-observed ambiguity. |
| ⚠️ lease_start_date | `LeaseType/ExpectedMoveInDate` · 🟡 partial | `RentalContract/RentBeginDate` · 🟢 close | **MITS:** MITS distinguishes ``ExpectedMoveInDate`` (contractual / planned) from ``ActualMoveIn`` (observed occupancy). The crosswalk targets the contractual start — consumers wanting move-in-as-observed should reference ``ActualMoveIn`` (also surfaced as the dedicated ``move_in_date`` crosswalk). Confidence ``partial`` reflects this contractual-vs-observed ambiguity; same shape as ``lease_end_date``. |
| ⚠️ state_province | `AddressType/State` · 🟡 partial | `Address/StateProvincePrefecture` · 🟢 exact | **MITS:** MITS calls the field ``State`` (U.S.-flavored naming) and constrains the range to ``StringMax3Type`` — a string capped at three characters, which fits U.S. state codes (``CA``, ``TX``) and Canadian province codes (``ON``, ``QC``) but not longer subnational names (e.g. Japanese prefectures spelled out, or German Länder names). Same concept as the canonical, narrower data-typing — ``partial`` rather than ``exact``. |
| ⚠️ street_address | `AddressType/AddressLine1` · 🟢 close | `Address/StreetName` · 🟡 partial | **IBPDI:** IBPDI splits an address into ``StreetName``, ``HouseNumber``, and ``HouseNumberSupplement`` rather than carrying a single composed first line. Mapped to ``StreetName`` as the closest single-field equivalent; consumers reconstructing a one-line address would concat the three. |
| building_id | `ChargeDetail/BuildingID` · 🟢 close | `Building/BuildingId` · 🟢 exact |  |
| city | `AddressType/City` · 🟢 exact | `Address/City` · 🟢 exact |  |
| country | `AddressType/Country` · 🟢 exact | `Address/Country` · 🟢 exact |  |
| currency | `CurrencyRangeType/Currency` · 🟢 close | `Portfolio/Currency` · 🟢 exact |  |
| first_name | `NameType/FirstName` · 🟢 exact | `Contact/FirstName` · 🟢 exact |  |
| job_title | `C_EmployerType/JobTitle` · 🟢 close | `Contact/JobTitle` · 🟢 exact |  |
| last_name | `NameType/LastName` · 🟢 exact | `Contact/LastName` · 🟢 exact |  |
| organisation_id | `CorporateID/IDNumber` · 🟢 close | `Contact/OrganisationId` · 🟢 exact |  |
| payment_frequency | `CharacteristicsType/PaymentFrequency` · 🟢 exact | `RentalContract/PaymentFrequency` · 🟢 exact |  |
| postal_code | `AddressType/PostalCode` · 🟢 exact | `Address/PostalCode` · 🟢 exact |  |
| rent_amount | `UnitType/UnitRent` · 🟢 close | `RentalPayment/ValueMonth` · 🟢 close |  |
| serial_number | `Device/SerialNumber` · 🟢 exact | `Component/SerialNumber` · 🟢 exact |  |
| space_number | `AdditionalSpace/SpaceNumber` · 🟢 exact | `Space/SpaceNumber` · 🟢 exact |  |
| space_type | `AdditionalSpace/SpaceType` · 🟢 exact | `EmissionFactor/SpaceType` · 🟢 exact |  |
| transaction_id | `ChargeDetail/TransactionID` · 🟢 close | `Transaction/TransactionId` · 🟢 exact |  |
| unit_id | `ServiceDetail/UnitID` · 🟢 close | `Unit/UnitId` · 🟢 exact |  |

## ② New territory (5)

Concepts IBPDI carries that MITS never modelled — data you'll be handling for the first time.

| Concept | IBPDI | What it means |
|---|---|---|
| accounting_standard | `Valuation/AccountingStandard` · 🟢 exact | The accounting framework used to prepare an entity's financial statements — for example IFRS, IFRS-EU, US GAAP, Luxembourg GAAP, or another national framework. Free-form text or controlled vocabulary depending on the source. |
| area_unit_of_measurement | `AreaMeasurement/Unit` · 🟢 exact | The unit in which an area or floor-size measurement is expressed — square feet, square metres, square yards, or another jurisdictional standard. Typically a controlled-vocabulary value the source defines. |
| discount_rate | `Valuation/DiscountRate` · 🟢 exact | The rate used to discount future cash flows to a present value during valuation — the cost of capital or required rate of return applied to an asset's projected cash flow series in DCF or fair-value modeling. Expressed as a percentage. |
| investment_type | `PortfolioStrategy/InvestmentType` · 🟢 exact | The category of investment strategy a fund or portfolio pursues — typically a controlled-vocabulary value such as core, value-add, opportunistic, debt, equity, or another classification the source defines. |
| ownership_type | `Portfolio/OwnershipType` · 🟢 exact | The legal ownership structure of an asset, portfolio, or holding — typically freehold, leasehold, joint venture, fund-of-funds, or another category from a controlled vocabulary the source defines. |

## ③ Stays home (8)

Your MITS concepts IBPDI won't carry — they remain yours to report.

- bathroom_count (`UnitType/UnitBathrooms`)
- bedroom_count (`UnitType/UnitBedrooms`)
- email_address (`PersonType/Email`)
- market_rent (`UnitType/MarketRent`)
- move_in_date (`LeaseType/ActualMoveIn`)
- move_out_date (`LeaseType/ActualMoveOut`)
- phone_number (`PhoneType/PhoneNumber`)
- square_footage (`UnitType/MaxSquareFeet`)

## ④ Coverage and what's missing

CORA maps **20** concept(s) across both MITS and IBPDI today. Coverage is partial and grows with the editorial corpus — this briefing reflects only what's mapped, not everything the journey needs. For candidate concepts not yet covered, see the [suggestions report](https://github.com/coradata/cora/blob/main/docs/concepts-analysis/suggestions.md); to ask for one, [request a crosswalk](https://github.com/coradata/cora/blob/main/docs/site/docs/requesting-a-crosswalk.md).

_Generated by `cora docs build`. Do not edit by hand — regenerate when the underlying inventories or crosswalks change._
