# MITS / lead-management

| Key | Value |
|---|---|
| Source artifact | `standards/mits/current/native/Lead-Management-4.0/Lead-Management-4.0.1-Schema-xsd.xml` |
| Version | 4.0.1 |
| Extractor | `cora_extractors.xsd@0.0.0` |
| Source label | `xsd` |
| Types | 28 |
| Fields | 136 |
| Unmatched enrichments | 28 |


## Types

| Name | Extends | Abstract | Definition |
|---|---|---|---|
| AdditionalPreference |  |  |  |
| AddressType |  |  |  |
| CallData |  |  |  |
| CompaniesType |  |  |  |
| CompanyContactType |  |  |  |
| CompanyContactsType |  |  |  |
| CompanyPersonContactType |  |  |  |
| CompanyType | Identifiable |  |  |
| ContactsType |  |  |  |
| CurrencyRangeType |  |  |  |
| CurrentNumberOccupantsType |  |  |  |
| EmailData |  |  |  |
| EventType |  |  | EventType |
| Identifiable |  |  |  |
| Identification |  |  |  |
| LeaseType | Identifiable |  |  |
| NameType |  |  |  |
| NumericRangeType |  |  |  |
| PersonType | Identifiable |  |  |
| PersonsType |  |  |  |
| PetType |  |  | Pet |
| PhoneType |  |  |  |
| PropertiesType |  |  |  |
| PropertyContactsType |  |  |  |
| PropertyType | Identifiable |  |  |
| SpecificAmenityType |  |  | Amenities that belongs to unit or floorplan level 11/28/06 |
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
| CallData/AudioLink | CallData | xs:string | optional | A link to the recorded conversation |
| CallData/CallFrom | CallData | xs:string | optional |  |
| CallData/CallStatus | CallData |  | optional | Answered, Not Answerd, etc |
| CallData/CallThrough | CallData | xs:string | optional | The number that is called |
| CallData/CallTracker | CallData | xs:string | optional | The name of the entity that has provided the tracking number |
| CallData/CallerId | CallData | Identification | optional |  |
| CallData/Duration | CallData | xs:string | optional | Length of the call |
| CallData/RingThrough | CallData | xs:string | optional | The number that rings on site |
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
| CurrencyRangeType/Exact | CurrencyRangeType | Money | optional | Exact |
| CurrencyRangeType/Max | CurrencyRangeType | Money | optional | Max |
| CurrencyRangeType/Min | CurrencyRangeType | Money | optional | Min |
| CurrentNumberOccupantsType/Child | CurrentNumberOccupantsType | xs:integer | optional |  |
| CurrentNumberOccupantsType/Total | CurrentNumberOccupantsType | xs:integer | required |  |
| EmailData/EmailAddresses | EmailData |  | required |  |
| EmailData/EmailBody | EmailData | xs:string | required | The contents of the email |
| EmailData/EmailDate | EmailData | xs:dateTime | optional |  |
| EmailData/IsHTML | EmailData | xs:boolean | optional | Boolean, was this email an HTML email |
| EmailData/MessageId | EmailData | xs:string | optional |  |
| EmailData/Subject | EmailData | xs:string | required | The subject of the email |
| EventType/Agent | EventType |  | optional | Person(on-site or not) or process that primarily performed the said event |
| EventType/CallData | EventType | CallData | optional | Information about a call specific action |
| EventType/Comments | EventType |  | optional | Comments about the event as made by the agent |
| EventType/EmailData | EventType | EmailData | optional | Information about a call specific action |
| EventType/EventDate | EventType | xs:dateTime | required |  |
| EventType/EventID | EventType | Identification | optional |  |
| EventType/EventReasons | EventType | xs:string | optional | Information about the event, such as reasons for failure to convert or reasons for leasing |
| EventType/EventType | EventType | EventTypes | required |  |
| EventType/FirstContact | EventType | xs:boolean | optional | The first contcat node denotes if the containing event node is the originating contact that has created this lead |
| EventType/Quotes | EventType |  | optional |  |
| EventType/TransactionSource | EventType |  | optional | TransactionSource contains the identification of the submitting system for this event. |
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
| NumericRangeType/Exact | NumericRangeType | xs:integer | optional | Exact |
| NumericRangeType/Max | NumericRangeType | xs:integer | optional | Max |
| NumericRangeType/Min | NumericRangeType | xs:integer | optional | Min |
| PersonType/Address | PersonType | AddressType | repeating | Element describs a (real-world or email) address |
| PersonType/Email | PersonType | StringMax80Type | optional |  |
| PersonType/Name | PersonType | NameType | required | Elements describing a persons name |
| PersonType/Phone | PersonType | PhoneType | repeating | Description, Number and Extension information for a phone contact |
| PersonsType/Person | PersonsType | PersonType | repeating |  |
| PetType/Count | PetType |  | required |  |
| PetType/Description | PetType |  | optional |  |
| PetType/PetType | PetType |  | required |  |
| PetType/Size | PetType |  | optional |  |
| PetType/Weight | PetType | xs:string | optional |  |
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
| SpecificAmenityType/AmenityType | SpecificAmenityType |  | required |  |
| SpecificAmenityType/Description | SpecificAmenityType |  | optional |  |
| SpecificAmenityType/Rank | SpecificAmenityType |  | optional |  |
| SpecificAmenityType/SubType | SpecificAmenityType |  | optional |  |
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
