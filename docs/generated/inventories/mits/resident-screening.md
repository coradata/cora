# MITS / resident-screening

| Key | Value |
|---|---|
| Source artifact | `standards/mits/current/native/Resident-Screening-3.0/Resident-Screening-3.0-xsd.xml` |
| Version | 3.0 |
| Extractor | `cora_extractors.xsd@0.0.0` |
| Source label | `xsd` |
| Types | 22 |
| Fields | 102 |
| Unmatched enrichments | 56 |

## Types

| Name | Extends | Abstract | Definition |
|---|---|---|---|
| AddressType |  |  |  |
| CompaniesType |  |  |  |
| CompanyContactType |  |  |  |
| CompanyContactsType |  |  |  |
| CompanyPersonContactType |  |  |  |
| CompanyType | Identifiable |  |  |
| ContactsType |  |  |  |
| CurrencyRangeType |  |  |  |
| CurrentNumberOccupantsType |  |  |  |
| Identifiable |  |  |  |
| Identification |  |  |  |
| LeaseType | Identifiable |  |  |
| NameType |  |  |  |
| NumericRangeType |  |  |  |
| PersonType | Identifiable |  |  |
| PersonsType |  |  |  |
| PhoneType |  |  |  |
| PropertiesType |  |  |  |
| PropertyContactsType |  |  |  |
| PropertyType | Identifiable |  |  |
| UnitType | Identifiable |  |  |
| UnitsType |  |  |  |

## Fields

| Path | Domain | Range | Cardinality | Definition |
|---|---|---|---|---|
| AddressType/AddressLine1 | AddressType | StringMax100Type | optional |  |
| AddressType/AddressLine2 | AddressType | StringMax100Type | optional |  |
| AddressType/AddressType | AddressType | AddressInfo | required |  |
| AddressType/City | AddressType | StringMax60Type | optional | City property is located in |
| AddressType/Country | AddressType | StringMax50Type | optional | Country property is located in |
| AddressType/CountyName | AddressType | StringMax60Type | optional | County common name |
| AddressType/Description | AddressType | StringMax100Type | optional | String description for Other Address Type |
| AddressType/PostalCode | AddressType | StringMax12Type | optional | Property postalcode |
| AddressType/Province | AddressType | StringMax60Type | optional | Province if not US property |
| AddressType/State | AddressType | StringMax3Type | optional | State property is located in (Three character state code) |
| AddressType/UnparsedAddress | AddressType | StringMax500Type | optional | Unparsed address |
| CompaniesType/Company | CompaniesType | CompanyType | repeating |  |
| CompanyContactType/CompanyContacts | CompanyContactType | CompanyContactsType | optional |  |
| CompanyContactType/CompanyRef | CompanyContactType | Identifiable | optional |  |
| CompanyContactType/CompanyRole | CompanyContactType | CompanyRoleType | optional |  |
| CompanyContactsType/CompanyContact | CompanyContactsType | CompanyPersonContactType | repeating |  |
| CompanyPersonContactType/PersonContactRef | CompanyPersonContactType | Identifiable | required |  |
| CompanyPersonContactType/PersonContactRole | CompanyPersonContactType | PersonCompanyRoleType | required |  |
| CompanyType/Address | CompanyType | AddressType | repeating |  |
| CompanyType/CompanyName | CompanyType | StringMax50Type | required |  |
| CompanyType/Email | CompanyType | StringMax80Type | optional |  |
| CompanyType/Logo | CompanyType | StringMax100Type | optional |  |
| CompanyType/Phone | CompanyType | PhoneType | repeating |  |
| CompanyType/WebSite | CompanyType | StringMax100Type | optional |  |
| ContactsType/Companies | ContactsType | CompaniesType | required |  |
| ContactsType/Persons | ContactsType | PersonsType | required |  |
| ContactsType/PropertyContacts | ContactsType | PropertyContactsType | required |  |
| CurrencyRangeType/Currency | CurrencyRangeType | Currency | optional |  |
| CurrencyRangeType/Exact | CurrencyRangeType | Money | optional |  |
| CurrencyRangeType/Max | CurrencyRangeType | Money | optional |  |
| CurrencyRangeType/Min | CurrencyRangeType | Money | optional |  |
| CurrentNumberOccupantsType/Child | CurrentNumberOccupantsType | xs:integer | optional |  |
| CurrentNumberOccupantsType/Total | CurrentNumberOccupantsType | xs:integer | required |  |
| Identifiable/Identification | Identifiable | Identification | repeating |  |
| Identification/IDRank | Identification | IDRank | optional |  |
| Identification/IDScopeType | Identification | IDScopeType | optional |  |
| Identification/IDType | Identification | StringMax50Type | optional |  |
| Identification/IDValue | Identification | xs:string | required |  |
| Identification/OrganizationName | Identification | xs:string | optional |  |
| LeaseType/AccountNumber | LeaseType | StringMax50Type | optional |  |
| LeaseType/ActualMoveIn | LeaseType | xs:date | optional |  |
| LeaseType/ActualMoveOut | LeaseType | xs:date | optional |  |
| LeaseType/CurrentNumberOccupants | LeaseType | CurrentNumberOccupantsType | optional |  |
| LeaseType/CurrentRent | LeaseType | xs:decimal | optional |  |
| LeaseType/ExpectedMoveInDate | LeaseType | xs:date | optional |  |
| LeaseType/ExpectedMoveOutDate | LeaseType | xs:date | optional |  |
| LeaseType/LeaseFromDate | LeaseType | xs:date | optional |  |
| LeaseType/LeaseSignDate | LeaseType | xs:date | optional |  |
| LeaseType/LeaseToDate | LeaseType | xs:date | optional |  |
| LeaseType/PaymentAccepted | LeaseType | StringMax50Type | optional |  |
| LeaseType/ResponsibleForLease | LeaseType | xs:boolean | optional |  |
| LeaseType/SpecialStatus | LeaseType | StringMax50Type | optional |  |
| NameType/FirstName | NameType | StringMax50Type | required |  |
| NameType/LastName | NameType | StringMax50Type | required |  |
| NameType/MaidenName | NameType | StringMax50Type | optional |  |
| NameType/MiddleName | NameType | StringMax50Type | optional |  |
| NameType/NamePrefix | NameType | StringMax50Type | optional |  |
| NameType/NameSuffix | NameType | StringMax50Type | optional |  |
| NumericRangeType/Exact | NumericRangeType | xs:integer | optional |  |
| NumericRangeType/Max | NumericRangeType | xs:integer | optional |  |
| NumericRangeType/Min | NumericRangeType | xs:integer | optional |  |
| PersonType/Address | PersonType | AddressType | repeating |  |
| PersonType/Email | PersonType | StringMax80Type | optional |  |
| PersonType/Name | PersonType | NameType | required |  |
| PersonType/Phone | PersonType | PhoneType | repeating |  |
| PersonsType/Person | PersonsType | PersonType | repeating |  |
| PhoneType/Extension | PhoneType | StringMax20Type | optional |  |
| PhoneType/PhoneDescription | PhoneType | StringMax50Type | optional |  |
| PhoneType/PhoneNumber | PhoneType | StringMax20Type | optional |  |
| PhoneType/PhoneType | PhoneType | PhoneInfo | required |  |
| PropertiesType/Property | PropertiesType | PropertyType | repeating |  |
| PropertyContactsType/PropertyContact | PropertyContactsType | CompanyContactType | repeating |  |
| PropertyType/APN | PropertyType | StringMax40Type | optional |  |
| PropertyType/Address | PropertyType | AddressType | repeating |  |
| PropertyType/Email | PropertyType | StringMax80Type | optional |  |
| PropertyType/LegalName | PropertyType | StringMax120Type | optional |  |
| PropertyType/MSA_Name | PropertyType | StringMax60Type | optional |  |
| PropertyType/MSA_Number | PropertyType | xs:integer | optional |  |
| PropertyType/MarketingName | PropertyType | StringMax120Type | required |  |
| PropertyType/Phone | PropertyType | PhoneType | repeating |  |
| PropertyType/StructureDescription | PropertyType | StringMax100Type | optional |  |
| PropertyType/WebSite | PropertyType | StringMax100Type | optional |  |
| UnitType/Address | UnitType | AddressType | repeating |  |
| UnitType/BuildingName | UnitType | StringMax50Type | optional |  |
| UnitType/FloorplanName | UnitType | StringMax50Type | optional |  |
| UnitType/MarketRent | UnitType | Decimal7Digits2Fraction | optional |  |
| UnitType/MarketingName | UnitType | StringMax120Type | optional |  |
| UnitType/MaxSquareFeet | UnitType | Integer5Digit | optional |  |
| UnitType/MinSquareFeet | UnitType | Integer5Digit | optional |  |
| UnitType/NumberOccupants | UnitType | CurrentNumberOccupantsType | optional |  |
| UnitType/PhaseName | UnitType | StringMax50Type | optional |  |
| UnitType/SquareFootType | UnitType | UnitSqftInfo | optional |  |
| UnitType/UnitBathrooms | UnitType | Decimal4Digits2Fraction | optional |  |
| UnitType/UnitBedrooms | UnitType | Decimal4Digits2Fraction | optional |  |
| UnitType/UnitEconomicStatus | UnitType | UnitEconStatusInfo | optional |  |
| UnitType/UnitEconomicStatusDescription | UnitType | StringMax100Type | optional |  |
| UnitType/UnitLeasedStatus | UnitType | UnitLeaseStatusInfo | optional |  |
| UnitType/UnitLeasedStatusDescription | UnitType | StringMax100Type | optional |  |
| UnitType/UnitOccupancyStatus | UnitType | UnitOccpStatusInfo | optional |  |
| UnitType/UnitRent | UnitType | Decimal7Digits2Fraction | optional |  |
| UnitType/UnitType | UnitType | StringMax50Type | optional |  |
| UnitsType/Unit | UnitsType | UnitType | repeating |  |

_Generated by `cora docs build`. Do not edit by hand — regenerate when the underlying inventories or crosswalks change._
