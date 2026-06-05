# MITS / lease-application

| Key | Value |
|---|---|
| Source artifact | `standards/mits/current/native/Lease-Application-Standard-xsd.xml` |
| Version | 1.0 |
| Extractor | `cora_extractors.xsd@0.0.0` |
| Source label | `xsd` |
| Types | 67 |
| Fields | 266 |

## Types

| Name | Extends | Abstract | Definition |
|---|---|---|---|
| AccountingData |  |  | This type is a simple container for ChargeSet elements. |
| AdditionalSpace | IdentificationType |  |  |
| AddressType |  |  |  |
| Asset |  |  |  |
| BankAccount |  |  |  |
| BaseTenant | IdentificationType | ✓ |  |
| Charge | IdentificationType |  |  |
| ChargeSet |  |  |  |
| CompaniesType |  |  |  |
| CompanyContactType |  |  |  |
| CompanyContactsType |  |  |  |
| CompanyPersonContactType |  |  |  |
| CompanyType | Identifiable |  |  |
| ContactsType |  |  |  |
| CorporateID |  |  |  |
| CorporateTenant | BaseTenant |  |  |
| CriminalBackground |  |  |  |
| CriminalRecord |  |  |  |
| CurrencyRangeType |  |  |  |
| CurrentNumberOccupantsType |  |  |  |
| DatedCurrency |  |  |  |
| Device |  |  |  |
| Devices |  |  | This type is a simple container for Device elements. |
| Document | IdentificationType |  |  |
| DocumentData |  |  | This type is a simple container for DocumentField elements. |
| DocumentField | IdentificationType |  |  |
| Documents |  |  |  |
| Error | IdentificationType |  |  |
| Fee |  |  |  |
| Finances |  |  |  |
| Identifiable |  |  |  |
| Identification |  |  |  |
| IncomeSource | Salary |  |  |
| LA_Lease | IdentificationType |  |  |
| LeaseApplication |  |  |  |
| LeaseEvent |  |  |  |
| LeaseEvents |  |  |  |
| LeaseStatus |  |  |  |
| LeaseType | Identifiable |  |  |
| Name |  |  |  |
| NameType |  |  |  |
| NoContent |  |  |  |
| NumericRangeType |  |  |  |
| Occupation |  |  |  |
| ParkingStorage |  |  |  |
| PersonType | Identifiable |  |  |
| PersonalID |  |  |  |
| PersonsType |  |  |  |
| PetType |  |  |  |
| Pets |  |  |  |
| PhoneType |  |  |  |
| Policies |  |  |  |
| Policy |  |  |  |
| PropertiesType |  |  |  |
| PropertyContactsType |  |  |  |
| PropertyType | Identifiable |  |  |
| Reference |  |  |  |
| Residence |  |  |  |
| Salary |  |  |  |
| Signature | IdentificationType |  |  |
| Tenant | BaseTenant |  |  |
| UnitType | Identifiable |  |  |
| UnitsType |  |  |  |
| Utilities |  |  |  |
| Utility | IdentificationType |  |  |
| UtilityCommonArea |  |  |  |
| Vehicle |  |  |  |

## Fields

| Path | Domain | Range | Cardinality | Definition |
|---|---|---|---|---|
| AccountingData/ChargeSet | AccountingData | ChargeSet | repeating |  |
| AdditionalSpace/Address | AdditionalSpace | AddressType | optional |  |
| AdditionalSpace/Description | AdditionalSpace | xs:string | optional |  |
| AdditionalSpace/Private | AdditionalSpace | xs:boolean | optional |  |
| AdditionalSpace/SpaceNumber | AdditionalSpace | xs:string | optional |  |
| AdditionalSpace/SpaceType | AdditionalSpace | AdditionalSpaceType | required |  |
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
| Asset/AssetType | Asset | AssetType | optional |  |
| Asset/Description | Asset | xs:string | required |  |
| Asset/IsLiquid | Asset | xs:boolean | optional |  |
| Asset/Value | Asset | DatedCurrency | required |  |
| BankAccount/AccountNumber | BankAccount | StringMax50 | required |  |
| BankAccount/Balance | BankAccount | DatedCurrency | required |  |
| BankAccount/Bank | BankAccount | CompanyType | required |  |
| BaseTenant/AccountingData | BaseTenant | AccountingData | optional |  |
| BaseTenant/DocumentData | BaseTenant | DocumentData | optional |  |
| BaseTenant/LeaseID | BaseTenant | IdentificationType | repeating |  |
| BaseTenant/Reference | BaseTenant | Reference | repeating |  |
| Charge/Amount | Charge | MITS-Currency | required |  |
| Charge/ChargeType | Charge | ChargeType | required |  |
| Charge/Label | Charge | xs:string | optional |  |
| ChargeSet/Charge | ChargeSet | Charge | repeating |  |
| ChargeSet/End | ChargeSet | xs:date | optional |  |
| ChargeSet/Frequency | ChargeSet | Frequency | required |  |
| ChargeSet/Start | ChargeSet | xs:date | required |  |
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
| CorporateID/CorporateIDType | CorporateID | CorporateIDType | required |  |
| CorporateID/IDIssuer | CorporateID | xs:string | optional |  |
| CorporateID/IDNumber | CorporateID | xs:string | required |  |
| CorporateID/IDTitle | CorporateID | xs:string | optional |  |
| CorporateTenant/Company | CorporateTenant | CompanyType | required |  |
| CorporateTenant/CorporateID | CorporateTenant | CorporateID | repeating |  |
| CorporateTenant/Representative | CorporateTenant | PersonType | optional |  |
| CorporateTenant/RepresentativeTitle | CorporateTenant | xs:string | optional |  |
| CriminalBackground/CriminalRecord | CriminalBackground | CriminalRecord | repeating |  |
| CriminalRecord/County | CriminalRecord | xs:string | optional |  |
| CriminalRecord/Description | CriminalRecord | xs:string | required |  |
| CriminalRecord/State | CriminalRecord | xs:string | optional |  |
| CurrencyRangeType/Currency | CurrencyRangeType | Currency | optional |  |
| CurrencyRangeType/Exact | CurrencyRangeType | Money | optional |  |
| CurrencyRangeType/Max | CurrencyRangeType | Money | optional |  |
| CurrencyRangeType/Min | CurrencyRangeType | Money | optional |  |
| CurrentNumberOccupantsType/Child | CurrentNumberOccupantsType | xs:integer | optional |  |
| CurrentNumberOccupantsType/Total | CurrentNumberOccupantsType | xs:integer | required |  |
| Device/Label | Device | xs:string | required |  |
| Device/Quantity | Device | xs:int | required |  |
| Device/ReplacementCost | Device | MITS-Currency | optional |  |
| Device/SerialNumber | Device | xs:string | repeating |  |
| Devices/Device | Devices | Device | repeating |  |
| Document/DocumentType | Document | DocumentType | optional |  |
| Document/Label | Document | xs:string | optional |  |
| Document/Signature | Document | Signature | optional |  |
| Document/Version | Document | xs:string | optional |  |
| DocumentData/DocumentField | DocumentData | DocumentField | repeating |  |
| DocumentField/Label | DocumentField | xs:string | optional |  |
| Documents/Document | Documents | Document | repeating |  |
| Error/Message | Error | xs:string | required |  |
| Error/RetryPossible | Error | xs:boolean | optional |  |
| Finances/Asset | Finances | Asset | repeating |  |
| Finances/BankAccount | Finances | BankAccount | repeating |  |
| Finances/IncomeSource | Finances | IncomeSource | repeating |  |
| Finances/Occupation | Finances | Occupation | repeating |  |
| Identifiable/Identification | Identifiable | Identification | repeating |  |
| Identification/IDRank | Identification | IDRank | optional |  |
| Identification/IDScopeType | Identification | IDScopeType | optional |  |
| Identification/IDType | Identification | StringMax50Type | optional |  |
| Identification/IDValue | Identification | xs:string | required |  |
| Identification/OrganizationName | Identification | xs:string | optional |  |
| IncomeSource/Description | IncomeSource | StringMax50 | required |  |
| LA_Lease/AccountingData | LA_Lease | AccountingData | optional |  |
| LA_Lease/Devices | LA_Lease | Devices | optional |  |
| LA_Lease/DocumentData | LA_Lease | DocumentData | optional |  |
| LA_Lease/Documents | LA_Lease | Documents | optional |  |
| LA_Lease/LeaseEvents | LA_Lease | LeaseEvents | optional |  |
| LA_Lease/ParkingStorage | LA_Lease | ParkingStorage | optional |  |
| LA_Lease/Pets | LA_Lease | Pets | optional |  |
| LA_Lease/Policies | LA_Lease | Policies | optional |  |
| LA_Lease/Property | LA_Lease | PropertyType | optional |  |
| LA_Lease/Status | LA_Lease | LeaseStatus | repeating |  |
| LA_Lease/Unit | LA_Lease | UnitType | optional |  |
| LA_Lease/Utilities | LA_Lease | Utilities | optional |  |
| LeaseApplication/CorporateTenant | LeaseApplication | CorporateTenant | repeating |  |
| LeaseApplication/Error | LeaseApplication | Error | repeating |  |
| LeaseApplication/LA_Lease | LeaseApplication | LA_Lease | repeating |  |
| LeaseApplication/Tenant | LeaseApplication | Tenant | repeating |  |
| LeaseApplication/anonymous | LeaseApplication |  | repeating |  |
| LeaseEvent/Date | LeaseEvent | xs:date | required |  |
| LeaseEvent/Description | LeaseEvent | xs:string | optional |  |
| LeaseEvent/EventType | LeaseEvent | LeaseEventType | required |  |
| LeaseEvents/LeaseEvent | LeaseEvents | LeaseEvent | repeating |  |
| LeaseStatus/ApprovalStatus | LeaseStatus | ApprovalStatus | required |  |
| LeaseStatus/ModifiedBy | LeaseStatus | PersonType | optional |  |
| LeaseStatus/ModifiedOn | LeaseStatus | xs:date | optional |  |
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
| Name/FirstName | Name | StringMax50 | required |  |
| Name/LastName | Name | StringMax50 | required |  |
| Name/MaidenName | Name | StringMax50 | optional |  |
| Name/MiddleName | Name | StringMax50 | optional |  |
| Name/NamePrefix | Name | StringMax50 | optional |  |
| Name/NameSuffix | Name | StringMax50 | optional |  |
| NameType/FirstName | NameType | StringMax50Type | required |  |
| NameType/LastName | NameType | StringMax50Type | required |  |
| NameType/MaidenName | NameType | StringMax50Type | optional |  |
| NameType/MiddleName | NameType | StringMax50Type | optional |  |
| NameType/NamePrefix | NameType | StringMax50Type | optional |  |
| NameType/NameSuffix | NameType | StringMax50Type | optional |  |
| NumericRangeType/Exact | NumericRangeType | xs:integer | optional |  |
| NumericRangeType/Max | NumericRangeType | xs:integer | optional |  |
| NumericRangeType/Min | NumericRangeType | xs:integer | optional |  |
| Occupation/Employer | Occupation | CompanyType | optional |  |
| Occupation/End | Occupation | xs:date | optional |  |
| Occupation/Salary | Occupation | Salary | required |  |
| Occupation/Start | Occupation | xs:date | optional |  |
| Occupation/Supervisor | Occupation | PersonType | optional |  |
| Occupation/Title | Occupation | StringMax50 | optional |  |
| ParkingStorage/AdditionalSpace | ParkingStorage | AdditionalSpace | repeating |  |
| ParkingStorage/Vehicle | ParkingStorage | Vehicle | repeating |  |
| PersonType/Address | PersonType | AddressType | repeating |  |
| PersonType/Email | PersonType | StringMax80Type | optional |  |
| PersonType/Name | PersonType | NameType | required |  |
| PersonType/Phone | PersonType | PhoneType | repeating |  |
| PersonalID/IDIssuer | PersonalID | xs:string | optional |  |
| PersonalID/IDNumber | PersonalID | xs:string | required |  |
| PersonalID/PersonalIDType | PersonalID | PersonalIDType | required |  |
| PersonsType/Person | PersonsType | PersonType | repeating |  |
| PetType/Count | PetType |  | required |  |
| PetType/Description | PetType |  | optional |  |
| PetType/PetType | PetType |  | required |  |
| PetType/Size | PetType |  | optional |  |
| PetType/Weight | PetType | xs:string | optional |  |
| Pets/Pet | Pets | PetType | repeating |  |
| PhoneType/Extension | PhoneType | StringMax20Type | optional |  |
| PhoneType/PhoneDescription | PhoneType | StringMax50Type | optional |  |
| PhoneType/PhoneNumber | PhoneType | StringMax20Type | optional |  |
| PhoneType/PhoneType | PhoneType | PhoneInfo | required |  |
| Policies/Policy | Policies | Policy | repeating |  |
| Policy/Eviction | Policy | NoContent | optional |  |
| Policy/Fee | Policy | Fee | optional |  |
| Policy/GuestVisitsLongerThan | Policy | xs:integer | optional |  |
| Policy/LockedOut | Policy | xs:integer | optional |  |
| Policy/LostKeys | Policy | xs:integer | optional |  |
| Policy/MoreGuestsThan | Policy | xs:integer | optional |  |
| Policy/NoticeServed | Policy | xs:integer | optional |  |
| Policy/OtherAction | Policy | xs:string | repeating |  |
| Policy/OtherCondition | Policy | xs:string | optional |  |
| Policy/RentIsLate | Policy | NoContent | optional |  |
| Policy/RentPaidLateMoreThan | Policy | xs:integer | optional |  |
| Policy/RentPaidOnOrAfter | Policy | xs:integer | optional |  |
| Policy/ReturnedChecks | Policy | xs:integer | optional |  |
| Policy/TerminationAfterLessThan | Policy | xs:integer | optional |  |
| Policy/TerminationEarlierThan | Policy | xs:integer | optional |  |
| Policy/UnathorizedPetFound | Policy | xs:integer | optional |  |
| Policy/UnauthorizedGuestVisitsLongerThan | Policy | xs:integer | optional |  |
| Policy/UncleanedPetWaste | Policy | xs:integer | optional |  |
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
| Reference/ContactInfo | Reference | PersonType | required |  |
| Reference/Description | Reference | xs:string | optional |  |
| Reference/ReferenceType | Reference | ReferenceType | required |  |
| Residence/Address | Residence | AddressType | required |  |
| Residence/Landlord | Residence | PersonType | optional |  |
| Residence/ManagementCompany | Residence | CompanyType | optional |  |
| Residence/MoveInDate | Residence | xs:date | optional |  |
| Residence/MoveOutDate | Residence | xs:date | optional |  |
| Residence/Rent | Residence | MITS-Currency | optional |  |
| Salary/Amount | Salary | MITS-Currency | required |  |
| Salary/Frequency | Salary | Frequency | required |  |
| Signature/Date | Signature | xs:date | optional |  |
| Signature/Description | Signature | xs:string | optional |  |
| Signature/HardCopyExists | Signature | xs:boolean | optional |  |
| Signature/IsLandlord | Signature | xs:boolean | optional |  |
| Signature/Reference | Signature | xs:anyURI | optional |  |
| Tenant/BirthDate | Tenant | xs:date | optional |  |
| Tenant/CriminalBackground | Tenant | CriminalBackground | optional |  |
| Tenant/Finances | Tenant | Finances | optional |  |
| Tenant/GuarantorFor | Tenant | IdentificationType | optional |  |
| Tenant/Name | Tenant | Name | required |  |
| Tenant/PersonalID | Tenant | PersonalID | repeating |  |
| Tenant/Phone | Tenant | PhoneType | repeating |  |
| Tenant/Residence | Tenant | Residence | repeating |  |
| Tenant/ResidentType | Tenant | ResidentType | optional |  |
| Tenant/Spouse | Tenant | IdentificationType | optional |  |
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
| Utilities/Utility | Utilities | Utility | repeating |  |
| Utility/CommonArea | Utility | UtilityCommonArea | optional |  |
| Utility/Description | Utility | xs:string | optional |  |
| Utility/Metering | Utility | UtilityMetering | optional |  |
| Utility/Name | Utility | xs:string | optional |  |
| Utility/PaidToCompany | Utility | CompanyType | optional |  |
| Utility/PaidToLandlord | Utility | NoContent | optional |  |
| Utility/Responsibility | Utility | UtilityResponsibility | required |  |
| Utility/UtilityType | Utility | UtilityType | repeating |  |
| Vehicle/Color | Vehicle | xs:string | optional |  |
| Vehicle/LicenseNumber | Vehicle | xs:string | optional |  |
| Vehicle/LicenseState | Vehicle | xs:string | optional |  |
| Vehicle/Make | Vehicle | xs:string | optional |  |
| Vehicle/Model | Vehicle | xs:string | optional |  |
| Vehicle/Owner | Vehicle | PersonType | optional |  |
| Vehicle/PermitNumber | Vehicle | xs:string | optional |  |
| Vehicle/Year | Vehicle | xs:gYear | optional |  |

_Generated by `cora docs build`. Do not edit by hand — regenerate when the underlying inventories or crosswalks change._
