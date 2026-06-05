# IBPDI / user-and-customer-experience

| Key | Value |
|---|---|
| Source artifact | `standards/ibpdi/current/native/Schema Documents/core/userAndCustomerExperience/userAndCustomerExperience.manifest.cdm.json` |
| Version | 1.0 |
| Extractor | `cora_extractors.cdm_json@0.0.0` |
| Source label | `cdm-json` |
| Types | 20 |
| Fields | 57 |

## Types

| Name | Extends | Abstract | Definition |
|---|---|---|---|
| AvailableResource | CdmEntity |  | Available resources on workspace |
| AvailableResourceWorkspace | CdmEntity |  | Linking entity between AvailableResources and Workspace |
| Booking | CdmEntity |  | Information about bookings |
| BookingWorkspace | CdmEntity |  | Linking entity between Booking and Workspace |
| Characteristic | CdmEntity |  | Characteristics of workspace |
| CharacteristicNeighbourhood | CdmEntity |  | Linking entity between Characteristics and Neighbourhood |
| CharacteristicWorkspace | CdmEntity |  | Linking entity between Characteristics and Workspace |
| CustomerFile | CdmEntity |  | Information about customer files |
| CustomerFileWorkArea | CdmEntity |  | Linking entity between CustomerFile and WorkArea |
| CustomerFileWorkspace | CdmEntity |  | Linking entity between CustomerFile and Workspace |
| Neighbourhood | CdmEntity |  | A group of workspaces that can be assigned to one or many organisational departments |
| NeighbourhoodWorkspace | CdmEntity |  | Linking entity between Neighbourhood and Workspace |
| Tag | CdmEntity |  | User defined tag information on neighbourhood |
| TagNeighbourhood | CdmEntity |  | Linking entity between Tag and Neighbourhood |
| WorkArea | CdmEntity |  | Work area that represents area used for certain functions within the organisation |
| WorkAreaFloor | CdmEntity |  | Linking entity between WorkArea and Floor |
| WorkAreaSpace | CdmEntity |  | Linking entity between WorkArea and Space |
| WorkAreaType | CdmEntity |  | Type of work area |
| Workspace | CdmEntity |  | All workplace related information ranging from the number of workplaces to security regulations that need to be in place within a work environment. |
| WorkspaceSensor | CdmEntity |  | Linking entity between Workspace and Sensor. The sensor represents the sensor measurement area which can be different from the physical location |

## Fields

| Path | Domain | Range | Cardinality | Definition |
|---|---|---|---|---|
| AvailableResource/AvailableResourceId | AvailableResource | string | optional | Available resources workplace |
| AvailableResource/Name | AvailableResource | string | optional | User specific name of workplace |
| AvailableResourceWorkspace/AvailableResourceId | AvailableResourceWorkspace |  | optional |  |
| AvailableResourceWorkspace/WorkspaceId | AvailableResourceWorkspace |  | optional |  |
| Booking/BookingDate | Booking | dateTime | optional | Date booking was created in yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| Booking/BookingId | Booking | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| Booking/Cancelled | Booking | boolean | optional | Has the reservation been cancelled |
| Booking/CheckInTime | Booking | dateTime | optional | Check in time yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| Booking/CheckOutTime | Booking | dateTime | optional | Check out time yyyy-mm-ddThh:mm:ssZ form (conform to ISO 8061) |
| BookingWorkspace/BookingId | BookingWorkspace |  | optional |  |
| BookingWorkspace/WorkspaceId | BookingWorkspace |  | optional |  |
| Characteristic/CharacteristicId | Characteristic | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| Characteristic/Name | Characteristic | string | optional | User specific name of workplace |
| CharacteristicNeighbourhood/CharacteristicId | CharacteristicNeighbourhood |  | optional |  |
| CharacteristicNeighbourhood/NeighbourhoodId | CharacteristicNeighbourhood |  | optional |  |
| CharacteristicWorkspace/CharacteristicId | CharacteristicWorkspace |  | optional |  |
| CharacteristicWorkspace/WorkspaceId | CharacteristicWorkspace |  | optional |  |
| CustomerFile/CustomerFileId | CustomerFile | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| CustomerFile/FileType | CustomerFile | string | optional | Type of file |
| CustomerFile/Link | CustomerFile | string | optional | Link to file location |
| CustomerFile/Metadata | CustomerFile | string | optional | Metadata information about the file stored in JSON format. This could be for example resolution and ordinal for an image. For different file types different metadata can be stored here |
| CustomerFile/Name | CustomerFile | string | optional | User specific name for file |
| CustomerFileWorkArea/CustomerFileId | CustomerFileWorkArea |  | optional |  |
| CustomerFileWorkArea/WorkAreaId | CustomerFileWorkArea |  | optional |  |
| CustomerFileWorkspace/CustomerFileId | CustomerFileWorkspace |  | optional |  |
| CustomerFileWorkspace/WorkspaceId | CustomerFileWorkspace |  | optional |  |
| Neighbourhood/Color | Neighbourhood | string | optional | User specific color code |
| Neighbourhood/Name | Neighbourhood | string | optional | User specific name of neighbourhood |
| Neighbourhood/NeighbourhoodId | Neighbourhood | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| Neighbourhood/OrganisationId | Neighbourhood |  | optional |  |
| NeighbourhoodWorkspace/NeighbourhoodId | NeighbourhoodWorkspace |  | optional |  |
| NeighbourhoodWorkspace/WorkspaceId | NeighbourhoodWorkspace |  | optional |  |
| Tag/Name | Tag | string | optional | User specific name of tag |
| Tag/TagId | Tag | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| TagNeighbourhood/NeighbourhoodId | TagNeighbourhood |  | optional |  |
| TagNeighbourhood/TagId | TagNeighbourhood |  | optional |  |
| WorkArea/AreaMeasurementId | WorkArea |  | optional |  |
| WorkArea/Name | WorkArea | string | optional | User specific name of work space |
| WorkArea/WorkAreaCode | WorkArea | string | optional | User specific work area code |
| WorkArea/WorkAreaId | WorkArea | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| WorkArea/WorkAreaTypeId | WorkArea |  | optional |  |
| WorkAreaFloor/FloorId | WorkAreaFloor |  | optional |  |
| WorkAreaFloor/WorkAreaId | WorkAreaFloor |  | optional |  |
| WorkAreaSpace/SpaceId | WorkAreaSpace |  | optional |  |
| WorkAreaSpace/WorkAreaId | WorkAreaSpace |  | optional |  |
| WorkAreaType/Color | WorkAreaType | string | optional | Color code of specific workspace template |
| WorkAreaType/Name | WorkAreaType | string | optional | User specific name of work space template ("type of workspace") |
| WorkAreaType/WorkAreaTypeId | WorkAreaType | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| Workspace/Bookable | Workspace | boolean | optional | Is the workplace bookable (Y/N) |
| Workspace/Capacity | Workspace | integer | optional | Capacity of workplace |
| Workspace/Name | Workspace | string | optional | User specific name of workplace |
| Workspace/Type | Workspace | string | optional | Type of workplace |
| Workspace/WorkAreaId | Workspace |  | optional |  |
| Workspace/WorkspaceCode | Workspace | string | optional | User specific work space code |
| Workspace/WorkspaceId | Workspace | string | optional | Unique identifier either coming from previous system otherwise it needs to be defined |
| WorkspaceSensor/SensorId | WorkspaceSensor |  | optional |  |
| WorkspaceSensor/WorkspaceId | WorkspaceSensor |  | optional |  |

_Generated by `cora docs build`. Do not edit by hand — regenerate when the underlying inventories or crosswalks change._
