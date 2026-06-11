# Adopting MITS when you report in IBPDI

You already report in **IBPDI**. You're taking on **MITS**. This briefing is generated from CORA's crosswalks: what you'll recognise, what's genuinely new, and — most importantly — where the two standards look equal but aren't.

- **20** concepts appear in both — recognise, but reconcile the caveats.
- **8** are new territory MITS carries that IBPDI never modelled.
- **5** stay home — IBPDI concepts MITS won't carry.

## ① Recognise, but reconcile (20)

Concepts both standards model. Rows flagged ⚠️ carry a `partial`/`divergent` mapping — the values look comparable but differ in scope or grain. Read the note before joining them.

| Concept | IBPDI | MITS | Watch out |
|---|---|---|---|
| ⚠️ lease_end_date | `RentalContract/RentEndDate` · 🟢 close | `LeaseType/ExpectedMoveOutDate` · 🟡 partial | **MITS:** MITS distinguishes ``ExpectedMoveOutDate`` (contractual / planned) from ``ActualMoveOut`` (observed). The crosswalk targets the contractual end — consumers wanting move-out-as-observed should reference ``ActualMoveOut``. Confidence ``partial`` reflects this contractual-vs-observed ambiguity. |
| ⚠️ lease_start_date | `RentalContract/RentBeginDate` · 🟢 close | `LeaseType/ExpectedMoveInDate` · 🟡 partial | **MITS:** MITS distinguishes ``ExpectedMoveInDate`` (contractual / planned) from ``ActualMoveIn`` (observed occupancy). The crosswalk targets the contractual start — consumers wanting move-in-as-observed should reference ``ActualMoveIn`` (also surfaced as the dedicated ``move_in_date`` crosswalk). Confidence ``partial`` reflects this contractual-vs-observed ambiguity; same shape as ``lease_end_date``. |
| ⚠️ state_province | `Address/StateProvincePrefecture` · 🟢 exact | `AddressType/State` · 🟡 partial | **MITS:** MITS calls the field ``State`` (U.S.-flavored naming) and constrains the range to ``StringMax3Type`` — a string capped at three characters, which fits U.S. state codes (``CA``, ``TX``) and Canadian province codes (``ON``, ``QC``) but not longer subnational names (e.g. Japanese prefectures spelled out, or German Länder names). Same concept as the canonical, narrower data-typing — ``partial`` rather than ``exact``. |
| ⚠️ street_address | `Address/StreetName` · 🟡 partial | `AddressType/AddressLine1` · 🟢 close | **IBPDI:** IBPDI splits an address into ``StreetName``, ``HouseNumber``, and ``HouseNumberSupplement`` rather than carrying a single composed first line. Mapped to ``StreetName`` as the closest single-field equivalent; consumers reconstructing a one-line address would concat the three. |
| building_id | `Building/BuildingId` · 🟢 exact | `ChargeDetail/BuildingID` · 🟢 close |  |
| city | `Address/City` · 🟢 exact | `AddressType/City` · 🟢 exact |  |
| country | `Address/Country` · 🟢 exact | `AddressType/Country` · 🟢 exact |  |
| currency | `Portfolio/Currency` · 🟢 exact | `CurrencyRangeType/Currency` · 🟢 close |  |
| first_name | `Contact/FirstName` · 🟢 exact | `NameType/FirstName` · 🟢 exact |  |
| job_title | `Contact/JobTitle` · 🟢 exact | `C_EmployerType/JobTitle` · 🟢 close |  |
| last_name | `Contact/LastName` · 🟢 exact | `NameType/LastName` · 🟢 exact |  |
| organisation_id | `Contact/OrganisationId` · 🟢 exact | `CorporateID/IDNumber` · 🟢 close |  |
| payment_frequency | `RentalContract/PaymentFrequency` · 🟢 exact | `CharacteristicsType/PaymentFrequency` · 🟢 exact |  |
| postal_code | `Address/PostalCode` · 🟢 exact | `AddressType/PostalCode` · 🟢 exact |  |
| rent_amount | `RentalPayment/ValueMonth` · 🟢 close | `UnitType/UnitRent` · 🟢 close |  |
| serial_number | `Component/SerialNumber` · 🟢 exact | `Device/SerialNumber` · 🟢 exact |  |
| space_number | `Space/SpaceNumber` · 🟢 exact | `AdditionalSpace/SpaceNumber` · 🟢 exact |  |
| space_type | `EmissionFactor/SpaceType` · 🟢 exact | `AdditionalSpace/SpaceType` · 🟢 exact |  |
| transaction_id | `Transaction/TransactionId` · 🟢 exact | `ChargeDetail/TransactionID` · 🟢 close |  |
| unit_id | `Unit/UnitId` · 🟢 exact | `ServiceDetail/UnitID` · 🟢 close |  |

## ② New territory (8)

Concepts MITS carries that IBPDI never modelled — data you'll be handling for the first time.

| Concept | MITS | What it means |
|---|---|---|
| bathroom_count | `UnitType/UnitBathrooms` · 🟢 close | The number of bathrooms in a residential unit. May be fractional (e.g., "1.5" for a unit with one full and one half-bath). |
| bedroom_count | `UnitType/UnitBedrooms` · 🟢 close | The number of bedrooms in a residential unit. May be fractional in some standards (e.g., "0" for a studio, "1.5" for a one-bedroom-plus-den). |
| email_address | `PersonType/Email` · 🟢 close | An RFC 5321 / RFC 5322 electronic mail address (local-part @ domain) used to reach a person, organization, or role. Does not constrain ownership semantics (personal vs. shared vs. role inbox). |
| market_rent | `UnitType/MarketRent` · 🟢 close | The market / asking rent for a unit or space — what a comparable unit would lease for at current market terms. Distinct from the contracted rent under any existing lease (see ``rent_amount``). |
| move_in_date | `LeaseType/ActualMoveIn` · 🟢 close | The date on which a resident or tenant actually took occupancy of a leased unit or space. Distinct from the contractual lease start date, which may precede or follow the observed move-in. |
| move_out_date | `LeaseType/ActualMoveOut` · 🟢 close | The date on which a resident or tenant actually vacated a leased unit or space. Distinct from the contractual lease end date, which may precede or follow the observed move-out. |
| phone_number | `PhoneType/PhoneNumber` · 🟢 close | A telephone number used to reach a person, company, or property — a digit string typically formatted per ITU-T E.164 or a national convention. Does not constrain ownership semantics (personal vs shared vs role-based). |
| square_footage | `UnitType/MaxSquareFeet` · 🟡 partial | The physical area of a unit or rentable space, expressed as a numeric size. The companion unit-of-measurement concept (square feet, square metres, etc.) is mapped under ``area_unit_of_measurement``. |

## ③ Stays home (5)

Your IBPDI concepts MITS won't carry — they remain yours to report.

- accounting_standard (`Valuation/AccountingStandard`)
- area_unit_of_measurement (`AreaMeasurement/Unit`)
- discount_rate (`Valuation/DiscountRate`)
- investment_type (`PortfolioStrategy/InvestmentType`)
- ownership_type (`Portfolio/OwnershipType`)

## ④ Coverage and what's missing

CORA maps **20** concept(s) across both IBPDI and MITS today. Coverage is partial and grows with the editorial corpus — this briefing reflects only what's mapped, not everything the journey needs. For candidate concepts not yet covered, see the [suggestions report](https://github.com/coradata/cora/blob/main/docs/concepts-analysis/suggestions.md); to ask for one, [request a crosswalk](https://github.com/coradata/cora/blob/main/docs/site/docs/requesting-a-crosswalk.md).

_Generated by `cora docs build`. Do not edit by hand — regenerate when the underlying inventories or crosswalks change._
