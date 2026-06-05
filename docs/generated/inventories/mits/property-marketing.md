# MITS / property-marketing

| Key | Value |
|---|---|
| Source artifact | `standards/mits/current/native/Property-Marketing-ILS-5.0-XSD-with-CORE/Property-Marketing-ILS-5.0.xsd` |
| Version | 5.0 |
| Extractor | `cora_extractors.xsd@0.0.0` |
| Source label | `xsd` |
| Types | 38 |
| Fields | 191 |

## Types

| Name | Extends | Abstract | Definition |
|---|---|---|---|
| AddressType |  |  |  |
| CharacteristicsType |  |  | The specific characteristics of items that are included in this limit. Any characteristics that are not specified are assumed to be allowed any value. If omitted, the limit applies to all characteristics in the class meeting any Applies To constraint. For example, this could be used to place a maximum monetary amount on non-refundable monthly pet charges, without including deposit items. |
| ChargeOfferAmountType |  |  |  |
| ChargeOfferItemType |  |  |  |
| ChargeOfferType |  |  |  |
| CompaniesType |  |  |  |
| CompanyContactType |  |  |  |
| CompanyContactsType |  |  |  |
| CompanyPersonContactType |  |  |  |
| CompanyType | Identifiable |  |  |
| ContactsType |  |  |  |
| CurrencyRangeType |  |  |  |
| CurrentNumberOccupantsType |  |  |  |
| FileType |  |  | Use for attaching files to Property,Building,Floorplan,Unit, and Phase |
| GeneralAmenityType |  |  | Amenities that belongs to phase or community level 11/28/06 |
| Identifiable |  |  |  |
| Identification |  |  |  |
| LeadChannelType | Identification |  |  |
| LeaseType | Identifiable |  |  |
| LimitsType |  |  | Restrict the maximum number or the maximum amount of items that appear in the charge class, for example to restrict the total number of storage spaces, or the maximum monthly pet rent. |
| NameType |  |  |  |
| NumericRangeType |  |  |  |
| ParkingOfferItemType | ChargeOfferItemType |  |  |
| PersonType | Identifiable |  |  |
| PersonsType |  |  |  |
| PetOfferItemType | ChargeOfferItemType |  |  |
| PhoneType |  |  |  |
| PropertiesType |  |  |  |
| PropertyContactsType |  |  |  |
| PropertyDataUploadResponseType |  |  | Defines a group of nodes that identify the processing status of the uploaded property data. |
| PropertyType | Identifiable |  |  |
| PropertyTypeExtended | PropertyType |  |  |
| RoomType |  |  |  |
| SeniorLivingAmenityType |  |  | Amenities that belong to Properties with Senior Living Facilities |
| SpecificAmenityType |  |  | Amenities that belongs to unit or floorplan level 11/28/06 |
| StorageOfferItemType | ChargeOfferItemType |  |  |
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
| CharacteristicsType/ChargeRequirement | CharacteristicsType |  | required | Included, Mandatory, Situational, Conditional, or Optional |
| CharacteristicsType/ConditionalAppliesTo | CharacteristicsType |  | optional | If the Charge Requirement is Conditional, this specifies the internal code(s) of the Charge Offer Item(s) the presence of (or any one of) will trigger the automatic inclusion of this Charge Offer Item |
| CharacteristicsType/Lifecycle | CharacteristicsType |  | required | The stage in the lifecycle of the resident’s lease that this item relates to. |
| CharacteristicsType/PaymentFrequency | CharacteristicsType |  | required | The frequency on which the amounts specified in this item will be payable. |
| CharacteristicsType/Refundability | CharacteristicsType |  | required | Determines whether this item is never refunded, expected to be refunded (e.g. a deposit), or possibly refunded (e.g. a hold fee). |
| CharacteristicsType/RefundabilityDescription | CharacteristicsType | xs:string | required | Description of the terms that apply to return of deposits or refunds. |
| CharacteristicsType/RefundabilityMax | CharacteristicsType | xs:decimal | required | The maximum monetary amount (if Refundability Max Type is amount) or percentage (if Refundability Max Type is percentage) of this fee that could be refunded. For percentages, ‘1’ = 100%. |
| CharacteristicsType/RefundabilityMaxType | CharacteristicsType |  | required | Determines whether the maximum amount refundable is specified as an explicit amount or as a percentage of the amount paid. |
| CharacteristicsType/RefundabilityPerType | CharacteristicsType |  | optional | Where a refundability maximum is specified, and this item Amount Per Type is either Applicant or Person, this attribute specifies whether the refundability max applies to each per-entity (i.e. per applicant/per person) or whether the max applies to the aggregate of all applicants/people. |
| CharacteristicsType/RequirementDescription | CharacteristicsType | xs:string | required | Description of the conditions under which situational or optional charges will be applied. |
| ChargeOfferAmountType/Amounts | ChargeOfferAmountType | xs:decimal | repeating | If the Amount Basis is Fixed Amount, the list contains one specific amount. If the Amount Basis is Within Range, the list contains two amounts, the first being the lowest amount in the range and the second being the highest amount in the range. If the Amount Basis is Stepped, the list contains the amount for each subsequent item – i.e. the first amount is the price for the first occurrence, the second amount is for the second occurrence and so on. If there is no maximum number of occurrences, or if the maximum is greater than the number of amounts in the list, the last amount will be used for subsequent occurrences. Negative amounts indicate credits to the customer account (e.g. concessions). Positive amounts indicate debits (i.e. charges). |
| ChargeOfferAmountType/Duration | ChargeOfferAmountType | xs:integer | required | The number of periods committed to, where the duration of each period is specified in the corresponding Charge Offer Item’s Payment Frequency. |
| ChargeOfferAmountType/Estimate | ChargeOfferAmountType | xs:boolean | required | If true, this amount is an estimate, and the actual amount charged could therefore be different. |
| ChargeOfferAmountType/EstimationBasis | ChargeOfferAmountType | xs:string | required | For estimated amounts, this narratively describes the basis of the estimation, for example utility company estimate, or average for the area. |
| ChargeOfferAmountType/Percentage | ChargeOfferAmountType | xs:decimal | required | If the Amount Basis is Percentage Of, the percentage. Negative percentages indicate credits to the customer account (e.g. concessions). Positive percentages indicate debits (i.e. charges). |
| ChargeOfferAmountType/StartTermEarliest | ChargeOfferAmountType | xs:date | required | If Term Basis is Specific Term, the start date of the specific term, or the earliest date in a range that the Specific Term start date lies. If omitted, any Specific Term start date preceding the Start Term Latest qualifies for this offer. |
| ChargeOfferAmountType/StartTermLatest | ChargeOfferAmountType | xs:date | required | If Term Basis is Specific Term, the latest date in a range that the Specific Term start date lies. If omitted, the Specific Term can start any time after the given Start Term Earliest. If the same as the Start Term Earliest date, then that is the only Specific Term start date on which this Charge Offer Amount applies. |
| ChargeOfferAmountType/TermBasis | ChargeOfferAmountType |  | required | Whole Lease or Specific Term. |
| ChargeOfferItemType/AmountBasis | ChargeOfferItemType |  | required | Explicit Amount, Percentage Of, Stepped, or Within Range |
| ChargeOfferItemType/AmountPerPeriod | ChargeOfferItemType | xs:string | required | For fees that have an Amount Per Type of Period, what is the duration of each period. |
| ChargeOfferItemType/AmountPerType | ChargeOfferItemType |  | required | Specifies what triggers a repeat of this charge. For example, per Unit would mean the charge is only incurred once per unit (for example, ‘monthly rent’), whereas per Person would indicate the charge is repeated for each Person using an item or taking part in an event (for example ‘overnight stay in guest suite’). |
| ChargeOfferItemType/ApplicableToAffordableUnits | ChargeOfferItemType |  | required | Indicates whether or not this specific fee applies to units that are identified as affordable. It may be omitted if there are no affordable units I the scope. |
| ChargeOfferItemType/Characteristics | ChargeOfferItemType | CharacteristicsType | required | A set of additional characteristics (or metadata) about the charge that can be used to make it easier for the resident to see specific charges and to allow pricing calculators to treat each charge appropriately. |
| ChargeOfferItemType/ChargeOfferAmount | ChargeOfferItemType | ChargeOfferAmountType | repeating |  |
| ChargeOfferItemType/Description | ChargeOfferItemType | xs:string | required | Description of the charge explaining what the charge is for using the operator’s preferred customer-facing language, including what the resident gets for the charge, or why they are being charged. This can also include an explanation of fees that are variable (e.g. what the variability depends upon). |
| ChargeOfferItemType/Group | ChargeOfferItemType | xs:string | required | In some cases, and operator may have a preferred grouping of fees. When this is the case, this preference should be provided here using the customer-facing name of the group under which this fee would preferably be listed. |
| ChargeOfferItemType/InternalCode | ChargeOfferItemType | xs:string | optional | The Internal Code, specific to each data publisher. |
| ChargeOfferItemType/ItemMaximumOccurrences | ChargeOfferItemType | xs:integer | required | If this item is subject to a maximum, it should be specified here. This can be used to limit items to one, or a specific number (e.g. pet dogs might be limited to a maximum of 2). If omitted, it is assumed that there is no limit on the number of individual items of this type that can be added. If class level limits are also specified, then the lowed of the two maximums is used. |
| ChargeOfferItemType/ItemMinimumOccurrences | ChargeOfferItemType | xs:integer | required | If this item is subject to a minimum, it should be specified here. |
| ChargeOfferItemType/Name | ChargeOfferItemType | xs:string | required | Short name indicating what the charge is for, using the operator’s preferred customer-facing language. |
| ChargeOfferItemType/PercentageOfCode | ChargeOfferItemType | xs:string | required | If Amount Basis is Percentage Of, the Internal Code that this Item is calculated as a percentage of. |
| ChargeOfferType/ChargeOfferItem | ChargeOfferType | ChargeOfferItemType | required |  |
| ChargeOfferType/Code | ChargeOfferType |  | required |  |
| ChargeOfferType/Limits | ChargeOfferType | LimitsType | repeating |  |
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
| FileType/Active | FileType | xs:boolean | required |  |
| FileType/AdID | FileType |  | optional |  |
| FileType/AffiliateID | FileType |  | optional |  |
| FileType/Caption | FileType |  | optional | Text description specified for subject |
| FileType/Description | FileType | xs:string | optional |  |
| FileType/FileID | FileType |  | required |  |
| FileType/FileType | FileType |  | required | Example: photo, floorplan, logo, etc. |
| FileType/Format | FileType |  | required |  |
| FileType/Height | FileType | xs:integer | optional |  |
| FileType/Name | FileType |  | required |  |
| FileType/Rank | FileType |  | required | Relative ranking of subject file among files of similar type |
| FileType/Src | FileType |  | required |  |
| FileType/Width | FileType | xs:integer | optional |  |
| GeneralAmenityType/AmenitySubType | GeneralAmenityType |  | optional |  |
| GeneralAmenityType/AmenityType | GeneralAmenityType |  | required |  |
| GeneralAmenityType/Description | GeneralAmenityType |  | optional |  |
| GeneralAmenityType/Rank | GeneralAmenityType | xs:integer | optional |  |
| Identifiable/Identification | Identifiable | Identification | repeating |  |
| Identification/IDRank | Identification | IDRank | optional |  |
| Identification/IDScopeType | Identification | IDScopeType | optional |  |
| Identification/IDType | Identification | StringMax50Type | optional |  |
| Identification/IDValue | Identification | xs:string | required |  |
| Identification/OrganizationName | Identification | xs:string | optional |  |
| LeadChannelType/LeadNotification | LeadChannelType |  | repeating | LeadNotification contains the exact contact data for the specified notification type. For example, if the notification type is ‘Email’, the LeadNotification content would be the email address itself. |
| LeadChannelType/Source | LeadChannelType | xs:string | optional |  |
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
| LimitsType/AppliesTo | LimitsType |  | optional | The specific item types (by Internal Code) that this maximum applies to. If omitted, it applies to all internal codes in the class meeting any Characteristic constraints. |
| LimitsType/Characteristic | LimitsType | CharacteristicsType | required |  |
| LimitsType/MaximumAmount | LimitsType | xs:decimal | required | The maximum total amount of items in the class, or – if Applies To or Characteristics are specified – the maximum number of items of the specified item types. |
| LimitsType/MaximumOccurences | LimitsType | xs:integer | required | The maximum number of items in the class, or – if Applies To or Characteristics are specified – the maximum number of items of the specified item types. |
| NameType/FirstName | NameType | StringMax50Type | required |  |
| NameType/LastName | NameType | StringMax50Type | required |  |
| NameType/MaidenName | NameType | StringMax50Type | optional |  |
| NameType/MiddleName | NameType | StringMax50Type | optional |  |
| NameType/NamePrefix | NameType | StringMax50Type | optional |  |
| NameType/NameSuffix | NameType | StringMax50Type | optional |  |
| NumericRangeType/Exact | NumericRangeType | xs:integer | optional |  |
| NumericRangeType/Max | NumericRangeType | xs:integer | optional |  |
| NumericRangeType/Min | NumericRangeType | xs:integer | optional |  |
| ParkingOfferItemType/Electric | ParkingOfferItemType |  | required | Specifies whether parking space with electric vehicle charging points are available, and – if so – whether they are also reservable. |
| ParkingOfferItemType/Handicapped | ParkingOfferItemType |  | required | Specifies whether handicapped parking is available, and – if so – whether it is also reservable. |
| ParkingOfferItemType/RegularSpace | ParkingOfferItemType |  | required | Specifies whether regular parking (i.e. not enhanced with EV or handicapped access) is available, and – if so – whether it is also reservable. |
| ParkingOfferItemType/SizeType | ParkingOfferItemType |  | required | Describes the general size of each parking space by reference to the kind of vehicle it is designed to accommodate. |
| ParkingOfferItemType/SpaceDescription | ParkingOfferItemType | xs:string | required | A narrative description of the space, include information about the mix of different types (e.g. “50 spaces in the surface lot, including 5 designated handicapped spaces, and 10 EV charging spaces” |
| ParkingOfferItemType/StructureType | ParkingOfferItemType |  | required | Information about the structure that contains the parking. |
| PersonType/Address | PersonType | AddressType | repeating |  |
| PersonType/Email | PersonType | StringMax80Type | optional |  |
| PersonType/Name | PersonType | NameType | required |  |
| PersonType/Phone | PersonType | PhoneType | repeating |  |
| PersonsType/Person | PersonsType | PersonType | repeating |  |
| PetOfferItemType/Allowed | PetOfferItemType |  | required | Indicates whether the specified type of pet (or all pets if no type is specified) are allowed. |
| PetOfferItemType/MaximumSize | PetOfferItemType | xs:string | required | Describes the maximum size of the pet. |
| PetOfferItemType/MaximumWeight | PetOfferItemType | xs:string | required | Describes the maximum weight of the pet. |
| PetOfferItemType/PetBreedorType | PetOfferItemType | xs:string | required | The breed (e.g. Airedale Terrier) or type of pet (e.g. Snake) that this item applies to. |
| PetOfferItemType/PetCare | PetOfferItemType |  | required | Indicates whether pet care is available at the property. |
| PhoneType/Extension | PhoneType | StringMax20Type | optional |  |
| PhoneType/PhoneDescription | PhoneType | StringMax50Type | optional |  |
| PhoneType/PhoneNumber | PhoneType | StringMax20Type | optional |  |
| PhoneType/PhoneType | PhoneType | PhoneInfo | required |  |
| PropertiesType/Property | PropertiesType | PropertyType | repeating |  |
| PropertyContactsType/PropertyContact | PropertyContactsType | CompanyContactType | repeating |  |
| PropertyDataUploadResponseType/completeDocumentRecieved | PropertyDataUploadResponseType | StatusTypes | optional |  |
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
| PropertyTypeExtended/Reason | PropertyTypeExtended |  | required |  |
| PropertyTypeExtended/status | PropertyTypeExtended | StatusTypes | optional |  |
| RoomType/Comment | RoomType | xs:string | required |  |
| RoomType/Count | RoomType | xs:decimal | required |  |
| RoomType/Description | RoomType | xs:string | optional |  |
| RoomType/GeneralType | RoomType | xs:string | optional |  |
| RoomType/RoomType | RoomType |  | required |  |
| RoomType/Size | RoomType | xs:decimal | optional |  |
| SeniorLivingAmenityType/AmenityType | SeniorLivingAmenityType |  | required |  |
| SeniorLivingAmenityType/Description | SeniorLivingAmenityType |  | optional |  |
| SeniorLivingAmenityType/Rank | SeniorLivingAmenityType | xs:integer | optional |  |
| SpecificAmenityType/AmenitySubType | SpecificAmenityType |  | optional |  |
| SpecificAmenityType/AmenityType | SpecificAmenityType |  | required |  |
| SpecificAmenityType/Description | SpecificAmenityType |  | optional |  |
| SpecificAmenityType/Rank | SpecificAmenityType |  | optional |  |
| StorageOfferItemType/Height | StorageOfferItemType | xs:decimal | required | The internal height of the storage space. |
| StorageOfferItemType/Length | StorageOfferItemType | xs:decimal | required | The internal length of the storage space. |
| StorageOfferItemType/StorageType | StorageOfferItemType |  | required |  |
| StorageOfferItemType/StorageUoM | StorageOfferItemType |  | required | The units of measurement used for the dimensions that follow |
| StorageOfferItemType/Width | StorageOfferItemType | xs:decimal | required | The internal width of the storage space. |
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
