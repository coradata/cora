# Adopting REDI when you report in MITS

You already report in **MITS**. You're taking on **REDI**. This briefing is generated from CORA's crosswalks: what you'll recognise, what's genuinely new, and — most importantly — where the two standards look equal but aren't.

- **9** concepts appear in both — recognise, but reconcile the caveats.
- **5** are new territory REDI carries that MITS never modelled.
- **19** stay home — MITS concepts REDI won't carry.

## ① Recognise, but reconcile (9)

Concepts both standards model. Rows flagged ⚠️ carry a `partial`/`divergent` mapping — the values look comparable but differ in scope or grain. Read the note before joining them.

| Concept | MITS | REDI | Watch out |
|---|---|---|---|
| ⚠️ market_rent | `UnitType/MarketRent` · 🟢 close | `Market_Rent_Next_12_Months` · 🔴 divergent | **REDI:** REDI ``Market_Rent_Next_12_Months`` is documented as "The total market rent under existing leases for year one of the DCF analysis (only total annual amounts should be provided)" — an annual aggregate across all leases, not a per-unit asking rent. Same *concept* (market-rate rent) but a different *grain* (fund / annual total vs unit / month) and a different *use case* (DCF input vs asking-rent display). Same posture as ``rent_amount`` for the REDI side — ``divergent``, not ``not_present``. |
| ⚠️ rent_amount | `UnitType/UnitRent` · 🟢 close | `Contract_Rent_Qtr` · 🔴 divergent | **REDI:** REDI ``Contract_Rent_Qtr`` is documented as "The total contract rent under existing leases for the reporting period" — a quarterly aggregate across all leases, not a per-lease monthly amount. Same *concept* (contractual rent receivable) but a different *grain* (fund / quarter vs unit / month). REDI also surfaces ``Contract_Rent_Next_12_Months`` for the year-one DCF projection. Consumers reconciling MITS / IBPDI per-unit rent against REDI portfolio aggregates need to sum and align reporting periods. |
| ⚠️ square_footage | `UnitType/MaxSquareFeet` · 🟡 partial | `Net_Rentable_Area` · 🔴 divergent | **MITS:** MITS ``UnitType`` represents a floor-plan class (one record per floor plan, not per physical unit). Size is expressed as the range ``UnitType/MinSquareFeet`` … ``UnitType/MaxSquareFeet``, with ``UnitType/SquareFootType`` controlling whether to display the min, max, or both. The crosswalk pins the upper bound (``MaxSquareFeet``) as the canonical single field; consumers reconstructing a single "size" value should consult ``SquareFootType`` and pick accordingly. Confidence ``partial`` reflects the range-vs-scalar shape mismatch and the implicit unit (square feet, as called out in ``area_unit_of_measurement``). **REDI:** REDI ``Net_Rentable_Area`` is documented as "The total square foot / meter area that may be leased or rented to tenants. For multi-building assets, use the total net rentable area across all buildings" — an asset-level aggregate, not a per-unit area. Same grain mismatch as ``rent_amount`` / ``market_rent`` on the REDI side. REDI also surfaces ``Area_Size_Unit_of_Measurement`` for the unit (mapped under ``area_unit_of_measurement``). |
| ⚠️ state_province | `AddressType/State` · 🟡 partial | `State_Province` · 🟢 exact | **MITS:** MITS calls the field ``State`` (U.S.-flavored naming) and constrains the range to ``StringMax3Type`` — a string capped at three characters, which fits U.S. state codes (``CA``, ``TX``) and Canadian province codes (``ON``, ``QC``) but not longer subnational names (e.g. Japanese prefectures spelled out, or German Länder names). Same concept as the canonical, narrower data-typing — ``partial`` rather than ``exact``. |
| city | `AddressType/City` · 🟢 exact | `City_Town` · 🟢 exact |  |
| country | `AddressType/Country` · 🟢 exact | `Country` · 🟢 exact |  |
| email_address | `PersonType/Email` · 🟢 close | `Contact_Email_Address` · 🟢 close |  |
| postal_code | `AddressType/PostalCode` · 🟢 exact | `Zip_Postal_Code` · 🟢 exact |  |
| street_address | `AddressType/AddressLine1` · 🟢 close | `Street_Address` · 🟢 close |  |

## ② New territory (5)

Concepts REDI carries that MITS never modelled — data you'll be handling for the first time.

| Concept | REDI | What it means |
|---|---|---|
| accounting_standard | `Accounting_Standard` · 🟢 exact | The accounting framework used to prepare an entity's financial statements — for example IFRS, IFRS-EU, US GAAP, Luxembourg GAAP, or another national framework. Free-form text or controlled vocabulary depending on the source. |
| area_unit_of_measurement | `Area_Size_Unit_of_Measurement` · 🟢 exact | The unit in which an area or floor-size measurement is expressed — square feet, square metres, square yards, or another jurisdictional standard. Typically a controlled-vocabulary value the source defines. |
| discount_rate | `Discount_Rate` · 🟢 exact | The rate used to discount future cash flows to a present value during valuation — the cost of capital or required rate of return applied to an asset's projected cash flow series in DCF or fair-value modeling. Expressed as a percentage. |
| investment_type | `Investment_Type` · 🟢 exact | The category of investment strategy a fund or portfolio pursues — typically a controlled-vocabulary value such as core, value-add, opportunistic, debt, equity, or another classification the source defines. |
| ownership_type | `Ownership_Type` · 🟢 exact | The legal ownership structure of an asset, portfolio, or holding — typically freehold, leasehold, joint venture, fund-of-funds, or another category from a controlled vocabulary the source defines. |

## ③ Stays home (19)

Your MITS concepts REDI won't carry — they remain yours to report.

- bathroom_count (`UnitType/UnitBathrooms`)
- bedroom_count (`UnitType/UnitBedrooms`)
- building_id (`ChargeDetail/BuildingID`)
- currency (`CurrencyRangeType/Currency`)
- first_name (`NameType/FirstName`)
- job_title (`C_EmployerType/JobTitle`)
- last_name (`NameType/LastName`)
- lease_end_date (`LeaseType/ExpectedMoveOutDate`)
- lease_start_date (`LeaseType/ExpectedMoveInDate`)
- move_in_date (`LeaseType/ActualMoveIn`)
- move_out_date (`LeaseType/ActualMoveOut`)
- organisation_id (`CorporateID/IDNumber`)
- payment_frequency (`CharacteristicsType/PaymentFrequency`)
- phone_number (`PhoneType/PhoneNumber`)
- serial_number (`Device/SerialNumber`)
- space_number (`AdditionalSpace/SpaceNumber`)
- space_type (`AdditionalSpace/SpaceType`)
- transaction_id (`ChargeDetail/TransactionID`)
- unit_id (`ServiceDetail/UnitID`)

## ④ Coverage and what's missing

CORA maps **9** concept(s) across both MITS and REDI today. Coverage is partial and grows with the editorial corpus — this briefing reflects only what's mapped, not everything the journey needs. For candidate concepts not yet covered, see the [suggestions report](https://github.com/coradata/cora/blob/main/docs/concepts-analysis/suggestions.md); to ask for one, [request a crosswalk](https://github.com/coradata/cora/blob/main/docs/site/docs/requesting-a-crosswalk.md).

_Generated by `cora docs build`. Do not edit by hand — regenerate when the underlying inventories or crosswalks change._
