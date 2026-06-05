# MITS / collections

| Key | Value |
|---|---|
| Source artifact | `standards/mits/current/native/Collections-Schema-Version-3.0-xsd.xml` |
| Version | 3.0 |
| Extractor | `cora_extractors.xsd@0.0.0` |
| Source label | `xsd` |
| Types | 33 |
| Fields | 174 |


## Types

| Name | Extends | Abstract | Definition |
|---|---|---|---|
| AddressType |  |  |  |
| C_CollectionTransactionType | IdentificationType |  | Collections 'CollectionTransactionType' used to describe tenants charges and payments after account has been placed with collections |
| C_EmployerType |  |  | Collections 'EmployerType' used to describe tenants employer |
| C_FileTransactionType | IdentificationType |  | Collections 'FileTransactionType' used to describe tenants charges and payments |
| C_IncomeType |  |  | Collections 'IncomeType' used to describe sources of income |
| C_LeaseFileType | IdentificationType |  | Collections 'LeaseFileType' used to describe lease/debt details |
| C_LeaseFilesType |  |  | Collections 'LeaseFileType' used to describe lease/debt details |
| C_OwnerChangedType |  |  | Collections 'OwnerChangedType' used to house the new owners information in the case where a property changes owners / property management company |
| C_PropertyFileType |  |  | Collections 'PropertyFileType' used to describe property details |
| C_PropertyFilesType |  |  | Collections 'PropertyFileTypes' used to group property details |
| C_SummaryType |  |  | Collections 'SummaryType' used to house elements as redundant checks against concurrency, duplication and parsing errors |
| C_TenantType |  |  | Collections 'ResidentType' used to describe tenantresident |
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
| AddressType/City | AddressType | StringMax60Type | optional |  |
| AddressType/Country | AddressType | StringMax50Type | optional |  |
| AddressType/CountyName | AddressType | StringMax60Type | optional |  |
| AddressType/Description | AddressType | StringMax100Type | optional |  |
| AddressType/PostalCode | AddressType | StringMax12Type | optional |  |
| AddressType/Province | AddressType | StringMax60Type | optional |  |
| AddressType/State | AddressType | StringMax3Type | optional |  |
| AddressType/UnparsedAddress | AddressType | StringMax500Type | optional |  |
| C_CollectionTransactionType/AgencyFee | C_CollectionTransactionType | MITS-Currency | optional |  |
| C_CollectionTransactionType/AmountDueClient | C_CollectionTransactionType | MITS-Currency | optional |  |
| C_CollectionTransactionType/CommissionPercentage | C_CollectionTransactionType | C_PercentageType | optional |  |
| C_CollectionTransactionType/FileTransactionIDRef | C_CollectionTransactionType | xs:string | optional | Populated if applicable/possible to tie transaction to specific file charge |
| C_CollectionTransactionType/RemainingBalance | C_CollectionTransactionType | MITS-Currency | optional |  |
| C_CollectionTransactionType/SalesTax | C_CollectionTransactionType | MITS-Currency | optional | Populated if applicable (may be required by State Law) |
| C_CollectionTransactionType/TransAmount | C_CollectionTransactionType | MITS-Currency | required |  |
| C_CollectionTransactionType/TransDate | C_CollectionTransactionType | xs:date | required |  |
| C_CollectionTransactionType/TransType | C_CollectionTransactionType | C_TransactionType | required |  |
| C_CollectionTransactionType/TransTypeDesc | C_CollectionTransactionType | xs:string | optional |  |
| C_CollectionTransactionType/anonymous | C_CollectionTransactionType |  | repeating |  |
| C_EmployerType/EmployerDetails | C_EmployerType | CompanyType | required | Employer Details (Mits Core Data 3.0 - CompanyType) |
| C_EmployerType/Income | C_EmployerType | C_IncomeType | repeating | Incomes derived from the employment in question |
| C_EmployerType/JobTitle | C_EmployerType | xs:string | optional |  |
| C_EmployerType/LastDateEmployed | C_EmployerType | xs:date | optional | If populated, implies that employment is not longer active |
| C_EmployerType/SupervisorContactNumber | C_EmployerType | PhoneType | optional | Supervisor Contact Details. (Mits Core Data 3.0 - PhoneType) |
| C_EmployerType/SupervisorName | C_EmployerType | xs:string | optional |  |
| C_FileTransactionType/OpenAmount | C_FileTransactionType | MITS-Currency | optional |  |
| C_FileTransactionType/TransAmount | C_FileTransactionType | MITS-Currency | required |  |
| C_FileTransactionType/TransDate | C_FileTransactionType | xs:date | required |  |
| C_FileTransactionType/TransType | C_FileTransactionType | C_TransactionType | required |  |
| C_FileTransactionType/TransTypeDesc | C_FileTransactionType | xs:string | optional |  |
| C_FileTransactionType/anonymous | C_FileTransactionType |  | repeating |  |
| C_IncomeType/IncomeAmount | C_IncomeType | xs:double | required |  |
| C_IncomeType/IncomeSource | C_IncomeType | xs:string | optional |  |
| C_IncomeType/PaymentPeriod | C_IncomeType | C_PaymentPeriodType | required |  |
| C_LeaseFileType/CollectionStatus | C_LeaseFileType | xs:boolean | required | Status of Collection Account (Active=True, Inactive=False) |
| C_LeaseFileType/CollectionStatusDesc | C_LeaseFileType | xs:string | optional | Description of account status |
| C_LeaseFileType/CollectionStatusLastChangeDate | C_LeaseFileType | xs:date | optional | Date of last Status change |
| C_LeaseFileType/CollectionTransaction | C_LeaseFileType | C_CollectionTransactionType | repeating | All transactions on the account subsequent to placement with collections made by the collections agency |
| C_LeaseFileType/FileTransactions | C_LeaseFileType | C_FileTransactionType | repeating | All lease / other transactions that make up the open balance |
| C_LeaseFileType/HousingType | C_LeaseFileType | xs:string | optional | Description of type of housing |
| C_LeaseFileType/LastPaymentDate | C_LeaseFileType | xs:date | optional |  |
| C_LeaseFileType/LeaseBegin | C_LeaseFileType | xs:date | optional |  |
| C_LeaseFileType/LeaseEnd | C_LeaseFileType | xs:date | optional |  |
| C_LeaseFileType/MonthlyRentAmount | C_LeaseFileType | xs:double | optional |  |
| C_LeaseFileType/MoveInDate | C_LeaseFileType | xs:date | optional |  |
| C_LeaseFileType/MoveOutDate | C_LeaseFileType | xs:date | optional |  |
| C_LeaseFileType/NoticeToVacateDate | C_LeaseFileType | xs:date | optional |  |
| C_LeaseFileType/RentDueFromDate | C_LeaseFileType | xs:date | optional |  |
| C_LeaseFileType/RentDueToDate | C_LeaseFileType | xs:date | optional |  |
| C_LeaseFileType/Tenants | C_LeaseFileType | C_TenantType | repeating | All tenants on lease |
| C_LeaseFileType/anonymous | C_LeaseFileType |  | repeating |  |
| C_LeaseFilesType/LeaseFile | C_LeaseFilesType | C_LeaseFileType | repeating |  |
| C_OwnerChangedType/ChangedOn | C_OwnerChangedType | xs:date | optional |  |
| C_OwnerChangedType/NewOwner | C_OwnerChangedType | CompanyType | optional |  |
| C_PropertyFileType/LeaseFiles | C_PropertyFileType | C_LeaseFilesType | required | Lease Collection Data |
| C_PropertyFileType/OwnerChanged | C_PropertyFileType | C_OwnerChangedType | repeating | If populated, then property ownership / management has changed |
| C_PropertyFileType/Property | C_PropertyFileType | PropertyType | required | Property Details. (Mits Core Data 3.0 - PropertyType) |
| C_PropertyFileType/PropertyManagementCompany | C_PropertyFileType | CompanyType | optional | PMC Details. (Mits Core Data 3.0 - CompanyType) |
| C_PropertyFileType/PropertyManager | C_PropertyFileType | PersonType | optional | Main contact at property pertaining to collections. (Mits Core Data 3.0 - PersonType) |
| C_PropertyFileType/anonymous | C_PropertyFileType |  | repeating |  |
| C_PropertyFilesType/PropertyFile | C_PropertyFilesType | C_PropertyFileType | repeating |  |
| C_SummaryType/GenerationTimeStamp | C_SummaryType | xs:dateTime | required | Date and Time XML generated |
| C_SummaryType/MITSDocVersion | C_SummaryType | xs:string | required | MITS Collection Data Standard Version, (e.g. 3.0x) |
| C_SummaryType/SourceOrganization | C_SummaryType | xs:string | required | From where the XML file originates |
| C_SummaryType/TotalLeaseFiles | C_SummaryType | xs:int | required |  |
| C_SummaryType/TotalOpenAmount | C_SummaryType | MITS-Currency | optional |  |
| C_SummaryType/TotalProperties | C_SummaryType | xs:int | required |  |
| C_SummaryType/TotalTenants | C_SummaryType | xs:int | required |  |
| C_TenantType/BankAccountNumber | C_TenantType | xs:string | optional |  |
| C_TenantType/BankName | C_TenantType | xs:string | optional |  |
| C_TenantType/BankRoutingNumber | C_TenantType | xs:string | optional |  |
| C_TenantType/Contact | C_TenantType | PersonType | repeating | Emergency Contact Details. (Mits Core Data 3.0 - PersonType) |
| C_TenantType/DateOfBirth | C_TenantType | xs:date | optional |  |
| C_TenantType/DriversLicense | C_TenantType | xs:string | optional |  |
| C_TenantType/Employer | C_TenantType | C_EmployerType | repeating |  |
| C_TenantType/Guarantor | C_TenantType | xs:boolean | optional | Set to True if tenant is guarantor |
| C_TenantType/Income | C_TenantType | C_IncomeType | repeating | Incomes other than employment income |
| C_TenantType/PersonDetails | C_TenantType | PersonType | required | Tenants Details. (Mits Core Data 3.0 - PersonType) |
| C_TenantType/SSN | C_TenantType | xs:string | optional |  |
| C_TenantType/anonymous | C_TenantType |  | repeating |  |
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
