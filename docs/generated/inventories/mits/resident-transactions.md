# MITS / resident-transactions

| Key | Value |
|---|---|
| Source artifact | `standards/mits/current/native/Resident-Transactions-3.0/Resident-Transactions-Schema-Version-3.0-xsd1.xml` |
| Version | 3.0 |
| Extractor | `cora_extractors.xsd@0.0.0` |
| Source label | `xsd` |
| Types | 24 |
| Fields | 135 |
| Unmatched enrichments | 136 |

## Types

| Name | Extends | Abstract | Definition |
|---|---|---|---|
| AddressType |  |  |  |
| ChargeDetail |  |  |  |
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
| ServiceDetail |  |  |  |
| UnitType | Identifiable |  |  |
| UnitsType |  |  |  |

## Fields

| Path | Domain | Range | Cardinality | Definition |
|---|---|---|---|---|
| AddressType/AddressLine1 | AddressType | StringMax100Type | optional |  |
| AddressType/AddressLine2 | AddressType | StringMax100Type | optional |  |
| AddressType/AddressType | AddressType | AddressInfo | required |  |
| AddressType/City | AddressType | StringMax60Type | optional |  |
| AddressType/Country | AddressType | StringMax50Type | optional |  |
| AddressType/CountyName | AddressType | StringMax60Type | optional |  |
| AddressType/Description | AddressType | StringMax100Type | optional |  |
| AddressType/PostalCode | AddressType | StringMax12Type | optional |  |
| AddressType/Province | AddressType | StringMax60Type | optional |  |
| AddressType/State | AddressType | StringMax3Type | optional |  |
| AddressType/UnparsedAddress | AddressType | StringMax500Type | optional |  |
| ChargeDetail/Amount | ChargeDetail | xs:decimal | optional |  |
| ChargeDetail/AmountPaid | ChargeDetail | xs:decimal | optional |  |
| ChargeDetail/BalanceDue | ChargeDetail | xs:decimal | optional |  |
| ChargeDetail/BankBook | ChargeDetail | xs:string | optional |  |
| ChargeDetail/BatchID | ChargeDetail |  | optional | Specialized ID - Left as a string element. |
| ChargeDetail/BuildingID | ChargeDetail | IdentificationType | optional | Left for backwards compatibility to ver 2.0 and will be removed in future versions. SupplementalID should be used. |
| ChargeDetail/ChargeCode | ChargeDetail |  | optional |  |
| ChargeDetail/Comment | ChargeDetail |  | optional |  |
| ChargeDetail/CustomerID | ChargeDetail | IdentificationType | optional | Left for backwards compatibility to ver 2.0 and will be removed in future versions. SupplementalID should be used. |
| ChargeDetail/Description | ChargeDetail |  | optional |  |
| ChargeDetail/GLAccountNumber | ChargeDetail |  | optional | General ledger account number |
| ChargeDetail/InvoiceNumber | ChargeDetail |  | optional |  |
| ChargeDetail/PaidBy | ChargeDetail | xs:string | optional |  |
| ChargeDetail/PropertyPrimaryID | ChargeDetail | IdentificationType | optional | Left for backwards compatibility to ver 2.0 and will be removed in future versions. SupplementalID should be used. |
| ChargeDetail/Reversal | ChargeDetail |  | optional |  |
| ChargeDetail/ReversalDescription | ChargeDetail |  | optional |  |
| ChargeDetail/ReversalTranID | ChargeDetail |  | optional | Specialized ID - Left as a string element. |
| ChargeDetail/Service | ChargeDetail |  | optional |  |
| ChargeDetail/ServiceFromDate | ChargeDetail | xs:date | optional |  |
| ChargeDetail/ServiceToDate | ChargeDetail | xs:date | optional |  |
| ChargeDetail/SupplementalID | ChargeDetail | IdentificationType | optional | New IDType node to house additional needed ID's |
| ChargeDetail/TransactionDate | ChargeDetail | xs:date | optional |  |
| ChargeDetail/TransactionID | ChargeDetail |  | optional | Specialized ID - Left as a string element. |
| ChargeDetail/UnitID | ChargeDetail | IdentificationType | optional | Left for backwards compatibility to ver 2.0 and will be removed in future versions. SupplementalID should be used. |
| CompaniesType/Company | CompaniesType | CompanyType | repeating |  |
| CompanyContactType/CompanyContacts | CompanyContactType | CompanyContactsType | optional |  |
| CompanyContactType/CompanyRef | CompanyContactType | Identifiable | optional |  |
| CompanyContactType/CompanyRole | CompanyContactType | CompanyRoleType | optional |  |
| CompanyContactsType/CompanyContact | CompanyContactsType | CompanyPersonContactType | repeating |  |
| CompanyPersonContactType/PersonContactRef | CompanyPersonContactType | Identifiable | required |  |
| CompanyPersonContactType/PersonContactRole | CompanyPersonContactType | PersonCompanyRoleType | required |  |
| CompanyType/Address | CompanyType | AddressType | repeating | PO Box or Street number, direction, street name, suffix |
| CompanyType/CompanyName | CompanyType | StringMax50Type | required | Name of company |
| CompanyType/Email | CompanyType | StringMax80Type | optional | Email address |
| CompanyType/Logo | CompanyType | StringMax100Type | optional | Logo |
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
| Identification/IDRank | Identification | IDRank | optional | Ranking value |
| Identification/IDScopeType | Identification | IDScopeType | optional | Where ID originates from |
| Identification/IDType | Identification | StringMax50Type | optional | ID Type attribute should mirror the element it describes or be used as an IDRef for a Company or Person in Contacts |
| Identification/IDValue | Identification | xs:string | required | Actual ID value |
| Identification/OrganizationName | Identification | xs:string | optional | Defines the ID Scope in terms of sender, receiver, or other third party |
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
| PersonType/Address | PersonType | AddressType | repeating | PO Box or Street number, direction, street name, suffix |
| PersonType/Email | PersonType | StringMax80Type | optional | Email address |
| PersonType/Name | PersonType | NameType | required |  |
| PersonType/Phone | PersonType | PhoneType | repeating |  |
| PersonsType/Person | PersonsType | PersonType | repeating |  |
| PhoneType/Extension | PhoneType | StringMax20Type | optional |  |
| PhoneType/PhoneDescription | PhoneType | StringMax50Type | optional |  |
| PhoneType/PhoneNumber | PhoneType | StringMax20Type | optional |  |
| PhoneType/PhoneType | PhoneType | PhoneInfo | required |  |
| PropertiesType/Property | PropertiesType | PropertyType | repeating |  |
| PropertyContactsType/PropertyContact | PropertyContactsType | CompanyContactType | repeating |  |
| PropertyType/APN | PropertyType | StringMax40Type | optional | APN |
| PropertyType/Address | PropertyType | AddressType | repeating | PO Box or Street number, direction, street name, suffix |
| PropertyType/Email | PropertyType | StringMax80Type | optional | Email address |
| PropertyType/LegalName | PropertyType | StringMax120Type | optional | Legal name of the property |
| PropertyType/MSA_Name | PropertyType | StringMax60Type | optional | MSA_Name |
| PropertyType/MSA_Number | PropertyType | xs:integer | optional | MSA_Number |
| PropertyType/MarketingName | PropertyType | StringMax120Type | required | Property name used for marketing purposes |
| PropertyType/Phone | PropertyType | PhoneType | repeating |  |
| PropertyType/StructureDescription | PropertyType | StringMax100Type | optional | Type of building; lowrise, highrise, etc. |
| PropertyType/WebSite | PropertyType | StringMax100Type | optional | URL of the property web site |
| ServiceDetail/Amount | ServiceDetail | xs:decimal | optional |  |
| ServiceDetail/BalanceForward | ServiceDetail | xs:decimal | optional |  |
| ServiceDetail/ChargeCode | ServiceDetail |  | optional |  |
| ServiceDetail/CustomerID | ServiceDetail | IdentificationType | optional | Left for backwards compatibility to ver 2.0 and will be removed in future versions. SupplementalID should be used. |
| ServiceDetail/Description | ServiceDetail |  | optional |  |
| ServiceDetail/GLAccountNumber | ServiceDetail |  | optional | general Ledger account number |
| ServiceDetail/Service | ServiceDetail |  | optional |  |
| ServiceDetail/SupplementalID | ServiceDetail | IdentificationType | optional | New IDType node to house additional needed ID's |
| ServiceDetail/UnitID | ServiceDetail | IdentificationType | optional | Left for backwards compatibility to ver 2.0 and will be removed in future versions. SupplementalID should be used. |
| UnitType/Address | UnitType | AddressType | repeating | PO Box or Street number, direction, street name, suffix |
| UnitType/BuildingName | UnitType | StringMax50Type | optional | Used in a case where buildings within a property are individually named |
| UnitType/FloorplanName | UnitType | StringMax50Type | optional | Name of Floorplan for this unit |
| UnitType/MarketRent | UnitType | Decimal7Digits2Fraction | optional | Market rent for this specific unit |
| UnitType/MarketingName | UnitType | StringMax120Type | optional | Name of the property as the property is presented in advertising and the marketplace |
| UnitType/MaxSquareFeet | UnitType | Integer5Digit | optional | Max Square ft. size of unit with a range of sizes |
| UnitType/MinSquareFeet | UnitType | Integer5Digit | optional | Minimum Square ft. size of units with a range of sizes |
| UnitType/NumberOccupants | UnitType | CurrentNumberOccupantsType | optional | Current number |
| UnitType/PhaseName | UnitType | StringMax50Type | optional | Name of Phase |
| UnitType/SquareFootType | UnitType | UnitSqftInfo | optional | Square foot of the unit as defined by the owner or manager |
| UnitType/UnitBathrooms | UnitType | Decimal4Digits2Fraction | optional | Number of bathrooms in unit |
| UnitType/UnitBedrooms | UnitType | Decimal4Digits2Fraction | optional | Number of bedrooms in unit |
| UnitType/UnitEconomicStatus | UnitType | UnitEconStatusInfo | optional | Economic status of the unit that describes the type of unit |
| UnitType/UnitEconomicStatusDescription | UnitType | StringMax100Type | optional | Description of Other Economic Status |
| UnitType/UnitLeasedStatus | UnitType | UnitLeaseStatusInfo | optional | Leased status of the unit |
| UnitType/UnitLeasedStatusDescription | UnitType | StringMax100Type | optional | Description of Other unit Leased Status |
| UnitType/UnitOccupancyStatus | UnitType | UnitOccpStatusInfo | optional | Occupied or Vacant Unit |
| UnitType/UnitRent | UnitType | Decimal7Digits2Fraction | optional | Unit effective rent |
| UnitType/UnitType | UnitType | StringMax50Type | optional |  |
| UnitsType/Unit | UnitsType | UnitType | repeating |  |

_Generated by `cora docs build`. Do not edit by hand — regenerate when the underlying inventories or crosswalks change._
