# IBPDI / energy-and-resources

| Key | Value |
|---|---|
| Source artifact | `standards/ibpdi/current/native/Schema Documents/core/energyAndResources/energyAndResources.manifest.cdm.json` |
| Version | 1.0 |
| Extractor | `cora_extractors.cdm_json@0.0.0` |
| Source label | `cdm-json` |
| Types | 21 |
| Fields | 90 |

## Types

| Name | Extends | Abstract | Definition |
|---|---|---|---|
| Climate | CdmEntity |  | Regional information on past and future amount of heating and cooling degree days (for potential climate normalisation and projection of energy demand) |
| ClimateBuilding | CdmEntity |  | Linking entity between Climate and Building |
| ClimateSite | CdmEntity |  | Linking entity between Climate and Site |
| EmissionFactor | CdmEntity |  | Emission factors that are applied to convert energy consumption data into greenhouse gas emissions. The entity also includes global warming potential data for non-CO2 greenhouse gases in order to calculate CO2-equivalents (CO2e) |
| EmissionFactorBuilding | CdmEntity |  | Linking entity between EmissionFactor and Building |
| EmissionFactorOperationalMeasurement | CdmEntity |  | Linking entity between EmissionFactor and OperationalMeasurement |
| EmissionFactorSite | CdmEntity |  | Linking entity between EmissionFactor and Site |
| GhgEmission | CdmEntity |  | Greenhouse gas (Ghg) emissions (in CO2e) corresponding to individual operational measurements. |
| GhgEmissionBuilding | CdmEntity |  | Linking entity between GhgEmission and Building |
| GhgEmissionEmissionFactor | CdmEntity |  | Linking entity between GhgEmission and EmissionFactor |
| GhgEmissionSite | CdmEntity |  | Linking entity between GhgEmission and Site |
| OperationalMeasurement | CdmEntity |  | Represents individual data on energy consumption, water consumption/withdrawal, waste output or fugitive emissions including various further information (procured by, subtypes, purpose, covered time period) |
| OperationalMeasurementBuilding | CdmEntity |  | Linking entity between OperationalMeasurement and Building |
| OperationalMeasurementFloor | CdmEntity |  | Linking entity between OperationalMeasurement and Floor |
| OperationalMeasurementLand | CdmEntity |  | Linking entity between OperationalMeasurement and Land |
| OperationalMeasurementRentalUnit | CdmEntity |  | Linking entity between OperationalMeasurement and RentalUnit |
| OperationalMeasurementSite | CdmEntity |  | Linking entity between OperationalMeasurement and Site |
| OperationalMeasurementSpace | CdmEntity |  | Linking entity between OperationalMeasurement and Space |
| OperationalMeasurementUnit | CdmEntity |  | Linking entity between OperationalMeasurement and Unit |
| SustainabilityIndicator | CdmEntity |  | Sustainability-related information on building-level: energy consumption, net energy demand, carbon emissions (total, separated in emissions scopes, market- and location-based, alignment with targets, excess emissions, carbon costs and penalties) |
| SustainabilityIndicatorEmissionFactor | CdmEntity |  | Linking entity between SustainabilityIndicator and EmissionFactor |

## Fields

| Path | Domain | Range | Cardinality | Definition |
|---|---|---|---|---|
| Climate/ClimateId | Climate | guid | optional | Unique identifier either coming from previous system otherwise it needs to be define |
| Climate/CoordinateSystem | Climate | string | optional | Specific coordinate system used |
| Climate/EnsembleMember | Climate | string | optional | Information on members of a model ensemble and changed conditions ('realisation', 'initialisation', 'physics'). Control member; 'r1i1p1' |
| Climate/Experiment | Climate | string | optional | Type of simulation of regional climate model e.g. Historical, Evaluation, RCP2.6 |
| Climate/GlobalCirculationModel | Climate | string | optional | Global circulation model used |
| Climate/Latitude | Climate | decimal | optional | Latitude coordinate in case of geographic coordinates |
| Climate/Location | Climate | string | optional | Localisation of observed data in case of non-grid location types |
| Climate/LocationType | Climate | string | optional | Type of spatial reference e.g. Zip code or geographic coordinates |
| Climate/Longitude | Climate | decimal | optional | Longitude coordinate in case of geographic coordinates |
| Climate/PosX | Climate | integer | optional | Vertical coordinate in case of projected coordinates |
| Climate/PosY | Climate | integer | optional | Vertical coordinate in case of projected coordinates |
| Climate/RegionalClimateModel | Climate | string | optional | Regional climate model used |
| Climate/SimulationVersion | Climate | string | optional | Run number of certain climate model or model combination |
| Climate/SpatialResolution | Climate | string | optional | Spatial resolution of data |
| Climate/TemporalResolution | Climate | string | optional | Temporal resolution of data (can be the time period over which raw data is aggregated) |
| Climate/Unit | Climate | string | optional | Unit of observed value |
| Climate/Variable | Climate | string | optional | Observed variable |
| ClimateBuilding/BuildingId | ClimateBuilding |  | optional |  |
| ClimateBuilding/ClimateId | ClimateBuilding |  | optional |  |
| ClimateSite/ClimateId | ClimateSite |  | optional |  |
| ClimateSite/SiteId | ClimateSite |  | optional |  |
| EmissionFactor/City | EmissionFactor | city | optional | Any official settlement including cities, towns, villages, hamlets, localities, etc |
| EmissionFactor/Country | EmissionFactor | string | optional | Sovereign nations and their dependent territories, anything with an ISO-3166 ALPHA-2 code |
| EmissionFactor/EmissionFactorId | EmissionFactor | guid | optional | Unique identifier either coming from previous system otherwise it needs to be define |
| EmissionFactor/Name | EmissionFactor | string | optional | User specific emission factor name (this can also be the name of a scenario) |
| EmissionFactor/Region | EmissionFactor | string | optional | Areas that are broadly divided by physical characteristics, human impact characteristics, and the interaction of humanity and the environment |
| EmissionFactor/Source | EmissionFactor | string | optional | Source of emission factor e.g. 'International Energy Agency' |
| EmissionFactor/SpaceType | EmissionFactor | string | optional | Differentiated emission factor for certain space type (within a building) |
| EmissionFactor/Type | EmissionFactor | string | optional | Specific type of emission factor e.g. district heating or water discharge |
| EmissionFactor/Unit | EmissionFactor | string | optional | Unit of emission factor in terms of kgCO2e per unit of resource consumption |
| EmissionFactorBuilding/BuildingId | EmissionFactorBuilding |  | optional |  |
| EmissionFactorBuilding/EmissionFactorId | EmissionFactorBuilding |  | optional |  |
| EmissionFactorOperationalMeasurement/EmissionFactorId | EmissionFactorOperationalMeasurement |  | optional |  |
| EmissionFactorOperationalMeasurement/OperationalMeasurementId | EmissionFactorOperationalMeasurement |  | optional |  |
| EmissionFactorSite/EmissionFactorId | EmissionFactorSite |  | optional |  |
| EmissionFactorSite/SiteId | EmissionFactorSite |  | optional |  |
| GhgEmission/Accuracy | GhgEmission | string | optional | Information on accuracy of value e.g. 'metered' or 'extrapolated' |
| GhgEmission/EmissionScope | GhgEmission | string | optional | Emission scope 1, 2 or 3 according to the Greenhouse Gas Protocol |
| GhgEmission/GhgEmissionId | GhgEmission | guid | optional | Unique identifier either coming from previous system otherwise it needs to be define |
| GhgEmission/LifeCycleAssessment | GhgEmission | string | optional | Related life cycle assessment stage according to ISO 14040 |
| GhgEmission/OperationalMeasurementId | GhgEmission |  | optional |  |
| GhgEmission/ReportingType | GhgEmission | string | optional | Approach of reporting emissions e.g. from 'green electricity consumption': Market-based or location-based |
| GhgEmission/SubType | GhgEmission | string | optional | Specific type of ghg emission generation e.g. district heating or water discharge |
| GhgEmission/Type | GhgEmission | string | optional | General source of emission e.g. energy, water or waste |
| GhgEmission/Unit | GhgEmission | string | optional | Unit of emission value: kgCO2e |
| GhgEmissionBuilding/BuildingId | GhgEmissionBuilding |  | optional |  |
| GhgEmissionBuilding/GhgEmissionId | GhgEmissionBuilding |  | optional |  |
| GhgEmissionEmissionFactor/EmissionFactorId | GhgEmissionEmissionFactor |  | optional |  |
| GhgEmissionEmissionFactor/GhgEmissionId | GhgEmissionEmissionFactor |  | optional |  |
| GhgEmissionSite/GhgEmissionId | GhgEmissionSite |  | optional |  |
| GhgEmissionSite/SiteId | GhgEmissionSite |  | optional |  |
| OperationalMeasurement/Accuracy | OperationalMeasurement | string | optional | Information on accuracy of value e.g. 'metered' or 'extrapolated' |
| OperationalMeasurement/LifeCycleAssessment | OperationalMeasurement | string | optional | Related life cycle assessment stage according to ISO 14040 |
| OperationalMeasurement/MeasurementDate | OperationalMeasurement | dateTime | optional | Date of measurement was taken in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| OperationalMeasurement/Name | OperationalMeasurement | entityName | optional | Name of entity. |
| OperationalMeasurement/OperationalMeasurementId | OperationalMeasurement | guid | optional | Unique identifier either coming from previous system otherwise it needs to be define |
| OperationalMeasurement/PostingDate | OperationalMeasurement | dateTime | optional | Date of measurement posting in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| OperationalMeasurement/ProcuredBy | OperationalMeasurement | string | optional | Information on operational control ('who bought it?') of resource consumption according to Greenhouse Gas Protocol |
| OperationalMeasurement/Purpose | OperationalMeasurement | string | optional | Specific purpose of resource consumption e.g. 'space heating' in case of burning natural gas |
| OperationalMeasurement/SensorId | OperationalMeasurement | string | optional | Unique identifier either coming from previous system otherwise it needs to be define |
| OperationalMeasurement/SpaceType | OperationalMeasurement | string | optional | Reference to specific space type (or 'whole building') |
| OperationalMeasurement/SubType | OperationalMeasurement | string | optional | Specific type of operational measurement e.g. district heating or water discharge |
| OperationalMeasurement/Type | OperationalMeasurement | string | optional | General type of operational measurement e.g. energy, water or waste |
| OperationalMeasurement/Unit | OperationalMeasurement | string | optional | Unit of operational measurement e.g. 'kWh' or 'cubm' |
| OperationalMeasurementBuilding/BuildingId | OperationalMeasurementBuilding |  | optional |  |
| OperationalMeasurementBuilding/OperationalMeasurementId | OperationalMeasurementBuilding |  | optional |  |
| OperationalMeasurementFloor/FloorId | OperationalMeasurementFloor |  | optional |  |
| OperationalMeasurementFloor/OperationalMeasurementId | OperationalMeasurementFloor |  | optional |  |
| OperationalMeasurementLand/LandId | OperationalMeasurementLand |  | optional |  |
| OperationalMeasurementLand/OperationalMeasurementId | OperationalMeasurementLand |  | optional |  |
| OperationalMeasurementRentalUnit/OperationalMeasurementId | OperationalMeasurementRentalUnit |  | optional |  |
| OperationalMeasurementRentalUnit/RentalUnitId | OperationalMeasurementRentalUnit |  | optional |  |
| OperationalMeasurementSite/OperationalMeasurementId | OperationalMeasurementSite |  | optional |  |
| OperationalMeasurementSite/SiteId | OperationalMeasurementSite |  | optional |  |
| OperationalMeasurementSpace/OperationalMeasurementId | OperationalMeasurementSpace |  | optional |  |
| OperationalMeasurementSpace/SpaceId | OperationalMeasurementSpace |  | optional |  |
| OperationalMeasurementUnit/OperationalMeasurementId | OperationalMeasurementUnit |  | optional |  |
| OperationalMeasurementUnit/UnitId | OperationalMeasurementUnit |  | optional |  |
| SustainabilityIndicator/BaseYear | SustainabilityIndicator | dateTime | optional | Base year of values projected into the future in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061). In case no exact date is used please use xxxx-01-01 00:00:00. |
| SustainabilityIndicator/BuildingId | SustainabilityIndicator |  | optional |  |
| SustainabilityIndicator/Category | SustainabilityIndicator | string | optional | Overall category of sustainability indicator e.g. energy, greenhouse gas emissions or costs |
| SustainabilityIndicator/ReferenceArea | SustainabilityIndicator | string | optional | Reference area of building used as denominator in intensity calculation |
| SustainabilityIndicator/ReportingType | SustainabilityIndicator | string | optional | Approach of reporting emissions e.g. from 'green electricity consumption': Market-based or location-based |
| SustainabilityIndicator/Source | SustainabilityIndicator | string | optional | Operational source of energy or emission figures e.g. electricity or water |
| SustainabilityIndicator/SubType | SustainabilityIndicator | string | optional | Subtype of sustainability indicator e.g. net-energy or  emission scope |
| SustainabilityIndicator/SustainabilityIndicatorId | SustainabilityIndicator | guid | optional | Unique identifier either coming from previous system otherwise it needs to be define |
| SustainabilityIndicator/Type | SustainabilityIndicator | string | optional | Type of sustainability indicator e.g. absolute or intensity figures or stranding |
| SustainabilityIndicator/Unit | SustainabilityIndicator | string | optional | Unit of sustainability indicator value |
| SustainabilityIndicatorEmissionFactor/EmissionFactorId | SustainabilityIndicatorEmissionFactor |  | optional |  |
| SustainabilityIndicatorEmissionFactor/SustainabilityIndicatorId | SustainabilityIndicatorEmissionFactor |  | optional |  |

_Generated by `cora docs build`. Do not edit by hand — regenerate when the underlying inventories or crosswalks change._
