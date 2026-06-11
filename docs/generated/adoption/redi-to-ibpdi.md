# Adopting IBPDI when you report in REDI

You already report in **REDI**. You're taking on **IBPDI**. This briefing is generated from CORA's crosswalks: what you'll recognise, what's genuinely new, and — most importantly — where the two standards look equal but aren't.

- **11** concepts appear in both — recognise, but reconcile the caveats.
- **14** are new territory IBPDI carries that REDI never modelled.
- **3** stay home — REDI concepts IBPDI won't carry.

## ① Recognise, but reconcile (11)

Concepts both standards model. Rows flagged ⚠️ carry a `partial`/`divergent` mapping — the values look comparable but differ in scope or grain. Read the note before joining them.

| Concept | REDI | IBPDI | Watch out |
|---|---|---|---|
| ⚠️ rent_amount | `Contract_Rent_Qtr` · 🔴 divergent | `RentalPayment/ValueMonth` · 🟢 close | **REDI:** REDI ``Contract_Rent_Qtr`` is documented as "The total contract rent under existing leases for the reporting period" — a quarterly aggregate across all leases, not a per-lease monthly amount. Same *concept* (contractual rent receivable) but a different *grain* (fund / quarter vs unit / month). REDI also surfaces ``Contract_Rent_Next_12_Months`` for the year-one DCF projection. Consumers reconciling MITS / IBPDI per-unit rent against REDI portfolio aggregates need to sum and align reporting periods. |
| ⚠️ street_address | `Street_Address` · 🟢 close | `Address/StreetName` · 🟡 partial | **IBPDI:** IBPDI splits an address into ``StreetName``, ``HouseNumber``, and ``HouseNumberSupplement`` rather than carrying a single composed first line. Mapped to ``StreetName`` as the closest single-field equivalent; consumers reconstructing a one-line address would concat the three. |
| accounting_standard | `Accounting_Standard` · 🟢 exact | `Valuation/AccountingStandard` · 🟢 exact |  |
| area_unit_of_measurement | `Area_Size_Unit_of_Measurement` · 🟢 exact | `AreaMeasurement/Unit` · 🟢 exact |  |
| city | `City_Town` · 🟢 exact | `Address/City` · 🟢 exact |  |
| country | `Country` · 🟢 exact | `Address/Country` · 🟢 exact |  |
| discount_rate | `Discount_Rate` · 🟢 exact | `Valuation/DiscountRate` · 🟢 exact |  |
| investment_type | `Investment_Type` · 🟢 exact | `PortfolioStrategy/InvestmentType` · 🟢 exact |  |
| ownership_type | `Ownership_Type` · 🟢 exact | `Portfolio/OwnershipType` · 🟢 exact |  |
| postal_code | `Zip_Postal_Code` · 🟢 exact | `Address/PostalCode` · 🟢 exact |  |
| state_province | `State_Province` · 🟢 exact | `Address/StateProvincePrefecture` · 🟢 exact |  |

## ② New territory (14)

Concepts IBPDI carries that REDI never modelled — data you'll be handling for the first time.

| Concept | IBPDI | What it means |
|---|---|---|
| building_id | `Building/BuildingId` · 🟢 exact | The unique identifier of a physical building within a property, portfolio, or asset hierarchy — the primary key the source standard uses to refer to the building across modules and across systems. Typically a string assigned by the property-management or asset-management system of record. |
| currency | `Portfolio/Currency` · 🟢 exact | The currency in which a monetary value or financial obligation is denominated. The conventional machine representation is an ISO 4217 three-letter code (e.g., ``USD``, ``EUR``, ``GBP``); some sources accept the currency name as free text. |
| first_name | `Contact/FirstName` · 🟢 exact | The given name (forename) of a person — the name component conventionally preceding the family name in Western naming order. Excludes prefixes (Mr., Dr.), middle names, last names, and suffixes (Jr., III). |
| job_title | `Contact/JobTitle` · 🟢 exact | The professional role or position a person holds with an employer, organization, or other affiliated entity. Free-form text rather than a controlled vocabulary; used to address the person correctly and to record occupational context. |
| last_name | `Contact/LastName` · 🟢 exact | The family name (surname) of a person — the name component conventionally following the given name in Western naming order. Excludes prefixes (Mr., Dr.), middle names, first names, and suffixes (Jr., III). |
| lease_end_date | `RentalContract/RentEndDate` · 🟢 close | The date on which a lease or rental contract terminates. Distinct from the start date and from any actual move-out date (which may differ from the contractually agreed end). |
| lease_start_date | `RentalContract/RentBeginDate` · 🟢 close | The date on which a lease or rental contract becomes effective. Distinct from the end date and from any actual move-in date (which may differ from the contractually agreed start). |
| organisation_id | `Contact/OrganisationId` · 🟢 exact | The unique identifier of an organisation — a company, fund manager, service provider, vendor, or other institutional entity referenced by other records in the corpus. The identifier is typically a string assigned by the system of record and used as a foreign key from contacts, properties, contracts, and related entities. |
| payment_frequency | `RentalContract/PaymentFrequency` · 🟢 exact | The cadence at which a recurring payment obligation falls due — weekly, bi-weekly, monthly, quarterly, semi-annually, annually, or another value from a controlled vocabulary the source defines. |
| serial_number | `Component/SerialNumber` · 🟢 exact | A unique identifier assigned by the manufacturer (or another authoritative party) to a single instance of a physical piece of equipment — building components, devices, fixtures, or other assets that need to be tracked individually for maintenance, warranty, or compliance. |
| space_number | `Space/SpaceNumber` · 🟢 exact | An identifier for a discrete space within a building or property — a room, unit, parking space, storage space, or other addressable location. Often numeric or alphanumeric and unique within its containing aggregate. |
| space_type | `EmissionFactor/SpaceType` · 🟢 exact | The category or function of a discrete space within a building — office, retail, residential unit, common area, storage, parking, or another value from a controlled vocabulary the source defines. Used to organize spaces by use class for reporting, leasing, and operational purposes. |
| transaction_id | `Transaction/TransactionId` · 🟢 exact | A unique identifier for a single financial transaction record — a posting, charge, payment, or other booking. The identifier is opaque to consumers; ownership and namespace semantics are defined by the source system. |
| unit_id | `Unit/UnitId` · 🟢 exact | The unique identifier of a rentable unit within a property or building — the primary key the source standard uses to refer to the unit across modules and across systems. Typically a string assigned by the property-management or asset-management system of record. |

## ③ Stays home (3)

Your REDI concepts IBPDI won't carry — they remain yours to report.

- email_address (`Contact_Email_Address`)
- market_rent (`Market_Rent_Next_12_Months`)
- square_footage (`Net_Rentable_Area`)

## ④ Coverage and what's missing

CORA maps **11** concept(s) across both REDI and IBPDI today. Coverage is partial and grows with the editorial corpus — this briefing reflects only what's mapped, not everything the journey needs. For candidate concepts not yet covered, see the [suggestions report](https://github.com/coradata/cora/blob/main/docs/concepts-analysis/suggestions.md); to ask for one, [request a crosswalk](https://github.com/coradata/cora/blob/main/docs/site/docs/requesting-a-crosswalk.md).

_Generated by `cora docs build`. Do not edit by hand — regenerate when the underlying inventories or crosswalks change._
