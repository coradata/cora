# IBPDI / portfolio-and-asset-management

| Key | Value |
|---|---|
| Source artifact | `standards/ibpdi/current/native/Schema Documents/core/portfolioAndAssetManagement/portfolioAndAssetManagement.manifest.cdm.json` |
| Version | 1.0 |
| Extractor | `cora_extractors.cdm_json@0.0.0` |
| Source label | `cdm-json` |
| Types | 11 |
| Fields | 61 |


## Types

| Name | Extends | Abstract | Definition |
|---|---|---|---|
| Portfolio | CdmEntity |  | Grouping of real estate assets |
| PortfolioBuilding | CdmEntity |  | Linking entity between Portfolio and Building |
| PortfolioLand | CdmEntity |  | Linking entity between Portfolio and Land |
| PortfolioSite | CdmEntity |  | Linking entity between Portfolio and Site |
| PortfolioStrategy | CdmEntity |  | Strategy and strategic targets for the use of real estate assets in a portfolio |
| PortfolioUnit | CdmEntity |  | Linking entity between Portfolio and Unit |
| Valuation | CdmEntity |  | Financial valuation of buildings or whole portfolios |
| ValuationBuilding | CdmEntity |  | Linking entity between Valuation and Building |
| ValuationIndividualAccount | CdmEntity |  | Linking entity between Valuation and IndividualAccount |
| ValuationLand | CdmEntity |  | Linking entity between Valuation and Land |
| ValuationOperationalMeasurement | CdmEntity |  | Linking entity between Valuation and OperationalMeasurement |


## Fields

| Path | Domain | Range | Cardinality | Definition |
|---|---|---|---|---|
| Portfolio/AssetCategory | Portfolio | string | optional | Describes the asset category |
| Portfolio/Currency | Portfolio | string | optional | Main/default currency of portfolio (depending on user it should be able to change this) |
| Portfolio/MarketValue | Portfolio | decimal | optional | Current market value of Portfolio |
| Portfolio/OwnershipType | Portfolio | string | optional | Describes the ownership structure of the portfolio |
| Portfolio/PortfolioCode | Portfolio | string | optional | User specific Portfolio Code e.g: MR003 |
| Portfolio/PortfolioId | Portfolio | string | optional | Customer ID from previous system (ID before onboarding data to CDM) |
| Portfolio/PrimaryUsageType | Portfolio | string | optional | Definition of the primary usage type/asset class of the portfolio (individual by portfolio owner) |
| Portfolio/ReportingCycle | Portfolio | string | optional | Reporting cycle which is used to determine the next reporting date |
| Portfolio/ReportingDate | Portfolio | dateTime | optional | Reporting date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| Portfolio/SecondaryUsageType | Portfolio | string | optional | Definition of the secondary usage type/asset class of the portfolio (individual by portfolio owner) |
| PortfolioBuilding/BuildingId | PortfolioBuilding |  | optional |  |
| PortfolioBuilding/PortfolioId | PortfolioBuilding |  | optional |  |
| PortfolioLand/LandId | PortfolioLand |  | optional |  |
| PortfolioLand/PortfolioId | PortfolioLand |  | optional |  |
| PortfolioSite/PortfolioId | PortfolioSite |  | optional |  |
| PortfolioSite/SiteId | PortfolioSite |  | optional |  |
| PortfolioStrategy/InvestmentType | PortfolioStrategy | string | optional | Type of Strategy |
| PortfolioStrategy/PortfolioId | PortfolioStrategy |  | optional |  |
| PortfolioStrategy/PortfolioStrategyId | PortfolioStrategy | string | optional | Customer ID from previous system (ID before onboarding data to CDM) |
| PortfolioStrategy/Source | PortfolioStrategy | string | optional | Source of Portfolio strategy |
| PortfolioStrategy/StrategyObjectiveTargets | PortfolioStrategy | string | optional | Target type of Portfolio Strategy |
| PortfolioStrategy/StrategyObjectiveTargetsSteering | PortfolioStrategy | string | optional | Steering target type of Portfolio Strategy |
| PortfolioStrategy/StrategyObjectiveUnit | PortfolioStrategy | string | optional | Unit of strategy objective values |
| PortfolioStrategy/StrategyObjectiveUnitSteering | PortfolioStrategy | string | optional | Unit of strategy objective values steering |
| PortfolioStrategy/StrategyObjectiveValues | PortfolioStrategy | decimal | optional | Value of the portfolio strategy targets |
| PortfolioStrategy/StrategyObjectiveValuesSteering | PortfolioStrategy | decimal | optional | Value of the portfolio strategy steering targets |
| PortfolioUnit/PortfolioId | PortfolioUnit |  | optional |  |
| PortfolioUnit/UnitId | PortfolioUnit |  | optional |  |
| Valuation/AccountingStandard | Valuation | string | optional | Name of Accounting standard used |
| Valuation/Approach | Valuation | string | optional | Valuation approach |
| Valuation/Assumptions | Valuation | string | optional | Concluded assumptions |
| Valuation/Constrains | Valuation | string | optional | Existing constrains |
| Valuation/Description | Valuation | string | optional | Description of valuation implementation |
| Valuation/DiscountPremiums | Valuation | decimal | optional | Discount premiums included |
| Valuation/DiscountRate | Valuation | decimal | optional | Discount rate included |
| Valuation/DocumentId | Valuation | string | optional | Unique identifier either coming from previous system otherwise it needs to be define |
| Valuation/EnergyEfficiency | Valuation | string | optional | Stating the energy efficiency class |
| Valuation/JurisdictionStandard | Valuation | string | optional | Name of Jurisdiction type used |
| Valuation/JurisdictionType | Valuation | string | optional | Type of Jurisdiction |
| Valuation/Keywords | Valuation | string | optional | Important keywords |
| Valuation/Liquidity | Valuation | decimal | optional | Amount of cash |
| Valuation/MaintenanceBacklog | Valuation | boolean | optional | Does a maintenance backlog exist (Y/N) |
| Valuation/PreviousValuationId | Valuation | string | optional | Unique identifier either coming from previous system otherwise it needs to be define |
| Valuation/ProfessionalStandard | Valuation | string | optional | Name of professional valuation standard used |
| Valuation/SingleTenant | Valuation | boolean | optional | Valuation of single tenant building (Y/N) |
| Valuation/SpaceEfficiency | Valuation | string | optional | Space usage efficiency |
| Valuation/SpecialAssumptions | Valuation | string | optional | Concluded special assumptions |
| Valuation/Text | Valuation | string | optional | Text field |
| Valuation/Uncertainty | Valuation | string | optional | LoV for uncertainty |
| Valuation/Unit | Valuation | string | optional | Unit of valuation |
| Valuation/Url | Valuation | string | optional | URL if existent |
| Valuation/ValuationId | Valuation | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| Valuation/Value | Valuation | decimal | optional | Value of Valuation |
| ValuationBuilding/BuildingId | ValuationBuilding |  | optional |  |
| ValuationBuilding/ValuationId | ValuationBuilding |  | optional |  |
| ValuationIndividualAccount/IndividualAccountId | ValuationIndividualAccount |  | optional |  |
| ValuationIndividualAccount/ValuationId | ValuationIndividualAccount |  | optional |  |
| ValuationLand/LandId | ValuationLand |  | optional |  |
| ValuationLand/ValuationId | ValuationLand |  | optional |  |
| ValuationOperationalMeasurement/OperationalMeasurementId | ValuationOperationalMeasurement |  | optional |  |
| ValuationOperationalMeasurement/ValuationId | ValuationOperationalMeasurement |  | optional |  |


_Generated by `cora docs build`. Do not edit by hand — regenerate when the underlying inventories or crosswalks change._
