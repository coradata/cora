# IBPDI / financials

| Key | Value |
|---|---|
| Source artifact | `standards/ibpdi/current/native/Schema Documents/core/financials/financials.manifest.cdm.json` |
| Version | 1.0 |
| Extractor | `cora_extractors.cdm_json@0.0.0` |
| Source label | `cdm-json` |
| Types | 12 |
| Fields | 45 |

## Types

| Name | Extends | Abstract | Definition |
|---|---|---|---|
| Account | CdmEntity |  | IBPDI defined account number based on standardized chart of account |
| CostCenter | CdmEntity |  | Function or department within a company which is not directly going to generate |
| CostCenterBuilding | CdmEntity |  | Linking entity between CostCenter and Building |
| CostCenterLand | CdmEntity |  | Linking entity between CostCenter and Land |
| CostCenterPortfolio | CdmEntity |  | Linking entity between CostCenter and Portfolio |
| CostCenterRentalUnit | CdmEntity |  | Linking entity between CostCenter and RentalUnit |
| CostCenterSite | CdmEntity |  | Linking entity between CostCenter and Site |
| IndividualAccount | CdmEntity |  | Company account number based on specific chart of account |
| IndividualAccountBuilding | CdmEntity |  | Linking entity between IndividualAccount and Building |
| IndividualAccountPortfolio | CdmEntity |  | Linking entity between IndividualAccount and Portfolio |
| IndividualAccountSite | CdmEntity |  | Linking entity between IndividualAccount and Site |
| Transaction | CdmEntity |  | Individual transaction or account balance at specific reporting date |

## Fields

| Path | Domain | Range | Cardinality | Definition |
|---|---|---|---|---|
| Account/AccountId | Account | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| Account/IbpdiCategory | Account | string | optional | Account category according to IBPDI charts of accounts (category aligned with RICS naming convention) |
| Account/IbpdiGroup | Account | string | optional | Account group according IBPDI charts of accounts (group aligned with RICS naming convention) |
| Account/IbpdiProject | Account | string | optional | Account type (project aligned with RICS naming convention) |
| Account/RecordType | Account | string | optional | Record type (Debit or Credit) |
| Account/StatementType | Account | string | optional | Statement type (Balance statement or P&L account) |
| Account/Version | Account | string | optional | Account version |
| CostCenter/CostCenterId | CostCenter | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| CostCenter/OrganisationId | CostCenter |  | optional |  |
| CostCenter/Type | CostCenter | string | optional | Type of cost center |
| CostCenterBuilding/BuildingId | CostCenterBuilding |  | optional |  |
| CostCenterBuilding/CostCenterId | CostCenterBuilding |  | optional |  |
| CostCenterLand/CostCenterId | CostCenterLand |  | optional |  |
| CostCenterLand/LandId | CostCenterLand |  | optional |  |
| CostCenterPortfolio/CostCenterId | CostCenterPortfolio |  | optional |  |
| CostCenterPortfolio/PortfolioId | CostCenterPortfolio |  | optional |  |
| CostCenterRentalUnit/CostCenterId | CostCenterRentalUnit |  | optional |  |
| CostCenterRentalUnit/RentalUnitId | CostCenterRentalUnit |  | optional |  |
| CostCenterSite/CostCenterId | CostCenterSite |  | optional |  |
| CostCenterSite/SiteId | CostCenterSite |  | optional |  |
| IndividualAccount/AccountId | IndividualAccount |  | optional |  |
| IndividualAccount/Category | IndividualAccount | string | optional | Account category according to IBPDI charts of accounts (category aligned with RICS naming convention) |
| IndividualAccount/GAAP | IndividualAccount | string | optional | GAAP type used (if applicable) |
| IndividualAccount/Group | IndividualAccount | string | optional | Account group according IBPDI charts of accounts (group aligned with RICS naming convention) |
| IndividualAccount/IndividualAccountId | IndividualAccount | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| IndividualAccount/OrganisationId | IndividualAccount |  | optional |  |
| IndividualAccount/Project | IndividualAccount | string | optional | Individual Account project (project aligned with RICS naming convention) |
| IndividualAccount/RecordType | IndividualAccount | string | optional | Record type (Debit or Credit) |
| IndividualAccount/StatementType | IndividualAccount | string | optional | Statement type (Balance statement or P&L account) |
| IndividualAccount/Version | IndividualAccount | string | optional | Account version |
| IndividualAccountBuilding/BuildingId | IndividualAccountBuilding |  | optional |  |
| IndividualAccountBuilding/IndividualAccountId | IndividualAccountBuilding |  | optional |  |
| IndividualAccountPortfolio/IndividualAccountId | IndividualAccountPortfolio |  | optional |  |
| IndividualAccountPortfolio/PortfolioId | IndividualAccountPortfolio |  | optional |  |
| IndividualAccountSite/IndividualAccountId | IndividualAccountSite |  | optional |  |
| IndividualAccountSite/SiteId | IndividualAccountSite |  | optional |  |
| Transaction/BookingCurrency | Transaction | string | optional | Currency code according to Iso 4217 |
| Transaction/BookingType | Transaction | string | optional | Booking type |
| Transaction/CostCenterId | Transaction |  | optional |  |
| Transaction/DocumentId | Transaction | string | optional | Reference to document |
| Transaction/IndividualAccountId | Transaction |  | optional |  |
| Transaction/PostingDate | Transaction | dateTime | optional | Date transaction is posted in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| Transaction/TransactionId | Transaction | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| Transaction/Type | Transaction | string | optional | Type of transaction |
| Transaction/Value | Transaction | decimal | optional | Cost/Income value of specific transaction |

_Generated by `cora docs build`. Do not edit by hand — regenerate when the underlying inventories or crosswalks change._
