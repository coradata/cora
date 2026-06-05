# IBPDI / digital-twin

| Key | Value |
|---|---|
| Source artifact | `standards/ibpdi/current/native/Schema Documents/core/digitalTwin/digitalTwin.manifest.cdm.json` |
| Version | 1.0 |
| Extractor | `cora_extractors.cdm_json@0.0.0` |
| Source label | `cdm-json` |
| Types | 140 |
| Fields | 1409 |

## Types

| Name | Extends | Abstract | Definition |
|---|---|---|---|
| AccessPanel | CdmEntity |  | Access panel information |
| AirCompressor | CdmEntity |  | Information about air compressor |
| AirFilter | CdmEntity |  | Information about air filter |
| AirHandlingUnit | CdmEntity |  |  |
| AreaMeasurement | CdmEntity |  | Information about the area measurements within the physical building |
| AreaMeasurementBuilding | CdmEntity |  | Linking entity between AreaMeasurement and Building |
| AreaMeasurementFloor | CdmEntity |  | Linking entity between AreaMeasurement and Floor |
| AreaMeasurementLand | CdmEntity |  | Linking entity between AreaMeasurement and Land |
| AreaMeasurementRentalUnit | CdmEntity |  | Linking entity between AreaMeasurement and RentalUnit |
| AreaMeasurementSite | CdmEntity |  | Linking entity between AreaMeasurement and Site |
| AreaMeasurementSpace | CdmEntity |  | Linking entity between AreaMeasurement and Space |
| AreaMeasurementUnit | CdmEntity |  | Linking entity between AreaMeasurement and Unit |
| AutomaticTransferSwitch | CdmEntity |  | Information about automatic transfer switch |
| BacNetController | CdmEntity |  | Information about bac net controller |
| Boiler | CdmEntity |  | Information about boiler |
| Building | CdmEntity |  | A building represents a structure that provides shelter for its occupants or contents and stands in one place. The building is also used to provide a basic element within the spatial structure hierarchy for the components of a building project (together with site, storey, and space) |
| CeilingFan | CdmEntity |  | Information about ceiling fan |
| Certificate | CdmEntity |  | Any official document related to building, equipment, system etc. |
| CertificateBuilding | CdmEntity |  | Linking entity between certificate and building |
| CertificateComponent | CdmEntity |  | Linking entity between certificate and component |
| CertificateSystem | CdmEntity |  | Linking entity between certificate and system |
| CertificateValuation | CdmEntity |  | Linking entity between certificate and valuation |
| Chiller | CdmEntity |  | Information about chiller |
| CoGenerator | CdmEntity |  | Information about co generator |
| Component | CdmEntity |  | Component [component, part, apparatus] is a named and individually defined physical object and may require management efforts such as inspections, maintenance, service, or replacement during the use phase |
| ComponentBuilding | CdmEntity |  | Linking entity between component and building |
| ComponentFloor | CdmEntity |  | Linking entity between component and floor |
| ComponentRentalUnit | CdmEntity |  | Linking entity between Component and RentalUnit |
| ComponentSite | CdmEntity |  | Linking entity between component and site |
| ComponentSpace | CdmEntity |  | Linking entity between component and space |
| ComponentSystem | CdmEntity |  | Linking entity between component and system |
| ComponentType | CdmEntity |  | Type is a specification for components including information on equipment, product types and materials |
| ComponentUnit | CdmEntity |  | Linking entity between component and unit |
| CondensingUnit | CdmEntity |  | Information about hvac heat tracing |
| Controller | CdmEntity |  | Information about controller |
| CoolingTower | CdmEntity |  | Information about cooling tower |
| Damper | CdmEntity |  | Information about the damper, also known as duct damper or volume balancing damper is a movable plate, situated in the ductwork that regulates the flow of air and redirects it to specific places of a house |
| DataNetworkEquipment | CdmEntity |  | Information about data network equipment |
| DataNetworkSubComponent | CdmEntity |  | Information about data network sub component |
| ElectricalDistributionEquipmentSubComponent | CdmEntity |  | Information about electrical distribution equipment sub component |
| ElectricalMeter | CdmEntity |  | Information about electrical meter |
| ElectricalPanelBoard | CdmEntity |  | Information about electrical panel board |
| ElectricalPanelBoardMcb | CdmEntity |  | Information about electrical panel board mcb |
| ElectricalPanelBoardMlo | CdmEntity |  | Information about electrical panel board mlo |
| ElectricalSystem | CdmEntity |  | Detailed information about the electrical system |
| ElectricalVehicleChargingStation | CdmEntity |  | Information about electric vehicle charging station |
| ElectronicSafetyAndSecuritySystem | CdmEntity |  | Detailed information about electronic safety and security system |
| Elevator | CdmEntity |  | Information about elevator |
| ElevatorMachine | CdmEntity |  | Information about elevator machine |
| Escalator | CdmEntity |  | Information about escalator |
| EthernetSwitchPort | CdmEntity |  | Information about ethernet switch point |
| FanCoilUnit | CdmEntity |  | Detailed information about fan coil |
| FanCoilUnitReheat | CdmEntity |  | Information about fan coil unit reheat |
| FanPoweredBox | CdmEntity |  | Information about fan powered box |
| FanPoweredBoxReheat | CdmEntity |  | Information about fan powered box reheat |
| Faucet | CdmEntity |  | Information about faucet |
| FireDamper | CdmEntity |  | Information about fire damper |
| FirePump | CdmEntity |  | Information about fire pump |
| FireSprinklerHead | CdmEntity |  | Information about fire sprinkler head |
| Floor | CdmEntity |  | The floor has an elevation and typically represents a (nearly) horizontal aggregation of spaces that are vertically bound. |
| FlushometerValve | CdmEntity |  | Information about flushometer valve |
| GasMeter | CdmEntity |  | Information about gas meter |
| Gateway | CdmEntity |  | Information about gateway |
| Generator | CdmEntity |  | Information about the generator |
| HvacFan | CdmEntity |  | Information about hvac fan |
| HvacFanSubComponent | CdmEntity |  | Information about other hvac fans |
| HvacHeatTracing | CdmEntity |  | Information about hvac heat tracing |
| HvacPump | CdmEntity |  | Information about hvac pump |
| HvacShutOffValve | CdmEntity |  | Information about hvac shut off valve |
| HvacSystem | CdmEntity |  | Detailed information about heating, ventilation, and air conditioning system (HVAC) .HVAC refers to the different systems used for moving air between indoor and outdoor areas, along with heating and cooling buildings |
| HvacTank | CdmEntity |  | Information about hvac tank |
| HvacValve | CdmEntity |  | Information about hvac valve used to control flow in pipes |
| IctHardware | CdmEntity |  | Information about ict hardware |
| InformationAndCommunicationSystem | CdmEntity |  | Information about information and communication system |
| ItRack | CdmEntity |  | Information about it rack |
| JockeyPump | CdmEntity |  | Information about jockey pump |
| Land | CdmEntity |  | A defined area of land, possibly covered with water, on which the project construction is to be completed or already completed |
| LightingSystem | CdmEntity |  | Information about lighting system |
| Luminaire | CdmEntity |  | Information about luminaire |
| ModbusController | CdmEntity |  | Information about modbus controller |
| MovingWalkway | CdmEntity |  | Information about moving walkway |
| PlumbingExpansionTank | CdmEntity |  | Information about plumbing expansion tank |
| PlumbingPump | CdmEntity |  | Information about plumbing pump |
| PlumbingPumpSubComponent | CdmEntity |  | Information about plumbing pump sub components |
| PlumbingShutOffValve | CdmEntity |  | Information about plumbing shut off valve |
| PlumbingStorageTank | CdmEntity |  | Information about plumbing storage tank |
| PlumbingSystem | CdmEntity |  | Information about system of pipes and fixtures installed in a building for the distribution and use of potable (drinkable) water and the removal of waterborne wastes |
| PlumbingTank | CdmEntity |  | Information about plumbing tank |
| PlumbingValve | CdmEntity |  | Information about plumbing valve |
| PlumbingValveSubComponent | CdmEntity |  | Information about plumbing valve sub components |
| Sensor | CdmEntity |  | Stores all sensor information, a device which detects or measures a physical property and records, indicates, or otherwise responds to it |
| SensorBuilding | CdmEntity |  | Linking entity between Sensor and Building. The sensor represents the sensor measurement area which can be different from the physical location |
| SensorComponent | CdmEntity |  | Linking entity between Sensor and Component |
| SensorEquipment | CdmEntity |  | Information about sensor equipment |
| SensorFloor | CdmEntity |  | Linking entity between Sensor and Floor. The sensor represents the sensor measurement area which can be different from the physical location |
| SensorLand | CdmEntity |  | Linking entity between Sensor and Land. The sensor represents the sensor measurement area which can be different from the physical location |
| SensorMeasurement | CdmEntity |  | Stores all measurements received from sensors. |
| SensorRentalUnit | CdmEntity |  | Linking entity between Sensor and RentalUnit. The sensor represents the sensor measurement area which can be different from the physical location |
| SensorSite | CdmEntity |  | Linking entity between Sensor and Site. The sensor represents the sensor measurement area which can be different from the physical location |
| SensorSpace | CdmEntity |  | Linking entity between Sensor and Space. The sensor represents the sensor measurement area which can be different from the physical location |
| SensorUnit | CdmEntity |  | Linking entity between Sensor and Unit. The sensor represents the sensor measurement area which can be different from the physical location |
| Server | CdmEntity |  | Information about server |
| Site | CdmEntity |  | Grouping of multiple buildings and lands |
| Space | CdmEntity |  | A space represents an area or volume bounded actually or theoretically. Spaces are areas or volumes that provide for certain functions within a building. |
| SprinklerHeatTracing | CdmEntity |  | Information about fire sprinkler head |
| SprinklerTank | CdmEntity |  | Information about fire sprinkler head |
| SprinklerValve | CdmEntity |  | Information about sprinkler valve |
| System | CdmEntity |  | Entirety of manageable components with a common function (supply air of a ventilation system) |
| SystemBuilding | CdmEntity |  | Linking entity between system and building |
| SystemFloor | CdmEntity |  | Linking entity between system and floor |
| SystemRentalUnit | CdmEntity |  | Linking entity between System and RentalUnit |
| SystemSite | CdmEntity |  | Linking entity between system and site |
| SystemSpace | CdmEntity |  | Linking entity between system and space |
| SystemUnit | CdmEntity |  | Linking entity between system and unit |
| TankWaterHeater | CdmEntity |  | Information about tank water heater |
| TankWaterHeaterSubComponent | CdmEntity |  | Information about tank water heater sub component |
| TanklessWaterHeater | CdmEntity |  | Information about tankless water heater |
| TanklessWaterHeaterSubComponent | CdmEntity |  | Information about tankless water heater sub component |
| TerminalUnit | CdmEntity |  | Information about the terminal unit |
| ThermalMeter | CdmEntity |  | Information about thermal meter |
| Toilet | CdmEntity |  | Information about toilet |
| ToiletFlushometer | CdmEntity |  | Information about toilet flushometer |
| ToiletTank | CdmEntity |  | Information about toilet tank |
| TransferSwitch | CdmEntity |  | Information about transfer switch |
| Transformer | CdmEntity |  | Information about transformer |
| Unit | CdmEntity |  | A unit is a physical quantity, with a value of one, which is used as a standard in terms of which other quantities are expressed. In the case of a building it can be a grouping of areas, spaces, floors, etc. |
| UnitBuilding | CdmEntity |  | Linking entity between Unit and Building |
| UnitFloor | CdmEntity |  | Linking entity between Unit and Floor |
| UnitHeater | CdmEntity |  | Information about steam unit heater |
| UnitLand | CdmEntity |  | Linking entity between Unit and Land |
| UnitSite | CdmEntity |  | Linking entity between Unit and Site |
| UnitSpace | CdmEntity |  | Linking entity between Unit and Space |
| Ups | CdmEntity |  | Information about ups |
| UrinalFlushometer | CdmEntity |  | Information about urinal flushometer |
| VariableFrequencyDrive | CdmEntity |  | Information about variable frequency drive |
| VavBoxReheat | CdmEntity |  | Information about the vav box reheat |
| WaterFiltration | CdmEntity |  | Information about water filtration |
| WaterHeater | CdmEntity |  | Information about water heater |
| WaterMeter | CdmEntity |  | Information about water meter |
| WirelessAccessPoint | CdmEntity |  | Information about wireless access point |

## Fields

| Path | Domain | Range | Cardinality | Definition |
|---|---|---|---|---|
| AccessPanel/AccessPanelId | AccessPanel | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| AccessPanel/ComponentTypeId | AccessPanel |  | optional |  |
| AccessPanel/FireRating | AccessPanel | string | optional | Fire rating |
| AccessPanel/FrameMaterial | AccessPanel | string | optional | Frame material |
| AccessPanel/Height | AccessPanel | decimal | optional | Height |
| AccessPanel/Material | AccessPanel | string | optional | Material of access panel |
| AccessPanel/Thickness | AccessPanel | decimal | optional | Thickness |
| AccessPanel/Type | AccessPanel | string | optional | Access panel type |
| AccessPanel/Width | AccessPanel | decimal | optional | Width |
| AirCompressor/AirCompressorId | AirCompressor | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| AirCompressor/ComponentTypeId | AirCompressor |  | optional |  |
| AirCompressor/FreeAirDelivery | AirCompressor | decimal | optional | Free air delivery |
| AirCompressor/MotorPower | AirCompressor | decimal | optional | Motor power |
| AirCompressor/WorkingPressure | AirCompressor | decimal | optional | WorkingPressure |
| AirFilter/AirFilterId | AirFilter | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| AirFilter/ComponentTypeId | AirFilter |  | optional |  |
| AirFilter/FanCommissionDate | AirFilter | dateTime | optional | Fan commission date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| AirFilter/FanDriveType | AirFilter | string | optional | Fan fan drive type |
| AirFilter/FanDurationLifeYear | AirFilter | integer | optional | Fan life span of component in years |
| AirFilter/FanExpectedEndOfLife | AirFilter | dateTime | optional | Fan expected end of life date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| AirFilter/FanExpectedReplacementCost | AirFilter | decimal | optional | Fan expected replacement costs |
| AirFilter/FanInitialCost | AirFilter | decimal | optional | Fan initial cost |
| AirFilter/FanInstallationDate | AirFilter | dateTime | optional | Installation date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| AirFilter/FanMaintenanceInterval | AirFilter | string | optional | Fan maintenance interval either as string: monthly, quarterly, etc. or as month |
| AirFilter/FanMaxAirflowRating | AirFilter | decimal | optional | Fan max flow capacity |
| AirFilter/FanMinAirflowRating | AirFilter | decimal | optional | Fan min flow capacity |
| AirFilter/FanModelNumber | AirFilter | string | optional | Model number of fan |
| AirFilter/FanMotorPower | AirFilter | decimal | optional | Fan motor power |
| AirFilter/FanName | AirFilter | string | optional | Name of fan |
| AirFilter/FanNominalAirflow | AirFilter | decimal | optional | Fan nominal airflow |
| AirFilter/FanSerialNumber | AirFilter | string | optional | Serial number of fan |
| AirFilter/FanTagNumber | AirFilter | string | optional | Fan tag number |
| AirFilter/FanTurnoverDate | AirFilter | dateTime | optional | Fan turnover date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| AirHandlingUnit/AirHandlingUnitId | AirHandlingUnit | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| AirHandlingUnit/AirflowModulation | AirHandlingUnit | string | optional | Airflow modulation |
| AirHandlingUnit/ComponentTypeId | AirHandlingUnit |  | optional |  |
| AirHandlingUnit/DehumidificationMethod | AirHandlingUnit | string | optional | Dehumidification method |
| AirHandlingUnit/DischargeDuctworkConfiguration | AirHandlingUnit | string | optional | Discharge ductwork configuration |
| AirHandlingUnit/ExhaustFanCommissionDate | AirHandlingUnit | dateTime | optional | Exhaust fan commission date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| AirHandlingUnit/ExhaustFanDriveType | AirHandlingUnit | string | optional | Exhaust fan fan drive type |
| AirHandlingUnit/ExhaustFanDurationLifeYear | AirHandlingUnit | integer | optional | Exhaust fan life span of component in years |
| AirHandlingUnit/ExhaustFanExpectedEndOfLife | AirHandlingUnit | dateTime | optional | Exhaust fan expected end of life date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| AirHandlingUnit/ExhaustFanExpectedReplacementCost | AirHandlingUnit | decimal | optional | Exhaust fan expected replacement costs |
| AirHandlingUnit/ExhaustFanInitialCost | AirHandlingUnit | decimal | optional | Exhaust fan initial cost |
| AirHandlingUnit/ExhaustFanInstallationDate | AirHandlingUnit | dateTime | optional | Installation date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| AirHandlingUnit/ExhaustFanMaintenanceInterval | AirHandlingUnit | string | optional | Exhaust fan maintenance interval either as string: monthly, quarterly, etc. or as month |
| AirHandlingUnit/ExhaustFanMaxAirflowRating | AirHandlingUnit | decimal | optional | Exhaust fan max flow capacity |
| AirHandlingUnit/ExhaustFanMinAirflowRating | AirHandlingUnit | decimal | optional | Exhaust fan min flow capacity |
| AirHandlingUnit/ExhaustFanModelNumber | AirHandlingUnit | string | optional | Model number of exhaust fan |
| AirHandlingUnit/ExhaustFanMotorPower | AirHandlingUnit | decimal | optional | Exhaust fan motor power |
| AirHandlingUnit/ExhaustFanName | AirHandlingUnit | string | optional | Name of exhaust fan |
| AirHandlingUnit/ExhaustFanNominalAirflow | AirHandlingUnit | decimal | optional | Exhaust fan nominal airflow |
| AirHandlingUnit/ExhaustFanSerialNumber | AirHandlingUnit | string | optional | Serial number of exhaust fan |
| AirHandlingUnit/ExhaustFanTagNumber | AirHandlingUnit | string | optional | Exhaust fan tag number |
| AirHandlingUnit/ExhaustFanTurnoverDate | AirHandlingUnit | dateTime | optional | Exhaust fan turnover date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| AirHandlingUnit/FilterType | AirHandlingUnit | string | optional | Filter type |
| AirHandlingUnit/HumidificationMethod | AirHandlingUnit | string | optional | Humidification method |
| AirHandlingUnit/MixingBoxCommissionDate | AirHandlingUnit | dateTime | optional | Mixing box commission date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| AirHandlingUnit/MixingBoxDurationLifeYear | AirHandlingUnit | integer | optional | Mixing box life span of component in years |
| AirHandlingUnit/MixingBoxEconomiser | AirHandlingUnit | string | optional | Mixing box economizer |
| AirHandlingUnit/MixingBoxExpectedEndOfLife | AirHandlingUnit | dateTime | optional | Mixing box expected end of life date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| AirHandlingUnit/MixingBoxExpectedReplacementCost | AirHandlingUnit | decimal | optional | Mixing box expected replacement costs |
| AirHandlingUnit/MixingBoxInitialCost | AirHandlingUnit | decimal | optional | Mixing box initial cost |
| AirHandlingUnit/MixingBoxInstallationDate | AirHandlingUnit | dateTime | optional | Installation date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| AirHandlingUnit/MixingBoxMaintenanceInterval | AirHandlingUnit | string | optional | Mixing box maintenance interval either as string: monthly, quarterly, etc. or as month |
| AirHandlingUnit/MixingBoxModelNumber | AirHandlingUnit | string | optional | Model number of mixing box |
| AirHandlingUnit/MixingBoxName | AirHandlingUnit | string | optional | Mixing box name of product |
| AirHandlingUnit/MixingBoxSerialNumber | AirHandlingUnit | string | optional | Serial number of re heating |
| AirHandlingUnit/MixingBoxTagNumber | AirHandlingUnit | string | optional | Mixing box tag number |
| AirHandlingUnit/MixingBoxTurnoverDate | AirHandlingUnit | dateTime | optional | Mixing box turnover date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| AirHandlingUnit/NetSensibleCoolingCapacity | AirHandlingUnit | decimal | optional | Net sensible cooling capacity |
| AirHandlingUnit/NominalCoolingCapacity | AirHandlingUnit | decimal | optional | Nominal cooling capacity |
| AirHandlingUnit/NominalHeatingCapacity | AirHandlingUnit | decimal | optional | Nominal heating capacity |
| AirHandlingUnit/PreHeatingCommissionDate | AirHandlingUnit | dateTime | optional | Pre heating commission date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| AirHandlingUnit/PreHeatingDurationLifeYear | AirHandlingUnit | integer | optional | Pre heating life span of component in years |
| AirHandlingUnit/PreHeatingExpectedEndOfLife | AirHandlingUnit | dateTime | optional | Pre heating expected end of life date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| AirHandlingUnit/PreHeatingExpectedReplacementCost | AirHandlingUnit | decimal | optional | Pre heating expected replacement costs |
| AirHandlingUnit/PreHeatingInitialCost | AirHandlingUnit | decimal | optional | Pre heating initial cost |
| AirHandlingUnit/PreHeatingInstallationDate | AirHandlingUnit | dateTime | optional | Installation date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| AirHandlingUnit/PreHeatingMaintenanceInterval | AirHandlingUnit | string | optional | Pre heating maintenance interval either as string: monthly, quarterly, etc. or as month |
| AirHandlingUnit/PreHeatingModelNumber | AirHandlingUnit | string | optional | Model number of pre heating |
| AirHandlingUnit/PreHeatingName | AirHandlingUnit | string | optional | Pre heating name of product |
| AirHandlingUnit/PreHeatingOutsideDiameter | AirHandlingUnit | decimal | optional | Pre heating outside diameter |
| AirHandlingUnit/PreHeatingSerialNumber | AirHandlingUnit | string | optional | Serial number of pre heating |
| AirHandlingUnit/PreHeatingTagNumber | AirHandlingUnit | string | optional | Pre heating tag number |
| AirHandlingUnit/PreHeatingTurnoverDate | AirHandlingUnit | dateTime | optional | Pre heating turnover date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| AirHandlingUnit/PreHeatingType | AirHandlingUnit | string | optional | Pre heating type |
| AirHandlingUnit/PrimaryCoolingCommissionDate | AirHandlingUnit | dateTime | optional | Primary cooling commission date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| AirHandlingUnit/PrimaryCoolingDurationLifeYear | AirHandlingUnit | integer | optional | Primary cooling life span of component in years |
| AirHandlingUnit/PrimaryCoolingExpectedEndOfLife | AirHandlingUnit | dateTime | optional | Primary cooling expected end of life date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| AirHandlingUnit/PrimaryCoolingExpectedReplacementCost | AirHandlingUnit | decimal | optional | Primary cooling expected replacement costs |
| AirHandlingUnit/PrimaryCoolingInitialCost | AirHandlingUnit | decimal | optional | Primary cooling initial cost |
| AirHandlingUnit/PrimaryCoolingInstallationDate | AirHandlingUnit | dateTime | optional | Installation date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| AirHandlingUnit/PrimaryCoolingMaintenanceInterval | AirHandlingUnit | string | optional | Primary cooling maintenance interval either as string: monthly, quarterly, etc. or as month |
| AirHandlingUnit/PrimaryCoolingMethodType | AirHandlingUnit | string | optional | Primary cooling method type |
| AirHandlingUnit/PrimaryCoolingMethodeRefrigerantType | AirHandlingUnit | string | optional | Primary cooling refrigerant type |
| AirHandlingUnit/PrimaryCoolingModelNumber | AirHandlingUnit | string | optional | Model number of primary cooling |
| AirHandlingUnit/PrimaryCoolingName | AirHandlingUnit | string | optional | Primary cooling name of product |
| AirHandlingUnit/PrimaryCoolingOutsideDiameter | AirHandlingUnit | decimal | optional | Primary cooling outside diameter |
| AirHandlingUnit/PrimaryCoolingSerialNumber | AirHandlingUnit | string | optional | Serial number of primary cooling |
| AirHandlingUnit/PrimaryCoolingTagNumber | AirHandlingUnit | string | optional | Primary cooling tag number |
| AirHandlingUnit/PrimaryCoolingTurnoverDate | AirHandlingUnit | dateTime | optional | Primary cooling turnover date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| AirHandlingUnit/ReHeatingCommissionDate | AirHandlingUnit | dateTime | optional | Re heating commission date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| AirHandlingUnit/ReHeatingDurationLifeYear | AirHandlingUnit | integer | optional | Re heating life span of component in years |
| AirHandlingUnit/ReHeatingExpectedEndOfLife | AirHandlingUnit | dateTime | optional | Re heating expected end of life date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| AirHandlingUnit/ReHeatingExpectedReplacementCost | AirHandlingUnit | decimal | optional | Re heating expected replacement costs |
| AirHandlingUnit/ReHeatingInitialCost | AirHandlingUnit | decimal | optional | Re heating initial cost |
| AirHandlingUnit/ReHeatingInstallationDate | AirHandlingUnit | dateTime | optional | Installation date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| AirHandlingUnit/ReHeatingMaintenanceInterval | AirHandlingUnit | string | optional | Re heating maintenance interval either as string: monthly, quarterly, etc. or as month |
| AirHandlingUnit/ReHeatingModelNumber | AirHandlingUnit | string | optional | Model number of re heating |
| AirHandlingUnit/ReHeatingName | AirHandlingUnit | string | optional | Re heating name of product |
| AirHandlingUnit/ReHeatingOutsideDiameter | AirHandlingUnit | decimal | optional | Re heating outside diameter |
| AirHandlingUnit/ReHeatingSerialNumber | AirHandlingUnit | string | optional | Serial number of re heating |
| AirHandlingUnit/ReHeatingTagNumber | AirHandlingUnit | string | optional | Re heating tag number |
| AirHandlingUnit/ReHeatingTurnoverDate | AirHandlingUnit | dateTime | optional | Re heating turnover date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| AirHandlingUnit/ReHeatingType | AirHandlingUnit | string | optional | Re heating type |
| AirHandlingUnit/RefrigerantType | AirHandlingUnit | string | optional | Refrigerant type |
| AirHandlingUnit/ReturnFanCommissionDate | AirHandlingUnit | dateTime | optional | Return fan commission date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| AirHandlingUnit/ReturnFanDriveType | AirHandlingUnit | string | optional | Return fan fan drive type |
| AirHandlingUnit/ReturnFanDurationLifeYear | AirHandlingUnit | integer | optional | Return fan life span of component in years |
| AirHandlingUnit/ReturnFanExpectedEndOfLife | AirHandlingUnit | dateTime | optional | Return fan expected end of life date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| AirHandlingUnit/ReturnFanExpectedReplacementCost | AirHandlingUnit | decimal | optional | Return fan expected replacement costs |
| AirHandlingUnit/ReturnFanInitialCost | AirHandlingUnit | decimal | optional | Return fan initial cost |
| AirHandlingUnit/ReturnFanInstallationDate | AirHandlingUnit | dateTime | optional | Installation date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| AirHandlingUnit/ReturnFanMaintenanceInterval | AirHandlingUnit | string | optional | Return fan maintenance interval either as string: monthly, quarterly, etc. or as month |
| AirHandlingUnit/ReturnFanMaxAirflowRating | AirHandlingUnit | decimal | optional | Return fan max flow capacity |
| AirHandlingUnit/ReturnFanMinAirflowRating | AirHandlingUnit | decimal | optional | Return fan min flow capacity |
| AirHandlingUnit/ReturnFanModelNumber | AirHandlingUnit | string | optional | Model number of return fan |
| AirHandlingUnit/ReturnFanMotorPower | AirHandlingUnit | decimal | optional | Return fan motor power |
| AirHandlingUnit/ReturnFanName | AirHandlingUnit | string | optional | Name of return fan |
| AirHandlingUnit/ReturnFanNominalAirflow | AirHandlingUnit | decimal | optional | Return fan nominal airflow |
| AirHandlingUnit/ReturnFanSerialNumber | AirHandlingUnit | string | optional | Serial number of return fan |
| AirHandlingUnit/ReturnFanTagNumber | AirHandlingUnit | string | optional | Return fan tag number |
| AirHandlingUnit/ReturnFanTurnoverDate | AirHandlingUnit | dateTime | optional | Return fan turnover date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| AirHandlingUnit/SecondaryCoolingCommissionDate | AirHandlingUnit | dateTime | optional | Secondary cooling commission date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| AirHandlingUnit/SecondaryCoolingDurationLifeYear | AirHandlingUnit | integer | optional | Secondary cooling life span of component in years |
| AirHandlingUnit/SecondaryCoolingExpectedEndOfLife | AirHandlingUnit | dateTime | optional | Secondary cooling expected end of life date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| AirHandlingUnit/SecondaryCoolingExpectedReplacementCost | AirHandlingUnit | decimal | optional | Secondary cooling expected replacement costs |
| AirHandlingUnit/SecondaryCoolingInitialCost | AirHandlingUnit | decimal | optional | Secondary cooling initial cost |
| AirHandlingUnit/SecondaryCoolingInstallationDate | AirHandlingUnit | dateTime | optional | Installation date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| AirHandlingUnit/SecondaryCoolingMaintenanceInterval | AirHandlingUnit | string | optional | Secondary cooling maintenance interval either as string: monthly, quarterly, etc. or as month |
| AirHandlingUnit/SecondaryCoolingMethodRefrigerantType | AirHandlingUnit | string | optional | Secondary cooling refrigerant type |
| AirHandlingUnit/SecondaryCoolingMethodType | AirHandlingUnit | string | optional | Secondary cooling method type |
| AirHandlingUnit/SecondaryCoolingModelNumber | AirHandlingUnit | string | optional | Model number of secondary cooling |
| AirHandlingUnit/SecondaryCoolingName | AirHandlingUnit | string | optional | Secondary cooling name of product |
| AirHandlingUnit/SecondaryCoolingOutsideDiameter | AirHandlingUnit | decimal | optional | Secondary cooling outside diameter |
| AirHandlingUnit/SecondaryCoolingSerialNumber | AirHandlingUnit | string | optional | Serial number of secondary cooling |
| AirHandlingUnit/SecondaryCoolingTagNumber | AirHandlingUnit | string | optional | Secondary cooling tag number |
| AirHandlingUnit/SecondaryCoolingTurnoverDate | AirHandlingUnit | dateTime | optional | Secondary cooling turnover date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| AirHandlingUnit/SupplyFanCommissionDate | AirHandlingUnit | dateTime | optional | Supply fan commission date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| AirHandlingUnit/SupplyFanDriveType | AirHandlingUnit | string | optional | Supply fan fan drive type |
| AirHandlingUnit/SupplyFanDurationLifeYear | AirHandlingUnit | integer | optional | Supply fan life span of component in years |
| AirHandlingUnit/SupplyFanExpectedEndOfLife | AirHandlingUnit | dateTime | optional | Supply fan expected end of life date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| AirHandlingUnit/SupplyFanExpectedReplacementCost | AirHandlingUnit | decimal | optional | Supply fan expected replacement costs |
| AirHandlingUnit/SupplyFanInitialCost | AirHandlingUnit | decimal | optional | Supply fan initial cost |
| AirHandlingUnit/SupplyFanInstallationDate | AirHandlingUnit | dateTime | optional | Installation date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| AirHandlingUnit/SupplyFanMaintenanceInterval | AirHandlingUnit | string | optional | Supply fan maintenance interval either as string: monthly, quarterly, etc. or as month |
| AirHandlingUnit/SupplyFanMaxAirflowRating | AirHandlingUnit | decimal | optional | Supply fan max flow capacity |
| AirHandlingUnit/SupplyFanMinAirflowRating | AirHandlingUnit | decimal | optional | Supply fan min flow capacity |
| AirHandlingUnit/SupplyFanModelNumber | AirHandlingUnit | string | optional | Model number of supply fan |
| AirHandlingUnit/SupplyFanMotorPower | AirHandlingUnit | decimal | optional | Supply fan motor power |
| AirHandlingUnit/SupplyFanName | AirHandlingUnit | string | optional | Name of supply fan |
| AirHandlingUnit/SupplyFanNominalAirflow | AirHandlingUnit | decimal | optional | Supply fan nominal airflow |
| AirHandlingUnit/SupplyFanSerialNumber | AirHandlingUnit | string | optional | Serial number of supply fan |
| AirHandlingUnit/SupplyFanTagNumber | AirHandlingUnit | string | optional | Supply fan tag number |
| AirHandlingUnit/SupplyFanTurnoverDate | AirHandlingUnit | dateTime | optional | Supply fan turnover date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| AirHandlingUnit/Type | AirHandlingUnit | string | optional | Air handling unit type |
| AirHandlingUnit/VentilationConfiguration | AirHandlingUnit | string | optional | Ventilation configuration |
| AirHandlingUnit/VentilationStrategy | AirHandlingUnit | string | optional | Ventilation strategy |
| AreaMeasurement/Accuracy | AreaMeasurement | string | optional | Accuracy of area measurement |
| AreaMeasurement/AreaMeasurementId | AreaMeasurement | string | optional | Customer ID from previous system  (ID before onboarding data to BM) |
| AreaMeasurement/Standard | AreaMeasurement | string | optional | Area measurement standard |
| AreaMeasurement/Type | AreaMeasurement | string | optional | Type of the standard area |
| AreaMeasurement/Unit | AreaMeasurement | string | optional | Unit area is measured with |
| AreaMeasurementBuilding/AreaMeasurementId | AreaMeasurementBuilding |  | optional |  |
| AreaMeasurementBuilding/BuildingId | AreaMeasurementBuilding |  | optional |  |
| AreaMeasurementFloor/AreaMeasurementId | AreaMeasurementFloor |  | optional |  |
| AreaMeasurementFloor/FloorId | AreaMeasurementFloor |  | optional |  |
| AreaMeasurementLand/AreaMeasurementId | AreaMeasurementLand |  | optional |  |
| AreaMeasurementLand/LandId | AreaMeasurementLand |  | optional |  |
| AreaMeasurementRentalUnit/AreaMeasurementId | AreaMeasurementRentalUnit |  | optional |  |
| AreaMeasurementRentalUnit/RentalUnitId | AreaMeasurementRentalUnit |  | optional |  |
| AreaMeasurementSite/AreaMeasurementId | AreaMeasurementSite |  | optional |  |
| AreaMeasurementSite/SiteId | AreaMeasurementSite |  | optional |  |
| AreaMeasurementSpace/AreaMeasurementId | AreaMeasurementSpace |  | optional |  |
| AreaMeasurementSpace/SpaceId | AreaMeasurementSpace |  | optional |  |
| AreaMeasurementUnit/AreaMeasurementId | AreaMeasurementUnit |  | optional |  |
| AreaMeasurementUnit/UnitId | AreaMeasurementUnit |  | optional |  |
| AutomaticTransferSwitch/AutomaticTransferSwitchId | AutomaticTransferSwitch | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| AutomaticTransferSwitch/MainBusCurrentRating | AutomaticTransferSwitch | decimal | optional | Current rating |
| AutomaticTransferSwitch/MainBusMaterial | AutomaticTransferSwitch | string | optional | Material |
| AutomaticTransferSwitch/MainsRating | AutomaticTransferSwitch | decimal | optional | Mains rating |
| AutomaticTransferSwitch/Poles | AutomaticTransferSwitch | integer | optional | Poles |
| AutomaticTransferSwitch/SwitchingMechanism | AutomaticTransferSwitch | string | optional | Switching Mechanism |
| AutomaticTransferSwitch/TransferSwitchId | AutomaticTransferSwitch |  | optional |  |
| AutomaticTransferSwitch/TransitionType | AutomaticTransferSwitch | string | optional | Transition type |
| BacNetController/Address | BacNetController | string | optional | Bac net controller address |
| BacNetController/BacNetControllerId | BacNetController | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| BacNetController/ConnectorId | BacNetController | string | optional | Registration id |
| BacNetController/ControllerId | BacNetController |  | optional |  |
| BacNetController/Detected | BacNetController | boolean | optional | Detected (Y/N) |
| BacNetController/Enabled | BacNetController | boolean | optional | Enabled (Y/N) |
| BacNetController/RegistrationId | BacNetController | string | optional | Registration id |
| BacNetController/RegistrationKey | BacNetController | string | optional | Registration key |
| Boiler/BoilerId | Boiler | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| Boiler/ComponentTypeId | Boiler |  | optional |  |
| Boiler/Medium | Boiler | string | optional | Medium of boiler |
| Boiler/PowerInput | Boiler | decimal | optional | Power input |
| Boiler/PowerOutput | Boiler | decimal | optional | Power output |
| Boiler/Recovery100FRise | Boiler | decimal | optional | Recovery rate to 100 frise in l per hour |
| Boiler/TankCapacity | Boiler | decimal | optional | Tank capacity |
| Boiler/Type | Boiler | string | optional | Boiler type |
| Building/AirConditioning | Building | boolean | optional | Does the building have air conditioning (Y/N) (Needed for precise  future emissions projection of building) |
| Building/BuildingCode | Building | string | optional | User specific Building Code |
| Building/BuildingId | Building | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| Building/ConstructionYear | Building | dateTime | optional | Year of construction in yyyy-mm-ddThh:mm:ssZ form (conform ISO 8061). In case only year exists use yyyy-01-01T00:00:00Z. |
| Building/ElectricVehicleChargingStations | Building | integer | optional | Number of electric vehicle charging stations |
| Building/EnergyEfficiencyClass | Building | string | optional | Energy Efficiency Class of Building |
| Building/MonumentProtection | Building | boolean | optional | The building is declared to be an ancient monument with national importance by the government |
| Building/ParkingSpaces | Building | integer | optional | Number of parking spaces |
| Building/PrimaryEnergyType | Building | string | optional | Type of energy used |
| Building/PrimaryHeatingType | Building | string | optional | Primary Type of heating |
| Building/PrimaryTypeOfBuilding | Building | string | optional | Type of building use |
| Building/PrimaryWaterType | Building | string | optional | Type of water used |
| Building/SecondaryHeatingType | Building | string | optional | Secondary Type of heating |
| Building/SecondaryTypeOfBuilding | Building | string | optional | Second type of building use |
| Building/SelfUse | Building | boolean | optional | Is building self used or not (Y/N) |
| Building/SiteId | Building |  | optional |  |
| Building/Status | Building | string | optional | Status of site |
| Building/TenantStructure | Building | string | optional | Is there multiple tenants in the building or only one |
| Building/TypeOfOwnership | Building | string | optional | Is the building owned or leased. |
| Building/YearOfLastRefurbishment | Building | dateTime | optional | Year of last refurbishment took place in yyyy-mm-ddThh:mm:ssZ form (conform ISO 8061). In case only year exists use yyyy-01-01T00:00:00Z. |
| CeilingFan/BladeDiameter | CeilingFan | decimal | optional | Blade diameter of ceiling fan |
| CeilingFan/CeilingFanId | CeilingFan | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| CeilingFan/DriveType | CeilingFan | string | optional | Ceiling fan drive type |
| CeilingFan/DuctInletCommissionDate | CeilingFan | dateTime | optional | Commission date if duct inlet in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| CeilingFan/DuctInletConfiguration | CeilingFan | string | optional | Duct inlet configuration |
| CeilingFan/DuctInletExpectedEndOfLife | CeilingFan | dateTime | optional | Expected end of life date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| CeilingFan/DuctInletExpectedReplacementCost | CeilingFan | decimal | optional | Duct inlet expected replacement costs |
| CeilingFan/DuctInletInitialCost | CeilingFan | decimal | optional | Duct inlet initial cost |
| CeilingFan/DuctInletInstallationDate | CeilingFan | dateTime | optional | Duct inlet Installation date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| CeilingFan/DuctInletMaintenanceInterval | CeilingFan | string | optional | Duct inlet maintenance interval either as string: monthly, quarterly, etc. or as month |
| CeilingFan/DuctInletModel | CeilingFan | string | optional | Duct inlet model number |
| CeilingFan/DuctInletName | CeilingFan | string | optional | Name of Duct inlet |
| CeilingFan/DuctInletSerialNumber | CeilingFan | string | optional | Serial number of component |
| CeilingFan/DuctInletShape | CeilingFan | decimal | optional | Duct inlet shape |
| CeilingFan/DuctInletSize | CeilingFan | decimal | optional | Duct inlet size |
| CeilingFan/DuctInletTagNumber | CeilingFan | string | optional | Tag number |
| CeilingFan/DuctInletTurnoverDate | CeilingFan | dateTime | optional | Duct inlet turnover date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| CeilingFan/FanCommissionDate | CeilingFan | dateTime | optional | Fan commission date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| CeilingFan/FanDriveType | CeilingFan | string | optional | Fan fan drive type |
| CeilingFan/FanDurationLifeYear | CeilingFan | integer | optional | Fan life span of component in years |
| CeilingFan/FanExpectedEndOfLife | CeilingFan | dateTime | optional | Fan expected end of life date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| CeilingFan/FanExpectedReplacementCost | CeilingFan | decimal | optional | Fan expected replacement costs |
| CeilingFan/FanInitialCost | CeilingFan | decimal | optional | Fan initial cost |
| CeilingFan/FanInstallationDate | CeilingFan | dateTime | optional | Installation date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| CeilingFan/FanMaintenanceInterval | CeilingFan | string | optional | Fan maintenance interval either as string: monthly, quarterly, etc. or as month |
| CeilingFan/FanMaxAirflowRating | CeilingFan | decimal | optional | Fan max flow capacity |
| CeilingFan/FanMinAirflowRating | CeilingFan | decimal | optional | Fan min flow capacity |
| CeilingFan/FanModelNumber | CeilingFan | string | optional | Model number of fan |
| CeilingFan/FanMotorPower | CeilingFan | decimal | optional | Fan motor power |
| CeilingFan/FanName | CeilingFan | string | optional | Name of fan |
| CeilingFan/FanNominalAirflow | CeilingFan | decimal | optional | Fan nominal airflow |
| CeilingFan/FanSerialNumber | CeilingFan | string | optional | Serial number of fan |
| CeilingFan/FanTagNumber | CeilingFan | string | optional | Fan tag number |
| CeilingFan/FanTurnoverDate | CeilingFan | dateTime | optional | Fan turnover date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| CeilingFan/HvacFanId | CeilingFan |  | optional |  |
| CeilingFan/MaxAirflowRating | CeilingFan | decimal | optional | Max flow capacity |
| CeilingFan/MaxRotationSpeed | CeilingFan | decimal | optional | Max rotation speed in rotations per minute |
| CeilingFan/MinAirflowRating | CeilingFan | decimal | optional | Min flow capacity |
| CeilingFan/MotorPower | CeilingFan | decimal | optional | Motor power |
| CeilingFan/NominalAirflow | CeilingFan | decimal | optional | Nominal airflow |
| CeilingFan/Type | CeilingFan | string | optional | Ceiling fan type |
| Certificate/CertificateId | Certificate | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| Certificate/CertificateUrl | Certificate | string | optional | Certificate Url |
| Certificate/CertificateValue | Certificate | string | optional | Score, grade if applicable for the certificate |
| Certificate/DocumentId | Certificate | string | optional | Unique identifier either coming from previous system otherwise it needs to be define |
| Certificate/IssuingDate | Certificate | dateTime | optional | Date certificate was issued in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| Certificate/Type | Certificate | string | optional | Type of Certificate e.g: LEED, BREEAM, DGNB |
| CertificateBuilding/BuildingId | CertificateBuilding |  | optional |  |
| CertificateBuilding/CertificateId | CertificateBuilding |  | optional |  |
| CertificateComponent/CertificateId | CertificateComponent |  | optional |  |
| CertificateComponent/ComponentId | CertificateComponent |  | optional |  |
| CertificateSystem/CertificateId | CertificateSystem |  | optional |  |
| CertificateSystem/SystemId | CertificateSystem |  | optional |  |
| CertificateValuation/CertificateId | CertificateValuation |  | optional |  |
| CertificateValuation/ValuationId | CertificateValuation |  | optional |  |
| Chiller/ChillerId | Chiller | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| Chiller/ComponentTypeId | Chiller |  | optional |  |
| Chiller/CompressorType | Chiller | string | optional | Compressor type |
| Chiller/NetSensibleCoolingCapacity | Chiller | decimal | optional | Net sensible cooling capacity |
| Chiller/NominalCoolingCapacity | Chiller | decimal | optional | Nominal cooling capacity |
| Chiller/RefrigerantType | Chiller | string | optional | Refrigerant type |
| Chiller/Type | Chiller | string | optional | Chiller type |
| CoGenerator/BulkStorageCapacity | CoGenerator | decimal | optional | Bulk storage capacity |
| CoGenerator/CoGeneratorId | CoGenerator | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| CoGenerator/DayTankCapacity | CoGenerator | decimal | optional | Day tank capacity |
| CoGenerator/Frequency | CoGenerator | string | optional | Frequency |
| CoGenerator/FuelType | CoGenerator | string | optional | Fuel type |
| CoGenerator/GeneratorId | CoGenerator |  | optional |  |
| CoGenerator/ModeOfOperation | CoGenerator | string | optional | Mode of operation |
| CoGenerator/OutputPhases | CoGenerator | string | optional | Output phases |
| CoGenerator/OutputVoltage | CoGenerator | decimal | optional | Output voltage |
| CoGenerator/PrimePower | CoGenerator | decimal | optional | Standby power |
| CoGenerator/PrimePowerKva | CoGenerator | decimal | optional | Prime power kva |
| CoGenerator/StandbyPower | CoGenerator | decimal | optional | Standby power |
| CoGenerator/StandbyPowerKva | CoGenerator | decimal | optional | Standby power kva |
| Component/Barcode | Component | string | optional | Barcode of component |
| Component/CommissionDate | Component | dateTime | optional | Commission date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| Component/ComponentId | Component | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| Component/ComponentTypeId | Component |  | optional |  |
| Component/ConditionStatus | Component | string | optional | Condition of component |
| Component/Description | Component | string | optional | Description of component |
| Component/DurationLifeYear | Component |  | optional | Life span of component in years |
| Component/ExpectedEndOfLife | Component | dateTime | optional | Expected end of life date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| Component/ExpectedReplacementCost | Component | decimal | optional | Expected replacement costs |
| Component/GeometrySpatialReference | Component | string | optional | Description of component |
| Component/InitialCost | Component | decimal | optional | Initial cost |
| Component/InstallationDate | Component | dateTime | optional | Installation date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| Component/SerialNumber | Component | string | optional | Serial number of component |
| Component/TagNumber | Component | string | optional | Tag number |
| Component/TurnoverDate | Component | dateTime | optional | Turnover date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| Component/WarrantyStartDate | Component | dateTime | optional | Warranty start date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| ComponentBuilding/BuildingId | ComponentBuilding |  | optional |  |
| ComponentBuilding/ComponentId | ComponentBuilding |  | optional |  |
| ComponentFloor/ComponentId | ComponentFloor |  | optional |  |
| ComponentFloor/FloorId | ComponentFloor |  | optional |  |
| ComponentRentalUnit/ComponentId | ComponentRentalUnit |  | optional |  |
| ComponentRentalUnit/RentalUnitId | ComponentRentalUnit |  | optional |  |
| ComponentSite/ComponentId | ComponentSite |  | optional |  |
| ComponentSite/SiteId | ComponentSite |  | optional |  |
| ComponentSpace/ComponentId | ComponentSpace |  | optional |  |
| ComponentSpace/SpaceId | ComponentSpace |  | optional |  |
| ComponentSystem/ComponentId | ComponentSystem |  | optional |  |
| ComponentSystem/SystemId | ComponentSystem |  | optional |  |
| ComponentType/CeIdentification | ComponentType | string | optional | European identification number |
| ComponentType/ComponentTypeId | ComponentType | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| ComponentType/Description | ComponentType | string | optional | Description of component type |
| ComponentType/DocumentId | ComponentType | string | optional | Link to document |
| ComponentType/ExpectedLifeYear | ComponentType |  | optional | Life span of product in years |
| ComponentType/MaintenanceGroup | ComponentType | string | optional | Maintenance group |
| ComponentType/MaintenanceInterval | ComponentType | string | optional | Maintenance interval either as string: monthly, quarterly, etc. or as month |
| ComponentType/MaintenanceRelevance | ComponentType | string | optional | Relevance of maintenance |
| ComponentType/Model | ComponentType | string | optional | Component type name and/or number |
| ComponentType/ModelNumber | ComponentType | string | optional | Model number of component type |
| ComponentType/UrlLibrary | ComponentType | string | optional | Product website |
| ComponentType/WarrantyDuration | ComponentType | integer | optional | Warranty duration in months |
| ComponentUnit/ComponentId | ComponentUnit |  | optional |  |
| ComponentUnit/UnitId | ComponentUnit |  | optional |  |
| CondensingUnit/ComponentTypeId | CondensingUnit |  | optional |  |
| CondensingUnit/CondensingUnitId | CondensingUnit | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| CondensingUnit/EnergyEfficiencyRating | CondensingUnit | string | optional | Energy efficiency rating |
| CondensingUnit/NetSensibleCoolingCapacity | CondensingUnit | decimal | optional | Net sensible cooling capacity |
| CondensingUnit/NetSensibleHeatingCapacity | CondensingUnit | decimal | optional | Net sensible heating capacity |
| CondensingUnit/NominalCoolingCapacity | CondensingUnit | decimal | optional | Nominal cooling capacity |
| CondensingUnit/NominalHeatingCapacity | CondensingUnit | decimal | optional | Nominal heating capacity |
| CondensingUnit/RefrigerantType | CondensingUnit | string | optional | Refrigerant type |
| CondensingUnit/Type | CondensingUnit | string | optional | Condensing unit type |
| Controller/ComponentTypeId | Controller |  | optional |  |
| Controller/ConnectorId | Controller | string | optional | Registration id |
| Controller/ControllerId | Controller | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| Controller/Detected | Controller | boolean | optional | Detected (Y/N) |
| Controller/Enabled | Controller | boolean | optional | Enabled (Y/N) |
| Controller/RegistrationId | Controller | string | optional | Registration id |
| Controller/RegistrationKey | Controller | string | optional | Registration key |
| Controller/Type | Controller | string | optional | Controller type |
| CoolingTower/ComponentTypeId | CoolingTower |  | optional |  |
| CoolingTower/CoolingTowerId | CoolingTower | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| CoolingTower/FanCommissionDate | CoolingTower | dateTime | optional | Fan commission date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| CoolingTower/FanDriveType | CoolingTower | string | optional | Fan fan drive type |
| CoolingTower/FanDurationLifeYear | CoolingTower | integer | optional | Fan life span of component in years |
| CoolingTower/FanExpectedEndOfLife | CoolingTower | dateTime | optional | Fan expected end of life date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| CoolingTower/FanExpectedReplacementCost | CoolingTower | decimal | optional | Fan expected replacement costs |
| CoolingTower/FanInitialCost | CoolingTower | decimal | optional | Fan initial cost |
| CoolingTower/FanInstallationDate | CoolingTower | dateTime | optional | Installation date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| CoolingTower/FanMaintenanceInterval | CoolingTower | string | optional | Fan maintenance interval either as string: monthly, quarterly, etc. or as month |
| CoolingTower/FanMaxAirflowRating | CoolingTower | decimal | optional | Fan max flow capacity |
| CoolingTower/FanMinAirflowRating | CoolingTower | decimal | optional | Fan min flow capacity |
| CoolingTower/FanModelNumber | CoolingTower | string | optional | Model number of fan |
| CoolingTower/FanMotorPower | CoolingTower | decimal | optional | Fan motor power |
| CoolingTower/FanName | CoolingTower | string | optional | Name of fan |
| CoolingTower/FanNominalAirflow | CoolingTower | decimal | optional | Fan nominal airflow |
| CoolingTower/FanSerialNumber | CoolingTower | string | optional | Serial number of fan |
| CoolingTower/FanTagNumber | CoolingTower | string | optional | Fan tag number |
| CoolingTower/FanTurnoverDate | CoolingTower | dateTime | optional | Fan turnover date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| CoolingTower/FlowCapacity | CoolingTower | decimal | optional | Flow capacity |
| CoolingTower/NominalCoolingCapacity | CoolingTower | decimal | optional | Nominal cooling capacity |
| Damper/BladeType | Damper | string | optional | Blade type of damper (usually two different types of blade dampers used to modulate air flow: parallel and opposed blade dampers) |
| Damper/ComponentTypeId | Damper |  | optional |  |
| Damper/DamperId | Damper | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| Damper/DuctInletCommissionDate | Damper | dateTime | optional | Commission date if duct inlet in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| Damper/DuctInletConfiguration | Damper | string | optional | Duct inlet configuration |
| Damper/DuctInletExpectedEndOfLife | Damper | dateTime | optional | Expected end of life date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| Damper/DuctInletExpectedReplacementCost | Damper | decimal | optional | Duct inlet expected replacement costs |
| Damper/DuctInletInitialCost | Damper | decimal | optional | Duct inlet initial cost |
| Damper/DuctInletInstallationDate | Damper | dateTime | optional | Duct inlet Installation date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| Damper/DuctInletMaintenanceInterval | Damper | string | optional | Duct inlet maintenance interval either as string: monthly, quarterly, etc. or as month |
| Damper/DuctInletModel | Damper | string | optional | Duct inlet model number |
| Damper/DuctInletName | Damper | string | optional | Name of Duct inlet |
| Damper/DuctInletSerialNumber | Damper | string | optional | Serial number of component |
| Damper/DuctInletShape | Damper | decimal | optional | Duct inlet shape |
| Damper/DuctInletSize | Damper | decimal | optional | Duct inlet size |
| Damper/DuctInletTagNumber | Damper | string | optional | Tag number |
| Damper/DuctInletTurnoverDate | Damper | dateTime | optional | Duct inlet turnover date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| Damper/LeakageClass | Damper | string | optional | Class component belongs to |
| Damper/Type | Damper | string | optional | Define the specific damper type |
| DataNetworkEquipment/ComponentTypeId | DataNetworkEquipment |  | optional |  |
| DataNetworkEquipment/DataNetworkEquipmentId | DataNetworkEquipment | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| DataNetworkEquipment/MountedInRack | DataNetworkEquipment | boolean | optional | Mounted in it rack |
| DataNetworkEquipment/RackPosition | DataNetworkEquipment | string | optional | It rack position |
| DataNetworkEquipment/Type | DataNetworkEquipment | string | optional | Data network type |
| DataNetworkSubComponent/DataNetworkEquipmentId | DataNetworkSubComponent |  | optional |  |
| DataNetworkSubComponent/DataNetworkSubComponentId | DataNetworkSubComponent | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| DataNetworkSubComponent/HeightRUs | DataNetworkSubComponent | decimal | optional | Height of RUs (rack units) |
| DataNetworkSubComponent/NumberOfPorts | DataNetworkSubComponent | integer | optional | Number of ports |
| DataNetworkSubComponent/RackPosition | DataNetworkSubComponent | string | optional | It rack position |
| DataNetworkSubComponent/Type | DataNetworkSubComponent | string | optional | Data network equipment sub component type |
| ElectricalDistributionEquipmentSubComponent/ComponentTypeId | ElectricalDistributionEquipmentSubComponent |  | optional |  |
| ElectricalDistributionEquipmentSubComponent/ElectricalDistributionEquipmentSubComponentId | ElectricalDistributionEquipmentSubComponent | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| ElectricalDistributionEquipmentSubComponent/InputPhases | ElectricalDistributionEquipmentSubComponent | string | optional | Input phases |
| ElectricalDistributionEquipmentSubComponent/InputVoltage | ElectricalDistributionEquipmentSubComponent | decimal | optional | Input voltage |
| ElectricalDistributionEquipmentSubComponent/MainBusCommissionDate | ElectricalDistributionEquipmentSubComponent | dateTime | optional | Electrical distribution equipment sub component commission date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| ElectricalDistributionEquipmentSubComponent/MainBusCurrentRating | ElectricalDistributionEquipmentSubComponent | decimal | optional | Current rating |
| ElectricalDistributionEquipmentSubComponent/MainBusDurationLifeYear | ElectricalDistributionEquipmentSubComponent | integer | optional | Electrical distribution equipment sub component life span of component in years |
| ElectricalDistributionEquipmentSubComponent/MainBusExpectedEndOfLife | ElectricalDistributionEquipmentSubComponent | dateTime | optional | Electrical distribution equipment sub component expected end of life date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| ElectricalDistributionEquipmentSubComponent/MainBusExpectedReplacementCost | ElectricalDistributionEquipmentSubComponent | decimal | optional | Electrical distribution equipment sub component expected replacement costs |
| ElectricalDistributionEquipmentSubComponent/MainBusInitialCost | ElectricalDistributionEquipmentSubComponent | decimal | optional | Electrical distribution equipment sub component initial cost |
| ElectricalDistributionEquipmentSubComponent/MainBusInstallationDate | ElectricalDistributionEquipmentSubComponent | dateTime | optional | Installation date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| ElectricalDistributionEquipmentSubComponent/MainBusMaintenanceInterval | ElectricalDistributionEquipmentSubComponent | string | optional | Electrical distribution equipment sub component maintenance interval either as string: monthly, quarterly, etc. or as month |
| ElectricalDistributionEquipmentSubComponent/MainBusMaterial | ElectricalDistributionEquipmentSubComponent | string | optional | Material |
| ElectricalDistributionEquipmentSubComponent/MainBusModelNumber | ElectricalDistributionEquipmentSubComponent | string | optional | Model number of electrical distribution equipment sub component |
| ElectricalDistributionEquipmentSubComponent/MainBusName | ElectricalDistributionEquipmentSubComponent | string | optional | Main bus name |
| ElectricalDistributionEquipmentSubComponent/MainBusSerialNumber | ElectricalDistributionEquipmentSubComponent | string | optional | Serial number of electrical distribution equipment sub component |
| ElectricalDistributionEquipmentSubComponent/MainBusTagNumber | ElectricalDistributionEquipmentSubComponent | string | optional | Electrical distribution equipment sub component tag number |
| ElectricalDistributionEquipmentSubComponent/MainBusTurnoverDate | ElectricalDistributionEquipmentSubComponent | dateTime | optional | Electrical distribution equipment sub component turnover date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| ElectricalDistributionEquipmentSubComponent/ShortCircuitRating | ElectricalDistributionEquipmentSubComponent | decimal | optional | Short circuit rating |
| ElectricalMeter/ComponentTypeId | ElectricalMeter |  | optional |  |
| ElectricalMeter/ElectricalMeterId | ElectricalMeter | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| ElectricalMeter/ExportEnergy | ElectricalMeter | decimal | optional | Export energy |
| ElectricalMeter/ExportPower | ElectricalMeter | decimal | optional | Export power |
| ElectricalMeter/ImportEnergy | ElectricalMeter | decimal | optional | Import energy |
| ElectricalMeter/ImportPower | ElectricalMeter | decimal | optional | Import power |
| ElectricalMeter/NetEnergy | ElectricalMeter | decimal | optional | Net energy |
| ElectricalMeter/NetPower | ElectricalMeter | decimal | optional | Net power |
| ElectricalMeter/Type | ElectricalMeter | string | optional | Electrical meter type |
| ElectricalPanelBoard/ComponentTypeId | ElectricalPanelBoard |  | optional |  |
| ElectricalPanelBoard/ElectricalPanelBoardId | ElectricalPanelBoard | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| ElectricalPanelBoard/InputPhases | ElectricalPanelBoard | string | optional | Input phases |
| ElectricalPanelBoard/InputVoltage | ElectricalPanelBoard | decimal | optional | Input voltage |
| ElectricalPanelBoard/MainBusCommissionDate | ElectricalPanelBoard | dateTime | optional | Electrical panel board commission date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| ElectricalPanelBoard/MainBusCurrentRating | ElectricalPanelBoard | decimal | optional | Current rating |
| ElectricalPanelBoard/MainBusDurationLifeYear | ElectricalPanelBoard | integer | optional | Electrical panel board life span of component in years |
| ElectricalPanelBoard/MainBusExpectedEndOfLife | ElectricalPanelBoard | dateTime | optional | Electrical panel board expected end of life date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| ElectricalPanelBoard/MainBusExpectedReplacementCost | ElectricalPanelBoard | decimal | optional | Electrical panel board expected replacement costs |
| ElectricalPanelBoard/MainBusInitialCost | ElectricalPanelBoard | decimal | optional | Electrical panel board initial cost |
| ElectricalPanelBoard/MainBusInstallationDate | ElectricalPanelBoard | dateTime | optional | Installation date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| ElectricalPanelBoard/MainBusMaintenanceInterval | ElectricalPanelBoard | string | optional | Electrical panel board maintenance interval either as string: monthly, quarterly, etc. or as month |
| ElectricalPanelBoard/MainBusMaterial | ElectricalPanelBoard | string | optional | Material |
| ElectricalPanelBoard/MainBusModelNumber | ElectricalPanelBoard | string | optional | Model number of electrical panel board |
| ElectricalPanelBoard/MainBusName | ElectricalPanelBoard | string | optional | Main bus name |
| ElectricalPanelBoard/MainBusSerialNumber | ElectricalPanelBoard | string | optional | Serial number of electrical panel board |
| ElectricalPanelBoard/MainBusTagNumber | ElectricalPanelBoard | string | optional | Electrical panel board number |
| ElectricalPanelBoard/MainBusTurnoverDate | ElectricalPanelBoard | dateTime | optional | Electrical panel board turnover date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| ElectricalPanelBoard/MaxNumberOfPoles | ElectricalPanelBoard | integer | optional | Max number of poles |
| ElectricalPanelBoard/OutputPhases | ElectricalPanelBoard | string | optional | Output phases |
| ElectricalPanelBoard/ShortCircuitRating | ElectricalPanelBoard | decimal | optional | Short circuit rating |
| ElectricalPanelBoard/Type | ElectricalPanelBoard | string | optional | Electrical panel board type |
| ElectricalPanelBoardMcb/ElectricalPanelBoardId | ElectricalPanelBoardMcb |  | optional |  |
| ElectricalPanelBoardMcb/ElectricalPanelBoardMcbId | ElectricalPanelBoardMcb | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| ElectricalPanelBoardMcb/InputPhases | ElectricalPanelBoardMcb | string | optional | Input phases |
| ElectricalPanelBoardMcb/InputVoltage | ElectricalPanelBoardMcb | decimal | optional | Input voltage |
| ElectricalPanelBoardMcb/MainBusCommissionDate | ElectricalPanelBoardMcb | dateTime | optional | Electrical panel board mcb commission date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| ElectricalPanelBoardMcb/MainBusCurrentRating | ElectricalPanelBoardMcb | decimal | optional | Current rating |
| ElectricalPanelBoardMcb/MainBusDurationLifeYear | ElectricalPanelBoardMcb | integer | optional | Electrical panel board mcb life span of component in years |
| ElectricalPanelBoardMcb/MainBusExpectedEndOfLife | ElectricalPanelBoardMcb | dateTime | optional | Electrical panel board mcb expected end of life date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| ElectricalPanelBoardMcb/MainBusExpectedReplacementCost | ElectricalPanelBoardMcb | decimal | optional | Electrical panel board mcb expected replacement costs |
| ElectricalPanelBoardMcb/MainBusInitialCost | ElectricalPanelBoardMcb | decimal | optional | Electrical panel board mcb initial cost |
| ElectricalPanelBoardMcb/MainBusInstallationDate | ElectricalPanelBoardMcb | dateTime | optional | Installation date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| ElectricalPanelBoardMcb/MainBusMaintenanceInterval | ElectricalPanelBoardMcb | string | optional | Electrical panel board mcb maintenance interval either as string: monthly, quarterly, etc. or as month |
| ElectricalPanelBoardMcb/MainBusMaterial | ElectricalPanelBoardMcb | string | optional | Material |
| ElectricalPanelBoardMcb/MainBusModelNumber | ElectricalPanelBoardMcb | string | optional | Model number of electrical panel board mcb |
| ElectricalPanelBoardMcb/MainBusName | ElectricalPanelBoardMcb | string | optional | Main bus name |
| ElectricalPanelBoardMcb/MainBusSerialNumber | ElectricalPanelBoardMcb | string | optional | Serial number of electrical panel board mcb |
| ElectricalPanelBoardMcb/MainBusTagNumber | ElectricalPanelBoardMcb | string | optional | Electrical panel board mcb tag number |
| ElectricalPanelBoardMcb/MainBusTurnoverDate | ElectricalPanelBoardMcb | dateTime | optional | Electrical panel board mcb turnover date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| ElectricalPanelBoardMcb/MaxNumberOfPoles | ElectricalPanelBoardMcb | integer | optional | Max number of poles |
| ElectricalPanelBoardMcb/McbRating | ElectricalPanelBoardMcb | string | optional | Mcb rating |
| ElectricalPanelBoardMcb/OutputPhases | ElectricalPanelBoardMcb | string | optional | Output phases |
| ElectricalPanelBoardMcb/ShortCircuitRating | ElectricalPanelBoardMcb | decimal | optional | Short circuit rating |
| ElectricalPanelBoardMlo/ElectricalPanelBoardId | ElectricalPanelBoardMlo |  | optional |  |
| ElectricalPanelBoardMlo/ElectricalPanelBoardMloId | ElectricalPanelBoardMlo | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| ElectricalPanelBoardMlo/InputPhases | ElectricalPanelBoardMlo | string | optional | Input phases |
| ElectricalPanelBoardMlo/InputVoltage | ElectricalPanelBoardMlo | decimal | optional | Input voltage |
| ElectricalPanelBoardMlo/MainBusCommissionDate | ElectricalPanelBoardMlo | dateTime | optional | Electrical panel board mlo commission date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| ElectricalPanelBoardMlo/MainBusCurrentRating | ElectricalPanelBoardMlo | decimal | optional | Current rating |
| ElectricalPanelBoardMlo/MainBusDurationLifeYear | ElectricalPanelBoardMlo | integer | optional | Electrical panel board mlo life span of component in years |
| ElectricalPanelBoardMlo/MainBusExpectedEndOfLife | ElectricalPanelBoardMlo | dateTime | optional | Electrical panel board mlo expected end of life date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| ElectricalPanelBoardMlo/MainBusExpectedReplacementCost | ElectricalPanelBoardMlo | decimal | optional | Electrical panel board mlo expected replacement costs |
| ElectricalPanelBoardMlo/MainBusInitialCost | ElectricalPanelBoardMlo | decimal | optional | Electrical panel board mlo initial cost |
| ElectricalPanelBoardMlo/MainBusInstallationDate | ElectricalPanelBoardMlo | dateTime | optional | Installation date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| ElectricalPanelBoardMlo/MainBusMaintenanceInterval | ElectricalPanelBoardMlo | string | optional | Electrical panel board mlo maintenance interval either as string: monthly, quarterly, etc. or as month |
| ElectricalPanelBoardMlo/MainBusMaterial | ElectricalPanelBoardMlo | string | optional | Material |
| ElectricalPanelBoardMlo/MainBusModelNumber | ElectricalPanelBoardMlo | string | optional | Model number of electrical panel board mlo |
| ElectricalPanelBoardMlo/MainBusName | ElectricalPanelBoardMlo | string | optional | Main bus name |
| ElectricalPanelBoardMlo/MainBusSerialNumber | ElectricalPanelBoardMlo | string | optional | Serial number of electrical panel board mlo |
| ElectricalPanelBoardMlo/MainBusTagNumber | ElectricalPanelBoardMlo | string | optional | Electrical panel board mlo tag number |
| ElectricalPanelBoardMlo/MainBusTurnoverDate | ElectricalPanelBoardMlo | dateTime | optional | Electrical panel board mlo turnover date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| ElectricalPanelBoardMlo/MaxNumberOfPoles | ElectricalPanelBoardMlo | integer | optional | Max number of poles |
| ElectricalPanelBoardMlo/OutputPhases | ElectricalPanelBoardMlo | string | optional | Output phases |
| ElectricalPanelBoardMlo/ShortCircuitRating | ElectricalPanelBoardMlo | decimal | optional | Short circuit rating |
| ElectricalSystem/CircuitLoadName | ElectricalSystem | string | optional | Circuit load name |
| ElectricalSystem/CircuitName | ElectricalSystem | string | optional | Circuit name |
| ElectricalSystem/CircuitNumber | ElectricalSystem | string | optional | Circuit number |
| ElectricalSystem/ConnectedDemand | ElectricalSystem | decimal | optional | Connected demand. The sum of ratings of all electrical equipments that are connected at the supply point regardless of their status of operation |
| ElectricalSystem/CurrentDraw | ElectricalSystem | decimal | optional | Amount of current an amplifier demands while it is operating in amps |
| ElectricalSystem/DedicatedCircuit | ElectricalSystem | boolean | optional | Dedicated circuit (Y/N) |
| ElectricalSystem/ElectricalCurrentDensity | ElectricalSystem | decimal | optional | Amount of electric current flowing through a unit cross-sectional area |
| ElectricalSystem/ElectricalPowerFactor | ElectricalSystem | decimal | optional | Power factor usually in percentage and expression of energy efficiency |
| ElectricalSystem/ElectricalSource | ElectricalSystem | string | optional | Electrical source |
| ElectricalSystem/ElectricalSystemId | ElectricalSystem | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| ElectricalSystem/EstimatedDemand | ElectricalSystem | decimal | optional | Estimated demand |
| ElectricalSystem/HVACConnectedDemand | ElectricalSystem | decimal | optional | Connected demand HVAC |
| ElectricalSystem/HVACEstimatedDemand | ElectricalSystem | decimal | optional | Estimated demand HVAC |
| ElectricalSystem/LightingConnectedDemand | ElectricalSystem | decimal | optional | Connected demand lighting |
| ElectricalSystem/LightingEstimatedDemand | ElectricalSystem | decimal | optional | Estimated demand lighting |
| ElectricalSystem/MaximumNumberOfPoleBreakers | ElectricalSystem | integer | optional | Maximum number of pole breakers |
| ElectricalSystem/NumberOfHotConductors | ElectricalSystem | integer | optional | Number of hot conductors |
| ElectricalSystem/NumberOfNeutralConductors | ElectricalSystem | integer | optional | Number of neutral conductors |
| ElectricalSystem/NumberOfPoles | ElectricalSystem | integer | optional | Number of poles |
| ElectricalSystem/NumberOfRuns | ElectricalSystem | integer | optional | Number of runs |
| ElectricalSystem/OtherConnectedDemand | ElectricalSystem | decimal | optional | Connected demand other |
| ElectricalSystem/OtherEstimatedDemand | ElectricalSystem | decimal | optional | Estimated demand other |
| ElectricalSystem/PowerConnectedDemand | ElectricalSystem | decimal | optional | Connected demand power |
| ElectricalSystem/PowerEstimatedDemand | ElectricalSystem | decimal | optional | Estimated demand power |
| ElectricalSystem/SystemId | ElectricalSystem |  | optional |  |
| ElectricalSystem/TotalPanels | ElectricalSystem | integer | optional | Number of panels |
| ElectricalSystem/TrueCurrent | ElectricalSystem | decimal | optional | True amount of current |
| ElectricalSystem/TrueLoad | ElectricalSystem | decimal | optional | True amount of load |
| ElectricalSystem/WireSize | ElectricalSystem | decimal | optional | Size of wire in square millimeters |
| ElectricalSystem/WireType | ElectricalSystem | string | optional | Type of wire |
| ElectricalVehicleChargingStation/ChargingLevel | ElectricalVehicleChargingStation | integer | optional | Charging level |
| ElectricalVehicleChargingStation/ComponentTypeId | ElectricalVehicleChargingStation |  | optional |  |
| ElectricalVehicleChargingStation/ElectricalVehicleChargingStationId | ElectricalVehicleChargingStation | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| ElectronicSafetyAndSecuritySystem/AlarmType | ElectronicSafetyAndSecuritySystem | string | optional | Type of alarm |
| ElectronicSafetyAndSecuritySystem/BackupBatteryCapacity | ElectronicSafetyAndSecuritySystem | boolean | optional | Backup battery capacity (Y/N) |
| ElectronicSafetyAndSecuritySystem/DisplayType | ElectronicSafetyAndSecuritySystem | string | optional | Type of display |
| ElectronicSafetyAndSecuritySystem/ElectronicSafetyAndSecuritySystemId | ElectronicSafetyAndSecuritySystem | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| ElectronicSafetyAndSecuritySystem/FailSafeCapability | ElectronicSafetyAndSecuritySystem | boolean | optional | Fail safe capability (Y/N) |
| ElectronicSafetyAndSecuritySystem/StatusCode | ElectronicSafetyAndSecuritySystem | string | optional | Status code of alarm |
| ElectronicSafetyAndSecuritySystem/SystemId | ElectronicSafetyAndSecuritySystem |  | optional |  |
| ElectronicSafetyAndSecuritySystem/SystemStatus | ElectronicSafetyAndSecuritySystem | string | optional | System status of electronic safety and security system |
| Elevator/ComponentTypeId | Elevator |  | optional |  |
| Elevator/ElevatorId | Elevator | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| Elevator/EmergencyCommunicationOneWayVideo | Elevator | boolean | optional | Emergency communication two way message display |
| Elevator/EmergencyCommunicationTwoWayMessageDisplay | Elevator | boolean | optional | Emergency communication two way message display |
| Elevator/EmergencyCommunicationTwoWayVoice | Elevator | boolean | optional | Emergency communication two way voice |
| Elevator/FireServiceAccessElevator | Elevator | boolean | optional | Fire service access elevator |
| Elevator/MaxLandings | Elevator | decimal | optional | Max landings |
| Elevator/MaxTravelDistance | Elevator | decimal | optional | Max travel distance |
| Elevator/MaxTravelSpeed | Elevator | decimal | optional | Max travel speed |
| Elevator/PersonCapacity | Elevator | integer | optional | Person capacity |
| Elevator/Type | Elevator | string | optional | Elevator type |
| Elevator/WeightCapacity | Elevator | decimal | optional | Heating capacity in british thermal unit (btu) |
| ElevatorMachine/ComponentTypeId | ElevatorMachine |  | optional |  |
| ElevatorMachine/ElevatorMachineId | ElevatorMachine | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| ElevatorMachine/MotorPower | ElevatorMachine | decimal | optional | Motor power |
| ElevatorMachine/Type | ElevatorMachine | string | optional | Elevator machine type |
| ElevatorMachine/WeightCapacity | ElevatorMachine | decimal | optional | Heating capacity in british thermal unit (btu) |
| Escalator/ComponentTypeId | Escalator |  | optional |  |
| Escalator/EscalatorId | Escalator | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| Escalator/Inclination | Escalator | string | optional | Inclination |
| Escalator/MaxTravelSpeed | Escalator | decimal | optional | Speed of escalator |
| Escalator/MaxVerticalRise | Escalator | decimal | optional | Motor power |
| Escalator/StepWidth | Escalator | decimal | optional | Step width |
| Escalator/Type | Escalator | string | optional | Escalator type |
| EthernetSwitchPort/DataNetworkEquipmentId | EthernetSwitchPort |  | optional |  |
| EthernetSwitchPort/EthernetSwitchPortId | EthernetSwitchPort | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| EthernetSwitchPort/MountedInRack | EthernetSwitchPort | boolean | optional | Mounted in it rack |
| EthernetSwitchPort/PortSpeed | EthernetSwitchPort | decimal | optional | Port speed |
| EthernetSwitchPort/PortType | EthernetSwitchPort | string | optional | Port type |
| EthernetSwitchPort/RackPosition | EthernetSwitchPort | string | optional | It rack position |
| FanCoilUnit/DuctInletCommissionDate | FanCoilUnit | dateTime | optional | Commission date if duct inlet in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanCoilUnit/DuctInletConfiguration | FanCoilUnit | string | optional | Duct inlet configuration |
| FanCoilUnit/DuctInletExpectedEndOfLife | FanCoilUnit | dateTime | optional | Expected end of life date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanCoilUnit/DuctInletExpectedReplacementCost | FanCoilUnit | decimal | optional | Duct inlet expected replacement costs |
| FanCoilUnit/DuctInletInitialCost | FanCoilUnit | decimal | optional | Duct inlet initial cost |
| FanCoilUnit/DuctInletInstallationDate | FanCoilUnit | dateTime | optional | Duct inlet Installation date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanCoilUnit/DuctInletMaintenanceInterval | FanCoilUnit | string | optional | Duct inlet maintenance interval either as string: monthly, quarterly, etc. or as month |
| FanCoilUnit/DuctInletModel | FanCoilUnit | string | optional | Duct inlet model number |
| FanCoilUnit/DuctInletName | FanCoilUnit | string | optional | Name of Duct inlet |
| FanCoilUnit/DuctInletSerialNumber | FanCoilUnit | string | optional | Serial number of component |
| FanCoilUnit/DuctInletShape | FanCoilUnit | decimal | optional | Duct inlet shape |
| FanCoilUnit/DuctInletSize | FanCoilUnit | decimal | optional | Duct inlet size |
| FanCoilUnit/DuctInletTagNumber | FanCoilUnit | string | optional | Tag number |
| FanCoilUnit/DuctInletTurnoverDate | FanCoilUnit | dateTime | optional | Duct inlet turnover date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanCoilUnit/FanCoilUnitId | FanCoilUnit | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| FanCoilUnit/FanCommissionDate | FanCoilUnit | dateTime | optional | Fan commission date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanCoilUnit/FanDriveType | FanCoilUnit | string | optional | Fan fan drive type |
| FanCoilUnit/FanDurationLifeYear | FanCoilUnit | integer | optional | Fan life span of component in years |
| FanCoilUnit/FanExpectedEndOfLife | FanCoilUnit | dateTime | optional | Fan expected end of life date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanCoilUnit/FanExpectedReplacementCost | FanCoilUnit | decimal | optional | Fan expected replacement costs |
| FanCoilUnit/FanInitialCost | FanCoilUnit | decimal | optional | Fan initial cost |
| FanCoilUnit/FanInstallationDate | FanCoilUnit | dateTime | optional | Installation date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanCoilUnit/FanMaintenanceInterval | FanCoilUnit | string | optional | Fan maintenance interval either as string: monthly, quarterly, etc. or as month |
| FanCoilUnit/FanMaxAirflowRating | FanCoilUnit | decimal | optional | Fan max flow capacity |
| FanCoilUnit/FanMinAirflowRating | FanCoilUnit | decimal | optional | Fan min flow capacity |
| FanCoilUnit/FanModelNumber | FanCoilUnit | string | optional | Model number of fan |
| FanCoilUnit/FanMotorPower | FanCoilUnit | decimal | optional | Fan motor power |
| FanCoilUnit/FanName | FanCoilUnit | string | optional | Name of fan |
| FanCoilUnit/FanNominalAirflow | FanCoilUnit | decimal | optional | Fan nominal airflow |
| FanCoilUnit/FanSerialNumber | FanCoilUnit | string | optional | Serial number of fan |
| FanCoilUnit/FanTagNumber | FanCoilUnit | string | optional | Fan tag number |
| FanCoilUnit/FanTurnoverDate | FanCoilUnit | dateTime | optional | Fan turnover date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanCoilUnit/FilterType | FanCoilUnit | string | optional | Filter type |
| FanCoilUnit/MaxAirflowRating | FanCoilUnit | decimal | optional | Max flow capacity |
| FanCoilUnit/MinAirflowRating | FanCoilUnit | decimal | optional | Min flow capacity |
| FanCoilUnit/NetSensibleCoolingCapacity | FanCoilUnit | decimal | optional | Net sensible cooling capacity |
| FanCoilUnit/NominalCoolingCapacity | FanCoilUnit | decimal | optional | Nominal cooling capacity |
| FanCoilUnit/PrimaryCoolingCommissionDate | FanCoilUnit | dateTime | optional | Primary cooling commission date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanCoilUnit/PrimaryCoolingDurationLifeYear | FanCoilUnit | integer | optional | Primary cooling life span of component in years |
| FanCoilUnit/PrimaryCoolingExpectedEndOfLife | FanCoilUnit | dateTime | optional | Primary cooling expected end of life date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanCoilUnit/PrimaryCoolingExpectedReplacementCost | FanCoilUnit | decimal | optional | Primary cooling expected replacement costs |
| FanCoilUnit/PrimaryCoolingInitialCost | FanCoilUnit | decimal | optional | Primary cooling initial cost |
| FanCoilUnit/PrimaryCoolingInstallationDate | FanCoilUnit | dateTime | optional | Installation date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanCoilUnit/PrimaryCoolingMaintenanceInterval | FanCoilUnit | string | optional | Primary cooling maintenance interval either as string: monthly, quarterly, etc. or as month |
| FanCoilUnit/PrimaryCoolingMethodRefrigerantType | FanCoilUnit | string | optional | Primary cooling refrigerant type |
| FanCoilUnit/PrimaryCoolingMethodType | FanCoilUnit | string | optional | Primary cooling method type |
| FanCoilUnit/PrimaryCoolingModelNumber | FanCoilUnit | string | optional | Model number of primary cooling |
| FanCoilUnit/PrimaryCoolingName | FanCoilUnit | string | optional | Primary cooling name of product |
| FanCoilUnit/PrimaryCoolingOutsideDiameter | FanCoilUnit | decimal | optional | Primary cooling outside diameter |
| FanCoilUnit/PrimaryCoolingSerialNumber | FanCoilUnit | string | optional | Serial number of primary cooling |
| FanCoilUnit/PrimaryCoolingTagNumber | FanCoilUnit | string | optional | Primary cooling tag number |
| FanCoilUnit/PrimaryCoolingTurnoverDate | FanCoilUnit | dateTime | optional | Primary cooling turnover date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanCoilUnit/RefrigerantType | FanCoilUnit | string | optional | Refrigerant type |
| FanCoilUnit/SecondaryCoolingCommissionDate | FanCoilUnit | dateTime | optional | Secondary cooling commission date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanCoilUnit/SecondaryCoolingDurationLifeYear | FanCoilUnit | integer | optional | Secondary cooling life span of component in years |
| FanCoilUnit/SecondaryCoolingExpectedEndOfLife | FanCoilUnit | dateTime | optional | Secondary cooling expected end of life date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanCoilUnit/SecondaryCoolingExpectedReplacementCost | FanCoilUnit | decimal | optional | Secondary cooling expected replacement costs |
| FanCoilUnit/SecondaryCoolingInitialCost | FanCoilUnit | decimal | optional | Secondary cooling initial cost |
| FanCoilUnit/SecondaryCoolingInstallationDate | FanCoilUnit | dateTime | optional | Installation date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanCoilUnit/SecondaryCoolingMaintenanceInterval | FanCoilUnit | string | optional | Secondary cooling maintenance interval either as string: monthly, quarterly, etc. or as month |
| FanCoilUnit/SecondaryCoolingMethodRefrigerantType | FanCoilUnit | string | optional | Secondary cooling refrigerant type |
| FanCoilUnit/SecondaryCoolingMethodType | FanCoilUnit | string | optional | Secondary cooling method type |
| FanCoilUnit/SecondaryCoolingModelNumber | FanCoilUnit | string | optional | Model number of secondary cooling |
| FanCoilUnit/SecondaryCoolingName | FanCoilUnit | string | optional | Secondary cooling name of product |
| FanCoilUnit/SecondaryCoolingOutsideDiameter | FanCoilUnit | decimal | optional | Secondary cooling outside diameter |
| FanCoilUnit/SecondaryCoolingSerialNumber | FanCoilUnit | string | optional | Serial number of secondary cooling |
| FanCoilUnit/SecondaryCoolingTagNumber | FanCoilUnit | string | optional | Secondary cooling tag number |
| FanCoilUnit/SecondaryCoolingTurnoverDate | FanCoilUnit | dateTime | optional | Secondary cooling turnover date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanCoilUnit/TerminalUnitId | FanCoilUnit |  | optional |  |
| FanCoilUnit/Type | FanCoilUnit | string | optional | Fan coil unit type |
| FanCoilUnitReheat/Configuration | FanCoilUnitReheat | string | optional | Fan coil unit reheat configuration |
| FanCoilUnitReheat/DuctInletCommissionDate | FanCoilUnitReheat | dateTime | optional | Commission date if duct inlet in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanCoilUnitReheat/DuctInletConfiguration | FanCoilUnitReheat | string | optional | Duct inlet configuration |
| FanCoilUnitReheat/DuctInletExpectedEndOfLife | FanCoilUnitReheat | dateTime | optional | Expected end of life date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanCoilUnitReheat/DuctInletExpectedReplacementCost | FanCoilUnitReheat | decimal | optional | Duct inlet expected replacement costs |
| FanCoilUnitReheat/DuctInletInitialCost | FanCoilUnitReheat | decimal | optional | Duct inlet initial cost |
| FanCoilUnitReheat/DuctInletInstallationDate | FanCoilUnitReheat | dateTime | optional | Duct inlet Installation date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanCoilUnitReheat/DuctInletMaintenanceInterval | FanCoilUnitReheat | string | optional | Duct inlet maintenance interval either as string: monthly, quarterly, etc. or as month |
| FanCoilUnitReheat/DuctInletModel | FanCoilUnitReheat | string | optional | Duct inlet model number |
| FanCoilUnitReheat/DuctInletName | FanCoilUnitReheat | string | optional | Name of Duct inlet |
| FanCoilUnitReheat/DuctInletSerialNumber | FanCoilUnitReheat | string | optional | Serial number of component |
| FanCoilUnitReheat/DuctInletShape | FanCoilUnitReheat | decimal | optional | Duct inlet shape |
| FanCoilUnitReheat/DuctInletSize | FanCoilUnitReheat | decimal | optional | Duct inlet size |
| FanCoilUnitReheat/DuctInletTagNumber | FanCoilUnitReheat | string | optional | Tag number |
| FanCoilUnitReheat/DuctInletTurnoverDate | FanCoilUnitReheat | dateTime | optional | Duct inlet turnover date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanCoilUnitReheat/FanCoilUnitId | FanCoilUnitReheat |  | optional |  |
| FanCoilUnitReheat/FanCoilUnitReheatId | FanCoilUnitReheat | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| FanCoilUnitReheat/FanCommissionDate | FanCoilUnitReheat | dateTime | optional | Fan commission date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanCoilUnitReheat/FanDriveType | FanCoilUnitReheat | string | optional | Fan fan drive type |
| FanCoilUnitReheat/FanDurationLifeYear | FanCoilUnitReheat | integer | optional | Fan life span of component in years |
| FanCoilUnitReheat/FanExpectedEndOfLife | FanCoilUnitReheat | dateTime | optional | Fan expected end of life date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanCoilUnitReheat/FanExpectedReplacementCost | FanCoilUnitReheat | decimal | optional | Fan expected replacement costs |
| FanCoilUnitReheat/FanInitialCost | FanCoilUnitReheat | decimal | optional | Fan initial cost |
| FanCoilUnitReheat/FanInstallationDate | FanCoilUnitReheat | dateTime | optional | Installation date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanCoilUnitReheat/FanMaintenanceInterval | FanCoilUnitReheat | string | optional | Fan maintenance interval either as string: monthly, quarterly, etc. or as month |
| FanCoilUnitReheat/FanMaxAirflowRating | FanCoilUnitReheat | decimal | optional | Fan max rate |
| FanCoilUnitReheat/FanMinAirflowRating | FanCoilUnitReheat | decimal | optional | Fan min flow capacity |
| FanCoilUnitReheat/FanModelNumber | FanCoilUnitReheat | string | optional | Model number of fan |
| FanCoilUnitReheat/FanMotorPower | FanCoilUnitReheat | decimal | optional | Fan motor power |
| FanCoilUnitReheat/FanName | FanCoilUnitReheat | string | optional | Name of fan |
| FanCoilUnitReheat/FanNominalAirflow | FanCoilUnitReheat | decimal | optional | Fan nominal airflow |
| FanCoilUnitReheat/FanSerialNumber | FanCoilUnitReheat | string | optional | Serial number of fan |
| FanCoilUnitReheat/FanTagNumber | FanCoilUnitReheat | string | optional | Fan tag number |
| FanCoilUnitReheat/FanTurnoverDate | FanCoilUnitReheat | dateTime | optional | Fan turnover date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanCoilUnitReheat/FilterType | FanCoilUnitReheat | string | optional | Filter type |
| FanCoilUnitReheat/MaxAirflowRating | FanCoilUnitReheat | decimal | optional | Max flow capacity |
| FanCoilUnitReheat/MinAirflowRating | FanCoilUnitReheat | decimal | optional | Min flow capacity |
| FanCoilUnitReheat/NetSensibleCoolingCapacity | FanCoilUnitReheat | decimal | optional | Net sensible cooling capacity |
| FanCoilUnitReheat/NominalCoolingCapacity | FanCoilUnitReheat | decimal | optional | Nominal cooling capacity |
| FanCoilUnitReheat/NominalHeatingCapacity | FanCoilUnitReheat | decimal | optional | Nominal heating capacity |
| FanCoilUnitReheat/PrimaryCoolingCommissionDate | FanCoilUnitReheat | dateTime | optional | Primary cooling commission date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanCoilUnitReheat/PrimaryCoolingDurationLifeYear | FanCoilUnitReheat | integer | optional | Primary cooling life span of component in years |
| FanCoilUnitReheat/PrimaryCoolingExpectedEndOfLife | FanCoilUnitReheat | dateTime | optional | Primary cooling expected end of life date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanCoilUnitReheat/PrimaryCoolingExpectedReplacementCost | FanCoilUnitReheat | decimal | optional | Primary cooling expected replacement costs |
| FanCoilUnitReheat/PrimaryCoolingInitialCost | FanCoilUnitReheat | decimal | optional | Primary cooling initial cost |
| FanCoilUnitReheat/PrimaryCoolingInstallationDate | FanCoilUnitReheat | dateTime | optional | Installation date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanCoilUnitReheat/PrimaryCoolingMaintenanceInterval | FanCoilUnitReheat | string | optional | Primary cooling maintenance interval either as string: monthly, quarterly, etc. or as month |
| FanCoilUnitReheat/PrimaryCoolingMethodType | FanCoilUnitReheat | string | optional | Primary cooling method type |
| FanCoilUnitReheat/PrimaryCoolingMethodeRefrigerantType | FanCoilUnitReheat | string | optional | Primary cooling refrigerant type |
| FanCoilUnitReheat/PrimaryCoolingModelNumber | FanCoilUnitReheat | string | optional | Model number of primary cooling |
| FanCoilUnitReheat/PrimaryCoolingName | FanCoilUnitReheat | string | optional | Primary cooling name of product |
| FanCoilUnitReheat/PrimaryCoolingOutsideDiameter | FanCoilUnitReheat | decimal | optional | Primary cooling outside diameter |
| FanCoilUnitReheat/PrimaryCoolingSerialNumber | FanCoilUnitReheat | string | optional | Serial number of primary cooling |
| FanCoilUnitReheat/PrimaryCoolingTagNumber | FanCoilUnitReheat | string | optional | Primary cooling tag number |
| FanCoilUnitReheat/PrimaryCoolingTurnoverDate | FanCoilUnitReheat | dateTime | optional | Primary cooling turnover date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanCoilUnitReheat/ReHeatingCommissionDate | FanCoilUnitReheat | dateTime | optional | Re heating commission date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanCoilUnitReheat/ReHeatingDurationLifeYear | FanCoilUnitReheat | integer | optional | Re heating life span of component in years |
| FanCoilUnitReheat/ReHeatingExpectedEndOfLife | FanCoilUnitReheat | dateTime | optional | Re heating expected end of life date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanCoilUnitReheat/ReHeatingExpectedReplacementCost | FanCoilUnitReheat | decimal | optional | Re heating expected replacement costs |
| FanCoilUnitReheat/ReHeatingInitialCost | FanCoilUnitReheat | decimal | optional | Re heating initial cost |
| FanCoilUnitReheat/ReHeatingInstallationDate | FanCoilUnitReheat | dateTime | optional | Installation date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanCoilUnitReheat/ReHeatingMaintenanceInterval | FanCoilUnitReheat | string | optional | Re heating maintenance interval either as string: monthly, quarterly, etc. or as month |
| FanCoilUnitReheat/ReHeatingModelNumber | FanCoilUnitReheat | string | optional | Model number of re heating |
| FanCoilUnitReheat/ReHeatingName | FanCoilUnitReheat | string | optional | Re heating name of product |
| FanCoilUnitReheat/ReHeatingOutsideDiameter | FanCoilUnitReheat | decimal | optional | Re heating outside diameter |
| FanCoilUnitReheat/ReHeatingSerialNumber | FanCoilUnitReheat | string | optional | Serial number of re heating |
| FanCoilUnitReheat/ReHeatingTagNumber | FanCoilUnitReheat | string | optional | Re heating tag number |
| FanCoilUnitReheat/ReHeatingTurnoverDate | FanCoilUnitReheat | dateTime | optional | Re heating turnover date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanCoilUnitReheat/ReHeatingType | FanCoilUnitReheat | string | optional | Re heating type |
| FanCoilUnitReheat/RefrigerantType | FanCoilUnitReheat | string | optional | Refrigerant type |
| FanCoilUnitReheat/SecondaryCoolingCommissionDate | FanCoilUnitReheat | dateTime | optional | Secondary cooling commission date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanCoilUnitReheat/SecondaryCoolingDurationLifeYear | FanCoilUnitReheat | integer | optional | Secondary cooling life span of component in years |
| FanCoilUnitReheat/SecondaryCoolingExpectedEndOfLife | FanCoilUnitReheat | dateTime | optional | Secondary cooling expected end of life date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanCoilUnitReheat/SecondaryCoolingExpectedReplacementCost | FanCoilUnitReheat | decimal | optional | Secondary cooling expected replacement costs |
| FanCoilUnitReheat/SecondaryCoolingInitialCost | FanCoilUnitReheat | decimal | optional | Secondary cooling initial cost |
| FanCoilUnitReheat/SecondaryCoolingInstallationDate | FanCoilUnitReheat | dateTime | optional | Installation date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanCoilUnitReheat/SecondaryCoolingMaintenanceInterval | FanCoilUnitReheat | string | optional | Secondary cooling maintenance interval either as string: monthly, quarterly, etc. or as month |
| FanCoilUnitReheat/SecondaryCoolingMethodRefrigerantType | FanCoilUnitReheat | string | optional | Secondary cooling refrigerant type |
| FanCoilUnitReheat/SecondaryCoolingMethodType | FanCoilUnitReheat | string | optional | Secondary cooling method type |
| FanCoilUnitReheat/SecondaryCoolingModelNumber | FanCoilUnitReheat | string | optional | Model number of secondary cooling |
| FanCoilUnitReheat/SecondaryCoolingName | FanCoilUnitReheat | string | optional | Secondary cooling name of product |
| FanCoilUnitReheat/SecondaryCoolingOutsideDiameter | FanCoilUnitReheat | decimal | optional | Secondary cooling outside diameter |
| FanCoilUnitReheat/SecondaryCoolingSerialNumber | FanCoilUnitReheat | string | optional | Serial number of secondary cooling |
| FanCoilUnitReheat/SecondaryCoolingTagNumber | FanCoilUnitReheat | string | optional | Secondary cooling tag number |
| FanCoilUnitReheat/SecondaryCoolingTurnoverDate | FanCoilUnitReheat | dateTime | optional | Secondary cooling turnover date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanCoilUnitReheat/Type | FanCoilUnitReheat | string | optional | Fan coil unit reheat type |
| FanPoweredBox/Configuration | FanPoweredBox | string | optional | Fan powered box configuration |
| FanPoweredBox/DuctInletCommissionDate | FanPoweredBox | dateTime | optional | Commission date if duct inlet in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanPoweredBox/DuctInletConfiguration | FanPoweredBox | string | optional | Duct inlet configuration |
| FanPoweredBox/DuctInletExpectedEndOfLife | FanPoweredBox | dateTime | optional | Expected end of life date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanPoweredBox/DuctInletExpectedReplacementCost | FanPoweredBox | decimal | optional | Duct inlet expected replacement costs |
| FanPoweredBox/DuctInletInitialCost | FanPoweredBox | decimal | optional | Duct inlet initial cost |
| FanPoweredBox/DuctInletInstallationDate | FanPoweredBox | dateTime | optional | Duct inlet Installation date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanPoweredBox/DuctInletMaintenanceInterval | FanPoweredBox | string | optional | Duct inlet maintenance interval either as string: monthly, quarterly, etc. or as month |
| FanPoweredBox/DuctInletModel | FanPoweredBox | string | optional | Duct inlet model number |
| FanPoweredBox/DuctInletName | FanPoweredBox | string | optional | Name of Duct inlet |
| FanPoweredBox/DuctInletSerialNumber | FanPoweredBox | string | optional | Serial number of component |
| FanPoweredBox/DuctInletShape | FanPoweredBox | decimal | optional | Duct inlet shape |
| FanPoweredBox/DuctInletSize | FanPoweredBox | decimal | optional | Duct inlet size |
| FanPoweredBox/DuctInletTagNumber | FanPoweredBox | string | optional | Tag number |
| FanPoweredBox/DuctInletTurnoverDate | FanPoweredBox | dateTime | optional | Duct inlet turnover date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanPoweredBox/FanCommissionDate | FanPoweredBox | dateTime | optional | Fan commission date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanPoweredBox/FanDriveType | FanPoweredBox | string | optional | Fan fan drive type |
| FanPoweredBox/FanDurationLifeYear | FanPoweredBox | integer | optional | Fan life span of component in years |
| FanPoweredBox/FanExpectedEndOfLife | FanPoweredBox | dateTime | optional | Fan expected end of life date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanPoweredBox/FanExpectedReplacementCost | FanPoweredBox | decimal | optional | Fan expected replacement costs |
| FanPoweredBox/FanInitialCost | FanPoweredBox | decimal | optional | Fan initial cost |
| FanPoweredBox/FanInstallationDate | FanPoweredBox | dateTime | optional | Installation date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanPoweredBox/FanMaintenanceInterval | FanPoweredBox | string | optional | Fan maintenance interval either as string: monthly, quarterly, etc. or as month |
| FanPoweredBox/FanMaxAirflowRating | FanPoweredBox | decimal | optional | Fan max flow capacity |
| FanPoweredBox/FanMinAirflowRating | FanPoweredBox | decimal | optional | Fan min flow capacity |
| FanPoweredBox/FanModelNumber | FanPoweredBox | string | optional | Model number of fan |
| FanPoweredBox/FanMotorPower | FanPoweredBox | decimal | optional | Fan motor power |
| FanPoweredBox/FanName | FanPoweredBox | string | optional | Name of fan |
| FanPoweredBox/FanNominalAirflow | FanPoweredBox | decimal | optional | Fan nominal airflow |
| FanPoweredBox/FanPoweredBoxId | FanPoweredBox | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| FanPoweredBox/FanSerialNumber | FanPoweredBox | string | optional | Serial number of fan |
| FanPoweredBox/FanTagNumber | FanPoweredBox | string | optional | Fan tag number |
| FanPoweredBox/FanTurnoverDate | FanPoweredBox | dateTime | optional | Fan turnover date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanPoweredBox/MaxAirflowRating | FanPoweredBox | decimal | optional | Max flow capacity |
| FanPoweredBox/MinAirflowRating | FanPoweredBox | decimal | optional | Min flow capacity |
| FanPoweredBox/TerminalUnitId | FanPoweredBox |  | optional |  |
| FanPoweredBoxReheat/Configuration | FanPoweredBoxReheat | string | optional | Fan powered box configuration |
| FanPoweredBoxReheat/DuctInletCommissionDate | FanPoweredBoxReheat | dateTime | optional | Commission date if duct inlet in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanPoweredBoxReheat/DuctInletConfiguration | FanPoweredBoxReheat | string | optional | Duct inlet configuration |
| FanPoweredBoxReheat/DuctInletExpectedEndOfLife | FanPoweredBoxReheat | dateTime | optional | Expected end of life date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanPoweredBoxReheat/DuctInletExpectedReplacementCost | FanPoweredBoxReheat | decimal | optional | Duct inlet expected replacement costs |
| FanPoweredBoxReheat/DuctInletInitialCost | FanPoweredBoxReheat | decimal | optional | Duct inlet initial cost |
| FanPoweredBoxReheat/DuctInletInstallationDate | FanPoweredBoxReheat | dateTime | optional | Duct inlet Installation date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanPoweredBoxReheat/DuctInletMaintenanceInterval | FanPoweredBoxReheat | string | optional | Duct inlet maintenance interval either as string: monthly, quarterly, etc. or as month |
| FanPoweredBoxReheat/DuctInletModel | FanPoweredBoxReheat | string | optional | Duct inlet model number |
| FanPoweredBoxReheat/DuctInletName | FanPoweredBoxReheat | string | optional | Name of Duct inlet |
| FanPoweredBoxReheat/DuctInletSerialNumber | FanPoweredBoxReheat | string | optional | Serial number of component |
| FanPoweredBoxReheat/DuctInletShape | FanPoweredBoxReheat | decimal | optional | Duct inlet shape |
| FanPoweredBoxReheat/DuctInletSize | FanPoweredBoxReheat | decimal | optional | Duct inlet size |
| FanPoweredBoxReheat/DuctInletTagNumber | FanPoweredBoxReheat | string | optional | Tag number |
| FanPoweredBoxReheat/DuctInletTurnoverDate | FanPoweredBoxReheat | dateTime | optional | Duct inlet turnover date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanPoweredBoxReheat/FanCommissionDate | FanPoweredBoxReheat | dateTime | optional | Fan commission date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanPoweredBoxReheat/FanDriveType | FanPoweredBoxReheat | string | optional | Fan fan drive type |
| FanPoweredBoxReheat/FanDurationLifeYear | FanPoweredBoxReheat | integer | optional | Fan life span of component in years |
| FanPoweredBoxReheat/FanExpectedEndOfLife | FanPoweredBoxReheat | dateTime | optional | Fan expected end of life date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanPoweredBoxReheat/FanExpectedReplacementCost | FanPoweredBoxReheat | decimal | optional | Fan expected replacement costs |
| FanPoweredBoxReheat/FanInitialCost | FanPoweredBoxReheat | decimal | optional | Fan initial cost |
| FanPoweredBoxReheat/FanInstallationDate | FanPoweredBoxReheat | dateTime | optional | Installation date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanPoweredBoxReheat/FanMaintenanceInterval | FanPoweredBoxReheat | string | optional | Fan maintenance interval either as string: monthly, quarterly, etc. or as month |
| FanPoweredBoxReheat/FanMaxAirflowRating | FanPoweredBoxReheat | decimal | optional | Fan max flow capacity |
| FanPoweredBoxReheat/FanMinAirflowRating | FanPoweredBoxReheat | decimal | optional | Fan min flow capacity |
| FanPoweredBoxReheat/FanModelNumber | FanPoweredBoxReheat | string | optional | Model number of fan |
| FanPoweredBoxReheat/FanMotorPower | FanPoweredBoxReheat | decimal | optional | Fan motor power |
| FanPoweredBoxReheat/FanName | FanPoweredBoxReheat | string | optional | Name of fan |
| FanPoweredBoxReheat/FanNominalAirflow | FanPoweredBoxReheat | decimal | optional | Fan nominal airflow |
| FanPoweredBoxReheat/FanPoweredBoxReheatId | FanPoweredBoxReheat | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| FanPoweredBoxReheat/FanSerialNumber | FanPoweredBoxReheat | string | optional | Serial number of fan |
| FanPoweredBoxReheat/FanTagNumber | FanPoweredBoxReheat | string | optional | Fan tag number |
| FanPoweredBoxReheat/FanTurnoverDate | FanPoweredBoxReheat | dateTime | optional | Fan turnover date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanPoweredBoxReheat/MaxAirflowRating | FanPoweredBoxReheat | decimal | optional | Max flow capacity |
| FanPoweredBoxReheat/MinAirflowRating | FanPoweredBoxReheat | decimal | optional | Min flow capacity |
| FanPoweredBoxReheat/NominalHeatingCapacity | FanPoweredBoxReheat | decimal | optional | Nominal heating capacity |
| FanPoweredBoxReheat/ReHeatingCommissionDate | FanPoweredBoxReheat | dateTime | optional | Re heating commission date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanPoweredBoxReheat/ReHeatingDurationLifeYear | FanPoweredBoxReheat | integer | optional | Re heating life span of component in years |
| FanPoweredBoxReheat/ReHeatingExpectedEndOfLife | FanPoweredBoxReheat | dateTime | optional | Re heating expected end of life date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanPoweredBoxReheat/ReHeatingExpectedReplacementCost | FanPoweredBoxReheat | decimal | optional | Re heating expected replacement costs |
| FanPoweredBoxReheat/ReHeatingInitialCost | FanPoweredBoxReheat | decimal | optional | Re heating initial cost |
| FanPoweredBoxReheat/ReHeatingInstallationDate | FanPoweredBoxReheat | dateTime | optional | Installation date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanPoweredBoxReheat/ReHeatingMaintenanceInterval | FanPoweredBoxReheat | string | optional | Re heating maintenance interval either as string: monthly, quarterly, etc. or as month |
| FanPoweredBoxReheat/ReHeatingModelNumber | FanPoweredBoxReheat | string | optional | Model number of re heating |
| FanPoweredBoxReheat/ReHeatingName | FanPoweredBoxReheat | string | optional | Re heating name of product |
| FanPoweredBoxReheat/ReHeatingOutsideDiameter | FanPoweredBoxReheat | decimal | optional | Re heating outside diameter |
| FanPoweredBoxReheat/ReHeatingSerialNumber | FanPoweredBoxReheat | string | optional | Serial number of re heating |
| FanPoweredBoxReheat/ReHeatingTagNumber | FanPoweredBoxReheat | string | optional | Re heating tag number |
| FanPoweredBoxReheat/ReHeatingTurnoverDate | FanPoweredBoxReheat | dateTime | optional | Re heating turnover date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FanPoweredBoxReheat/ReHeatingType | FanPoweredBoxReheat | string | optional | Re heating type |
| FanPoweredBoxReheat/TerminalUnitId | FanPoweredBoxReheat |  | optional |  |
| Faucet/ComponentTypeId | Faucet |  | optional |  |
| Faucet/FaucetId | Faucet | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| Faucet/MaxFlowRate | Faucet | decimal | optional | Max flow capacity |
| Faucet/MountedOn | Faucet | boolean | optional | Mounted on |
| Faucet/NumberOfHandles | Faucet | integer | optional | Number of handles |
| Faucet/Type | Faucet | string | optional | Faucet type |
| FireDamper/BladeType | FireDamper | string | optional | Blade type of damper (usually two different types of blade dampers used to modulate air flow: parallel and opposed blade dampers) |
| FireDamper/DamperId | FireDamper |  | optional |  |
| FireDamper/DuctInletCommissionDate | FireDamper | dateTime | optional | Commission date if duct inlet in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FireDamper/DuctInletConfiguration | FireDamper | string | optional | Duct inlet configuration |
| FireDamper/DuctInletExpectedEndOfLife | FireDamper | dateTime | optional | Expected end of life date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FireDamper/DuctInletExpectedReplacementCost | FireDamper | decimal | optional | Duct inlet expected replacement costs |
| FireDamper/DuctInletInitialCost | FireDamper | decimal | optional | Duct inlet initial cost |
| FireDamper/DuctInletInstallationDate | FireDamper | dateTime | optional | Duct inlet Installation date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FireDamper/DuctInletMaintenanceInterval | FireDamper | string | optional | Duct inlet maintenance interval either as string: monthly, quarterly, etc. or as month |
| FireDamper/DuctInletModel | FireDamper | string | optional | Duct inlet model number |
| FireDamper/DuctInletName | FireDamper | string | optional | Name of Duct inlet |
| FireDamper/DuctInletSerialNumber | FireDamper | string | optional | Serial number of component |
| FireDamper/DuctInletShape | FireDamper | decimal | optional | Duct inlet shape |
| FireDamper/DuctInletSize | FireDamper | decimal | optional | Duct inlet size |
| FireDamper/DuctInletTagNumber | FireDamper | string | optional | Tag number |
| FireDamper/DuctInletTurnoverDate | FireDamper | dateTime | optional | Duct inlet turnover date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| FireDamper/FireDamperId | FireDamper | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| FireDamper/FireRating | FireDamper | string | optional | Fire rating of fire damper |
| FireDamper/LeakageClass | FireDamper | string | optional | Class component belongs to |
| FirePump/ComponentTypeId | FirePump |  | optional |  |
| FirePump/FirePumpId | FirePump | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| FirePump/FlowCapacity | FirePump | decimal | optional | Flow capacity |
| FirePump/HeadCapacity | FirePump | decimal | optional | Head capacity |
| FirePump/PressureCapacity | FirePump | decimal | optional | Pressure capacity |
| FirePump/PumpingMedia | FirePump | string | optional | Pumping media |
| FireSprinklerHead/ComponentTypeId | FireSprinklerHead |  | optional |  |
| FireSprinklerHead/FireSprinklerHeadId | FireSprinklerHead | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| FireSprinklerHead/KFactorImperial | FireSprinklerHead | decimal | optional | K factor imperial |
| FireSprinklerHead/KFactorMetric | FireSprinklerHead | decimal | optional | K factor metric |
| FireSprinklerHead/Type | FireSprinklerHead | string | optional | Fire sprinkler head type |
| Floor/BuildingId | Floor |  | optional |  |
| Floor/FloorCode | Floor | string | optional | User specific Floor Code |
| Floor/FloorId | Floor | string | optional | Customer ID from previous system  (ID before onboarding data to BM) |
| Floor/FloorNumber | Floor | integer | optional | Number of floor |
| FlushometerValve/ComponentTypeId | FlushometerValve |  | optional |  |
| FlushometerValve/FlushometerValveId | FlushometerValve | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| FlushometerValve/MountedOn | FlushometerValve | boolean | optional | Mounted on |
| FlushometerValve/Technology | FlushometerValve | string | optional | Technology |
| FlushometerValve/Type | FlushometerValve | string | optional | Faucet type |
| FlushometerValve/WaterPerFlush | FlushometerValve | decimal | optional | Water per flush |
| GasMeter/ComponentTypeId | GasMeter |  | optional |  |
| GasMeter/GasMeterId | GasMeter | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| GasMeter/Mass | GasMeter | decimal | optional | Volume flow |
| GasMeter/MassFlow | GasMeter | decimal | optional | Mass flow |
| GasMeter/Measures | GasMeter | string | optional | Substance that is measured |
| GasMeter/Type | GasMeter | string | optional | Water meter type |
| Gateway/ComponentTypeId | Gateway |  | optional |  |
| Gateway/ConnectorId | Gateway | string | optional | Registration id |
| Gateway/Detected | Gateway | boolean | optional | Detected (Y/N) |
| Gateway/Enabled | Gateway | boolean | optional | Enabled (Y/N) |
| Gateway/GatewayId | Gateway | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| Gateway/MountedInRack | Gateway | boolean | optional | Mounted in it rack |
| Gateway/RackPosition | Gateway | string | optional | It rack position |
| Gateway/RegistrationId | Gateway | string | optional | Registration id |
| Gateway/RegistrationKey | Gateway | string | optional | Registration key |
| Generator/BulkStorageCapacity | Generator | decimal | optional | Bulk storage capacity |
| Generator/ComponentTypeId | Generator |  | optional |  |
| Generator/DayTankCapacity | Generator | decimal | optional | Day tank capacity |
| Generator/Frequency | Generator | string | optional | Frequency |
| Generator/FuelType | Generator | string | optional | Fuel type |
| Generator/GeneratorId | Generator | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| Generator/ModeOfOperation | Generator | string | optional | Mode of operation |
| Generator/OutputPhases | Generator | string | optional | Output phases |
| Generator/OutputVoltage | Generator | decimal | optional | Output voltage |
| Generator/PrimePower | Generator | decimal | optional | Standby power |
| Generator/PrimePowerKva | Generator | decimal | optional | Prime power kva |
| Generator/StandbyPower | Generator | decimal | optional | Standby power |
| Generator/StandbyPowerKva | Generator | decimal | optional | Standby power kva |
| Generator/Type | Generator | string | optional | Generator type |
| HvacFan/ComponentTypeId | HvacFan |  | optional |  |
| HvacFan/DriveType | HvacFan | string | optional | Hvac fan drive type |
| HvacFan/HvacFanId | HvacFan | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| HvacFan/MaxAirflowRating | HvacFan | decimal | optional | Max flow capacity |
| HvacFan/MinAirflowRating | HvacFan | decimal | optional | Min flow capacity |
| HvacFan/MotorPower | HvacFan | decimal | optional | Motor power |
| HvacFan/NominalAirflow | HvacFan | decimal | optional | Nominal airflow |
| HvacFan/Type | HvacFan | string | optional | Define the specific hvac fan type |
| HvacFanSubComponent/DriveType | HvacFanSubComponent | string | optional | Other hvac fan drive type |
| HvacFanSubComponent/DuctInletCommissionDate | HvacFanSubComponent | dateTime | optional | Commission date if duct inlet in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| HvacFanSubComponent/DuctInletConfiguration | HvacFanSubComponent | string | optional | Duct inlet configuration |
| HvacFanSubComponent/DuctInletExpectedEndOfLife | HvacFanSubComponent | dateTime | optional | Expected end of life date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| HvacFanSubComponent/DuctInletExpectedReplacementCost | HvacFanSubComponent | decimal | optional | Duct inlet expected replacement costs |
| HvacFanSubComponent/DuctInletInitialCost | HvacFanSubComponent | decimal | optional | Duct inlet initial cost |
| HvacFanSubComponent/DuctInletInstallationDate | HvacFanSubComponent | dateTime | optional | Duct inlet Installation date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| HvacFanSubComponent/DuctInletMaintenanceInterval | HvacFanSubComponent | string | optional | Duct inlet maintenance interval either as string: monthly, quarterly, etc. or as month |
| HvacFanSubComponent/DuctInletModel | HvacFanSubComponent | string | optional | Duct inlet model number |
| HvacFanSubComponent/DuctInletName | HvacFanSubComponent | string | optional | Name of Duct inlet |
| HvacFanSubComponent/DuctInletSerialNumber | HvacFanSubComponent | string | optional | Serial number of component |
| HvacFanSubComponent/DuctInletShape | HvacFanSubComponent | decimal | optional | Duct inlet shape |
| HvacFanSubComponent/DuctInletSize | HvacFanSubComponent | decimal | optional | Duct inlet size |
| HvacFanSubComponent/DuctInletTagNumber | HvacFanSubComponent | string | optional | Tag number |
| HvacFanSubComponent/DuctInletTurnoverDate | HvacFanSubComponent | dateTime | optional | Duct inlet turnover date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| HvacFanSubComponent/FanCommissionDate | HvacFanSubComponent | dateTime | optional | Fan commission date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| HvacFanSubComponent/FanDriveType | HvacFanSubComponent | string | optional | Fan fan drive type |
| HvacFanSubComponent/FanDurationLifeYear | HvacFanSubComponent | integer | optional | Fan life span of component in years |
| HvacFanSubComponent/FanExpectedEndOfLife | HvacFanSubComponent | dateTime | optional | Fan expected end of life date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| HvacFanSubComponent/FanExpectedReplacementCost | HvacFanSubComponent | decimal | optional | Fan expected replacement costs |
| HvacFanSubComponent/FanInitialCost | HvacFanSubComponent | decimal | optional | Fan initial cost |
| HvacFanSubComponent/FanInstallationDate | HvacFanSubComponent | dateTime | optional | Installation date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| HvacFanSubComponent/FanMaintenanceInterval | HvacFanSubComponent | string | optional | Fan maintenance interval either as string: monthly, quarterly, etc. or as month |
| HvacFanSubComponent/FanMaxAirflowRating | HvacFanSubComponent | decimal | optional | Fan max flow capacity |
| HvacFanSubComponent/FanMinAirflowRating | HvacFanSubComponent | decimal | optional | Fan min flow capacity |
| HvacFanSubComponent/FanModelNumber | HvacFanSubComponent | string | optional | Model number of fan |
| HvacFanSubComponent/FanMotorPower | HvacFanSubComponent | decimal | optional | Fan motor power |
| HvacFanSubComponent/FanName | HvacFanSubComponent | string | optional | Name of fan |
| HvacFanSubComponent/FanNominalAirflow | HvacFanSubComponent | decimal | optional | Fan nominal airflow |
| HvacFanSubComponent/FanSerialNumber | HvacFanSubComponent | string | optional | Serial number of fan |
| HvacFanSubComponent/FanTagNumber | HvacFanSubComponent | string | optional | Fan tag number |
| HvacFanSubComponent/FanTurnoverDate | HvacFanSubComponent | dateTime | optional | Fan turnover date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| HvacFanSubComponent/HvacFanId | HvacFanSubComponent |  | optional |  |
| HvacFanSubComponent/HvacFanSubComponentId | HvacFanSubComponent | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| HvacFanSubComponent/MaxAirflowRating | HvacFanSubComponent | decimal | optional | Max flow capacity |
| HvacFanSubComponent/MaxRotationSpeed | HvacFanSubComponent | decimal | optional | Max rotation speed in rotations per minute |
| HvacFanSubComponent/MinAirflowRating | HvacFanSubComponent | decimal | optional | Min flow capacity |
| HvacFanSubComponent/MotorPower | HvacFanSubComponent | decimal | optional | Motor power |
| HvacFanSubComponent/NominalAirflow | HvacFanSubComponent | decimal | optional | Nominal airflow |
| HvacFanSubComponent/Type | HvacFanSubComponent | string | optional | Ceiling fan type |
| HvacHeatTracing/ComponentTypeId | HvacHeatTracing |  | optional |  |
| HvacHeatTracing/HvacHeatTracingId | HvacHeatTracing | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| HvacHeatTracing/PowerDensity | HvacHeatTracing | decimal | optional | Amount of power density |
| HvacHeatTracing/Type | HvacHeatTracing | string | optional | Hvac pump type |
| HvacPump/ComponentTypeId | HvacPump |  | optional |  |
| HvacPump/FlowCapacity | HvacPump | decimal | optional | Flow capacity |
| HvacPump/HeadCapacity | HvacPump | decimal | optional | Head capacity |
| HvacPump/HvacPumpId | HvacPump | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| HvacPump/PressureCapacity | HvacPump | decimal | optional | Pressure capacity of hvac pump |
| HvacPump/PumpingMedia | HvacPump | string | optional | Pumping media |
| HvacPump/Type | HvacPump | string | optional | Hvac pump type |
| HvacShutOffValve/FlowCapacity | HvacShutOffValve | decimal | optional | Flow capacity |
| HvacShutOffValve/HvacShutOffValveId | HvacShutOffValve | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| HvacShutOffValve/HvacValveId | HvacShutOffValve |  | optional |  |
| HvacShutOffValve/PipeDiameter | HvacShutOffValve | decimal | optional | Pipe diameter of hvac sub component |
| HvacShutOffValve/PressureCapacity | HvacShutOffValve | decimal | optional | Pressure capacity of hvac sub component |
| HvacSystem/ActualExhaustAirflow | HvacSystem | decimal | optional | Actual exhaust airflow |
| HvacSystem/ActualLoad | HvacSystem | decimal | optional | Actual hvac load |
| HvacSystem/ActualSupplyAirflow | HvacSystem | decimal | optional | Actual supply airflow |
| HvacSystem/AirflowUnit | HvacSystem | string | optional | Unit of airflow |
| HvacSystem/CalculatedCoolingLoad | HvacSystem | decimal | optional | Calculated cooling load per area |
| HvacSystem/CalculatedHeatingLoad | HvacSystem | decimal | optional | Calculated heating load per area |
| HvacSystem/CalculatedSupplyAirflow | HvacSystem | decimal | optional | Specified supply airflow |
| HvacSystem/CoolingCapacity | HvacSystem | decimal | optional | Cooling capacity in tonnes |
| HvacSystem/CoolingSensibleHeatRatio | HvacSystem | decimal | optional | Cooling sensible heat ratio |
| HvacSystem/DesignCoolingLoad | HvacSystem | decimal | optional | Design cooling load per area |
| HvacSystem/DesignHeatingLoad | HvacSystem | decimal | optional | Design heating load per area |
| HvacSystem/DesignLoadPerArea | HvacSystem | decimal | optional | Design load per area |
| HvacSystem/HeatingCapacity | HvacSystem | decimal | optional | Heating capacity |
| HvacSystem/HvacSystemId | HvacSystem | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| HvacSystem/LoadUnit | HvacSystem | string | optional | Unit of load |
| HvacSystem/ManufacturerCoilBypassFactor | HvacSystem | decimal | optional | Manufacturer coil bypass factor |
| HvacSystem/MaximumCoolingCapacity | HvacSystem | decimal | optional | Maximum cooling capacity |
| HvacSystem/SpecifiedExhaustAirflow | HvacSystem | decimal | optional | Specified exhaust airflow |
| HvacSystem/SpecifiedSupplyAirflow | HvacSystem | decimal | optional | Specified supply airflow |
| HvacSystem/SystemId | HvacSystem |  | optional |  |
| HvacTank/ComponentTypeId | HvacTank |  | optional |  |
| HvacTank/FlowCapacity | HvacTank | decimal | optional | Flow capacity |
| HvacTank/HeadCapacity | HvacTank | decimal | optional | Head capacity |
| HvacTank/HvacTankId | HvacTank | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| HvacTank/PressureCapacity | HvacTank | decimal | optional | Pressure capacity of hvac pump |
| HvacTank/PumpingMedia | HvacTank | string | optional | Pumping media |
| HvacTank/Type | HvacTank | string | optional | Hvac tank type |
| HvacValve/ComponentTypeId | HvacValve |  | optional |  |
| HvacValve/FlowCapacity | HvacValve | decimal | optional | Flow capacity |
| HvacValve/HvacValveId | HvacValve | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| HvacValve/PipeDiameter | HvacValve | decimal | optional | Pipe diameter of hvac valve |
| HvacValve/PressureCapacity | HvacValve | decimal | optional | Pressure capacity of hvac valve |
| HvacValve/Type | HvacValve | string | optional | Hvac valve type |
| IctHardware/ComponentTypeId | IctHardware |  | optional |  |
| IctHardware/IctHardwareId | IctHardware | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| IctHardware/MountedInRack | IctHardware | boolean | optional | Mounted in it rack |
| IctHardware/RackPosition | IctHardware | string | optional | It rack position |
| IctHardware/Type | IctHardware | string | optional | Ict hardware type |
| InformationAndCommunicationSystem/CableCategory | InformationAndCommunicationSystem | string | optional | Category of cable |
| InformationAndCommunicationSystem/CableRating | InformationAndCommunicationSystem | string | optional | Determine the parameters within which a cable can be safely used |
| InformationAndCommunicationSystem/CableType | InformationAndCommunicationSystem | string | optional | Type of cable |
| InformationAndCommunicationSystem/FibreType | InformationAndCommunicationSystem | string | optional | Cable type of fibre |
| InformationAndCommunicationSystem/InformationAndCommunicationSystemId | InformationAndCommunicationSystem | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| InformationAndCommunicationSystem/SignalType | InformationAndCommunicationSystem | string | optional | Cable signal type |
| InformationAndCommunicationSystem/SystemId | InformationAndCommunicationSystem |  | optional |  |
| ItRack/ComponentTypeId | ItRack |  | optional |  |
| ItRack/HeightRUs | ItRack | decimal | optional | Height of RUs (rack units) |
| ItRack/ItRackId | ItRack | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| ItRack/Mounting | ItRack | string | optional | Mounting details |
| ItRack/Type | ItRack | string | optional | It rack type |
| JockeyPump/ComponentTypeId | JockeyPump |  | optional |  |
| JockeyPump/FlowCapacity | JockeyPump | decimal | optional | Flow capacity |
| JockeyPump/HeadCapacity | JockeyPump | decimal | optional | Head capacity |
| JockeyPump/JockeyPumpId | JockeyPump | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| JockeyPump/PressureCapacity | JockeyPump | decimal | optional | Pressure capacity of jockey pump |
| JockeyPump/PumpingMedia | JockeyPump | string | optional | Pumping media |
| JockeyPump/Type | JockeyPump | string | optional | Jockey pump type |
| Land/LandCode | Land | string | optional | User specific Land Code |
| Land/LandCoverage | Land | string | optional | Development level of land |
| Land/LandId | Land | string | optional | Customer ID from previous system  (ID before onboarding data to BM) |
| Land/LandParcelNr | Land | string | optional | District/Zoning number registered for the Plot of land |
| Land/SelfUse | Land | boolean | optional | Is land self used or not (Y/N) |
| Land/SiteId | Land |  | optional |  |
| Land/Status | Land | string | optional | Status of site |
| Land/Type | Land | string | optional | Type of land |
| Land/TypeOfOwnership | Land | string | optional | Is the land owned or leased. |
| LightingSystem/GlareIndex | LightingSystem | integer | optional | Glare index |
| LightingSystem/IEEEIlluminationLevels | LightingSystem | integer | optional | Volume domestic cold water |
| LightingSystem/IlluminationUnit | LightingSystem | string | optional | Measurement unit for illumination |
| LightingSystem/LightBrightness | LightingSystem | integer | optional | Light brightness |
| LightingSystem/LightingSystemId | LightingSystem | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| LightingSystem/RoomCavityRatio | LightingSystem | decimal | optional | Room cavity ratio |
| LightingSystem/SolarReflectanceIndex | LightingSystem | decimal | optional | Solar reflectance index (SRI) |
| LightingSystem/SystemId | LightingSystem |  | optional |  |
| Luminaire/ComponentTypeId | Luminaire |  | optional |  |
| Luminaire/LuminaireId | Luminaire | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| Luminaire/Type | Luminaire | string | optional | Luminaire type |
| ModbusController/ConnectorId | ModbusController | string | optional | Registration id |
| ModbusController/ControllerId | ModbusController |  | optional |  |
| ModbusController/Detected | ModbusController | boolean | optional | Detected (Y/N) |
| ModbusController/Enabled | ModbusController | boolean | optional | Enabled (Y/N) |
| ModbusController/ModbusControllerId | ModbusController | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| ModbusController/RegistrationId | ModbusController | string | optional | Registration id |
| ModbusController/RegistrationKey | ModbusController | string | optional | Registration key |
| MovingWalkway/ComponentTypeId | MovingWalkway |  | optional |  |
| MovingWalkway/Inclination | MovingWalkway | string | optional | Inclination |
| MovingWalkway/MaxLength | MovingWalkway | decimal | optional | Max travel distance |
| MovingWalkway/MaxTravelSpeed | MovingWalkway | decimal | optional | Speed of escalator |
| MovingWalkway/MovingWalkwayId | MovingWalkway | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| MovingWalkway/StepWidth | MovingWalkway | decimal | optional | Step width |
| MovingWalkway/Type | MovingWalkway | string | optional | Escalator type |
| PlumbingExpansionTank/PlumbingExpansionTankId | PlumbingExpansionTank | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| PlumbingExpansionTank/PlumbingTankId | PlumbingExpansionTank |  | optional |  |
| PlumbingExpansionTank/SystemPressure | PlumbingExpansionTank | decimal | optional | System pressure |
| PlumbingExpansionTank/TankCapacity | PlumbingExpansionTank | decimal | optional | Tank capacity |
| PlumbingExpansionTank/Type | PlumbingExpansionTank | string | optional | Plumbing tank sub component type |
| PlumbingPump/ComponentTypeId | PlumbingPump |  | optional |  |
| PlumbingPump/FlowCapacity | PlumbingPump | decimal | optional | Flow capacity |
| PlumbingPump/HeadCapacity | PlumbingPump | decimal | optional | Head capacity |
| PlumbingPump/PlumbingPumpId | PlumbingPump | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| PlumbingPump/PressureCapacity | PlumbingPump | decimal | optional | Pressure capacity of hvac valve |
| PlumbingPump/PumpingMedia | PlumbingPump | string | optional | Pumping media |
| PlumbingPump/Type | PlumbingPump | string | optional | Plumbing media type |
| PlumbingPumpSubComponent/FlowCapacity | PlumbingPumpSubComponent | decimal | optional | Flow capacity |
| PlumbingPumpSubComponent/HeadCapacity | PlumbingPumpSubComponent | decimal | optional | Head capacity |
| PlumbingPumpSubComponent/PlumbingPumpId | PlumbingPumpSubComponent |  | optional |  |
| PlumbingPumpSubComponent/PlumbingPumpSubComponentId | PlumbingPumpSubComponent | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| PlumbingPumpSubComponent/PressureCapacity | PlumbingPumpSubComponent | decimal | optional | Pressure capacity of hvac valve |
| PlumbingPumpSubComponent/PumpingMedia | PlumbingPumpSubComponent | string | optional | Pumping media |
| PlumbingPumpSubComponent/Type | PlumbingPumpSubComponent | string | optional | Plumbing media type |
| PlumbingShutOffValve/FlowCapacity | PlumbingShutOffValve | decimal | optional | Flow capacity |
| PlumbingShutOffValve/PipeDiameter | PlumbingShutOffValve | decimal | optional | Pipe diameter of plumbing valve sub component |
| PlumbingShutOffValve/PlumbingShutOffValveId | PlumbingShutOffValve | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| PlumbingShutOffValve/PlumbingValveId | PlumbingShutOffValve |  | optional |  |
| PlumbingShutOffValve/Type | PlumbingShutOffValve | string | optional | Plumbing shut off valve type (only applies for sub component plumbing shut off valve) |
| PlumbingStorageTank/Arrangement | PlumbingStorageTank | string | optional | Arrangement of plumbing storage tank (only applies for sub component plumbing storage tank) |
| PlumbingStorageTank/PlumbingStorageTankId | PlumbingStorageTank | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| PlumbingStorageTank/PlumbingTankId | PlumbingStorageTank |  | optional |  |
| PlumbingStorageTank/SystemPressure | PlumbingStorageTank | decimal | optional | System pressure |
| PlumbingStorageTank/TankCapacity | PlumbingStorageTank | decimal | optional | Tank capacity |
| PlumbingStorageTank/Type | PlumbingStorageTank | string | optional | Plumbing tank sub component type |
| PlumbingSystem/PlumbingSystemId | PlumbingSystem | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| PlumbingSystem/PlumbingVolume | PlumbingSystem | integer | optional | Plumbing volume |
| PlumbingSystem/SystemId | PlumbingSystem |  | optional |  |
| PlumbingSystem/VolumeDomesticColdWater | PlumbingSystem | integer | optional | Volume domestic cold water |
| PlumbingSystem/VolumeDomesticHotWater | PlumbingSystem | integer | optional | Volume domestic hot water |
| PlumbingSystem/VolumeFireDepartmentWater | PlumbingSystem | integer | optional | Volume fire department water |
| PlumbingSystem/VolumeSanitaryWater | PlumbingSystem | integer | optional | Volume domestic hot water |
| PlumbingSystem/VolumeStormWater | PlumbingSystem | integer | optional | Volume storm water |
| PlumbingSystem/VolumeWasteWater | PlumbingSystem | integer | optional | Volume waste water |
| PlumbingTank/ComponentTypeId | PlumbingTank |  | optional |  |
| PlumbingTank/PlumbingTankId | PlumbingTank | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| PlumbingTank/SystemPressure | PlumbingTank | decimal | optional | System pressure |
| PlumbingTank/TankCapacity | PlumbingTank | decimal | optional | Tank capacity |
| PlumbingTank/Type | PlumbingTank | string | optional | Plumbing tank type |
| PlumbingValve/ComponentTypeId | PlumbingValve |  | optional |  |
| PlumbingValve/FlowCapacity | PlumbingValve | decimal | optional | Flow capacity |
| PlumbingValve/PipeDiameter | PlumbingValve | decimal | optional | Pipe diameter |
| PlumbingValve/PlumbingValveId | PlumbingValve | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| PlumbingValve/Type | PlumbingValve | string | optional | Plumbing valve type |
| PlumbingValveSubComponent/FlowCapacity | PlumbingValveSubComponent | decimal | optional | Flow capacity |
| PlumbingValveSubComponent/PipeDiameter | PlumbingValveSubComponent | decimal | optional | Pipe diameter of plumbing valve sub component |
| PlumbingValveSubComponent/PlumbingValveId | PlumbingValveSubComponent |  | optional |  |
| PlumbingValveSubComponent/PlumbingValveSubComponentId | PlumbingValveSubComponent | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| PlumbingValveSubComponent/Type | PlumbingValveSubComponent | string | optional | Plumbing valve sub component type |
| Sensor/DataProvider | Sensor | string | optional | Name of data provider |
| Sensor/MeasurementType | Sensor | string | optional | Defines the measurement type of sensor |
| Sensor/Model | Sensor | string | optional | Model of sensor |
| Sensor/Name | Sensor | string | optional | User specific sensor name |
| Sensor/ParentId | Sensor | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| Sensor/SensorAccuracy | Sensor | decimal | optional | Accuracy of the sensor. It is the maximum difference that will exist between the actual value (which must be measured by a primary or good secondary standard) and the indicated value at the output of the sensor |
| Sensor/SensorId | Sensor | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| Sensor/Type | Sensor | string | optional | Type of sensor |
| SensorBuilding/BuildingId | SensorBuilding |  | optional |  |
| SensorBuilding/SensorId | SensorBuilding |  | optional |  |
| SensorComponent/ComponentId | SensorComponent |  | optional |  |
| SensorComponent/SensorId | SensorComponent |  | optional |  |
| SensorEquipment/BatteryPercentage | SensorEquipment | decimal | optional | Battery percentage |
| SensorEquipment/ComponentTypeId | SensorEquipment |  | optional |  |
| SensorEquipment/SensorEquipmentId | SensorEquipment | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| SensorEquipment/Type | SensorEquipment | string | optional | Sensor type |
| SensorEquipment/WifiSignalStrength | SensorEquipment | string | optional | Wifi signal strength |
| SensorFloor/FloorId | SensorFloor |  | optional |  |
| SensorFloor/SensorId | SensorFloor |  | optional |  |
| SensorLand/LandId | SensorLand |  | optional |  |
| SensorLand/SensorId | SensorLand |  | optional |  |
| SensorMeasurement/MeasurementDate | SensorMeasurement | dateTime | optional | Date of measurement in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| SensorMeasurement/Reliability | SensorMeasurement | string | optional | Is this sensor measurement reliable |
| SensorMeasurement/SensorId | SensorMeasurement |  | optional |  |
| SensorMeasurement/SensorMeasurementId | SensorMeasurement | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| SensorMeasurement/Unit | SensorMeasurement | string | optional | Unit of sensor measurement |
| SensorMeasurement/Value | SensorMeasurement | float | optional | Value of sensor measurement |
| SensorRentalUnit/RentalUnitId | SensorRentalUnit |  | optional |  |
| SensorRentalUnit/SensorId | SensorRentalUnit |  | optional |  |
| SensorSite/SensorId | SensorSite |  | optional |  |
| SensorSite/SiteId | SensorSite |  | optional |  |
| SensorSpace/SensorId | SensorSpace |  | optional |  |
| SensorSpace/SpaceId | SensorSpace |  | optional |  |
| SensorUnit/SensorId | SensorUnit |  | optional |  |
| SensorUnit/UnitId | SensorUnit |  | optional |  |
| Server/HeightRUs | Server | decimal | optional | Height of RUs (rack units) |
| Server/IctHardwareId | Server |  | optional |  |
| Server/MountedInRack | Server | boolean | optional | Mounted in it rack |
| Server/NumberOfPorts | Server | integer | optional | Number of ports |
| Server/RackPosition | Server | string | optional | It rack position |
| Server/ServerId | Server | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| Site/SiteCode | Site | string | optional | User specific Site Code |
| Site/SiteId | Site | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| Site/Status | Site | string | optional | Status of site |
| Site/Type | Site | string | optional | Type of site |
| Space/ClimateCooled | Space | boolean | optional | Define if space is climate cooled (Y/N) |
| Space/ClimateHeated | Space | boolean | optional | Define if space is climate heated (Y/N) |
| Space/CoUseArea | Space | boolean | optional | Is the space used by multiple tenants (Y/N) |
| Space/EffectZonesCooling | Space | decimal | optional | Area that is cooled |
| Space/EffectZonesHeating | Space | decimal | optional | Area that is heated |
| Space/EffectZonesVentilation | Space | decimal | optional | Area that is ventilated |
| Space/FloorId | Space |  | optional |  |
| Space/MaximumOccupancy | Space | integer | optional | Define maximum occupancy of space |
| Space/PrimaryCeilingMaterial | Space | string | optional | Material of ceiling e.g: cement |
| Space/PrimaryFloorMaterial | Space | string | optional | Material of floor |
| Space/PrimaryWallMaterial | Space | string | optional | Material of wall |
| Space/Rentability | Space | boolean | optional | Status of the space is eligible for renting out (Y/N) |
| Space/SpaceCode | Space | string | optional | User specific Space Code |
| Space/SpaceHeight | Space | decimal | optional | Actual space height e.g: 3.6 m |
| Space/SpaceHeightUsable | Space | decimal | optional | Usable Height of space |
| Space/SpaceId | Space | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| Space/SpaceNumber | Space | decimal | optional | Number of space |
| Space/SpaceVolumeGross | Space | decimal | optional | Gross volume of space including surrounding walls |
| Space/SpaceVolumeNet | Space | decimal | optional | Gross volume of space excluding surrounding  walls |
| Space/Type | Space | string | optional | Type of space |
| Space/VentilationType | Space | string | optional | Define the ventilation type e.g: exhaust, supply, balanced, and heat-recovery |
| SprinklerHeatTracing/ComponentTypeId | SprinklerHeatTracing |  | optional |  |
| SprinklerHeatTracing/PowerDensity | SprinklerHeatTracing | decimal | optional | Amount of power density |
| SprinklerHeatTracing/SprinklerHeatTracingId | SprinklerHeatTracing | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| SprinklerHeatTracing/Type | SprinklerHeatTracing | string | optional | Sprinkler heat tracing type |
| SprinklerTank/ComponentTypeId | SprinklerTank |  | optional |  |
| SprinklerTank/SprinklerTankId | SprinklerTank | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| SprinklerTank/SystemPressure | SprinklerTank | decimal | optional | System pressure |
| SprinklerTank/TankCapacity | SprinklerTank | decimal | optional | Tank capacity |
| SprinklerValve/ComponentTypeId | SprinklerValve |  | optional |  |
| SprinklerValve/FlowCapacity | SprinklerValve | decimal | optional | Flow capacity |
| SprinklerValve/PipeDiameter | SprinklerValve | decimal | optional | Pipe diameter of hvac valve |
| SprinklerValve/PressureCapacity | SprinklerValve | decimal | optional | Pressure capacity of jockey pump |
| SprinklerValve/SprinklerValveId | SprinklerValve | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| SprinklerValve/Type | SprinklerValve | string | optional | Sprinkler valve type |
| System/Description | System | string | optional | Description of system |
| System/Model | System | string | optional | System model name and/or number |
| System/SerialNumber | System | string | optional | Serial number of system |
| System/SystemId | System | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| System/SystemReferenceId | System | string | optional | Reference system id coming from another system |
| System/WarrantyStartDate | System | dateTime | optional | Warranty start date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| SystemBuilding/BuildingId | SystemBuilding |  | optional |  |
| SystemBuilding/SystemId | SystemBuilding |  | optional |  |
| SystemFloor/FloorId | SystemFloor |  | optional |  |
| SystemFloor/SystemId | SystemFloor |  | optional |  |
| SystemRentalUnit/RentalUnitId | SystemRentalUnit |  | optional |  |
| SystemRentalUnit/SystemId | SystemRentalUnit |  | optional |  |
| SystemSite/SiteId | SystemSite |  | optional |  |
| SystemSite/SystemId | SystemSite |  | optional |  |
| SystemSpace/SpaceId | SystemSpace |  | optional |  |
| SystemSpace/SystemId | SystemSpace |  | optional |  |
| SystemUnit/SystemId | SystemUnit |  | optional |  |
| SystemUnit/UnitId | SystemUnit |  | optional |  |
| TankWaterHeater/FirstHourDelivery | TankWaterHeater | decimal | optional | First hour delivery |
| TankWaterHeater/Recovery100FRise | TankWaterHeater | decimal | optional | Recovery rate to 100 frise in l per hour |
| TankWaterHeater/TankCapacity | TankWaterHeater | decimal | optional | Tank capacity |
| TankWaterHeater/TankWaterHeaterId | TankWaterHeater | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| TankWaterHeater/Type | TankWaterHeater | string | optional | Tank water heater type |
| TankWaterHeater/WaterHeaterId | TankWaterHeater |  | optional |  |
| TankWaterHeaterSubComponent/FirstHourDelivery | TankWaterHeaterSubComponent | decimal | optional | First hour delivery |
| TankWaterHeaterSubComponent/PowerInput | TankWaterHeaterSubComponent | decimal | optional | Power input |
| TankWaterHeaterSubComponent/Recovery100FRise | TankWaterHeaterSubComponent | decimal | optional | Recovery rate to 100 frise in l per hour |
| TankWaterHeaterSubComponent/TankCapacity | TankWaterHeaterSubComponent | decimal | optional | Tank capacity |
| TankWaterHeaterSubComponent/TankWaterHeaterId | TankWaterHeaterSubComponent |  | optional |  |
| TankWaterHeaterSubComponent/TankWaterHeaterSubComponentId | TankWaterHeaterSubComponent | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| TankWaterHeaterSubComponent/Type | TankWaterHeaterSubComponent | string | optional | Tank water heater sub component type |
| TanklessWaterHeater/FirstHourDelivery | TanklessWaterHeater | decimal | optional | First hour delivery |
| TanklessWaterHeater/Recovery100FRise | TanklessWaterHeater | decimal | optional | Recovery rate to 100 frise in l per hour |
| TanklessWaterHeater/TanklessWaterHeaterId | TanklessWaterHeater | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| TanklessWaterHeater/Type | TanklessWaterHeater | string | optional | Tankless water heater type |
| TanklessWaterHeater/WaterHeaterId | TanklessWaterHeater |  | optional |  |
| TanklessWaterHeaterSubComponent/FirstHourDelivery | TanklessWaterHeaterSubComponent | decimal | optional | First hour delivery |
| TanklessWaterHeaterSubComponent/PowerInput | TanklessWaterHeaterSubComponent | decimal | optional | Power input |
| TanklessWaterHeaterSubComponent/Recovery100FRise | TanklessWaterHeaterSubComponent | decimal | optional | Recovery rate to 100 frise in l per hour |
| TanklessWaterHeaterSubComponent/TanklessWaterHeaterId | TanklessWaterHeaterSubComponent |  | optional |  |
| TanklessWaterHeaterSubComponent/TanklessWaterHeaterSubComponentId | TanklessWaterHeaterSubComponent | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| TanklessWaterHeaterSubComponent/Type | TanklessWaterHeaterSubComponent | string | optional | Tankless water heater sub component type |
| TerminalUnit/ComponentTypeId | TerminalUnit |  | optional |  |
| TerminalUnit/DuctInletCommissionDate | TerminalUnit | dateTime | optional | Commission date if duct inlet in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| TerminalUnit/DuctInletConfiguration | TerminalUnit | string | optional | Duct inlet configuration |
| TerminalUnit/DuctInletExpectedEndOfLife | TerminalUnit | dateTime | optional | Expected end of life date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| TerminalUnit/DuctInletExpectedReplacementCost | TerminalUnit | decimal | optional | Duct inlet expected replacement costs |
| TerminalUnit/DuctInletInitialCost | TerminalUnit | decimal | optional | Duct inlet initial cost |
| TerminalUnit/DuctInletInstallationDate | TerminalUnit | dateTime | optional | Duct inlet Installation date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| TerminalUnit/DuctInletMaintenanceInterval | TerminalUnit | string | optional | Duct inlet maintenance interval either as string: monthly, quarterly, etc. or as month |
| TerminalUnit/DuctInletModel | TerminalUnit | string | optional | Duct inlet model number |
| TerminalUnit/DuctInletName | TerminalUnit | string | optional | Name of Duct inlet |
| TerminalUnit/DuctInletSerialNumber | TerminalUnit | string | optional | Serial number of component |
| TerminalUnit/DuctInletShape | TerminalUnit | decimal | optional | Duct inlet shape |
| TerminalUnit/DuctInletSize | TerminalUnit | decimal | optional | Duct inlet size |
| TerminalUnit/DuctInletTagNumber | TerminalUnit | string | optional | Tag number |
| TerminalUnit/DuctInletTurnoverDate | TerminalUnit | dateTime | optional | Duct inlet turnover date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| TerminalUnit/MaxAirflowRating | TerminalUnit | decimal | optional | Max flow capacity |
| TerminalUnit/MinAirflowRating | TerminalUnit | decimal | optional | Min flow capacity |
| TerminalUnit/TerminalUnitId | TerminalUnit | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| TerminalUnit/Type | TerminalUnit | string | optional | Define the specific terminal unit type |
| ThermalMeter/ComponentTypeId | ThermalMeter |  | optional |  |
| ThermalMeter/DeltaTemperature | ThermalMeter | decimal | optional | Export energy |
| ThermalMeter/EnergyRate | ThermalMeter | decimal | optional | Export energy |
| ThermalMeter/EnergyTotal | ThermalMeter | decimal | optional | Energy total |
| ThermalMeter/Measures | ThermalMeter | string | optional | Substance that is measured |
| ThermalMeter/ReturnTemperature | ThermalMeter | decimal | optional | Return temperature |
| ThermalMeter/SupplyTemperature | ThermalMeter | decimal | optional | Supply temperature |
| ThermalMeter/ThermalMeterId | ThermalMeter | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| ThermalMeter/Type | ThermalMeter | string | optional | Water meter type |
| ThermalMeter/VolumeFlow | ThermalMeter | decimal | optional | Volume flow |
| ThermalMeter/VolumeTotal | ThermalMeter | decimal | optional | Volume |
| Toilet/ComponentTypeId | Toilet |  | optional |  |
| Toilet/InstallationType | Toilet | string | optional | Installation type |
| Toilet/ToiletId | Toilet | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| Toilet/WaterPerFlush | Toilet | decimal | optional | Water per flush |
| ToiletFlushometer/InstallationType | ToiletFlushometer | string | optional | Installation type |
| ToiletFlushometer/ToiletFlushometerId | ToiletFlushometer | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| ToiletFlushometer/ToiletId | ToiletFlushometer |  | optional |  |
| ToiletFlushometer/WaterPerFlush | ToiletFlushometer | decimal | optional | Water per flush |
| ToiletTank/FlushingType | ToiletTank | string | optional | Flushing type |
| ToiletTank/InstallationType | ToiletTank | string | optional | Installation type |
| ToiletTank/ToiletId | ToiletTank |  | optional |  |
| ToiletTank/ToiletTankId | ToiletTank | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| ToiletTank/WaterPerFlush | ToiletTank | decimal | optional | Water per flush |
| TransferSwitch/ComponentTypeId | TransferSwitch |  | optional |  |
| TransferSwitch/MainBusCurrentRating | TransferSwitch | decimal | optional | Current rating |
| TransferSwitch/MainBusMaterial | TransferSwitch | string | optional | Material |
| TransferSwitch/MainsRating | TransferSwitch | decimal | optional | Mains rating |
| TransferSwitch/Poles | TransferSwitch | integer | optional | Poles |
| TransferSwitch/TransferSwitchId | TransferSwitch | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| TransferSwitch/Type | TransferSwitch | string | optional | Transfer switch type |
| Transformer/ComponentTypeId | Transformer |  | optional |  |
| Transformer/Phases | Transformer | string | optional | Phases |
| Transformer/SizeKva | Transformer | decimal | optional | Size kva (kilovolt-ampere) |
| Transformer/TransformerId | Transformer | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| Transformer/Type | Transformer | string | optional | Transformer type |
| Transformer/VoltagePrimary | Transformer | decimal | optional | Voltage primary |
| Transformer/VoltageSecondary | Transformer | decimal | optional | Voltage secondary |
| Unit/UnitCode | Unit | string | optional | User specific unit code |
| Unit/UnitId | Unit | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| UnitBuilding/BuildingId | UnitBuilding |  | optional |  |
| UnitBuilding/UnitId | UnitBuilding |  | optional |  |
| UnitFloor/FloorId | UnitFloor |  | optional |  |
| UnitFloor/UnitId | UnitFloor |  | optional |  |
| UnitHeater/ComponentTypeId | UnitHeater |  | optional |  |
| UnitHeater/ElectricUnitHeaterPowerInput | UnitHeater | decimal | optional | Power input |
| UnitHeater/FanCommissionDate | UnitHeater | dateTime | optional | Fan commission date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| UnitHeater/FanDriveType | UnitHeater | string | optional | Fan fan drive type |
| UnitHeater/FanDurationLifeYear | UnitHeater | integer | optional | Fan life span of component in years |
| UnitHeater/FanExpectedEndOfLife | UnitHeater | dateTime | optional | Fan expected end of life date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| UnitHeater/FanExpectedReplacementCost | UnitHeater | decimal | optional | Fan expected replacement costs |
| UnitHeater/FanInitialCost | UnitHeater | decimal | optional | Fan initial cost |
| UnitHeater/FanInstallationDate | UnitHeater | dateTime | optional | Installation date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| UnitHeater/FanMaintenanceInterval | UnitHeater | string | optional | Fan maintenance interval either as string: monthly, quarterly, etc. or as month |
| UnitHeater/FanMaxAirflowRating | UnitHeater | decimal | optional | Fan max flow capacity |
| UnitHeater/FanMinAirflowRating | UnitHeater | decimal | optional | Fan min flow capacity |
| UnitHeater/FanModelNumber | UnitHeater | string | optional | Model number of fan |
| UnitHeater/FanMotorPower | UnitHeater | decimal | optional | Fan motor power |
| UnitHeater/FanName | UnitHeater | string | optional | Name of fan |
| UnitHeater/FanNominalAirflow | UnitHeater | decimal | optional | Fan nominal airflow |
| UnitHeater/FanSerialNumber | UnitHeater | string | optional | Serial number of fan |
| UnitHeater/FanTagNumber | UnitHeater | string | optional | Fan tag number |
| UnitHeater/FanTurnoverDate | UnitHeater | dateTime | optional | Fan turnover date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| UnitHeater/HeatingMethodCommissionDate | UnitHeater | dateTime | optional | Heating method commission date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| UnitHeater/HeatingMethodDurationLifeYear | UnitHeater | integer | optional | Heating method life span of component in years |
| UnitHeater/HeatingMethodExpectedEndOfLife | UnitHeater | dateTime | optional | Heating method expected end of life date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| UnitHeater/HeatingMethodExpectedReplacementCost | UnitHeater | decimal | optional | Heating method expected replacement costs |
| UnitHeater/HeatingMethodInitialCost | UnitHeater | decimal | optional | Heating method initial cost |
| UnitHeater/HeatingMethodInstallationDate | UnitHeater | dateTime | optional | Installation date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| UnitHeater/HeatingMethodMaintenanceInterval | UnitHeater | string | optional | Heating method maintenance interval either as string: monthly, quarterly, etc. or as month |
| UnitHeater/HeatingMethodModelNumber | UnitHeater | string | optional | Model number of heating method |
| UnitHeater/HeatingMethodName | UnitHeater | string | optional | Heating method name of product |
| UnitHeater/HeatingMethodOutsideDiameter | UnitHeater | decimal | optional | Heating method outside diameter |
| UnitHeater/HeatingMethodSerialNumber | UnitHeater | string | optional | Serial number of heating method |
| UnitHeater/HeatingMethodTagNumber | UnitHeater | string | optional | Heating method tag number |
| UnitHeater/HeatingMethodTurnoverDate | UnitHeater | dateTime | optional | Heating method turnover date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| UnitHeater/HeatingMethodType | UnitHeater | string | optional | Heating method type |
| UnitHeater/HotWaterUnitHeaterFlowCapacity | UnitHeater | decimal | optional | Flow capacity |
| UnitHeater/NominalHeatingCapacity | UnitHeater | decimal | optional | Nominal heating capacity |
| UnitHeater/SteamUnitHeaterCondensate | UnitHeater | string | optional | Condensate information if steam unit heater |
| UnitHeater/Type | UnitHeater | string | optional | Unit heater sub component type |
| UnitHeater/UnitHeaterId | UnitHeater | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| UnitLand/LandId | UnitLand |  | optional |  |
| UnitLand/UnitId | UnitLand |  | optional |  |
| UnitSite/SiteId | UnitSite |  | optional |  |
| UnitSite/UnitId | UnitSite |  | optional |  |
| UnitSpace/SpaceId | UnitSpace |  | optional |  |
| UnitSpace/UnitId | UnitSpace |  | optional |  |
| Ups/ComponentTypeId | Ups |  | optional |  |
| Ups/InputPhases | Ups | string | optional | Input phases |
| Ups/InputVoltage | Ups | decimal | optional | Input voltage |
| Ups/OutputPhases | Ups | string | optional | Output phases |
| Ups/OutputVoltage | Ups | decimal | optional | Output voltage |
| Ups/PowerOutput | Ups | decimal | optional | Power output |
| Ups/PowerOutputKva | Ups | decimal | optional | Power output |
| Ups/UpsId | Ups | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| UrinalFlushometer/ComponentTypeId | UrinalFlushometer |  | optional |  |
| UrinalFlushometer/InstallationType | UrinalFlushometer | string | optional | Installation type |
| UrinalFlushometer/UrinalFlushometerId | UrinalFlushometer | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| UrinalFlushometer/WaterPerFlush | UrinalFlushometer | decimal | optional | Water per flush |
| VariableFrequencyDrive/ComponentTypeId | VariableFrequencyDrive |  | optional |  |
| VariableFrequencyDrive/Type | VariableFrequencyDrive | string | optional | Variable frequency type |
| VariableFrequencyDrive/VariableFrequencyDriveId | VariableFrequencyDrive | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| VavBoxReheat/DuctInletCommissionDate | VavBoxReheat | dateTime | optional | Commission date if duct inlet in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| VavBoxReheat/DuctInletConfiguration | VavBoxReheat | string | optional | Duct inlet configuration |
| VavBoxReheat/DuctInletExpectedEndOfLife | VavBoxReheat | dateTime | optional | Expected end of life date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| VavBoxReheat/DuctInletExpectedReplacementCost | VavBoxReheat | decimal | optional | Duct inlet expected replacement costs |
| VavBoxReheat/DuctInletInitialCost | VavBoxReheat | decimal | optional | Duct inlet initial cost |
| VavBoxReheat/DuctInletInstallationDate | VavBoxReheat | dateTime | optional | Duct inlet Installation date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| VavBoxReheat/DuctInletMaintenanceInterval | VavBoxReheat | string | optional | Duct inlet maintenance interval either as string: monthly, quarterly, etc. or as month |
| VavBoxReheat/DuctInletModel | VavBoxReheat | string | optional | Duct inlet model number |
| VavBoxReheat/DuctInletName | VavBoxReheat | string | optional | Name of Duct inlet |
| VavBoxReheat/DuctInletSerialNumber | VavBoxReheat | string | optional | Serial number of component |
| VavBoxReheat/DuctInletShape | VavBoxReheat | decimal | optional | Duct inlet shape |
| VavBoxReheat/DuctInletSize | VavBoxReheat | decimal | optional | Duct inlet size |
| VavBoxReheat/DuctInletTagNumber | VavBoxReheat | string | optional | Tag number |
| VavBoxReheat/DuctInletTurnoverDate | VavBoxReheat | dateTime | optional | Duct inlet turnover date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| VavBoxReheat/MaxAirflowRating | VavBoxReheat | decimal | optional | Max flow capacity |
| VavBoxReheat/MinAirflowRating | VavBoxReheat | decimal | optional | Min flow capacity |
| VavBoxReheat/NominalHeatingCapacity | VavBoxReheat | decimal | optional | Nominal heating capacity |
| VavBoxReheat/ReHeatingCommissionDate | VavBoxReheat | dateTime | optional | Re heating commission date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| VavBoxReheat/ReHeatingDurationLifeYear | VavBoxReheat | integer | optional | Re heating life span of component in years |
| VavBoxReheat/ReHeatingExpectedEndOfLife | VavBoxReheat | dateTime | optional | Re heating expected end of life date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| VavBoxReheat/ReHeatingExpectedReplacementCost | VavBoxReheat | decimal | optional | Re heating expected replacement costs |
| VavBoxReheat/ReHeatingInitialCost | VavBoxReheat | decimal | optional | Re heating initial cost |
| VavBoxReheat/ReHeatingInstallationDate | VavBoxReheat | dateTime | optional | Installation date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| VavBoxReheat/ReHeatingMaintenanceInterval | VavBoxReheat | string | optional | Re heating maintenance interval either as string: monthly, quarterly, etc. or as month |
| VavBoxReheat/ReHeatingModelNumber | VavBoxReheat | string | optional | Model number of re heating |
| VavBoxReheat/ReHeatingName | VavBoxReheat | string | optional | Re heating name of product |
| VavBoxReheat/ReHeatingOutsideDiameter | VavBoxReheat | decimal | optional | Re heating outside diameter |
| VavBoxReheat/ReHeatingSerialNumber | VavBoxReheat | string | optional | Serial number of re heating |
| VavBoxReheat/ReHeatingTagNumber | VavBoxReheat | string | optional | Re heating tag number |
| VavBoxReheat/ReHeatingTurnoverDate | VavBoxReheat | dateTime | optional | Re heating turnover date in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| VavBoxReheat/ReHeatingType | VavBoxReheat | string | optional | Re heating type |
| VavBoxReheat/TerminalUnitId | VavBoxReheat |  | optional |  |
| VavBoxReheat/VavBoxReheatId | VavBoxReheat | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| WaterFiltration/ComponentTypeId | WaterFiltration |  | optional |  |
| WaterFiltration/FiltrationRating | WaterFiltration | string | optional | Water filtration rating |
| WaterFiltration/FlowCapacity | WaterFiltration | decimal | optional | Flow capacity |
| WaterFiltration/TankCapacity | WaterFiltration | decimal | optional | Tank capacity |
| WaterFiltration/Type | WaterFiltration | string | optional | Water filtration type |
| WaterFiltration/WaterFiltrationId | WaterFiltration | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| WaterHeater/ComponentTypeId | WaterHeater |  | optional |  |
| WaterHeater/FirstHourDelivery | WaterHeater | decimal | optional | First hour delivery |
| WaterHeater/Recovery100FRise | WaterHeater | decimal | optional | Recovery rate to 100 frise in l per hour |
| WaterHeater/Type | WaterHeater | string | optional | Hvac valve type |
| WaterHeater/WaterHeaterId | WaterHeater | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| WaterMeter/ComponentTypeId | WaterMeter |  | optional |  |
| WaterMeter/Measures | WaterMeter | string | optional | Substance that is measured |
| WaterMeter/SupplyTemperature | WaterMeter | decimal | optional | Supply temperature |
| WaterMeter/Type | WaterMeter | string | optional | Water meter type |
| WaterMeter/Volume | WaterMeter | decimal | optional | Volume in liter |
| WaterMeter/VolumeFlow | WaterMeter | decimal | optional | Volume flow |
| WaterMeter/WaterMeterId | WaterMeter | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| WirelessAccessPoint/DataNetworkEquipmentId | WirelessAccessPoint |  | optional |  |
| WirelessAccessPoint/MountedInRack | WirelessAccessPoint | boolean | optional | Mounted in it rack |
| WirelessAccessPoint/Mounting | WirelessAccessPoint | string | optional | Mounting details |
| WirelessAccessPoint/RackPosition | WirelessAccessPoint | string | optional | It rack position |
| WirelessAccessPoint/Type | WirelessAccessPoint | string | optional | Wireless access point type |
| WirelessAccessPoint/WirelessAccessPointId | WirelessAccessPoint | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |

_Generated by `cora docs build`. Do not edit by hand — regenerate when the underlying inventories or crosswalks change._
