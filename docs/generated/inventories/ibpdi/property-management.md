# IBPDI / property-management

| Key | Value |
|---|---|
| Source artifact | `standards/ibpdi/current/native/Schema Documents/core/propertyManagement/propertyManagement.manifest.cdm.json` |
| Version | 1.0 |
| Extractor | `cora_extractors.cdm_json@0.0.0` |
| Source label | `cdm-json` |
| Types | 13 |
| Fields | 59 |

## Types

| Name | Extends | Abstract | Definition |
|---|---|---|---|
| Dunning | CdmEntity |  | Information about outstanding rent receivables |
| RentalContract | CdmEntity |  | Agreement identifying all information regarding the rental relationship |
| RentalContractRentalUnit | CdmEntity |  | Linking entity between RentalContract and RentalUnit |
| RentalOption | CdmEntity |  | Information about rental option of rental contract |
| RentalPayment | CdmEntity |  | Information about payments related to rental contract |
| RentalUnit | CdmEntity |  | Structure or part of a structure rented out to a third party as a home, residence, office or for any other use |
| RentalUnitBuilding | CdmEntity |  | Linking entity between RentalUnit and Building |
| RentalUnitFloor | CdmEntity |  | Linking entity between RentalUnit and Floor |
| RentalUnitLand | CdmEntity |  | Linking entity between RentalUnit and Land |
| RentalUnitSite | CdmEntity |  | Linking entity between RentalUnit and Site |
| RentalUnitSpace | CdmEntity |  | Linking entity between RentalUnit and Space |
| RentalUnitUnit | CdmEntity |  | Linking entity between RentalUnit and Unit |
| TenantCommunication | CdmEntity |  | Communication between different parties involved in operation, control, and oversight of the real estate |

## Fields

| Path | Domain | Range | Cardinality | Definition |
|---|---|---|---|---|
| Dunning/DunningAmount | Dunning | decimal | optional | Dunning Amount |
| Dunning/DunningId | Dunning | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| Dunning/DunningLevel | Dunning | string | optional | Dunning level |
| Dunning/InitialDueDate | Dunning | dateTime | optional | Initial due date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| Dunning/PaymentAmount | Dunning | decimal | optional | Value of payment |
| Dunning/PaymentDate | Dunning | dateTime | optional | Payment date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| Dunning/RentalPaymentId | Dunning |  | optional |  |
| RentalContract/CompanyCode | RentalContract | string | optional | Company Code (e.g. SAP code) |
| RentalContract/ContractCode | RentalContract | string | optional | Contract Code (e.g. SAP) |
| RentalContract/ContractGroup | RentalContract | string | optional | Contract group |
| RentalContract/ContractName | RentalContract | string | optional | Contract name |
| RentalContract/ContractType | RentalContract | string | optional | Contract type |
| RentalContract/MainContractId | RentalContract | string | optional | Main contract code |
| RentalContract/PaymentFrequency | RentalContract | string | optional | Frequency of payment e.g. weekly, monthly, quarterly etc. |
| RentalContract/PaymentInAdvance | RentalContract | boolean | optional | Does the payment have to be conducted in advance (Y/N) |
| RentalContract/PeriodOfNotice | RentalContract | string | optional | Period of notice e.g. monthly; 3 month; 6 month etc. |
| RentalContract/RentBeginDate | RentalContract | dateTime | optional | Date original contract starts in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| RentalContract/RentEndDate | RentalContract | dateTime | optional | Date original contract ends in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| RentalContract/RentalContractId | RentalContract | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| RentalContract/ShortTermLease | RentalContract | boolean | optional | Is this a short term lease (Y/N) |
| RentalContract/TenantSector | RentalContract | string | optional | Sector / Business area of the tenant |
| RentalContract/TurnoverReportingInterval | RentalContract | string | optional | If turnover rent, reporting interval for the tenant turnover: monthly, quarterly, etc. |
| RentalContractRentalUnit/RentalContractId | RentalContractRentalUnit |  | optional |  |
| RentalContractRentalUnit/RentalUnitId | RentalContractRentalUnit |  | optional |  |
| RentalOption/DocumentId | RentalOption | string | optional | Reference to document |
| RentalOption/RentalContractId | RentalOption |  | optional |  |
| RentalOption/RentalOptionId | RentalOption | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| RentalOption/SubType | RentalOption | string | optional | Subtype of the option |
| RentalPayment/DiscountInPercentage | RentalPayment | decimal | optional | Discount percentage of payment |
| RentalPayment/IndexId | RentalPayment | string | optional | Reference to index table |
| RentalPayment/RentalContractId | RentalPayment |  | optional |  |
| RentalPayment/RentalPaymentId | RentalPayment | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| RentalPayment/ValueMonth | RentalPayment | decimal | optional | Value of payment per month |
| RentalPayment/ValueYear | RentalPayment | decimal | optional | Value of payment per year |
| RentalPayment/VatOpted | RentalPayment | boolean | optional | Is the vat payable  (Y/N) |
| RentalUnit/RentalUnitCode | RentalUnit | string | optional | User specific RentalUnit Code |
| RentalUnit/RentalUnitId | RentalUnit | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| RentalUnit/RentedOut | RentalUnit | boolean | optional | Is the RentalUnit rented out (Y/N) |
| RentalUnit/UsageType | RentalUnit | string | optional | Usage type of the rental unit |
| RentalUnit/Vacancy | RentalUnit | boolean | optional | Is the rental unit vacant (Y/N) |
| RentalUnitBuilding/BuildingId | RentalUnitBuilding |  | optional |  |
| RentalUnitBuilding/RentalUnitId | RentalUnitBuilding |  | optional |  |
| RentalUnitFloor/FloorId | RentalUnitFloor |  | optional |  |
| RentalUnitFloor/RentalUnitId | RentalUnitFloor |  | optional |  |
| RentalUnitLand/LandId | RentalUnitLand |  | optional |  |
| RentalUnitLand/RentalUnitId | RentalUnitLand |  | optional |  |
| RentalUnitSite/RentalUnitId | RentalUnitSite |  | optional |  |
| RentalUnitSite/SiteId | RentalUnitSite |  | optional |  |
| RentalUnitSpace/RentalUnitId | RentalUnitSpace |  | optional |  |
| RentalUnitSpace/SpaceId | RentalUnitSpace |  | optional |  |
| RentalUnitUnit/RentalUnitId | RentalUnitUnit |  | optional |  |
| RentalUnitUnit/UnitId | RentalUnitUnit |  | optional |  |
| TenantCommunication/Description | TenantCommunication | string | optional | Description of communciation |
| TenantCommunication/Medium | TenantCommunication | string | optional | Medium of communication |
| TenantCommunication/RentalUnitId | TenantCommunication |  | optional |  |
| TenantCommunication/Status | TenantCommunication | string | optional | Status of communication |
| TenantCommunication/TenantCommunicationId | TenantCommunication | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| TenantCommunication/ValidFrom | TenantCommunication | dateTime | optional | Date communication occurred in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| TenantCommunication/ValidUntil | TenantCommunication | dateTime | optional | Date communication is valid until in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |

_Generated by `cora docs build`. Do not edit by hand — regenerate when the underlying inventories or crosswalks change._
