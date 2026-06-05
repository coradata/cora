# IBPDI / organisational-management

| Key | Value |
|---|---|
| Source artifact | `standards/ibpdi/current/native/Schema Documents/core/organisationalManagement/organisationalManagement.manifest.cdm.json` |
| Version | 1.0 |
| Extractor | `cora_extractors.cdm_json@0.0.0` |
| Source label | `cdm-json` |
| Types | 39 |
| Fields | 131 |

## Types

| Name | Extends | Abstract | Definition |
|---|---|---|---|
| Address | CdmEntity |  | Collection of information used to give the location of a building, apartment, or other structure or a plot of land |
| AddressBuilding | CdmEntity |  | Linking entity between Address and Building |
| AddressContact | CdmEntity |  | Linking entity between Address and Contact |
| AddressLand | CdmEntity |  | Linking entity between Address and Land |
| AddressOrganisation | CdmEntity |  | Linking entity between Address and Organisation |
| AddressRentalUnit | CdmEntity |  | Linking entity between Address and RentalUnit |
| AddressSite | CdmEntity |  | Linking entity between Address and Site |
| Contact | CdmEntity |  | Contact details |
| GeoCoordinate | CdmEntity |  | Information about geographic data to enable the use of common locations of geographic features, imagery, and observation within a common geographic framework |
| Organisation | CdmEntity |  | Information about organisations (internal and external) |
| Role | CdmEntity |  | Defining the role of the organisation or contact |
| RoleBuildingContact | CdmEntity |  | Linking entity between Role, Building and Organisation |
| RoleBuildingOrganisation | CdmEntity |  | Linking entity between Role, Building and Organisation |
| RoleComponentContact | CdmEntity |  | Linking entity between Role, Component and Contact |
| RoleComponentOrganisation | CdmEntity |  | Linking entity between Role, Component and Organisation |
| RoleComponentTypeContact | CdmEntity |  | Linking entity between Role, ComponentType and Contact |
| RoleComponentTypeOrganisation | CdmEntity |  | Linking entity between Role, ComponentType and Organisation |
| RoleEmissionFactorContact | CdmEntity |  | Linking entity between Role ,EmissionFactor and Contact |
| RoleEmissionFactorOrganisation | CdmEntity |  | Linking entity between Role, EmissionFactor and Organisation |
| RoleLandContact | CdmEntity |  | Linking entity between Role, Land and Contact |
| RoleLandOrganisation | CdmEntity |  | Linking entity between Role, Land and Organisation |
| RoleOperationalMeasurementContact | CdmEntity |  | Linking entity between Role, OperationalMeasurement and Contact |
| RoleOperationalMeasurementOrganisation | CdmEntity |  | Linking entity between Role, OperationalMeasurement and Organisation |
| RolePortfolioContact | CdmEntity |  | Linking entity between Role, Portfolio and Contact |
| RolePortfolioOrganisation | CdmEntity |  | Linking entity between Role, Portfolio and Organisation |
| RolePortfolioStrategyContact | CdmEntity |  | Linking entity between Role, PortfolioStrategy and Contact |
| RolePortfolioStrategyOrganisation | CdmEntity |  | Linking entity between Role, PortfolioStrategy and Organisation |
| RoleRentalContractContact | CdmEntity |  | Linking entity between Role, RentalContract and Contact |
| RoleRentalContractOrganisation | CdmEntity |  | Linking entity between Role, RentalContract and Organisation |
| RoleRentalUnitContact | CdmEntity |  | Linking entity between Role, RentalUnit and Contact |
| RoleRentalUnitOrganisation | CdmEntity |  | Linking entity between Role, RentalUnit and Organisation |
| RoleSiteContact | CdmEntity |  | Linking entity between Role, Site and Organisation |
| RoleSiteOrganisation | CdmEntity |  | Linking entity between Role, Site and Organisation |
| RoleSystemContact | CdmEntity |  | Linking entity between Role, System and Contact |
| RoleSystemOrganisation |  |  | Linking entity between Role, System and Organisation |
| RoleTenantCommunicationContact | CdmEntity |  | Linking entity between Role, TenantCommunication and Organisation |
| RoleTenantCommunicationOrganisation | CdmEntity |  | Linking entity between Role, TenantCommunication and Organisation |
| RoleValuationContact | CdmEntity |  | Linking entity between Role, Valuation and Contact |
| RoleValuationOrganisation | CdmEntity |  | Linking entity between Role, Valuation and Organisation |

## Fields

| Path | Domain | Range | Cardinality | Definition |
|---|---|---|---|---|
| Address/AdditionalInformation | Address | string | optional | Additional information that can not be displayed in the other attributes such as Building, Door Nr. etc. |
| Address/AddressId | Address | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| Address/ApartmentOrUnit | Address | string | optional | Unit number |
| Address/City | Address | city | optional | Any official settlement including cities, towns, villages, hamlets, localities, etc. |
| Address/Country | Address | string | optional | Sovereign nations and their dependent territories, anything with an ISO-3166 ALPHA-2 code |
| Address/DepricatedLatitude | Address | decimal | optional | (Deprecated) Latitude coordinate in case of geographic coordinates |
| Address/DepricatedLongitude | Address | decimal | optional | (Deprecated) Longitude coordinate in case of geographic coordinates |
| Address/District | Address | string | optional | Boroughs or districts within a city that serve some official purpose |
| Address/HouseNumber | Address | string | optional | House number of the street |
| Address/PostalCode | Address | postalCode | optional | Postal codes used for mail sorting |
| Address/StateProvincePrefecture | Address | stateOrProvince | optional | First-level administrative division, depending on the continent or country if might be named differently. |
| Address/StreetName | Address | string | optional | Name of the street |
| AddressBuilding/AddressId | AddressBuilding |  | optional |  |
| AddressBuilding/BuildingId | AddressBuilding |  | optional |  |
| AddressContact/AddressId | AddressContact |  | optional |  |
| AddressContact/ContactId | AddressContact |  | optional |  |
| AddressLand/AddressId | AddressLand |  | optional |  |
| AddressLand/LandId | AddressLand |  | optional |  |
| AddressOrganisation/AddressId | AddressOrganisation |  | optional |  |
| AddressOrganisation/OrganisationId | AddressOrganisation |  | optional |  |
| AddressRentalUnit/AddressId | AddressRentalUnit |  | optional |  |
| AddressRentalUnit/RentalUnitId | AddressRentalUnit |  | optional |  |
| AddressSite/AddressId | AddressSite |  | optional |  |
| AddressSite/SiteId | AddressSite |  | optional |  |
| Contact/ContactId | Contact | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| Contact/EmployeeId | Contact | string | optional | Employee ID or number for the contact for reference in orders, service cases, or other communications with the contact's organisation |
| Contact/FirstName | Contact | firstName | optional | First Name of Business Partner or responsible contact person |
| Contact/JobTitle | Contact | string | optional | Job title of the contact to make sure the contact is addressed correctly in sales calls, email, and marketing campaigns |
| Contact/LastName | Contact | lastName | optional | Surname of Business Partner or responsible contact person |
| Contact/OrganisationId | Contact |  | optional |  |
| Contact/Salutation | Contact | string | optional | Title of Business Partner |
| Contact/ValidFrom | Contact | dateTime | optional | The records can be used from this date onwards in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| Contact/ValidUntil | Contact | dateTime | optional | The records can be used until this date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| GeoCoordinate/AddressId | GeoCoordinate |  | optional |  |
| GeoCoordinate/CoordinateReferenceSystem | GeoCoordinate | string | optional | Specific coordinate reference system used |
| GeoCoordinate/GeoCoordinateId | GeoCoordinate | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| GeoCoordinate/Latitude | GeoCoordinate | decimal | optional | Latitude coordinate in case of geographic coordinates |
| GeoCoordinate/Longitude | GeoCoordinate | decimal | optional | Longitude coordinate in case of geographic coordinates |
| Organisation/FiscalYearStartDate | Organisation | dateTime | optional | Start date of fiscal year for organisation in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| Organisation/Industry | Organisation | string | optional | Industry of organisation |
| Organisation/LegalEntity | Organisation | boolean | optional | Is the organisation an legal entity (Y/N) |
| Organisation/OrganisationId | Organisation | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| Organisation/ParentId | Organisation | string | optional | Parent (guid or id) of entity |
| Organisation/ValidFrom | Organisation | dateTime | optional | The records can be used from this date onwards in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| Organisation/ValidUntil | Organisation | dateTime | optional | The records can be used until this date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| Organisation/VatNumber | Organisation | string | optional | Vat number of organisation |
| Role/RoleId | Role | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| RoleBuildingContact/BuildingId | RoleBuildingContact |  | optional |  |
| RoleBuildingContact/ContactId | RoleBuildingContact |  | optional |  |
| RoleBuildingContact/RoleId | RoleBuildingContact |  | optional |  |
| RoleBuildingOrganisation/BuildingId | RoleBuildingOrganisation |  | optional |  |
| RoleBuildingOrganisation/OrganisationId | RoleBuildingOrganisation |  | optional |  |
| RoleBuildingOrganisation/RoleId | RoleBuildingOrganisation |  | optional |  |
| RoleComponentContact/ComponentId | RoleComponentContact |  | optional |  |
| RoleComponentContact/ContactId | RoleComponentContact |  | optional |  |
| RoleComponentContact/RoleId | RoleComponentContact |  | optional |  |
| RoleComponentOrganisation/ComponentId | RoleComponentOrganisation |  | optional |  |
| RoleComponentOrganisation/OrganisationId | RoleComponentOrganisation |  | optional |  |
| RoleComponentOrganisation/RoleId | RoleComponentOrganisation |  | optional |  |
| RoleComponentTypeContact/ComponentTypeId | RoleComponentTypeContact |  | optional |  |
| RoleComponentTypeContact/ContactId | RoleComponentTypeContact |  | optional |  |
| RoleComponentTypeContact/RoleId | RoleComponentTypeContact |  | optional |  |
| RoleComponentTypeOrganisation/ComponentTypeId | RoleComponentTypeOrganisation |  | optional |  |
| RoleComponentTypeOrganisation/OrganisationId | RoleComponentTypeOrganisation |  | optional |  |
| RoleComponentTypeOrganisation/RoleId | RoleComponentTypeOrganisation |  | optional |  |
| RoleEmissionFactorContact/ContactId | RoleEmissionFactorContact |  | optional |  |
| RoleEmissionFactorContact/EmissionFactorId | RoleEmissionFactorContact |  | optional |  |
| RoleEmissionFactorContact/RoleId | RoleEmissionFactorContact |  | optional |  |
| RoleEmissionFactorOrganisation/EmissionFactorId | RoleEmissionFactorOrganisation |  | optional |  |
| RoleEmissionFactorOrganisation/OrganisationId | RoleEmissionFactorOrganisation |  | optional |  |
| RoleEmissionFactorOrganisation/RoleId | RoleEmissionFactorOrganisation |  | optional |  |
| RoleLandContact/ContactId | RoleLandContact |  | optional |  |
| RoleLandContact/LandId | RoleLandContact |  | optional |  |
| RoleLandContact/RoleId | RoleLandContact |  | optional |  |
| RoleLandOrganisation/LandId | RoleLandOrganisation |  | optional |  |
| RoleLandOrganisation/OrganisationId | RoleLandOrganisation |  | optional |  |
| RoleLandOrganisation/RoleId | RoleLandOrganisation |  | optional |  |
| RoleOperationalMeasurementContact/ContactId | RoleOperationalMeasurementContact |  | optional |  |
| RoleOperationalMeasurementContact/OperationalMeasurementId | RoleOperationalMeasurementContact |  | optional |  |
| RoleOperationalMeasurementContact/RoleId | RoleOperationalMeasurementContact |  | optional |  |
| RoleOperationalMeasurementOrganisation/OperationalMeasurementId | RoleOperationalMeasurementOrganisation |  | optional |  |
| RoleOperationalMeasurementOrganisation/OrganisationId | RoleOperationalMeasurementOrganisation |  | optional |  |
| RoleOperationalMeasurementOrganisation/RoleId | RoleOperationalMeasurementOrganisation |  | optional |  |
| RolePortfolioContact/ContactId | RolePortfolioContact |  | optional |  |
| RolePortfolioContact/PortfolioId | RolePortfolioContact |  | optional |  |
| RolePortfolioContact/RoleId | RolePortfolioContact |  | optional |  |
| RolePortfolioOrganisation/OrganisationId | RolePortfolioOrganisation |  | optional |  |
| RolePortfolioOrganisation/PortfolioId | RolePortfolioOrganisation |  | optional |  |
| RolePortfolioOrganisation/RoleId | RolePortfolioOrganisation |  | optional |  |
| RolePortfolioStrategyContact/ContactId | RolePortfolioStrategyContact |  | optional |  |
| RolePortfolioStrategyContact/PortfolioStrategyId | RolePortfolioStrategyContact |  | optional |  |
| RolePortfolioStrategyContact/RoleId | RolePortfolioStrategyContact |  | optional |  |
| RolePortfolioStrategyOrganisation/OrganisationId | RolePortfolioStrategyOrganisation |  | optional |  |
| RolePortfolioStrategyOrganisation/PortfolioStrategyId | RolePortfolioStrategyOrganisation |  | optional |  |
| RolePortfolioStrategyOrganisation/RoleId | RolePortfolioStrategyOrganisation |  | optional |  |
| RoleRentalContractContact/ContactId | RoleRentalContractContact |  | optional |  |
| RoleRentalContractContact/RentalContractId | RoleRentalContractContact |  | optional |  |
| RoleRentalContractContact/RoleId | RoleRentalContractContact |  | optional |  |
| RoleRentalContractOrganisation/OrganisationId | RoleRentalContractOrganisation |  | optional |  |
| RoleRentalContractOrganisation/RentalContractId | RoleRentalContractOrganisation |  | optional |  |
| RoleRentalContractOrganisation/RoleId | RoleRentalContractOrganisation |  | optional |  |
| RoleRentalUnitContact/ContactId | RoleRentalUnitContact |  | optional |  |
| RoleRentalUnitContact/RentalUnitId | RoleRentalUnitContact |  | optional |  |
| RoleRentalUnitContact/RoleId | RoleRentalUnitContact |  | optional |  |
| RoleRentalUnitOrganisation/OrganisationId | RoleRentalUnitOrganisation |  | optional |  |
| RoleRentalUnitOrganisation/RentalUnitId | RoleRentalUnitOrganisation |  | optional |  |
| RoleRentalUnitOrganisation/RoleId | RoleRentalUnitOrganisation |  | optional |  |
| RoleSiteContact/ContactId | RoleSiteContact |  | optional |  |
| RoleSiteContact/RoleId | RoleSiteContact |  | optional |  |
| RoleSiteContact/SiteId | RoleSiteContact |  | optional |  |
| RoleSiteOrganisation/OrganisationId | RoleSiteOrganisation |  | optional |  |
| RoleSiteOrganisation/RoleId | RoleSiteOrganisation |  | optional |  |
| RoleSiteOrganisation/SiteId | RoleSiteOrganisation |  | optional |  |
| RoleSystemContact/ContactId | RoleSystemContact |  | optional |  |
| RoleSystemContact/RoleId | RoleSystemContact |  | optional |  |
| RoleSystemContact/SystemId | RoleSystemContact |  | optional |  |
| RoleSystemOrganisation/OrganisationId | RoleSystemOrganisation |  | optional |  |
| RoleSystemOrganisation/RoleId | RoleSystemOrganisation |  | optional |  |
| RoleSystemOrganisation/SystemId | RoleSystemOrganisation |  | optional |  |
| RoleTenantCommunicationContact/ContactId | RoleTenantCommunicationContact |  | optional |  |
| RoleTenantCommunicationContact/RoleId | RoleTenantCommunicationContact |  | optional |  |
| RoleTenantCommunicationContact/TenantCommunicationId | RoleTenantCommunicationContact |  | optional |  |
| RoleTenantCommunicationOrganisation/OrganisationId | RoleTenantCommunicationOrganisation |  | optional |  |
| RoleTenantCommunicationOrganisation/RoleId | RoleTenantCommunicationOrganisation |  | optional |  |
| RoleTenantCommunicationOrganisation/TenantCommunicationId | RoleTenantCommunicationOrganisation |  | optional |  |
| RoleValuationContact/ContactId | RoleValuationContact |  | optional |  |
| RoleValuationContact/RoleId | RoleValuationContact |  | optional |  |
| RoleValuationContact/ValuationId | RoleValuationContact |  | optional |  |
| RoleValuationOrganisation/OrganisationId | RoleValuationOrganisation |  | optional |  |
| RoleValuationOrganisation/RoleId | RoleValuationOrganisation |  | optional |  |
| RoleValuationOrganisation/ValuationId | RoleValuationOrganisation |  | optional |  |

_Generated by `cora docs build`. Do not edit by hand — regenerate when the underlying inventories or crosswalks change._
