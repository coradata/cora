# Adopting MITS when you report in REDI

You already report in **REDI**. You're taking on **MITS**. This briefing is generated from CORA's crosswalks: what you'll recognise, what's genuinely new, and — most importantly — where the two standards look equal but aren't.

- **9** concepts appear in both — recognise, but reconcile the caveats.
- **19** are new territory MITS carries that REDI never modelled.
- **5** stay home — REDI concepts MITS won't carry.

## ① Recognise, but reconcile (9)

Concepts both standards model. Rows flagged ⚠️ carry a `partial`/`divergent` mapping — the values look comparable but differ in scope or grain. Read the note before joining them.

| Concept | REDI | MITS | Watch out |
|---|---|---|---|
| ⚠️ market_rent | `Market_Rent_Next_12_Months` · 🔴 divergent | `UnitType/MarketRent` · 🟢 close | **REDI:** REDI ``Market_Rent_Next_12_Months`` is documented as "The total market rent under existing leases for year one of the DCF analysis (only total annual amounts should be provided)" — an annual aggregate across all leases, not a per-unit asking rent. Same *concept* (market-rate rent) but a different *grain* (fund / annual total vs unit / month) and a different *use case* (DCF input vs asking-rent display). Same posture as ``rent_amount`` for the REDI side — ``divergent``, not ``not_present``. |
| ⚠️ rent_amount | `Contract_Rent_Qtr` · 🔴 divergent | `UnitType/UnitRent` · 🟢 close | **REDI:** REDI ``Contract_Rent_Qtr`` is documented as "The total contract rent under existing leases for the reporting period" — a quarterly aggregate across all leases, not a per-lease monthly amount. Same *concept* (contractual rent receivable) but a different *grain* (fund / quarter vs unit / month). REDI also surfaces ``Contract_Rent_Next_12_Months`` for the year-one DCF projection. Consumers reconciling MITS / IBPDI per-unit rent against REDI portfolio aggregates need to sum and align reporting periods. |
| ⚠️ square_footage | `Net_Rentable_Area` · 🔴 divergent | `UnitType/MaxSquareFeet` · 🟡 partial | **REDI:** REDI ``Net_Rentable_Area`` is documented as "The total square foot / meter area that may be leased or rented to tenants. For multi-building assets, use the total net rentable area across all buildings" — an asset-level aggregate, not a per-unit area. Same grain mismatch as ``rent_amount`` / ``market_rent`` on the REDI side. REDI also surfaces ``Area_Size_Unit_of_Measurement`` for the unit (mapped under ``area_unit_of_measurement``). **MITS:** MITS ``UnitType`` represents a floor-plan class (one record per floor plan, not per physical unit). Size is expressed as the range ``UnitType/MinSquareFeet`` … ``UnitType/MaxSquareFeet``, with ``UnitType/SquareFootType`` controlling whether to display the min, max, or both. The crosswalk pins the upper bound (``MaxSquareFeet``) as the canonical single field; consumers reconstructing a single "size" value should consult ``SquareFootType`` and pick accordingly. Confidence ``partial`` reflects the range-vs-scalar shape mismatch and the implicit unit (square feet, as called out in ``area_unit_of_measurement``). |
| ⚠️ state_province | `State_Province` · 🟢 exact | `AddressType/State` · 🟡 partial | **MITS:** MITS calls the field ``State`` (U.S.-flavored naming) and constrains the range to ``StringMax3Type`` — a string capped at three characters, which fits U.S. state codes (``CA``, ``TX``) and Canadian province codes (``ON``, ``QC``) but not longer subnational names (e.g. Japanese prefectures spelled out, or German Länder names). Same concept as the canonical, narrower data-typing — ``partial`` rather than ``exact``. |
| city | `City_Town` · 🟢 exact | `AddressType/City` · 🟢 exact |  |
| country | `Country` · 🟢 exact | `AddressType/Country` · 🟢 exact |  |
| email_address | `Contact_Email_Address` · 🟢 close | `PersonType/Email` · 🟢 close |  |
| postal_code | `Zip_Postal_Code` · 🟢 exact | `AddressType/PostalCode` · 🟢 exact |  |
| street_address | `Street_Address` · 🟢 close | `AddressType/AddressLine1` · 🟢 close |  |

## ② New territory (19)

Concepts MITS carries that REDI never modelled — data you'll be handling for the first time.

| Concept | MITS | What it means |
|---|---|---|
| bathroom_count | `UnitType/UnitBathrooms` · 🟢 close | The number of bathrooms in a residential unit. May be fractional (e.g., "1.5" for a unit with one full and one half-bath). |
| bedroom_count | `UnitType/UnitBedrooms` · 🟢 close | The number of bedrooms in a residential unit. May be fractional in some standards (e.g., "0" for a studio, "1.5" for a one-bedroom-plus-den). |
| building_id | `ChargeDetail/BuildingID` · 🟢 close | The unique identifier of a physical building within a property, portfolio, or asset hierarchy — the primary key the source standard uses to refer to the building across modules and across systems. Typically a string assigned by the property-management or asset-management system of record. |
| currency | `CurrencyRangeType/Currency` · 🟢 close | The currency in which a monetary value or financial obligation is denominated. The conventional machine representation is an ISO 4217 three-letter code (e.g., ``USD``, ``EUR``, ``GBP``); some sources accept the currency name as free text. |
| first_name | `NameType/FirstName` · 🟢 exact | The given name (forename) of a person — the name component conventionally preceding the family name in Western naming order. Excludes prefixes (Mr., Dr.), middle names, last names, and suffixes (Jr., III). |
| job_title | `C_EmployerType/JobTitle` · 🟢 close | The professional role or position a person holds with an employer, organization, or other affiliated entity. Free-form text rather than a controlled vocabulary; used to address the person correctly and to record occupational context. |
| last_name | `NameType/LastName` · 🟢 exact | The family name (surname) of a person — the name component conventionally following the given name in Western naming order. Excludes prefixes (Mr., Dr.), middle names, first names, and suffixes (Jr., III). |
| lease_end_date | `LeaseType/ExpectedMoveOutDate` · 🟡 partial | The date on which a lease or rental contract terminates. Distinct from the start date and from any actual move-out date (which may differ from the contractually agreed end). |
| lease_start_date | `LeaseType/ExpectedMoveInDate` · 🟡 partial | The date on which a lease or rental contract becomes effective. Distinct from the end date and from any actual move-in date (which may differ from the contractually agreed start). |
| move_in_date | `LeaseType/ActualMoveIn` · 🟢 close | The date on which a resident or tenant actually took occupancy of a leased unit or space. Distinct from the contractual lease start date, which may precede or follow the observed move-in. |
| move_out_date | `LeaseType/ActualMoveOut` · 🟢 close | The date on which a resident or tenant actually vacated a leased unit or space. Distinct from the contractual lease end date, which may precede or follow the observed move-out. |
| organisation_id | `CorporateID/IDNumber` · 🟢 close | The unique identifier of an organisation — a company, fund manager, service provider, vendor, or other institutional entity referenced by other records in the corpus. The identifier is typically a string assigned by the system of record and used as a foreign key from contacts, properties, contracts, and related entities. |
| payment_frequency | `CharacteristicsType/PaymentFrequency` · 🟢 exact | The cadence at which a recurring payment obligation falls due — weekly, bi-weekly, monthly, quarterly, semi-annually, annually, or another value from a controlled vocabulary the source defines. |
| phone_number | `PhoneType/PhoneNumber` · 🟢 close | A telephone number used to reach a person, company, or property — a digit string typically formatted per ITU-T E.164 or a national convention. Does not constrain ownership semantics (personal vs shared vs role-based). |
| serial_number | `Device/SerialNumber` · 🟢 exact | A unique identifier assigned by the manufacturer (or another authoritative party) to a single instance of a physical piece of equipment — building components, devices, fixtures, or other assets that need to be tracked individually for maintenance, warranty, or compliance. |
| space_number | `AdditionalSpace/SpaceNumber` · 🟢 exact | An identifier for a discrete space within a building or property — a room, unit, parking space, storage space, or other addressable location. Often numeric or alphanumeric and unique within its containing aggregate. |
| space_type | `AdditionalSpace/SpaceType` · 🟢 exact | The category or function of a discrete space within a building — office, retail, residential unit, common area, storage, parking, or another value from a controlled vocabulary the source defines. Used to organize spaces by use class for reporting, leasing, and operational purposes. |
| transaction_id | `ChargeDetail/TransactionID` · 🟢 close | A unique identifier for a single financial transaction record — a posting, charge, payment, or other booking. The identifier is opaque to consumers; ownership and namespace semantics are defined by the source system. |
| unit_id | `ServiceDetail/UnitID` · 🟢 close | The unique identifier of a rentable unit within a property or building — the primary key the source standard uses to refer to the unit across modules and across systems. Typically a string assigned by the property-management or asset-management system of record. |

## ③ Stays home (5)

Your REDI concepts MITS won't carry — they remain yours to report.

- accounting_standard (`Accounting_Standard`)
- area_unit_of_measurement (`Area_Size_Unit_of_Measurement`)
- discount_rate (`Discount_Rate`)
- investment_type (`Investment_Type`)
- ownership_type (`Ownership_Type`)

## ④ Coverage and what's missing

CORA maps **9** concept(s) across both REDI and MITS today. Coverage is partial and grows with the editorial corpus — this briefing reflects only what's mapped, not everything the journey needs. For candidate concepts not yet covered, see the [suggestions report](https://github.com/coradata/cora/blob/main/docs/concepts-analysis/suggestions.md); to ask for one, [request a crosswalk](https://github.com/coradata/cora/blob/main/docs/site/docs/requesting-a-crosswalk.md).

_Generated by `cora docs build`. Do not edit by hand — regenerate when the underlying inventories or crosswalks change._
